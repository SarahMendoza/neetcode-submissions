class Solution:
    def maxArea(self, heights: List[int]) -> int:


        # brute force solution: Big-Oh is O(N^2), where N = length of heights array

        # for each elem in the array
        # max_volume = -1
        # length = len(heights)

        # for i in range(0, length):
        #     elem_i = heights[i]
        #     for k in range(0, length):
        #         if( i != k):
        #             elem_k = heights[k]
        #             height = min(elem_i, elem_k)
        #             width = abs(k - i)

        #             vol = height * width

        #             #print ( "index ", i, " and index ", k, " yield volume: ", height, " * ", width, " = ", vol)
        #             if vol > max_volume:
        #                 max_volume = vol
        #                 #print( "UPDATED MAX VOLUME = ", max_volume)
        
        # return max_volume

        # improved solution:

        # two pointer solution. begin pointers at outer edges, move shorter height pointer inwards incrementally
        max_volume = -1
        right_ptr = (len(heights) - 1)
        left_ptr = 0

        while left_ptr < right_ptr:
            height = min(heights[left_ptr], heights[right_ptr])
            width = right_ptr - left_ptr
            vol = height * width

            if (vol > max_volume):
                max_volume = vol
                #print("UPDATE MAX VOLUME: ", max_volume, " left = ", left_ptr, " and right = ", right_ptr)

            if (heights[left_ptr] <= heights[right_ptr]):
                left_ptr += 1
            elif ( heights[left_ptr] > heights[right_ptr]):
                right_ptr -= 1

        return max_volume


        