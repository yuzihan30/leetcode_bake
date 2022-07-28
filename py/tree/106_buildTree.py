# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    106. 从中序与后序遍历序列构造二叉树
    给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
    """
    # 私有属性存放中序列表的值和索引，方便根据后序列表中的值快速找到值在中序列表的索引
    __inorder_map = {}
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 思路：参考105题，后续序列的尾值是根值，后序中的根值在中序列表将左右子树分割开；
        # 递归上面的过程
        # 1. 初始化
        n = len(inorder)
        for i in range(n):
            # self.__inorder_map[preorder[i]] = i # 易错点
            self.__inorder_map[inorder[i]] = i
        # 2. 执行构建二叉树的过程, 并返回结果
        return self.build(inorder, 0, n-1, postorder, 0, n-1)

    # 定义递归构建方法
    # pl、pr代表前序列表起始索引，il、ir代表中序列表的起始索引
    def build(self, inorder: List[int], il: int , ir: int, postorder: List[int], pl: int, pr: int) -> Optional[TreeNode]:
        # 1. 初始化及特殊处理, 递归终止条件
        # if pr > pl or ir > il: return None # 易错点1
        if pl > pr or il > ir: return None
        # 后序列表的尾值就是根值
        root = TreeNode(postorder[pr])
        # 求中序列表中分割点的索引
        # k = self.__inorder_map[pl] # 易错点2
        k = self.__inorder_map[postorder[pr]]

        # 2. 递归构建根节点下的左右子树
        root.left = self.build(inorder, il, k-1, postorder, pl, pl+k-il-1)
        root.right = self.build(inorder, k+1, ir, postorder, pl+k-il, pr-1)

        # 3. 返回根节点
        return root