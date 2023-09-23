from abc import ABC, abstractmethod

class State:
    def __init__(self, description) -> None:
        self.description = description

    def __eq__(self, s: object) -> bool:
        return isinstance(s, State) and s.description == self.description

class Searchable(ABC):
    @abstractmethod
    def getInit(self) -> State:
        pass

    @abstractmethod
    def getGoal(self) -> State:
        pass

    @abstractmethod
    def getStates(self, state: State) -> list[State]:
        pass

class Maze:
    def __init__(self) -> None:
        self.mazeData = [
            [0, 1, 1, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1]
        ]

    def getStart(self):
        return (0, 0)

    def getEnd(self):
        return (3, 3)

    def isBound(self, i, j):
        return 0 <= i < len(self.mazeData) and 0 <= j < len(self.mazeData[0])

    def getWays(self, row, col):
        if not self.isBound(row, col):
            return None

        i, j = row, col
        l = []
        if self.isBound(i - 1, j) and self.mazeData[i - 1][j] == 0:
            l.append((i - 1, j))
        if self.isBound(i, j - 1) and self.mazeData[i][j - 1] == 0:
            l.append((i, j - 1))
        if self.isBound(i + 1, j) and self.mazeData[i + 1][j] == 0:
            l.append((i + 1, j))
        if self.isBound(i, j + 1) and self.mazeData[i][j + 1] == 0:
            l.append((i, j + 1))

        return l

class SearchableMaze(Searchable):
    def __init__(self, m: Maze):
        self.m = m

    def getInit(self) -> State:
        d = self.m.getStart()
        return State(d)

    def getGoal(self) -> State:
        d = self.m.getEnd()
        return State(d)

    def getStates(self, state: State) -> list[State]:
        l = self.m.getWays(state.description[0], state.description[1])
        r = []
        for d in l:
            r.append(State(d))

        return r

    def search(searchable: Searchable):
        visited = []
        sol = []
        def dfs(state: State, visited, sol):
            visited.append(state)

            if state == searchable.getGoal():
                return state.description

            for s in searchable.getStates(state):
                if s not in visited:
                    p = dfs(s, visited, sol)
                    if p is not None:
                        sol.insert(0,s.description)
                        return p

            return None

        dfs(searchable.getInit(), visited, sol)

        return sol

m = Maze()
p = SearchableMaze(m)

print(p.search())
