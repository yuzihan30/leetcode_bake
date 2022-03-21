'''
Author: your name
Date: 2021-10-12 15:03:44
LastEditTime: 2022-03-21 08:26:02
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/linked_list/2_add_two_numbers.py
'''
"""
2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能
存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. 定义单向链表
# class ListNode(object):
#     # 注意点：python中的空用None表示
#     # 1.1 初始化，初始化方法也就是构造函数，入参初始默认值
#     def __init__(self, val=0, next=None):
#         # 1.2 初始化私有属性
#         self.val = val
#         self.next = next
# 2. 定义解题类及方法
class Solution:
    # 2.1 定义方法，入参、出参做类型限制
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 2.2（关键点） 定义虚拟指针和当前指针，并同时指向初始化默认值为0的节点，该节点也是
        # 结果链表的头节点。dummy用于返回最后计算结果列表
        # 注意点：创建新节点不用new关键词，区别与其他编程语言
        dummy = curr = ListNode()
        # 2.3 定义并初始化进位
        carry = 0
        # 2.4（关键点）while循环同时遍历l1、l2，当不知道要循环多少次的时候要用while,
        # 注意点：while循环链表的时候，循环体中一定要有推进循环结束的指针后移，这里l1、l2、curr都要
        # 后移（定性加定量分析，涉及到3个指针的移动）
        # 注意点：不为空的判断选择简洁的方式，但这不是最严谨的方式
        # while l1 is not None or l2 is not None:
        while l1 or l2:
            # 2.5 同时取两个相加链表当前节点位的值，长度短的链表节点位的value取值为0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # 2.6 处理结果链表头结点的下一节点的值（这也是返回值取头结点的下一节点的原因）
            # 和进位值，这里的carry是上一步结果中的进位值
            sum = x + y + carry
            # 2.7 计算当前位的值，基于该值创建节点，并将当前指针指向该节点
            curr.next = ListNode(sum % 10)
            # 2.8 将当前指针后移，注意顺序是先创建节点，再移动指针
            curr = curr.next
            # 2.9 计算进位值 "/"表示浮点数除法，返回浮点结果; "//"表示整数除法,返回不大于结果的一个最大的整数
            carry = sum // 10
            
            # 2.10 移动加数链表指针，移动前注意判断非空
            if l1:
                l1 = l1.next
            # 2.11 移动被加数位链表指针，移动前注意判断非空
            if l2:
                l2 = l2.next
        # 2.12 l1、l2移动结束后，如果进位值依然大于0，将当前进位值保存到当前指针的下一个节点（这一步是不是可以不要？）
        # 易错点：容易遗漏, 而且要写在while循环之外
        if carry:
            curr.next = ListNode(carry)
        # 易错点：不是返回dummy, 可以画图理解, 初始化时dummy、curr中的值是0
        return dummy.next

"""
总结：涉及到三次指针的移动，两次指针的赋值
方法名称：单链表求两数之和
步骤：
考查知识点：
关键点：定义1个虚拟指针，1个移动指针
"""