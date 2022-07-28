# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    105. 从前序与中序遍历序列构造二叉树
    给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
    """
    # 私有属性存放中序列表的值和索引，方便根据前序遍历列表中的值快速找到值在中序列表的索引
    __inorder_map = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 思路：前序遍历列表的第一个位置是树的根节点，前序中的根节点在中序列表将左右子树分割开；
        # 递归上面的过程
        # 1. 初始化
        n = len(preorder)
        for i in range(n):
            # self.__inorder_map[preorder[i]] = i # 易错点
            self.__inorder_map[inorder[i]] = i
        # 2. 执行构建二叉树的过程, 并返回结果
        return self.build(preorder, 0, n-1, inorder, 0, n-1)

    # 定义递归构建方法
    # pl、pr代表前序列表起始索引，il、ir代表中序列表的起始索引
    def build(self, preorder: List[int], pl: int, pr: int, inorder: List[int], il: int , ir: int) -> Optional[TreeNode]:
        # 1. 初始化及特殊处理, 递归终止条件
        # if pr > pl or ir > il: return None # 易错点1
        if pl > pr or il > ir: return None
        # 前序列表的第一个值就是根值
        root = TreeNode(preorder[pl])
        # 求中序列表中分割点的索引
        # k = self.__inorder_map[pl] # 易错点2
        k = self.__inorder_map[preorder[pl]]

        # 2. 递归构建根节点下的左右子树
        root.left = self.build(preorder, pl+1, pl+k-il, inorder, il, k-1)
        root.right = self.build(preorder, pl+k-il+1, pr, inorder, k+1, ir)

        # 3. 返回根节点
        return root



