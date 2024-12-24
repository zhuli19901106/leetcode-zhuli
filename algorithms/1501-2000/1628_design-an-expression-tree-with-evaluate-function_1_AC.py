# medium
# https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/
# 1AC, rather tiring

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class NumNode(Node):
    def __init__(self, val=0):
        self.val = val

    def evaluate(self) -> int:
        return self.val

class OpNode(Node):
    op_map = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()
        return OpNode.op_map[self.op](left_val, right_val)

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for tk in postfix:
            if not tk in OpNode.op_map:
                val = int(tk)
                node = NumNode(val)
                stack.append(node)
                continue
            else:
                right = stack.pop()
                left = stack.pop()
                node = OpNode(tk, left, right)
                stack.append(node)
        return stack.pop()
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
