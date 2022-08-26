#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef set<int> si;
#define PB push_back

const int N=9999;
int dp[N][N];
int w[N],v[N];
int main()
{
   ios::sync_with_stdio(0);
   cin.tie(0);
   int t,m;
   cin>>t>>m;
   for(int i=1;i<=m;i++)cin>>w[i]>>v[i];
   for(int i=1;i<=m;i++){
   	for(int j=1;j<=t;j++){
   		if(j>=w[i]){
   			dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]);
   		}else{
   			dp[i][j]=dp[i-1][j];
   		}
   	}
   }
   int ans=0;
   for(int i=1;i<=t;i++)ans=max(ans,dp[m][i]);
   	cout<<ans<<endl;
}
