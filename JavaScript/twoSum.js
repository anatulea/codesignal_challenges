
// Two Sum II - 

// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input will have at most one solution, and you may not use the same index twice.

// In case no solution exists, return [-1, -1]

// Example:

// Input: nums = [2, 7, 11, 15], target = 9
// Output: [0, 1]
// Explanation: nums[0] + nums[1] = 2 + 7 = 9


//O(n log n) Advanced
class Solution {
    /**
    * @param {number[]} nums
    * @param {number} target
    * @return {number[]}
    */
    binarySearch(sortedNums, first, last, value){
        while(first <= last){
            let middle = first + Math.floor((last - first) / 2);
            if(sortedNums[middle][0] == value) {
                return middle;
            } else if (sortedNums[middle][0] < value) {
                first = middle + 1;
            } else {
                last = middle - 1;
            }
        }
        return -1;
    }
    
    twoSum(nums, target) {
    let sortedNums = []
    for(let i= 0; i<nums.length; i++){
        sortedNums.push([nums[i], i]);
    }
    sortedNums.sort((first, second)=>{return first[0]- second[0]})
    
    for (let i=0; i<sortedNums.length; i++){
        let j = this.binarySearch(sortedNums,i+1, sortedNums.length-1, target- sortedNums[i][0]);
        if(j != -1){
            return[sortedNums[i][1], sortedNums[j][1]];
        }
    }
    return [-1, -1]
    }
};



//  O(n^2)
twoSum(nums, target) {
    for (let i=0; i<nums.length; i++)
        for (let j = i+1; j <nums.length; j++);
            if(nums[i]+nums[j]===target){
                return [i, j];
            } 
        return[-1,-1];
};


// O(n log n) + O(n)
class Solution {
    /**
    * @param {number[]} nums
    * @param {number} target
    * @return {number[]}
    */
    twoSum(nums, target) {
        let sortedNums = [(0,0)]
        for (let i = 0; i< nums.length; i++){
            sortedNums[i] = [nums[i],i];
        
        }
        sortedNums.sort((first, second)=>first[0]-second[0])
        let first = 0
        let last = sortedNums.length-1
        
        while (first < last){
            let sum = sortedNums[first][0]+ sortedNums[last][0]
            if (sum === target){
                return[ sortedNums[first][1], sortedNums[last][1]]
            }else if(sum<target){
                first+=1
            }else{
                last-=1
            }
            
        }
        return [-1,-1]
     
    }
}

// O(n)
class Solution {
    /**
    * @param {number[]} nums
    * @param {number} target
    * @return {number[]}
    */
    twoSum(nums, target) {
        let indexOfValue = {};
        for (let i = 0; i < nums.length; i++ ) {
            if (target - nums[i] in indexOfValue) {
                return [i, indexOfValue[target - nums[i]]];
            }
            indexOfValue[nums[i]] = i;
        }
        return [-1, -1];
    }
}
