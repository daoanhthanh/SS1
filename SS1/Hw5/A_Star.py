class State_String(State):
    def __init__(self, value, parent, start = 0,
                    goal = 0, solver = 0):
        super(State_String, self).__init__(value, parent, start, goal, solver)
        self.dist = self.GetDist()

    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist
    def CreateChildren(self):
        if not self.children:
            for i in xrange(len(seft.goal)-1):
                val = self.value
                val = 