#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
  ll testcase;
  cin>>testcase;
  while(testcase--)
  {
    ll n,k;
    cin>>n>>k;
    string s1;
    cin>>s1;
    string s2=s1;
 
    ll i=0;
    ll x=n;
    while(i<n)
    {
        string s;
 
      if(s1[i]=='1' && s1[i-1]!='1')
      {
        s=s1.substr(i,n-i)+s1.substr(0,i);
      }
      if (s>s2)
      {
        s2=s;
        x=i;
      }
      i++;
    }
 
 
    vector<int> pi(n);
 
    for(ll i=1;i<n;i++)
    {
      ll j=pi[i-1];
      while(j>0 && s2[i]!=s2[j])
      {
        j=pi[j-1];
      }
      if(s2[i]==s2[j])
      {
        j++;
      }
      pi[i]=j;
    }
    int val=n-pi[n-1];
    ll ans=(k-1)*val+(1)*(x);
 
    if (x==n)
    {
      cout<<(k-1)*val<<endl;
    }
    else
    {
      cout<<ans<<endl;
    }
 
  }
  return 0;
}