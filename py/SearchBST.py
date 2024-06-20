# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution():
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if val < root:
            root.left = self.searchBST(root.left, val)
        elif val > root:
            root.right = self.searchBST(root.right, val)
        else:
            self._preOrderTraversal(root, val)
       
        #return root
       # return subtree
    def _preOrderTraversal(self, TNode, node):
        if TNode is None:
            return None
        print(TNode.val)
        TNode.left = self._preOrderTraversal(TNode.left, node)
        TNode.right = self._preOrderTraversal(TNode.right, node)

tree = [4,2,7,1,3]
BST = Solution()
BST.searchBST(tree, 2)