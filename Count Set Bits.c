#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
long long checkbit(long long n){
    int c=0;
    while(n!=0){
        if((n&1)==1){
            c++;
        }
        n=n>>1;
    }
    return c;
}
    

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t;
    scanf("%d",&t);
    while(t--){
        long long a;
        scanf("%lld",&a);
        printf("%lld\n",checkbit(a));
    }
    return 0;
}
