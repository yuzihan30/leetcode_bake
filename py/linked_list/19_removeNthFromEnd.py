# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    19. 删除链表的倒数第 N 个结点
    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 思路：三种方法，1、暴力法，遍历到第L-n+1个节点 2、压栈出栈 3、双指针，快慢指针法
        # 1、初始化和特殊处理
        if not head:
            return head
        dummy = ListNode(0)  # 假节点，辅助节点，防止在链表长度正好为n的情况下，快指针被移出链表末尾
        dummy.next = head
        fast = slow = dummy

        # 2、双指针法
        # 快指针先移动n步
        for i in range(n):
            if fast.next:
                fast = fast.next
            # 这里面不用对链表长度小于n处理，其实return dummy.next已经把这种情况涵盖进去了

        # 快指针和慢指针开始同时移动
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 删除慢指针的下一个元素，即为倒数第n个元素
        slow.next = slow.next.next

        return dummy.next