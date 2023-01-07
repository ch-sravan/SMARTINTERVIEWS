#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        long long arr[n],sum=0;
        for(int i=0;i<n;i++){
            scanf("%lld",&arr[i]);
            sum=sum+arr[i];  
        }
        printf("%lld\n",sum);
    }

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
