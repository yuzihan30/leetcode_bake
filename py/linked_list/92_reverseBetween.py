# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    92. 反转链表 II
    给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
    """
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 思路：头插法，一次遍历，遍历的同时反转
        # 1. 初始化及特殊处理
        dummy = ListNode(0, head)
        pre = dummy
        # cur = head

        # 2. 遍历
        # 将pre节点移动到left前一个节点
        for _ in range(left - 1):
            # pre.next = pre
            pre = pre.next
        # 将当前节点指向left节点
        cur = pre.next
        # 将next节点指向left的下一个节点
        # next = cur.next # 易错点
        # 关键部分：头插法，注意移动right-left-1次;头插法就是每次将下一个值插到头节点的后面，
        # 这里就是将cur.next插入到pre的后面
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next

        # 3. 返回结果值
        return dummy.next