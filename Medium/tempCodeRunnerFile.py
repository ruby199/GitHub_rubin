        nums_str = [str(item) for item in nums]
        n = len(nums_str)
        for i in range(n):
            for j in range(0, n - i - 1):
                comp1 = nums_str[j] + nums_str[j + 1]
                comp2 = nums_str[j + 1] + nums_str[j]
                if comp1 < comp2:  # If the current pair is in the wrong order
                    nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]  # Swap

        result = ''.join(nums_str)
        if result[0] == '0':  # Handle the edge case where the largest number is '0'
            return '0'
        return result