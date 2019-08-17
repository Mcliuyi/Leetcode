# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 9:50 AM
# @Author  : 仲冬初七
# @FileName: 51N皇后.py
# @Software: PyCharm
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
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        # 结果集
        self.rlt =[]
        self.queens(n, [], [], [])
        # 格式化输出结果
        return [["."*j + "Q" + "."*(n-1-j) for j in i] for i in self.rlt]

    def queens(self, n, col, left, right):
        """
        DFS递归模式
        :param n: 皇后数量
        :param col: 存储放了哪些列
        :param left: 左边的斜线
        :param right: 右边的斜线
        :return:
        """
        leve = len(col)
        if leve == n:
            # 如果当前行数等于n则代表摆放完毕，存储结果
            self.rlt.append(col)
            return

        for i in range(n):
            # 循环每一行，判断是否已经摆放了棋子
            # 左边的斜线的规律是  x+y相等， 右边为 y-x相等
            # x为行，y为列
            if i not in col and i+leve-1 not in left and leve-1 - i not in right:
                # 将本次摆放记录并进入下一次
                self.queens(n, col+[i], left+[i+leve-1], right + [leve-1 - i])




