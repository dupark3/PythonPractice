#ifndef GUARD_example_h
#define GUARD_example_h

#include <string>
#include <vector>

int factorial(int); 


class User{
public:
    User() { }
    User(const std::string& n) : name(n) { }

    void setName(std::string n) { name = n; }
    std::string getName() { return name; }

    std::vector<int> getNumbers() { return numbers; }
    void addNumber(int n) { numbers.push_back(n); }
    int getNumberAt(int n) { 
        if (n < numbers.size()){
            return numbers[n];
        } else {
            return 0;
        }
    }

    void sortNumbers();

private:
    std::string name;
    std::vector<int> numbers;
    
};

#endif