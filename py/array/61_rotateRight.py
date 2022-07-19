# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 思路：将链表成环，找到分段点，将头节点指向分段点的下一个节点，断开环状链表
        # 注意点：成环需要遍历找到尾节点；k大于n时，需要取模，n-k%n指向分段点；
        # 链表的缺点就是查询慢，查询某个节点都需要遍历
        # 1. 初始化及特殊处理
        if not head:
            return None
        # n = 0 # 记录链表长度
        n = 1 # 记录链表长度 易错点
        curr = head
        
        # 2. 找到尾结点成环
        while curr.next:
            n += 1
            # curr.next = curr # 易错点
            curr = curr.next
        curr.next = head

        # 3. 找到分段点, 移动头节点，断开环状链表
        for i in range(n - k%n):
            # curr.next = curr
            curr = curr.next
        head = curr.next 
        curr.next = None

        # 4. 返回结果值
        return head
