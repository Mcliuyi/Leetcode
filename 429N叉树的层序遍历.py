# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 11:11 AM
# @Author  : 仲冬初七
# @FileName: 429N叉树的层序遍历.py
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
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :

返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
 

说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import collections

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node) -> [[int]]:
        if not root:
            return []

        self.rlt = []
        # dfs
        self.dfs(0, root)
        # bfs
        self.bfs(root)
        return self.rlt


    def bfs(self, root: Node):
        # BFS广度优先搜索
        # 创建一个队列
        q = collections.deque()
        q.append(root)
        rlt = []

        while q:
            # 如果队列不为空，则创建一个列表用户存储当前层次数据
            level = []
            for i in range(len(q)):
                # 将当前层次所有节点进行遍历，并保存结果
                root = q.popleft()
                level.append(root.val)
                for c in root.children:
                    q.append(c)
            rlt.append(level)

        return rlt

    def dfs(self, level, root: Node):

        if not root:
            return None

        if len(self.rlt) < level+1:
            self.rlt.append([])

        self.rlt[level].append(root.val)
        for c in root.children:
            self.dfs(level+1, c)
        return None
