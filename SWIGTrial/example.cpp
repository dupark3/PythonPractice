#include <algorithm>
#include <vector>
#include <string>

#include "example.h"

using namespace std;

int factorial(int n){
    if (n == 0)
        return 1;
    else
        return n * factorial(n - 1);
}

void User::sortNumbers(){
    sort(numbers.begin(), numbers.end());
}