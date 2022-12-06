class Solution {
    public boolean canJump(int[] nums) {
        int goalpost = nums.length - 1;
//		start with the penultimate position
		for (int i = nums.length -2; i >= 0; i--) {
			if(nums[i]+i >= goalpost) {
				goalpost = i;
			}
		}
		if (goalpost == 0) {return true;}
		return false;
    }
}