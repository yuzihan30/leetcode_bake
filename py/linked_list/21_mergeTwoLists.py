# Definition of singly-linked list
# class listNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    21. 合并两个有序链表
    将两个升序链表合并为一个新的 升序 链表并返回。
    新链表是通过拼接给定的两个链表的所有节点组成的。 
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 思路：先暴力解法，再用递归解法
        # # 1、初始化
        # # first = list1
        # # second = list2
        # dummy = preHead = ListNode(0) # 方便返回结果值

        # # 2、 遍历
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         preHead.next = list1
        #         list1 = list1.next
        #     else:
        #         preHead.next = list2
        #         list2 = list2.next
        #     preHead = preHead.next

        # # preHead.next = list1.next if list1.next else list2.next # 易错点
        # preHead.next = list1 if list1 else list2

        # return dummy.next

        # 递归法：每次子问题返回剩余未比较链表的较小节点
        # 1、特殊情况处理
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1  # 注意出口的写法, 最终是没有增加新的链表空间，所以返回最开始小的头节点就行
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2  # 注意出口的写法
