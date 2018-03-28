''' Python implemention of the missionaries and
cannibals problem.
References:
BFS:
https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3
https://gist.github.com/jamiees2/5527131
http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html
Miss/Cann Implement:
https://github.com/findkim/The-Missionary-and-Cannibals-Problem/blob/master/missionaries_cannibals.py
https://github.com/marianafranco/missionaries-and-cannibals/blob/master/python/missionaries_and_cannibals.py
http://dhruvbird.blogspot.com/2009/11/missionaries-and-cannibals-problem.html
Other:
https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
'''

masterList = []
parent = {}

class State:
    def __init__(self, boat, mLeft, cLeft, mRight, cRight, ID, parent):
        self.boat = boat
        self.mLeft = mLeft
        self.cLeft = cLeft
        self.mRight = mRight
        self.cRight = cRight
        self.ID = ID
        self.parent = parent

''' Hard coded graph of all states '''
def graph():
    state = State("left", 3,3,0,0,0,None) # Beginning State, boat left - all on left
    listSet(state)
    state = State("right", 3,2,0,1,1,0) # State 1 - boat right, one cannibal crosses
    listSet(state)
    state = State("right", 2,2,1,1,2,0) # State 2 - one missionary and one cannibal crosses
    listSet(state)
    state = State("right", 1,3,2,0,3,0) # State 3 -
    listSet(state)
    state = State("right", 2,3,1,0,4,0) # State 4 -
    listSet(state)
    state = State("right", 3,1,0,2,5,0) # State 5 - one missionary and one cannibal crosses
    listSet(state)


def listSet(state):
    masterList.append(state) # add to master list
    parent[state.ID] = state.parent # state ID: parent ID

def printList():
    for x in masterList:
        print ("ID: %s | Boat: %s | mLeft: %s | cLeft: %s | mRight: %s | cRight: %s | Parent: %s"
        % (x.ID, x.boat, x.mLeft, x.cLeft, x.mRight, x.cRight, x.parent))
    print parent

def BFS(ID):
    visited = []
    queue = []
    queue.append(ID)
    while queue:
        state = queue.pop(0)
        if state not in visited:
            visited.append(state)
            for key, value in parent.items(): # key is the state ID, value is the parent
                if state == value: queue.append(key)

graph()
printList()
BFS(0)

# Run BFS on graph
