class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1 = []
        a2 = []
        tot = []
        count = 0
        for num in nums1:
            a1.append(num)
        for num in nums2:
            a2.append(num)
        for num in nums1:
            if num in nums2:
                tot.append(num)
                nums2.remove(num)
        return tot
