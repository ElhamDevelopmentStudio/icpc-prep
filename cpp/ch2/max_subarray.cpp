#include<bits/stdc++.h>
using namespace std;

int main(){
	int arr[] = {-1,2,4,-3,5,2,-5,2};
	int sum = 0;
	int best = 0;
	for (int i = 0;i < 7;i++){
		sum = max(arr[i],sum+arr[i]);
		best=max(sum,best);
	}
	std::cout<<best<<"\n";

	return 0;
}
