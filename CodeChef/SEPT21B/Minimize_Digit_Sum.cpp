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
   int t;
   cin>>t;
   while(t--)
   {
      int n,l,r,ds,nb,base,i,min=INT32_MAX;
      cin>>n>>l>>r;
      for(i=r;i>=l;i--)
      {
        ds=0;
        nb=n;
        if(r>=n && n%i==0)
        {
          base=i;
          break;
        }
        while(nb>0)
        {
          ds+=nb%i;
          nb/=i;
        }
        if(min>ds)
        {
          min=ds;
          base=i;
        }
        if(min==1)
        {
          break;
        }
      }
      cout<<base<<endl;
   }
   return 0;
}
