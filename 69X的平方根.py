# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 11:16 AM
# @Author  : 仲冬初七
# @FileName: 69X的平方根.py
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
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""

class Solution:
    def mySqrt(self, x):
        return self.sol2(x)

    def sol1(self, x):
        """
        牛顿迭代法
        :param x:
        :return:
        """
        if x <= 1:
            return x
        r = x // 2
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)

    def sol2(self, x):
        """
        二分法
        :param x:
        :return:
        """
        l = 0
        r = x
        mid = 0
        # 如果是求小数，则 abs(l-r)>= 1e-5
        while l<=r:

            mid = (l+r) / 2
            if mid < x/mid:
                l = mid + 1
            elif mid > x/mid:
                r = mid - 1
            else:
                return mid

        return int(mid)

if __name__ == '__main__':

    sol = Solution()
    print(sol.mySqrt(16))