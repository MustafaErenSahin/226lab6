#include <iostream>
using namespace std;

int x = -1;

double sum(int n){
    if(n == 0){
        return 0;
    }
    return (1.0 / n) + sum(n - 1);
}

double sum(){
    if(x == -1){
        cout<<"Enter int"<<endl;
        cin>>x;
    }
    if(x == 0){
        return 0;
    }
    return (1.0 / x) + sum(x - 1);
}

int main()
{
    cout<<sum(3)<<endl;
    cout<<sum();
    return 0;
}
