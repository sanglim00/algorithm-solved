function solution(nums) {
    
    const mySet = new Set(nums);
    return mySet.size < nums.length / 2 ? mySet.size : nums.length / 2 ;
}