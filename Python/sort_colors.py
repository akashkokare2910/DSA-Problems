class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red_color,white_color,blue_color = 0,0, len(nums)-1

        while white_color <= blue_color:
            if nums[white_color] == 0:
                nums[red_color],nums[white_color]= nums[white_color],nums[red_color]
                red_color += 1
                white_color += 1
            
            elif nums[white_color] == 1:
                white_color += 1
            
            else:
                nums[white_color],nums[blue_color]=nums[blue_color],nums[white_color]
                blue_color -= 1