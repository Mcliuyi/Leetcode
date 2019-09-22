# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 4:18 PM
# @Author  : 仲冬初七
# @FileName: 200岛屿数量.py
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
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        clo = len(grid[-1])
        ans = 0
        for x in range(row):
            for y in range(clo):
                if grid[x][y] == "1":
                    ans += 1
                    self.tool(grid, x, y)

    def tool(self, grid , x, y):
        """
        将整块相连接的陆地都修改为2
        :param grid:
        :param x:
        :param y:
        :return:
        """
        row = len(grid)
        clo = len(grid[-1])
        if x >= row or y >= clo or x < 0 or y < 0 or grid[x][y] != "1":

            return
        grid[x][y] = '2'
        self.tool(grid, x - 1, y)
        self.tool(grid, x + 1, y)
        self.tool(grid, x, y - 1)
        self.tool(grid, x, y + 1)

if __name__ == '__main__':

    s = Solution()
    s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]])