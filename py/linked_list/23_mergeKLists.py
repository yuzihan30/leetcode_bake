# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    23. 合并K个升序链表
    给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 思路：直接上最容易理解的分治法，将问题转化为合并两个升序链表的遍历问题
        # 1. 初始化和特殊处理
        # if not lists or not lists[0]:  # 易错点not lists[0]，这种情况只能考虑只有一个链表元素的情况
        if not lists:
            return None
        count = len(lists)
        if count == 1:
            return lists[0]
        
        # 2、遍历
        while len(lists) > 1:
            first = lists.pop()
            second = lists.pop()
            three = self.mergeTwoLists(first, second)
            lists.append(three)
        
        # 3、返回结果
        return lists[0]

    # 定义合并两个有序链表的方法
    def mergeTwoLists(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        if not first:
            return second
        elif not second:
            return first
        elif first.val < second.val:
            first.next = self.mergeTwoLists(first.next, second)
            return first
        else: 
            second.next = self.mergeTwoLists(first, second.next)
            return second
