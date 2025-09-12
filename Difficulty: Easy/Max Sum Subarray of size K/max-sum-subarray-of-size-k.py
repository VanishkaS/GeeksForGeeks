class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        i=0
        j=0
        max_sum=float('-inf')
        local=0
        while j<k:
            local+=arr[j]
            j+=1
        max_sum=local
        while j<len(arr):
            local=local-arr[i]+arr[j]
            max_sum=max(local,max_sum)
            i+=1
            j+=1
        return max_sum
        