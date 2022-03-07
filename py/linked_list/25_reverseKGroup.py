'''
Author: your name
Date: 2022-03-07 22:56:04
LastEditTime: 2022-03-07 22:56:11
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/linked_list/25_reverseKGroup.py
'''
"""
25. K 个一组翻转链表
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 思路：划分成两个子问题，前k个单独翻转，剩下的又可以当做同一问题处理；前k个翻转可以用迭代或者递归求，
        # 这里用递归
        # 1. 递归终止条件
        # 终止条件1， 头节点为空或者只有一个节点，直接返回head
        if not head or not head.next:
            return head
        
        firstHead = head
        firstTail = head
        # 终止条件2， 遍历k次，不足k个，也是直接返回当前不足k可个节点链表的头节点
        # for i in range(k):  # 易错点
        for i in range(k-1):
            firstTail = firstTail.next
            if not firstTail:  # 前k-1个如果遇到None就直接返回头节点
                return firstHead

        # 2. 切断前k个节点和后面节点链表的联系
        secondHead = firstTail.next
        firstTail.next = None  

        # 3. 前k个节点翻转, 返回k个节点翻转后的新的首节点，也就是旧的尾结点
        # 递归法使链表翻转，首位节点并未移动，只是最终首节点变成尾节点，尾节点变成首节点
        firstTail = self.reverseList(firstHead)  

        # 4. 递归调用
        firstHead.next = self.reverseKGroup(secondHead, k)

        # 5. 返回结果
        return firstTail


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
