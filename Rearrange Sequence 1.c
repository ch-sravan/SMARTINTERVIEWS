#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<limits.h>
using namespace std;
int solve(int a[],int n)
{
    int ans=0;
    for(int i=0;i<n;i++)
    {
        int mi=INT_MAX;
        int ma=INT_MIN;
        for(int k=i;k<n;k++)
        {
            mi=min(mi,a[k]);
            ma=max(ma,a[k]);
            if(ma-mi==k-i)
            {
                ans=max(ans,k-i+1);
            }
        }
    }
    return ans;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t;
    scanf("%d",&t);
    while(t--){
        int  n;
        scanf("%d",&n);
        int a[n];
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
        }
        printf("%d\n",solve(a,n));
    }
    return 0;
}
