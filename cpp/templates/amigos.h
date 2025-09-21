#include<bits/stdc++.h>
using namespace std;

#define SYNC_STDIN(input) \
    istringstream in(input); \
    streambuf* orig_cin = cin.rdbuf(in.rdbuf());

#define RESTORE_STDIN() cin.rdbuf(orig_cin);

#define ll long long

#define FASTIO() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

#define PARSE_CSV_TO_VECTOR(str, vec) { \
    stringstream ss(str); \
    string temp; \
    while (getline(ss, temp, ',')) { \
        vec.push_back(stoi(temp)); \
    } \
}

#define PRINT_VECTOR(vec) { \
    cout << "[ "; \
    for (auto &_v : vec) cout << _v << " "; \
    cout << "]\n"; \
}

#define PRINT_ARRAY(arr, n) { \
    cout << "[ "; \
    for (int _i = 0; _i < (n); ++_i) cout << arr[_i] << " "; \
    cout << "]\n"; \
}

