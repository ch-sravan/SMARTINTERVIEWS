#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void Mergesort(int arr[],int low,int mid,int high)
{
    int r=high-low+1;
    int temp[r],p1=low,p2=mid+1,k=0;
    while(p1<=mid && p2<=high)
    {
        if(arr[p1]<arr[p2])
        {
            temp[k++]=arr[p1++];
        }
        else
        {
            temp[k++]=arr[p2++];
        }
    }
    while(p1<=mid)
    {
        temp[k++]=arr[p1++];
    }
    while(p2<=high)
    {
        temp[k++]=arr[p2++];
    }
    for(int i=0;i<r;i++)
    {
        arr[low+i]=temp[i];
    }
}
void Ms(int arr[],int low,int high)
{
    if(low<high)
    {
        int mid=(low+high)/2;
        Ms(arr,low,mid);
        Ms(arr,mid+1,high);
        Mergesort(arr,low,mid,high);
    }
}
int triples(int arr[],int n,int k)
{
    for(int i=0;i<n-1;i++)
    {
        int a=i+1;
        int b=n-1;
        int c=arr[i];
        while(a<b)
        {
            if(arr[a]+arr[b]+c==k)
            {
                return 1;
            }
            else if(arr[a]+arr[b]+c<k)
            {
                a++;
            }
            else
            {
                b--;
            }
        }
    }
    return 2;
}
int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        int low=0,high=n-1;
        int arr[n];
        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
        }
        Ms(arr,low,high);
        int s= triples(arr,n,k);
        if(s==1)
        {
            printf("true\n");
        }
        else
        {
            printf("false\n");
        }
    }
    return 0;
}
