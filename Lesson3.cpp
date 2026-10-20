#include <iostream>
using namespace std;

int main() {
    int n,sum = 0;
    cin >> n;


     while (n > 0) {
        sum = sum + n % 10;
        n = n / 10;
    }

    cout << "Sum = " << sum;

int a,b;
cin >> a >> b;
for (int i = 1; i <= a && i <= b; i++) {
        if (a % i == 0 && b % i == 0) {
            cout << i << " ";
        }
    }

    return 0;

}