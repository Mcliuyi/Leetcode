# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 11:03 AM
# @Author  : 仲冬初七
# @FileName: 637二叉树的层平均值.py
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

import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> [float]:

        self.rlt = []
        self.dfs(0, root)
        for i in range(len(self.rlt)):

            self.rlt[i] = sum(self.rlt[i]) / len(self.rlt[i])

        return self.rlt


    def bfs(self, root: TreeNode):
        # BFS广度优先搜索
        # 创建一个队列
        q = collections.deque()
        q.append(root)

        while q:
            # 如果队列不为空，则创建一个列表用户存储当前层次数据
            level = []
            for i in range(len(q)):
                # 将当前层次所有节点进行遍历，并保存结果
                root = q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            self.rlt.append(level)

        return self.rlt

    def dfs(self, level, root: TreeNode):

        if not root:
            return None

        if len(self.rlt) < level+1:
            self.rlt.append([])

        self.rlt[level].append(root.val)
        self.dfs(level+1, root.left)
        self.dfs(level+1, root.right)
        return None
