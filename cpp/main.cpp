#include<bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int n;
	cin>>n;
	(n & (n-1))==0 ? cout<<"True" : cout<<"False";
	cout<<"\n";
}
