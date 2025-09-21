#include "amigos.h"



int main(){
	FASTIO();
	string input = R"(5
2, 3, 1, 1, 4)";
	int n;
	SYNC_STDIN(input);
	cin >> n;
	cin.ignore();


	string input_string;
	getline(cin,input_string);
	vector<int> arr;
	PARSE_CSV_TO_VECTOR(input_string,arr);

	vector<int> dp(n,0);
	//PRINT_ARRAY(dp,n);
	
	dp[0] = 1;
	for(int i = 0; i <= n;++i){
		if(i+arr[i] < n){
			dp[i+arr[i]] = 1;
		}
	}
	//PRINT_VECTOR(dp);
	//cout << n << "\n";
	string result = dp[n-1] == 0 ? "False" : "True";
	cout << result << "\n";

}
