class Solution {
    public int minMoves(int[] nums) {
        int net = 0, min = nums[0], len = nums.length;  
        for (int i = 0; i < len; i++) {
            net += nums[i]; 
            if (nums[i] < min) min = nums[i] ; 
        }
        return net - min * len ; 
    }
}