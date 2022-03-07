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
        resultHead = head

        curNode = head  # 游标节点用于遍历

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
            curNode = curNode.next

        # 3. 返回结果
        return result.Head

