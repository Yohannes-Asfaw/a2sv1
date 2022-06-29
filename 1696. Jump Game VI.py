    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = [(-nums[0], 0)]
        heapify(heap)
        for i in range(1, n):
            while heap[0][1] < max(0, i - k):
                heappop(heap)
            
            nums[i] -= heap[0][0]
            heappush(heap, (-nums[i], i))
        
        return nums[-1]
