class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        while True:
            m = (l + r) // 2 # portion from A
            n = half - (m + 1) - 1 # portion from B

            Aleft = A[m] if m >= 0 else float("-inf")
            Bleft = B[n] if n >= 0 else float("-inf")
            Aright = A[m + 1] if (m + 1) < len(A) else float("inf")
            Bright = B[n + 1] if (n + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # if odd:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1
            
        return 0
                

