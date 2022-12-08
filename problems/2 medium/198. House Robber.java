class Solution {
    public int rob(int[] nums) {
        if(nums == null || nums.length == 0 ) return 0;
        if(nums.length == 1) return nums[0];
		int robIncludingLast = 0;
		int robExcludingLast = 0;
        for (int n: nums) {
			int tmp = Math.max(robIncludingLast, robExcludingLast+n);
			robExcludingLast = robIncludingLast;
			robIncludingLast = tmp;
		}
        return robIncludingLast;
    }
}