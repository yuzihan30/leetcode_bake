# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    107. 二叉树的层序遍历 II
    给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # 思路：注意返回结果是二维列表，结果为从上到下层序遍历结果的逆序；和102题采用队列
        # 双层循环的计算方式相同,双层循环，外层遍历层间，内层遍历层内，然后将结果逆序；
        # 内层循环弹出二叉树的当前层，将当前层的值存放到cur列表内，并将下一层的节点入队；
        # 外层循环遍历新一层组成的队列，并将存放该层节点值存入结果数组中
        # 1. 初始化及特殊处理
        if not root:
            return []
        ans = []
        # 数组模拟队列
        # queue = [root]
        queue = []
        queue.append(root)
        # count = 1

        # 2. 双层循环
        while len(queue):
            count = len(queue)
            # cur存放当前层所有节点的值
            cur = []
            while count:
                node = queue.pop(0)
                cur.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                count -= 1
            ans.append(cur)
        
        # 3. 返回结果值
        ans.reverse()
        return ans