#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int x, y;
    int n;
    scanf("%d", &n);

    for (x = 0; x < n; x++)
    {
        for (y = 0; y < (n-1) - x; y++)
            printf(" ");
        for (y = (n-1) - x; y < n; y++)
            printf("*");
        printf("\n");
    }

    return 0;
}