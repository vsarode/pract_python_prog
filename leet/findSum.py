class Solution:
    def linearSearch(self, nums, key):
        for i, num in enumerate(nums):
            if key == num:
                return i
        return -1

    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            index = self.linearSearch(nums[i + 1:], target - num)
            if index >= 0:
                if index == 0:
                    last_index = i + 1
                else:
                    last_index = index + i + 1
                return [i, last_index]

if __name__ == '__main__':
    input = [
        {"list": [2, 7, 11, 15], "key": 9, "expected": [0, 1]},
        {"list": [3, 2, 4], "key": 6, "expected": [1, 2]},
        {"list": [3, 3], "key": 6, "expected": [0, 1]},
        {"list": [3, 2, 3], "key": 6, "expected": [0, 2]}
    ]
    for l in input:
        print(Solution().twoSum(nums=l['list'], target=l['key']))
        print("***************************")

    # print binarySearch(l,7,0,4)
#
# class Solution {
    def binarySearch(self, arr, k, l, r):
        if l < r:
            m = (l + r) / 2
            # print m
            if arr[m] == k:
                return m
            if arr[m] > k:
                return self.binarySearch(arr, k, l, m)
            else:
                return self.binarySearch(arr, k, m + 1, r)
        return None
#
#
#     def twoSum(self,nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         tempArray = sorted(nums)
#         for i, num in enumerate(tempArray):
#             # print i, num, tempArray[i+1:]
#             index = self.binarySearch(tempArray[i+1:], (target - num), i+1, len(tempArray[i+1:]))
#             # print index
#             if index:
#                 if num == (target - num):
#                     firstIndex = nums.index(num)
#                     secondIndex = nums[firstIndex + 1:].index(target - num) + 1
#                     return [firstIndex, secondIndex]
#                 return [nums.index(num), nums.index(target - num)]

#
# class Solution:
#     def binarySearch(self, arr: List[int], k: int, l: int, r: int) -> int:
#         if l < r:
#             m = int((l + r) / 2)
#             if arr[m] == k:
#                 return m
#             if arr[m] > k:
#                 return self.binarySearch(arr, k, l, m)
#             else:
#                 return self.binarySearch(arr, k, m + 1, r)
#         return None
#
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#
#         tempArray = sorted(nums)
#         for i, num in enumerate(tempArray):
#             index = self.binarySearch(tempArray[i + 1:], (target - num), 0, len(tempArray[i + 1:]))
#             if index != None:
#                 firstIndex = nums.index(num)
#                 secondIndex = nums[firstIndex:].index(target - num) + firstIndex if firstIndex != 0 else 1
#                 return [firstIndex, secondIndex]