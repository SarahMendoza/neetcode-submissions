class Solution:
    def rob(self, nums: List[int]) -> int:
        

        house_total = [0] * (len(nums) +1)
        house_total[0] = 0
        house_total[1] = nums[0]

        for i in range(2, len(nums)+1):
            #
            leave_total = house_total[i-1]
            rob_total = house_total[i-2] + nums[i-1]

            house_total[i] = max(leave_total, rob_total)

        for elem in house_total:
            print(elem)
        return house_total.pop()