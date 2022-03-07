"""
206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 思路：采用递归方法，确定递归终止条件，划分为子问题，递归分为递和归两个步骤；
        # 实际归的过程相当于逆序不断在尾部接上前一个节点
        #  1. 递归终止条件, 其实就是递的终止条件，终止完后不断往前回归
        if not head or not head.next:
            return head

        # 2. 递归调用
        p = self.reverseList(head.next)  # p相当于子问题每次排好序后返回的头节点

        # 3. 子问题处理
        head.next.next = head
        head.next = None  # 易错点

        # 4. 返回结果
        return p