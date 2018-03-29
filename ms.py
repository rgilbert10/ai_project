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
visited = []

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
    state = State("left", 3,3,0,0,1,None) # Beginning State, boat left - all on left
    listSet(state)
    state = State("right", 3,2,0,1,2,1) # State 1 - boat right, one cannibal crosses
    listSet(state)
    state = State("right", 2,2,1,1,3,1) # State 2 - one missionary and one cannibal crosses
    listSet(state)
    state = State("right", 3,1,0,2,4,1) # State 3 -
    listSet(state)
    state = State("left", 3,2,0,1,5,4) # State 4 -
    listSet(state)
    state = State("right", 3,1,0,2,6,5) # State 5 -
    listSet(state)
    state = State("right", 2,1,1,1,7,5) # State 6 -
    listSet(state)
    state = State("right", 3,0,0,3,8,5) # State 6 -
    listSet(state)
    state = State("left", 3,1,0,2,9,8) # State 6 -
    listSet(state)
    state = State("right", 1,1,2,2,10,9) # State 6 -
    listSet(state)
    state = State("left", 2,2,1,1,11,10) # State 6 -
    listSet(state)
    state = State("right", 0,2,3,1,12,11) # State 6 -
    listSet(state)
    state = State("left", 0,3,3,0,13,12) # State 6 -
    listSet(state)
    state = State("right", 0,1,3,2,14,13) # State 6 -
    listSet(state)
    state = State("left", 1,1,2,1,15,14) # State 6 -
    listSet(state)
    state = State("left", 0,2,3,1,16,14) # State 6 -
    listSet(state)
    state = State("right", 0,0,3,3,17,16) # State 6 -
    listSet(state)

def listSet(state):
    masterList.append(state) # add to master list
    parent[state.ID] = state.parent # state ID: parent ID

def printList():
    for x in masterList:
        print ("ID: %s | Boat: %s | mLeft: %s | cLeft: %s | mRight: %s | cRight: %s | Parent: %s"
        % (x.ID, x.boat, x.mLeft, x.cLeft, x.mRight, x.cRight, x.parent))
    print parent
    print visited

def BFS(ID):
    queue = []
    queue.append(ID)
    while queue:
        state = queue.pop(0)
        if(isGoal(state)):
            return state
        if state not in visited:
            visited.append(state)
            for key, value in parent.items(): # key is the state ID, value is the parent
                if state == value: queue.append(key)

def isGoal(state):
    for x in masterList:
        if x.ID == state:
            state = x
    if state.mLeft == 0 and state.cLeft == 0 and \
    state.mRight == 3 and state.cRight == 3:
        return True
    else:
        return False

def solution(state):
    answer = []
    answer.append(state)
    for x in masterList:
        if x.ID == state:
            state = x
    parent = state.parent
    while parent:
        answer.append(parent)
        for x in masterList:
            if x.ID == parent:
                parent = x
        parent = parent.parent

    temp = []
    for i in reversed(answer):
        for x in masterList:
            if x.ID == i:
                temp.append(x)
    print ("mc            mc")
    for t in temp:

        if t.boat == "left":
            print ("%s%s  |B    |   %s%s" % (t.mLeft, t.cLeft, t.mRight, t.cRight))
        else:
            print ("%s%s  |    B|   %s%s" % (t.mLeft, t.cLeft, t.mRight, t.cRight))

graph()
state = BFS(1)
#printList()
solution(state)

# Run BFS on graph
