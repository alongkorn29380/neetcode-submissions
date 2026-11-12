public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // 1. set dict obj to collect arr value
        // <value, index>
        Dictionary<int, int> temp = new();
        
        for(int i = 0; i < nums.Length; i++){
            // nums[i] + key in dict
            int findTarget = target - nums[i]; 
            if (temp.ContainsKey(findTarget)) {
                return [temp[findTarget], i];
            }
            else {
                temp.Add(nums[i], i);
            }
        }

        return [];
    }
}
