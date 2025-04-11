#include "amigos.h"


int main(){
	FASTIO();
	string input_string = R"(11
1,2,5)";
	SYNC_STDIN(input_string);

	int amount;
	cin >> amount;
	cin.ignore();

	string coins_string;
	getline(cin,coins_string);

	cout << coins_string <<"\n";
	vector<int> coins;
	PARSE_CSV_TO_VECTOR(coins_string,coins);
	int m = coins.size();
	vector<int> dp(amount+1,INT_MAX);
	int n = dp.size();
	dp[0] = 0;
	/*
	* 0 1 2 3 4 5 6 7 8 9 10 11
	* 0 1 2 
	*
	*/

	for(int i = 1;i <= n;++i){
		for(int j = 0;j <= m;++j){
			if(i - coins[j] >= 0 && dp[i-coins[j]] != INT_MAX){
				dp[i] = min(
					dp[i],
					1+dp[i-coins[j]]
				);
			}
			
		}
	}
	//PRINT_VECTOR(dp);
	cout << dp[n-1] << "\n";


}
