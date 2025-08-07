#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void)
{
	int i;
	int n;
	int result=1;
	scanf("%d", &n);

	for (i = 1; i <= n; i++)
	{
		result *= i;
		if (n == 0)
			printf("1");
	}
	printf("%d", result);
	return 0;
}