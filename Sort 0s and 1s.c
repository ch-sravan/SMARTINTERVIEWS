#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void sort(int a[],int n)
{
    int i=0,j=n-1;
    while(i<j)
    {
        if(a[i]==1 && a[j]==0)
        {
            int t=a[i];
            a[i]=a[j];
            a[j]=t;
            i++;
            j--;
        }
        else if(a[i]==0 && a[j]==1)
        {
            i++;
            j--;
        }
        else if(a[i]==0 && a[j]==0)
        {
            i++;
        }
        else
        {
            j--;   
        }
    }
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        int a[n];
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
        }
        sort(a,n);
        for(int i=0;i<n;i++){
            printf("%d ",a[i]);
        }
        printf("\n");
    }
    return 0;
}
