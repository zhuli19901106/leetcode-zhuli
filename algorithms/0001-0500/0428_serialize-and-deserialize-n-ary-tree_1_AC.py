# hard
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
# 1AC, not difficult, but error-prone
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root is None:
            return '{}'
        res = []
        res.append('{')
        res.append(str(root.val))
        res.append(',')
        res.append('[')
        for c in root.children:
            res.append(self.serialize(c))
            res.append(',')
        if len(root.children) > 0:
            res.pop()
        res.append(']')
        res.append('}')
        res = ''.join(res)
        return res

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        def traverse(s, i):
            if s[i + 1] == '}':
                return None, i + 1
            j = i + 1
            v = 0
            while s[j].isdigit():
                v = v * 10 + ord(s[j]) - ord('0')
                j += 1
            root = Node(v)
            root.children = []

            j += 2
            while s[j] != ']':
                c, j1 = traverse(s, j)
                root.children.append(c)
                j = j1 + 1
                if s[j] == ']':
                    break
                else:
                    j += 1
            j += 1
            return root, j

        root, _ = traverse(data, 0)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
