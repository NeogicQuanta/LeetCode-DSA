class ThroneInheritance(object):

    def __init__(self, kingName):
        self.king = kingName
        self.children = {kingName: []}  
        self.dead = set()

    def birth(self, parentName, childName):
        if parentName not in self.children:
            self.children[parentName] = []
        self.children[parentName].append(childName)
        self.children[childName] = []

    def death(self, name):
        self.dead.add(name)

    def getInheritanceOrder(self):
        order = []

        def dfs(name):
            if name not in self.dead:
                order.append(name)
            for child in self.children.get(name, []):
                dfs(child)

        dfs(self.king)
        return order
