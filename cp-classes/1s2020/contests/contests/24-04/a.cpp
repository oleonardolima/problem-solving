#include <iostream>
#include <bits/stdc++.h>
#include <math.h> 

using namespace std;
int calc_nth_fib(int n, int moduloed_fibonacci) {
    if (n == 1) {
        return 1;
    }

    int ptr1 = 1;
    int ptr2 = 1;
    int counter = 3;
    while (counter <= n) {
        int next_num = (int) (ptr1 + ptr2) % moduloed_fibonacci;
        ptr1 = ptr2;
        ptr2 = next_num;
        counter++;
    return ptr2;
    }
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 

    int moduloed_fibonacci = (int) pow(10, 8) + 7;
    int num_test_case;
    cin >> num_test_case;
    for (int i = 0; i < num_test_case; i++) {
        int nth_fibonacci;
        cin >> nth_fibonacci;
        nth_fibonacci = calc_nth_fib(nth_fibonacci, moduloed_fibonacci);
        cout << nth_fibonacci << "\n";
    }
}