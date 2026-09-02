#include<iostream>
#include<vector>
#include<algorithm>
#include<unordered_map>
using namespace std;
int longestsum0(vector<int> &nums){
    unordered_map<int,int>firstindex;//here we are creating an map key-prefixsum; value;- nearest index[9:0]
    int prefixsum=0;//initially 0
    int maxlength=0;//initially 0 longest 0 sum subarray found so far
    for(int i=0;i<nums.size();i++){
        prefixsum+=nums[i];//adds value of array to prefix sum
        if (prefixsum==0){
            maxlength=i+1;
        }
        if (firstindex.count(prefixsum)){//checks whether the prefix sum number has appeared in the map
            int previousindex=firstindex[prefixsum];//index of where the prefix sum is 
            int length=i-previousindex;//
            maxlength=max(maxlength,length);//Calculates the length of the zero-sum subarray.
        }
        else{
            firstindex[prefixsum]=i;//Stores the current prefix sum and its index.


        }

    }
    return maxlength;






}

int main (){
    vector<int> nums ={9, -3, 3, -1, 6, -5};
    cout<<longestsum0(nums)<<endl;
    return 0;

}

 
