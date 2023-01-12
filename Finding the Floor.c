#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <limits.h>
using namespace std;
int floor(int arr[],int n,int x){
    int ans=INT_MIN;
    int low=0,high=n-1;
    while(low<=high){
        int mid=(low+high)/2;
        if(arr[mid]<=x){
            ans=arr[mid];
            low=mid+1;
        }
        else{
            high=mid-1;
        }
    }
    return ans;
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    scanf("%d",&n);
    int a[n];
    for (int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    sort(a,a+n);
    int q,x;
    scanf("%d",&q);
    for(int j=0;j<q;j++){
        scanf("%d",&x);
        printf("%d\n",floor(a,n,x));
    }
    
    return 0;
}
