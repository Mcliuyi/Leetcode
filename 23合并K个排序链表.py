# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 9:34 PM
# @Author  : 仲冬初七
# @FileName: 23合并K个排序链表.py
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
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import collections
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if not lists:
            return None
        # 归并排序法
        # 1. 将所有链表进行排序
        for i in range(len(lists)):
            lists[i] = self.middle(lists[i])
        # 2. 将排序后的链表进行拼接
        result = lists[0]
        for i in range(1, len(lists)):

            result = self.join(result, lists[i])

        return result
        # return self.baoli(lists)


    def baoli(self, lists:[ListNode]):

        rlt = []
        for node in lists:
            while node:
                rlt.append(node.val)
                node = node.next
        if not rlt:
            return None
        rlt.sort(reverse=True)
        root = ListNode(rlt.pop())
        prev = root
        while rlt:
            val = rlt.pop()
            n = ListNode(val)
            prev.next = n
            prev = n
        return root

    def join(self, node1: ListNode, node2: ListNode):
        """
        合并两个有序链表
        :param node1:
        :param node2:
        :return:
        """
        head = ListNode(0)
        rlt = head
        while node1 and node2:
            # 每次将大的值用指针指向
            if node1.val > node2.val:
                # head: 1 -> 2  node2 3 -> 4
                # head: 1 -> 2 -> 3 -> 4
                head.next = node2
                # 1 -> 2 -> 3 -> 4
                #           head
                # 相当于拼接后移动指针
                head = node2
                node2 = node2.next
            else:
                head.next = node1
                head = node1
                node1 = node1.next

        if node1: head.next = node1
        if node2: head.next = node2
        # 跳过临时节点
        return rlt.next

    def middle(self, head: ListNode):
        """
        找出链表的中间节点
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 继续拆分
        # 下次迭代的为上次链表的中点
        fast = self.middle(slow.next)
        # 第一部分链表的终点
        slow.next = None
        # 继续迭代，起点为初始起点，终点为链表的中点继续分割
        slow = self.middle(head)
        return self.join(fast, slow)


if __name__ == '__main__':
    import random
    node1 = ListNode(1)
    tmp = node1
    for i in range(5):
        _ = ListNode(random.randint(1, 50))
        tmp.next = _
        tmp = _

    node2 = ListNode(2)
    tmp = node2
    for i in range(5):
        _ = ListNode(random.randint(1, 50))
        tmp.next = _
        tmp = _


    node3 = ListNode(3)
    tmp = node3
    for i in range(5):
        _ = ListNode(random.randint(1, 50))
        tmp.next = _
        tmp = _

    sol = Solution()
    sol.mergeKLists([node1, node2])




