class Solution {
  /**
   * @param {number[]} nums
   * @param {number} target
   * @return {number[]}
   */
  twoSum(nums, target) {
    // Create tow pointers (start and end)
    let start = 0,
      end = nums.length - 1;

    // Sort the array
    nums.sort();

    // Iterate over the array, checking when the smallest
    // number plus the highest number equals the target
    while (nums[start] + nums[end] !== target) {
      if (nums[start] + nums[end] < target) {
        start++;
        continue;
      }
      end--;
    }
    return [start, end];
  }
}

const nums = [5, 5];
const target = 10;

const solution = new Solution();
console.log(solution.twoSum(nums, target));
