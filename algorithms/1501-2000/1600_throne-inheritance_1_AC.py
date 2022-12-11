# https://leetcode.com/problems/throne-inheritance/
# a very poor written problem with huge downvotes
# hard description + easy idea = medium problem
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.tree_child = {}
        self.tree_parent = {}
        self.root = kingName
        self.tree_child[self.root] = []

        self.live = set()
        self.live.add(kingName)

    def birth(self, parentName: str, childName: str) -> None:
        if not parentName in self.tree_child:
            return
        if childName in self.tree_parent:
            return

        self.tree_child[parentName].append(childName)
        self.tree_child[childName] = []
        self.tree_parent[childName] = parentName

        self.live.add(childName)

    def death(self, name: str) -> None:
        if not name in self.live:
            return
        self.live.remove(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        self._traverse(self.root, order)

        return order

    def _traverse(self, root, order):
        if root in self.live:
            order.append(root)
        for child in self.tree_child[root]:
            self._traverse(child, order)

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
