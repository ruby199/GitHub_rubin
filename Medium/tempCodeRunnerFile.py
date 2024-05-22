            max_seen = max(max_seen, nums[i])
        
        # Find the left boundary
        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                start = i

            min_seen = min(min_seen, nums[i])
            
        return 0 if end - start < 1 else end - start + 1
