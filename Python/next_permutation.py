
#Approach: One Pass 
#traverse the list from right to left and find the first decreasing element, 
#then swap it with the smallest element to its right that is greater than it. 
#Finally, reverse the sublist to the right of the swapped element. 
#This approach takes only one pass through the list and is efficient.



class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #The first step is to initialize the variable i to len(nums) - 2. This is because we need to find the first decreasing element from right to left, 
        # and we start by checking the second-to-last element in the list. We also check that the current element is greater than the next element in the list
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        # Next, we check if i is greater than or equal to zero. If it is, we set the variable j to len(nums) - 1 and search for the smallest element to the right of i that is greater than nums[i]. 
        # We do this by decrementing j until we find an element that is greater than nums[i]:
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            # If we find such an element, we swap it with nums[i]:
            (nums[i], nums[j]) = (nums[j], nums[i])

        # Finally, we reverse the sublist to the right of i to get the lexicographically next permutation:
        nums[::] = nums[:i + 1] + nums[i + 1:][::-1]

        
        # Here, we concatenate the sublist nums[:i+1], which includes all elements up to and including the element at index i, with the reversed sublist nums[i+1:][::-1], which includes all elements after the element at index i, in reverse order. We then assign the resulting list to nums[::] to update the original list in place.

        #Overall, this implementation uses two passes through the list and avoids generating all possible permutations, making it an efficient solution for the Next Permutation problem.