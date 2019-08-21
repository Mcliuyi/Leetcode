# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 4:32 PM
# @Author  : 仲冬初七
# @FileName: 在排序34数组中查找元素的第一个和最后一个位置.py
# @email   : ly288@qq.com
# @qq      : 1145994037

"""
                     _ooOoo_
                    o8888888o
                    88" . "88
                    (| -_- |)
                     O\ = /O
                 ____/`---'\____
               .   ' \\| |// `.
                / \\||| : |||// \
              / _||||| -:- |||||- \
                | | \\\ - /// | |
              | \_| ''\---/'' | |
               \ .-\__ `-` ___/-. /
            ___`. .' /--.--\ `. . __
         ."" '< `.___\_<|>_/___.' >'"".
        | | : `- \`.;`\ _ /`;.`/ - ` : | |
          \ \ `-. \_ __\ /__ _/ .-` / /
  ======`-.____`-.___\_____/___.-`____.-'======
                     `=---='
 
  .............................................
           佛祖保佑             永无BUG
 """
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if not nums:
            return [-1, -1]
        x = self.low(nums, target)
        y = self.height(nums, target)
        return [x, y]


    def low(self, nums, target):
        """
        获取下界
        :param nums:
        :param target:
        :return:
        """
        x = -1
        h = len(nums) - 1
        l = 0
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                x = mid
                h -= 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1


        return x

    def height(self, nums, target):
        """
        获取上界
        :param nums:
        :param target:
        :return:
        """
        y = -1
        h = len(nums) - 1
        l = 0
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                y = mid
                l += 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        return y


if __name__ == '__main__':
    nums = [1,2,3,8,8,8]
    sol = Solution()
    print(sol.searchRange(nums, 8))
