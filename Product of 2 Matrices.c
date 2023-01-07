#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t;
    scanf("%d",&t);
    while(t--){
        int n1,m1;
        scanf("%d%d",&n1,&m1);
        int a[n1][m1];
        for(int i=0;i<n1;i++)    
        {    
            for(int j=0;j<m1;j++)    
            {    
                scanf("%d",&a[i][j]);    
            }    
        }  
        int n2,m2;
        scanf("%d%d",&n2,&m2);
        int b[n2][m2];
        for(int i=0;i<n2;i++)    
        {    
            for(int j=0;j<m2;j++)    
            {    
                scanf("%d",&b[i][j]);    
            }    
        }  
        int prod[n1][m2];    
        for(int i = 0; i < n1; i++)
        {  
            for(int j = 0; j < m2; j++)
            {  
                prod[i][j] = 0;  
                for(int k = 0; k < n2; k++)
                {  
                   prod[i][j] = prod[i][j] + a[i][k] * b[k][j];   
                }
                printf("%d ",prod[i][j]);
            }
            printf("\n");
        } 
        
    }
        return 0;   
}
