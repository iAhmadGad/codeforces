#include <iostream>
#include <cmath>
using namespace std;

/*
* A - New Year Candles
*/

int main() {
	int a, b;
	cin >> a >> b;

	int hours = a;
	while(a >= b)
	{
		hours += a / b;
		a = a / b + a % b;
	}

	cout << hours;

	return 0;
}
