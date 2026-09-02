#include<iostream>
#include<vector>
#include<algorithm>
#include<unordered_map>
using namespace std;
int longestzerosumsubarray(vector<int>&nums){
    unordered_map(<int,int>) firstIndex;
    int prefixsum=0;
    int maxlenght=0;
    for (int i=0;i<nums.size;i++){
        prefixsum+=nums[i];
        if (prefixsum==0){
            
        }
    }



}