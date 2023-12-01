class Solution:
    def partitionLabels(self, s: str):
        # Build hash map (every character -> last index in s)
        lastIndex = {}

        # Iterate over the string 's'. For each character 'c' at index 'i',
        # update lastIndex to store 'i' as the last occurrence of 'c'.
        for i, c in enumerate(s):
            lastIndex[c] = i

        # Initialize a list 'res' to store the sizes of each partition.
        # Initialize 'size' to track the current partition's size and 'end' to track the
        # end index of the current partition.
        res = []
        size, end = 0, 0

        # Iterate over the string 's' again.
        for i, c in enumerate(s):
            # Increment the size of the current partition for each character.
            size += 1

            # Update 'end' to be the maximum of its current value or the last index of 'c'.
            # This ensures that the partition includes all occurrences of 'c'.
            end = max(end, lastIndex[c])

            # If the current index 'i' is equal to 'end', it indicates the end of the current
            # partition. Append the size of this partition to 'res' and reset 'size' for the next partition.
            if i == end:
                res.append(size)
                size = 0

        # Return the list of partition sizes.
        return res
    

def test_partition_labels():
    solution = Solution()

    # Test cases: A list of tuples, each containing the input string and the expected output.
    test_cases = [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
        ("a", [1]),
        ("abcd", [1, 1, 1, 1]),
        # Add more test cases as needed
    ]

    # Iterating through each test case
    for i, (input_str, expected_output) in enumerate(test_cases):
        # Getting the actual output from the function
        actual_output = solution.partitionLabels(input_str)

        # Comparing the actual output with the expected output
        assert actual_output == expected_output, f"Test case {i+1} failed: Expected {expected_output}, got {actual_output}"

        print(f"Test case {i+1} passed.")

# Run the test function
test_partition_labels()
