%module example
%include "std_string.i"
%include "std_vector.i"
%{
#include "example.h"

%}

namespace std{
    %template(IntVector) vector<int>;
};

%include "example.h"