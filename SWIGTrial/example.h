#ifndef GUARD_example_h
#define GUARD_example_h

#include <string>
#include <vector>

int factorial(int); 


class User{
public:
    User() { }

    void setName(std::string n) { name = n; }
    std::string getName() { return name; }

    void addNumber(int n) { numbers.push_back(n); }
    int getNumberAt(int n) { 
        if (n < numbers.size()){
            return numbers[n];
        } else {
            return 0;
        }
    }

private:
    std::string name;
    std::vector<int> numbers;
    
};

#endif