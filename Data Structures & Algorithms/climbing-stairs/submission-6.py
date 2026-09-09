class Solution:
    def climbStairs(self, n: int) -> int:

        array = [0] * (n+1)  #create a DP array of len (n+1) where index i represents i out of n steps traversed 

        if n < 3:
            return n
        array[0] = 0
        array[1] = 1
        array[2] = 2 # standard total number of ways to reach step at index i

        step = 3
        while step <= n:

            total_two_steps = array[step - 2]
            total_one_steps = array[step - 1]

            array[step] = total_two_steps + total_one_steps
            step += 1

        return array[n]