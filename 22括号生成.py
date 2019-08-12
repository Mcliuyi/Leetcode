# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 11:01 AM
# @Author  : 仲冬初七
# @FileName: 22括号生成.py
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
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n==0:
            return []
        self.result = []
        self.tool(0,0,n,"")
        return self.result

    def tool(self, left, right, n, rlt):
         """
         工具方法辅助
         :param left: 左括号数量
         :param right: 右括号数量
         :param n: 需要生成几对
         :param rlt: 结果
         :return:
         """
         # 如果左右括号数量都等于n，则结束并添加结果
         if left == n and right == n:
             self.result.append(rlt)
             return

         # 只要左括号小于n则可以继续添加
         if left<n:
             self.tool(left+1, right, n, rlt+"(")
         # 右括号的数量必须小于左括号，同时小于n才能继续添加
         if left>right and right<n:
             self.tool(left, right+1, n, rlt+")")

if __name__ == '__main__':

    sol = Solution()
    print(sol.generateParenthesis(3))