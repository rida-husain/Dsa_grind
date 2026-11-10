class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def left_most():
            l = 0
            h = len(nums) - 1
            ans = -1

            while l <= h:
                mid = l + (h - l) // 2

                if nums[mid] == target:
                    ans = mid
                    h = mid - 1

                elif nums[mid] < target:
                    l = mid + 1

                else:
                    h = mid - 1

            return ans

        def right_most():
            l = 0
            h = len(nums) - 1
            ans = -1

            while l <= h:
                mid = l + (h - l) // 2

                if nums[mid] == target:
                    ans = mid
                    l = mid + 1

                elif nums[mid] < target:
                    l = mid + 1

                else:
                    h = mid - 1

            return ans

        first = left_most()
        last = right_most()

        return [first, last]