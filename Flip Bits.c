#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
long long checkbit(long long n){
    long long count=0;
    while(n!=0){
        if((n&1)==1){
            count++;
        }
        n=n>>1;
    }
    return count;
}
int FlippedCount(int a,int b)
{
    return checkbit(a^b);
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int t;
    scanf("%d",&t);
    while(t--){
        int x,y;
        scanf("%d %d",&x,&y);
        printf("%d\n",FlippedCount(x,y));
    }
    return 0;
}
