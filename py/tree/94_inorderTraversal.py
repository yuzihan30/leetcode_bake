# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 思路：递归性能差，用迭代法；前、中、后序遍历是以根节点为基准，中序就是左根右的顺序；
        # 节点的存储和读取过程具有后进先出的特点，适合用栈结构处理；
        # 两层while循环处理，外层while循环左、中值放到结果列表中，并将当前指针指向右节点；
        # 内层循环负责遍历根或者右侧节点的左侧节点，并压栈；
        # 1. 初始化及特殊处理
        if not root: return []
        cur = root
        # 用列表模拟栈的功能
        stack = []
        ans = []

        # 2. 遍历，两层while循环并伴随压栈出栈的过程
        # 当前节点或者栈不为空时, 易错点：not stack
        # while cur or not stack:
        while cur or stack:
            # 当前节点不为空时
            while cur:
                # 将当前节点压栈，而不是节点值压栈
                stack.append(cur)
                # 不断移动当前指针, 指向左子节点
                cur = cur.left
            # 此时cur为空，将栈顶元素弹出，并将cur指向弹出的栈顶元素
            cur = stack.pop()
            # 将弹出的栈顶元素值放入结果列表里
            ans.append(cur.val)
            # 将当前指针指向弹出的栈顶元素的右子节点，如果右子节点为空就继续出栈，
            # 右子节点不空的话继续深度遍历压栈左子节点
            cur = cur.right

        # 3. 返回结果值
        return ans

