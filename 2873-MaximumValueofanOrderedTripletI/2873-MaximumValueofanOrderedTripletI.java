// Last updated: 4/1/2025, 9:18:15 PM
class Solution {
    public long maximumTripletValue(int[] nums) {
        long res = 0;
        long maxValue = 0;
        long maxPair = 0;

        for(int cur : nums) {
            res = Math.max(res, (long) maxPair * cur);
            maxPair = Math.max(maxPair, maxValue - cur);
            maxValue = Math.max(maxValue, cur);
        }

        return res;
    }
}