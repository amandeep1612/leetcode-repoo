#include <iostream>
#include<vector>
using namespace std;
int linear_Search(vector<int>& arr,int num){
    for(int i=0;i<arr.size();i++){
        if(arr[i]==num){
            return i;
        }

    }
    return -1;

}
int main() {
    vector<int> arr = {10, 20, 30, 40, 50};
    int num = 30;

    int index = linear_Search(arr, num);

    if (index != -1) {
        cout << "Element found at index: " << index;
    } else {
        cout << "Element not found";
    }

    return 0;
}