#include "amigos.h"


int main(){
	FASTIO();
	string input_string = R"(10)";
	SYNC_STDIN(input_string);

	int n;
	cin >> n;


	vector<int> dp(n+1,0);
	// one way to create 1
	dp[1] = 1;

	/*
	* 0 1 2 3 4 5 6
	* 0 1 1 1 
	*/
	for(int i = 2;i <= n;++i){
		if(i % 2 == 0){
			int mod = i / 2;
			dp[i] = dp[mod] + 1;
		}if(i % 3 == 0){
			int mod = i / 3;
			//cout << "here with mod 2 " << i << "and dp mod of "<<dp[mod] << "\n";
			dp[i] = dp[mod] + 1;
		}else{
			dp[i] = dp[i-1] + 1;
		}
	}

	PRINT_VECTOR(dp);
	cout << dp[n-1] << "\n";

}
