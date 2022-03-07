'''
Author: your name
Date: 2022-03-07 16:49:56
LastEditTime: 2022-03-07 19:51:48
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/linked_list/24_swapPairs.py
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 思路：交换两个节点会涉及到前后相邻两个节点的变动，变动讲究顺序；需要设置假节点（用于返回结果）和
        #  游标节点（用于遍历）
        # 1. 初始化
        resultHead = ListNode(0)  # 定义并设置dummyNode或者叫resultHead
        # resultHead = head # 易错点：假节点的指向头节点，而不是直接赋值
        resultHead.next = head

        # curNode = head  # 游标节点用于遍历
        curNode = resultHead  # 易错点：游标节点初始化为假节点而不是都节点

        # 2. 遍历并交换
        while curNode and curNode.next and curNode.next.next:
            # f/s/t(first/second/three)
            # 初始化f/s/t
            f = curNode
            s = curNode.next
            t = curNode.next.next

            # 交换，注意交换的先后次序, 先处理前后的衔接，再处理中间的衔接
            f.next = t
            s.next = t.next
            t.next = s

            # 移动游标
            # curNode = curNode.next
            curNode = curNode.next.next  # 易错点：游标移动两位而不是1位

        # 3. 返回结果
        return resultHead.next

