class Solution:
    def trap(self, height: List[int]) -> int:

        vol = 0
        l = r = 0

        # Find location of the maximum peak
        max_height = height[0]
        max_height_idx = 0
        for i in range(len(height)):
            if height[i] > max_height:
                max_height = height[i]
                max_height_idx = i

        # Climb the mountain from left to right
        while r < max_height_idx:
            prev_height = height[l]

            while height[r] < prev_height:
                r += 1

            while l < r:
                vol += prev_height - height[l]
                l += 1
            
            r += 1

        # Climb the mountain from right to left            
        l = r = len(height) - 1
        while l > max_height_idx:
            prev_height = height[r]

            while height[l] < prev_height:
                l -= 1

            while r > l:
                vol += prev_height - height[r]
                r -= 1

            l -= 1

        return vol
        
"""
For this problem I used two pointers and split the problem into two halves. First,
I iterated once over the area to find the highest peak on the "mountain", and
split the problem in half from this point.

Calculate the volume of trapped rain water by doing the following:

    - Climb to the peak of the mountain from left to right
    - If you come across a valley, shoot a grappling hook straight across to
      traverse it (move the right pointer until you find a peak with a height
      equal to or greater than the height of the left pointer)
    - Calculate the volume of the valley as you zip over it
    - Once you've reached the peak, climb the mountain again, this time going
      from right to left
    - If you come across a valley, shoot a grappling hook straight across to
      traverse it (move the left pointer until you find a peak with a height
      equal to or greater than the height of the right pointer)
    - Calculate the volume of the valley as you zip over it
    - Add together the volumes calculated from each of your summits
    
Time Complexity: O(N)
Space complexity: O(1)
"""