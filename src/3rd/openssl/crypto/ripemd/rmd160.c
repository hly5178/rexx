
#include <stdio.h>
#include <stdlib.h>
#include <openssl/ripemd.h>

#define BUFSIZE 1024*16

void do_fp(FILE *f);
void pt(unsigned char *md);
#if !defined(_OSD_POSIX) && !defined(__DJGPP__)
int read(int, void *, unsigned int);
#endif

int main(int argc, char **argv)
{
    int i, err = 0;
    FILE *IN;

    if (argc == 1) {
        do_fp(stdin);
    } else {
        for (i = 1; i < argc; i++) {
            IN = fopen(argv[i], "r");
            if (IN == NULL) {
                perror(argv[i]);
                err++;
                continue;
            }
            printf("RIPEMD160(%s)= ", argv[i]);
            do_fp(IN);
            fclose(IN);
        }
    }
    exit(err);
}

void do_fp(FILE *f)
{
    RIPEMD160_CTX c;
    unsigned char md[RIPEMD160_DIGEST_LENGTH];
    int fd;
    int i;
    static unsigned char buf[BUFSIZE];

    fd = fileno(f);
    RIPEMD160_Init(&c);
    for (;;) {
        i = read(fd, buf, BUFSIZE);
        if (i <= 0)
            break;
        RIPEMD160_Update(&c, buf, (unsigned long)i);
    }
    RIPEMD160_Final(&(md[0]), &c);
    pt(md);
}

void pt(unsigned char *md)
{
    int i;

    for (i = 0; i < RIPEMD160_DIGEST_LENGTH; i++)
        printf("%02x", md[i]);
    printf("\n");
}
