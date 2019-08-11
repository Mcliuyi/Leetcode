# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 11:16 AM
# @Author  : 仲冬初七
# @FileName: 235二叉搜索树的最近公共祖先.py
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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        递归法
        根据二叉搜索树的性质
        1. 如果q,p的值都大于跟节点的值，那么q,p均在右子树，否则是左子树
        :param root:
        :param p:
        :param q:
        :return:
        """
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        迭代法
        根据二叉搜索树的性质
        1. 如果q,p的值都大于跟节点的值，那么q,p均在右子树，否则是左子树
        :param root:
        :param p:
        :param q:
        :return:
        """
        while root:

            if p.val > root.val < q.val:
                root = root.right
            elif p.val < root.val > q.val:
                root = root.left
            else:
                return root