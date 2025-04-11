#include "amigos.h"


int main(){
	FASTIO();
	string input_string = R"(3
2 3
5 -2
0 -1)";

	SYNC_STDIN(input_string);

	ll mod_of = pow(10,9) + 1;
	cout << mod_of << "\n";
	ll test_cases;
	cin >> test_cases;
	cin.ignore();
	cout<<test_cases<<"\n";
	ll base,exponent;
	while(test_cases--){
		cin>>base>>exponent;
		if(base <= 0){
			cout << 1 << "\n";
		}
		else if(exponent > 0){
			ll result = pow(base,exponent); 
			cout<< result % mod_of <<"\n";
		}else{
			/*
			*
			*  2 -1
			*  1/2
			*/ 
			ll num_exponent = ~exponent+1;
			ll num_base = pow(base,num_exponent);
			ll output = 1 / num_base;
			cout << output % mod_of << "\n";
		}
	}
}
