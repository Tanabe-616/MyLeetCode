from typing import List
n1 = [1,3]
n2 = [2]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > 1000:
            return
        if len(nums2) > 1000:
            return
        
        for i in range(len(nums1)):
            flag = 0
            for j in range(len(nums2)):
                if nums1[i] < nums2[j]:
                    nums2.append(0)
                    tmp = 0
                    for k in range(len(nums2)-j-1):
                        tmp = nums2[k+j+1] 
                        nums2[k+j+1] = nums2[j]
                        nums2[j] = tmp
                    nums2[j] = nums1[i]
                    flag = 1
                    break
            if flag == 0:
                nums2.append(nums1[i])
        tmp = int(len(nums2)/2)-1
        if len(nums2)%2 == 0:
            anser = (nums2[tmp] + nums2[tmp+1])/2
        else:
            tmp = float(tmp)
            tmp += 1.5
            tmp = int(tmp)
            anser = nums2[tmp]
        
        
        return anser

a = Solution()
print(a.findMedianSortedArrays(n1,n2))
