# include<iostream>
using namespace std;
class solution{
    public:
    void pattern(int n){
        for (int i=0;i<n;i++){
            for(int j=1;j<=i;j++){
                cout<<j;

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