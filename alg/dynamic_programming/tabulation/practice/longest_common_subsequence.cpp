#include<bits/stdc++.h>
using namespace std;

#define SYNC_STDIN(input) \
    istringstream in(input); \
    streambuf* orig_cin = cin.rdbuf(in.rdbuf());

#define RESTORE_STDIN() cin.rdbuf(orig_cin);

/*
 
			   ""   A   B   C   D   G   H
			------------------------------
		   ""   |   0   0   0   0   0   0   0
		   A    |   0   1   1   1   1   1   1
		   E    |   0   1   1   1   1   1   1
		   D    |   0   1   1   1   2   2   2
		   F    |   0   1   1   1   2   2   2
		   H    |   0   1   1   1   2   2   3
		   R    |   0   1   1   1   2   2   3

 */

/*
*	A B C D G H
*    A  1 1 1 1 1 1
*    E  1 1 1 1 1 1
*    D  1 1 1 2 2 2
*    F  2 2 2 2 2 2
*    H  2 2 2 2 2 3
*    R  3 3 3 3 3 3
*
*
*/


int main(){
	string input = R"(ABCDGH
AEDFHR)";

	SYNC_STDIN(input);
	string s,t;
	cin >> s >> t;
	cout << s << "\n";
	cout << t << "\n";
	
	int n = s.size();
	int m = t.size();

	int dp[n+1][m+1];
	for (int _i = 0;_i <= n;++_i)
		dp[_i][0] = 0;

	for (int _j = 0;_j <= m;++_j)
		dp[0][_j] = 0;



	for(int i = 1;i <= n;++i){
		for(int j = 1;j <= m;++j){
			if(s[i] == t[j]){
				dp[i][j] = dp[i-1][j-1] + 1;
			}else{
				dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
			}
		}
	}

	cout <<  dp[n][m] << "\n";

}
