import time


class Solution:
  # Iterativo
  '''
  def search(self, nums: list[int], target: int) -> int:    
    size = len(nums)

    start = 0    
    end = size - 1
    middle = (start + end) // 2

    while start <= end:
      if nums[middle] == target:
        return middle
      
      if nums[middle] < target:
        start = middle + 1
      else:
        end = middle - 1

      middle = (start + end) // 2

    return -1
  '''

  # Recursivo
  def search(self, nums: list[int], target: int) -> int:  
    return self.searchAux(nums, 0, len(nums) - 1, target)

  
  def searchAux(self, nums: list[int], start, end, target: int) -> int:
    middle = (start + end) // 2

    if start > end:
      return -1
    
    if nums[middle] == target:
      return middle

    if nums[middle] < target:
      return self.searchAux(nums, middle + 1, end, target)
    
    return self.searchAux(nums, start, middle - 1, target)

    

    
  

  
solution = Solution()

nums = [-1,0,2,4,6,8]
target = 3


print(solution.search(nums, 0, len(nums) - 1, target))