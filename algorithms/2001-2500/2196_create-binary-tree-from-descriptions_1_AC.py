# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mm_nodes = {}
        st_child = set()
        for par, child, is_left in descriptions:
            if not par in mm_nodes:
                mm_nodes[par] = TreeNode(par)
            if not child in mm_nodes:
                mm_nodes[child] = TreeNode(child)
            st_child.add(child)

            if is_left:
                mm_nodes[par].left = mm_nodes[child]
            else:
                mm_nodes[par].right = mm_nodes[child]

        root = None
        for val in mm_nodes:
            if not val in st_child:
                root = mm_nodes[val]
                break

        return root
