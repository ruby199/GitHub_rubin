        # Sort the array using merge sort.
        sorted_heights = heights[:]
        temp_arr = [0] * len(heights)
        merge_sort(sorted_heights, 0, len(sorted_heights) - 1, temp_arr)

        count = 0
        # Loop through the original and sorted arrays.
        for i in range(len(sorted_heights)):
            # Increment count if elements at the same index differ.
            if heights[i] != sorted_heights[i]:
                count += 1
        # Return the total count of differing elements.
        return count
