//https://www.codechef.com/problems/INTEST
#include<stdio.h>
int main()
{
    int n, k, i, t, c=0;
    scanf("%d %d",&n, &k);
    for(i=0;i<n;i++)
    {
        scanf("%d",&t);
        if(t%k==0)
        {
            c++;
        }
    }
    printf("%d",c);
    return 0;
}
