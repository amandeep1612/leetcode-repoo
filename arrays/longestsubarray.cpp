#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

    int longestsubarray(vector<int> & nums,int k){
        int left =0;//initialindex of the window 
        int maxlength=0;// will store the longest valid length till now 
        int sum=0;// stores sum of current window 
        for (int right =0;right<nums.size();right++){
            //add current element to sum 
            sum+= nums[right];
            //if sum becomes greater than k then remove element from left
            while (sum>k && left<=right){
                sum-=nums[left];
                left++;

            }
            //if current window has sum k 
            //calculate its length
            if (sum==k){
                int length=(right-left+1);
                maxlength=max(maxlength,length);
 
            }

        }
        return maxlength;





    }

int main() {
    vector<int> nums = {10, 5, 2, 7, 1, 9};
    int k = 15;

    cout << longestsubarray(nums, k) << endl;

    return 0;
}