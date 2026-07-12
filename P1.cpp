#include <iostream>
using namespace std;

void print1(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n+1;j++){
            cout<<"*";
        }
        cout << endl;
    }}
void print2(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<i+1;j++){
            cout<<"*";
        }
        cout << endl;
    }
}
void print3(int n){
    for(int i=1;i<n+1;i++){
        for(int j=1;j<i+1;j++){
            cout<<j;
        }
        cout << endl;
    }
}
void print4(int n){
    for(int i=1;i<n+1;i++){
        for(int j=1;j<i+1;j++){
            cout<<i;
        }
        cout << endl;
    }
}
void print5(int n){
    for(int i=1;i<=n;i++){
        for(int j=0;j<n-i+1;j++){
            cout<<"*";
        }
        cout << endl;
    }
}
void print7(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++){
            cout<<" ";
        }
        for(int j=0;j<2*i+1;j++){
            cout<<"$";
        }
        for(int j=0;j<n-i-1;j++){
            cout<<" ";
        }
        cout << endl;
    }
}
int main(){
    int n;
    cin>>n;
    print7(n);
}

