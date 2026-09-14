#define _POSIX_C_SOURCE 200809L

/*
 * Direct rigorous SPD gate for the frozen A1 C-even exact integer matrix.
 *
 * This checker deliberately avoids a full eigenvalue decomposition. It reads
 * the already-built binary artifact, reconstructs the exact symmetric fmpz
 * matrix, independently recomputes the canonical row-major SHA-256 used by
 * the Python builder, and then asks Arb for a rigorous LDL^T certificate.
 *
 * arb_mat_ldl() returns nonzero only if positive definiteness is CERTAIN.
 * A zero return is therefore UNDECIDED here, never a negative theorem.
 */

#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <gmp.h>
#include <openssl/evp.h>

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/fmpz_mat.h>
#include <flint/arb_mat.h>

#define DIM 1075
#define MAGIC "A1CEVEN1"
#define MAGIC_LEN 8
#define MAX_MAG_BYTES 65535

static const char *EXPECTED_SHA256 =
    "97b761e9f89517303f557d3c18061cc1b232c821e5804fcf9071298e17e60183";

static void die(const char *msg)
{
    fprintf(stderr, "ERROR: %s\n", msg);
    exit(2);
}

static uint16_t read_u16_be(FILE *f)
{
    unsigned char b[2];
    if (fread(b, 1, 2, f) != 2)
        die("truncated uint16");
    return ((uint16_t)b[0] << 8) | (uint16_t)b[1];
}

static uint32_t read_u32_be(FILE *f)
{
    unsigned char b[4];
    if (fread(b, 1, 4, f) != 4)
        die("truncated uint32");
    return ((uint32_t)b[0] << 24) | ((uint32_t)b[1] << 16)
         | ((uint32_t)b[2] << 8) | (uint32_t)b[3];
}

static void write_u32_be(unsigned char out[4], uint32_t x)
{
    out[0] = (unsigned char)(x >> 24);
    out[1] = (unsigned char)(x >> 16);
    out[2] = (unsigned char)(x >> 8);
    out[3] = (unsigned char)x;
}

static double now_seconds(void)
{
    struct timespec ts;
    if (clock_gettime(CLOCK_MONOTONIC, &ts) != 0)
        die("clock_gettime failed");
    return (double)ts.tv_sec + 1e-9 * (double)ts.tv_nsec;
}

static void load_artifact(const char *path, fmpz_mat_t A)
{
    FILE *f = fopen(path, "rb");
    unsigned char magic[MAGIC_LEN];
    unsigned char *buf = NULL;
    mpz_t z;
    long i, j;

    if (f == NULL) {
        fprintf(stderr, "ERROR: fopen(%s): %s\n", path, strerror(errno));
        exit(2);
    }

    if (fread(magic, 1, MAGIC_LEN, f) != MAGIC_LEN ||
        memcmp(magic, MAGIC, MAGIC_LEN) != 0)
        die("matrix artifact magic mismatch");

    if (read_u32_be(f) != DIM)
        die("matrix artifact dimension mismatch");

    buf = (unsigned char *) malloc(MAX_MAG_BYTES);
    if (buf == NULL)
        die("malloc failed");
    mpz_init(z);

    for (i = 0; i < DIM; i++) {
        for (j = i; j < DIM; j++) {
            int sign = fgetc(f);
            uint16_t n;
            size_t count;

            if (sign == EOF)
                die("truncated integer sign");
            if (sign != 0 && sign != 1)
                die("invalid integer sign byte");

            n = read_u16_be(f);
            if (n == 0)
                die("zero-length integer magnitude");
            if (fread(buf, 1, n, f) != n)
                die("truncated integer magnitude");

            mpz_import(z, n, 1, 1, 1, 0, buf);
            if (sign) {
                if (mpz_sgn(z) == 0)
                    die("negative zero in artifact");
                mpz_neg(z, z);
            }

            fmpz_set_mpz(fmpz_mat_entry(A, i, j), z);
            if (i != j)
                fmpz_set_mpz(fmpz_mat_entry(A, j, i), z);

            count = (size_t)n;
            (void)count;
        }
    }

    if (fgetc(f) != EOF)
        die("matrix artifact has trailing bytes");
    if (ferror(f))
        die("I/O error reading artifact");

    mpz_clear(z);
    free(buf);
    fclose(f);
}

static void canonical_sha256(char out_hex[65], const fmpz_mat_t A)
{
    EVP_MD_CTX *ctx = EVP_MD_CTX_new();
    unsigned char digest[EVP_MAX_MD_SIZE];
    unsigned int digest_len = 0;
    unsigned char *buf = NULL;
    unsigned char len_be[4];
    char header[64];
    mpz_t z;
    long i, j;
    int hlen;

    if (ctx == NULL)
        die("EVP_MD_CTX_new failed");
    if (EVP_DigestInit_ex(ctx, EVP_sha256(), NULL) != 1)
        die("EVP_DigestInit_ex failed");

    hlen = snprintf(header, sizeof(header), "fmpz-matrix-v1:%d:%d\n", DIM, DIM);
    if (hlen <= 0 || hlen >= (int)sizeof(header))
        die("hash header construction failed");
    if (EVP_DigestUpdate(ctx, header, (size_t)hlen) != 1)
        die("EVP_DigestUpdate header failed");

    buf = (unsigned char *) malloc(MAX_MAG_BYTES);
    if (buf == NULL)
        die("malloc failed");
    mpz_init(z);

    for (i = 0; i < DIM; i++) {
        for (j = 0; j < DIM; j++) {
            int neg = fmpz_sgn(fmpz_mat_entry(A, i, j)) < 0;
            size_t len, count = 0;
            unsigned char sign = neg ? '-' : '+';

            fmpz_get_mpz(z, fmpz_mat_entry(A, i, j));
            if (mpz_sgn(z) < 0)
                mpz_neg(z, z);

            if (mpz_sgn(z) == 0) {
                len = 1;
                buf[0] = 0;
            } else {
                size_t bits = mpz_sizeinbase(z, 2);
                len = (bits + 7) / 8;
                if (len == 0 || len >= 65536)
                    die("canonical hash magnitude length out of range");
                memset(buf, 0, len);
                mpz_export(buf, &count, 1, 1, 1, 0, z);
                if (count != len)
                    die("canonical hash mpz_export length mismatch");
            }

            if (len > UINT32_MAX)
                die("canonical hash length overflow");
            write_u32_be(len_be, (uint32_t)len);

            if (EVP_DigestUpdate(ctx, &sign, 1) != 1 ||
                EVP_DigestUpdate(ctx, len_be, 4) != 1 ||
                EVP_DigestUpdate(ctx, buf, len) != 1)
                die("EVP_DigestUpdate matrix entry failed");
        }
    }

    if (EVP_DigestFinal_ex(ctx, digest, &digest_len) != 1)
        die("EVP_DigestFinal_ex failed");
    if (digest_len != 32)
        die("unexpected SHA-256 digest length");

    for (i = 0; i < 32; i++)
        sprintf(out_hex + 2 * i, "%02x", digest[i]);
    out_hex[64] = '\0';

    mpz_clear(z);
    free(buf);
    EVP_MD_CTX_free(ctx);
}

static int certify_spd_ldl(const fmpz_mat_t Z, slong prec)
{
    arb_mat_t A, L;
    double t0, t1;
    int ok;

    arb_mat_init(A, DIM, DIM);
    arb_mat_init(L, DIM, DIM);

    /* Exact integer embedding; all rounding happens rigorously inside LDL. */
    arb_mat_set_fmpz_mat(A, Z);

    printf("LDL_PRECISION=%ld\n", (long)prec);
    fflush(stdout);
    t0 = now_seconds();
    ok = arb_mat_ldl(L, A, prec);
    t1 = now_seconds();
    printf("LDL_DONE precision=%ld elapsed=%.3f certified=%d\n",
           (long)prec, t1 - t0, ok != 0);
    fflush(stdout);

    arb_mat_clear(A);
    arb_mat_clear(L);
    return ok != 0;
}

int main(int argc, char **argv)
{
    const slong ladder[] = {256, 512, 768, 1024, 1536, 2048, 3072};
    const size_t ladder_len = sizeof(ladder) / sizeof(ladder[0]);
    const char *path;
    fmpz_mat_t Z, T;
    char digest[65];
    size_t k;
    double t0, t1;

    if (argc != 2) {
        fprintf(stderr, "usage: %s a1_c_even_exact_matrix.bin\n", argv[0]);
        return 2;
    }
    path = argv[1];

    flint_set_num_threads(2);
    fmpz_mat_init(Z, DIM, DIM);
    fmpz_mat_init(T, DIM, DIM);

    t0 = now_seconds();
    load_artifact(path, Z);
    t1 = now_seconds();
    printf("ARTIFACT_LOAD elapsed=%.3f\n", t1 - t0);

    fmpz_mat_transpose(T, Z);
    if (!fmpz_mat_equal(Z, T))
        die("decoded matrix is not symmetric");
    printf("CERTIFIED: decoded matrix is exactly symmetric 1075x1075\n");

    t0 = now_seconds();
    canonical_sha256(digest, Z);
    t1 = now_seconds();
    printf("MATRIX_SHA256=%s\n", digest);
    printf("HASH_RECOMPUTE elapsed=%.3f\n", t1 - t0);
    if (strcmp(digest, EXPECTED_SHA256) != 0)
        die("canonical matrix SHA-256 mismatch");
    printf("CERTIFIED: C checker reconstructed the frozen exact matrix fingerprint\n");
    fflush(stdout);

    for (k = 0; k < ladder_len; k++) {
        if (certify_spd_ldl(Z, ladder[k])) {
            printf("CERTIFIED_PRECISION=%ld\n", (long)ladder[k]);
            printf("CERTIFIED: exact hash-fixed 1075x1075 C-even integer matrix is positive definite by Arb LDL\n");
            printf("CERTIFIED: A_e >= 1e-35 I_1075 after the frozen finite-model ledger\n");
            fmpz_mat_clear(T);
            fmpz_mat_clear(Z);
            flint_cleanup();
            return 0;
        }
    }

    printf("UNDECIDED: exact hash-fixed matrix loaded correctly, but Arb LDL did not certify positivity on the precision ladder\n");
    fmpz_mat_clear(T);
    fmpz_mat_clear(Z);
    flint_cleanup();
    return 3;
}
