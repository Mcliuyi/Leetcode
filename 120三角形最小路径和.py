# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 4:01 PM
# @Author  : 仲冬初七
# @FileName: 120三角形最小路径和.py
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
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache

class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        # 递归
        self.triangle = triangle
        self.ans = []
        self.tool(0,0,self.triangle[0][0])
        return min(self.ans)

    def tool(self, i, j, rlt):
        """
        递归，将所有结果搜索出来
        时间复杂度O(n^2)
        :param i:
        :param j:
        :param rlt:
        :return:
        """
        if i+1>=len(self.triangle):
            self.ans.append(rlt)
            return None
        self.tool(i+1,j,rlt+self.triangle[i+1][j])
        self.tool(i+1,j+1,rlt+self.triangle[i+1][j+1])

    def dp(self, triangle: [[int]]):
        """
        动态规划
        :param triangle:
        :return:
        """
        for i in range(len(triangle)-2, -1,-1):
            # 从倒数第二层开始计算
            for j in range(0, len(triangle[i])):
                # 每次计算当前节点最有解
                triangle[i][j] = min(triangle[i+1][j],triangle[i+1][j+1]) + triangle[i][j]

        return triangle[0][0]



if __name__ == '__main__':
    triangle = [
                [2],
                [3,4],
                [6,5,7],
                [4,1,8,3]
                ]
    sol = Solution()
    # print(sol.minimumTotal(triangle))
    sol.dp(triangle)



