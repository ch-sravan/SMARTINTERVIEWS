#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int n;
        printf("Case #%d:\n",i);
        scanf("%d",&n);
        for(int r=1;r<=n;r++)
        {
            for(int s=0;s<=n-r-1;s++)
            {
                printf(" ");
            }
                for(int c=1;c<=r;c++)
                {
                    printf("*");
                }
             printf("\n");
            }
        }
    return 0;
}
