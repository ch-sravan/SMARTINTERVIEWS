#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
long long mypow(long long x,long long y){
    long long ans=1;
    while(y!=0){
        if((y&1)==1){
            ans=(ans*x)%1000000007;
        }
        x=(x*x)%1000000007;
        y=y>>1;
    }
    return ans%1000000007;
}
int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t;
    scanf("%d",&t);
    while(t--){
        long long a,b;
        scanf("%lld %lld",&a,&b);
        printf("%lld\n",mypow(a,b));
    }
    
    return 0;
}
