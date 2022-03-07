'''
Author: your name
Date: 2022-03-07 19:50:53
LastEditTime: 2022-03-07 19:51:50
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/linked_list/206_reverseList.py
'''
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
        # 思路：先上迭代法，设置pre、curr、next三个指针，每次处理curr节点；
        # 关键点是每次移动当前节点之前需要保存下一个节点，防止链表断掉
        # 1. 初始化
        pre, curr = None, head

        # 2. 遍历
        while curr:
            # 先保存下一个节点
            next = curr.next
            curr.next = pre
            #  向后移动pre、curr节点, 注意先移动前一个节点
            pre = curr
            curr = next

        # 3. 返回结果
        return pre
