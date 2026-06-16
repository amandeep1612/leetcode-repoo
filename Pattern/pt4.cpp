#include <iostream>
using namespace std;
class solution {
    public:
    void pattern(int n){
        for(int i=1;i<=5;i++){
            for(int j=1;j<=i;j++){
                cout<<i;

            }
         cout<<endl;
        }

    }
};
int main(){
    solution s;
    s.pattern(5);
    return 0;
}