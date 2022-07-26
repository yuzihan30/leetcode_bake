# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    144. 二叉树的前序遍历
    给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 思路：递归性能差，用迭代法；前、中、后序遍历是以根节点为基准，中序就是左根右的顺序；
        # 节点的存储和读取过程具有后进先出的特点，适合用栈结构处理；
        # 两层while循环处理，外层while循环执行出栈，并将当前指针指向右节点；
        # 内层循环负责遍历根或者右侧节点的左侧子节点，并压栈，左、中、右称谓都是相对的
        # 前序遍历和中序遍历的区别就是：前序遍历压栈的同时要将值压入结果列表
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
                # 将节点值压栈
                ans.append(cur.val)
                # 不断移动当前指针, 指向左子节点
                cur = cur.left
            # 此时cur为空，将栈顶元素弹出，走到这里的栈不会为空，并将cur指向弹出的栈顶元素
            # 反证法：若为空，cur不为空，内层循环就会将cur节点压栈
            cur = stack.pop()
            # 将当前指针指向弹出的栈顶元素的右子节点，如果右子节点为空就继续出栈，
            # 右子节点不空的话继续深度遍历压栈左子节点
            cur = cur.right

        # 3. 返回结果值
        return ans