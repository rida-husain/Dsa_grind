class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      
    
     m = len(haystack)
     n = len(needle)

     if n==0 or m == 0:
        return 0

     for i in range(0,m-n+1):
        for j in range(0,n):

            if haystack[i+j] != needle[j]:
                break
            
            if j == n-1:
             return i

     return -1
