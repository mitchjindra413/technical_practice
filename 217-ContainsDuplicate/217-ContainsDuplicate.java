class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<>();

        for(int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if(s.contains(num)) {
                return true;
            }
            s.add(num);
        }
        return false;
    }
}