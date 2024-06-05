class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:  # left part is sorted
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

  def search2(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[l] <= nums[mid]:
                    if nums[l] <= target:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[r] >= nums[mid]:
                    if nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    l = mid + 1
        return -1
