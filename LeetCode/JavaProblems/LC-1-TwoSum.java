import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer,Integer> numMap = new HashMap<Integer,Integer>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numMap.containsKey(complement)) {
                return new int[]{i,numMap.get(complement)};
            }
            numMap.put(nums[i], i);
        }
        return new int[]{};
    }
}