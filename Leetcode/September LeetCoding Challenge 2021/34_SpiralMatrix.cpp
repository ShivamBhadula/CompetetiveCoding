#include <bits/stdc++.h>
using namespace std;
#define pi (3.141592653589)
#define mod 1000000007
//#define int long long int
#define float double
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(c) c.begin(), c.end()
#define min3(a, b, c) min(c, min(a, b))
#define min4(a, b, c, d) min(d, min(c, min(a, b)))
#define rfo(i, n) for(int i=n-1;i>=0;i--)
#define fo(i,n) for(int i=0;i<n;i++)
#define fast ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);


int32_t main()
{
   fast
   int m,n;
   cin>>m>>n;
   int a[m][n];
   for(int i=0;i<m;i++)
   {
       for(int j=0;j<n;j++)
       {
           cin>>a[i][j];
       }
   }
   int top=0;
   int down=m-1;
   int right=n-1;
   int left=0;
   string dir="right";
   while (top<=down && left<=right)
   {
       if (dir=="right")
       {
           for(int i=left;i<=right;i++)
           {
               cout<<a[top][i]<<" ";
           }
           top++;
           dir="down";
       }
        else if(dir=="down")
        {
            for(int i=top;i<=down;i++)
            {
                cout<<a[i][right]<<" ";
            }
            right--;
            dir="left";
        }
        else if(dir=="left")
        {
            for(int i=right;i>=left;i--)
            {
                cout<<a[down][i]<<" ";
            }
            down--;
            dir="up";
        }
        else
        {
            for(int i=down;i>=top;i--)
            {
                cout<<a[i][left]<<" ";
            }
            left++;
            dir="right";
        }
        cout<<endl;
   }
   return 0;
}
