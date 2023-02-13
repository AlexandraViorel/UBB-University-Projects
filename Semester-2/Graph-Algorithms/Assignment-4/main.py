import copy
import random
import math
from collections import deque


class DirectedGraph:
    def __init__(self, numberOfVertices, numberOfEdges):
        self._numberOfVertices = numberOfVertices
        self._numberOfEdges = numberOfEdges
        self._vertices = []
        self._inDict = {}
        self._outDict = {}
        self._costDict = {}
        for i in range(self.numberOfVertices):
            self.inDict[i] = []
            self.outDict[i] = []

    @property
    def vertices(self):
        return self._vertices

    @property
    def inDict(self):
        return self._inDict

    @property
    def outDict(self):
        return self._outDict

    @property
    def costDict(self):
        return self._costDict

    @property
    def numberOfVertices(self):
        return self._numberOfVertices

    @property
    def numberOfEdges(self):
        return self._numberOfEdges

    def parseTheSetOfVertices(self):
        vertices = []
        for vertex in self.inDict.keys():
            vertices.append(vertex)
        for vertex in vertices:
            yield vertex

    def parse_cost(self):
        keys = list(self._costDict.keys())
        for key in keys:
            yield key

    def checkIfThereIsEdge(self, x, y):
        if x in self.inDict[y]:
            return self.costDict[(x, y)]
        if y in self.outDict[x]:
            return self.costDict[(x, y)]
        return False

    def getInDegree(self, x):
        if x not in self.inDict.keys():
            return -1
        return len(self.inDict[x])

    def getOutDegree(self, x):
        if x not in self.outDict.keys():
            return -1
        return len(self.outDict[x])

    def parseOutboundEdges(self, x):
        for y in self.outDict[x]:
            yield y

    def parseInboundEdges(self, x):
        for y in self.inDict[x]:
            yield y

    def modifyEdgeCost(self, x, y, newCost):
        if (x, y) not in self.costDict.keys():
            return False
        self.costDict[(x, y)] = newCost
        return True

    def addVertex(self, x):
        if x in self.inDict.keys() and x in self.outDict.keys():
            return False
        self.inDict[x] = []
        self.outDict[x] = []
        self._vertices.append(x)
        self._numberOfVertices += 1
        return True

    def removeVertex(self, x):
        if x not in self.inDict.keys() and x not in self.outDict.keys():
            return False
        self.inDict.pop(x)
        self.outDict.pop(x)
        self._vertices.remove(x)
        for vertex in self.inDict.keys():
            if x in self.inDict[vertex]:
                self.inDict[vertex].remove(x)
            elif x in self.outDict.keys():
                self.outDict[vertex].remove(x)
        costEdgesList = list(self.costDict.keys())
        for edge in costEdgesList:
            if edge[0] == x or edge[1] == x:
                self.costDict.pop(edge)
                self._numberOfEdges -= 1
        self._numberOfVertices -= 1
        return True

    def addEdge(self, x, y, cost):
        if x in self.inDict[y]:
            return False
        elif y in self.outDict[x]:
            return False
        elif (x, y) in self.costDict.keys():
            return False
        self.inDict[y].append(x)
        self.outDict[x].append(y)
        self.costDict[(x, y)] = cost
        return True

    def removeEdge(self, x, y):
        if x not in self.inDict.keys() or x not in self.outDict.keys() or y not in self.inDict.keys() \
                or y not in self.outDict.keys():
            return False
        if x not in self.inDict[y]:
            return False
        elif y not in self.outDict[x]:
            return False
        elif (x, y) not in self.costDict.keys():
            return False
        self.inDict[y].remove(x)
        self.outDict[x].remove(y)
        self.costDict.pop((x, y))
        self._numberOfEdges -= 1
        return True

    def copyGraph(self):
        return copy.deepcopy(self)

    def lowestCostWalk(self, s, t, prev):
        e = self._numberOfEdges
        v = self._numberOfVertices
        # d[x][k]=the cost of the lowest cost walk from s to x and of length at most k, where s is the starting vertex
        d = [[math.inf for x in range(e + 1)] for y in range(v)]
        for i in range(e + 1):
            d[s][i] = 0
        # dynamically modify the matrix
        for k in range(1, e + 1):
            for i in range(1, v):
                # d[i][k]=min(d[i][k],min(d[j][k-1]+cost(j,i)), where j belongs to the set of inbound edges of i
                d[i][k] = d[i][k - 1]
                for j in self.inDict[i]:
                    if d[j][k - 1] + self.costDict[(j, i)] < d[i][k]:
                        d[i][k] = d[j][k - 1] + self.costDict[(j, i)]
                        # i is now the direct predecessor of j
                        prev[i] = j
        # check for negative cost cycles
        for i in range(1, v):
            minCost = d[i][e]
            for j in self.inDict[i]:
                if d[j][e] + self.costDict[(j, i)] < minCost:
                    return -1
        # the lowest cost found
        return d[t][e]

    def topologicalSort(self):
        """
            Function that sorts the graph topologically using the predecessor counting algorithm. We have to take a
        vertex with no predecessors, put it in the sorted list and eliminate it from the graph. We continue like this
        with all the vertices remaining. Finally, we either end up with the topologically sorted list or we have a cycle
        if we cannot get a vertex with no predecessors.
        :return: the sorted list or an empty list if we have a cycle
        """
        sortedList = []
        q = deque()
        count = {}
        for vertex in self._vertices:
            count[vertex] = self.getInDegree(vertex)
            if count[vertex] == 0:
                q.append(vertex)

        while len(q) != 0:
            vertex = q.popleft()
            sortedList.append(vertex)
            for y in self.outDict[vertex]:
                count[y] = count[y] - 1
                if count[y] == 0:
                    q.append(y)

        if len(sortedList) < len(self._vertices):
            return []
        return sortedList

    def highestCostPath(self, beginVertex, endVertex):
        """
        Function to compute the highest cost path from vertex begin to vertex end.
        :param beginVertex: the beginning of the path
        :param endVertex: the end of the path
        :return: the distance(cost) of the path and the dictionary of previous vertices
        """
        topologicalOrderList = self.topologicalSort()  # get the topological sort
        distance = {}  # dictionary of costs from the source
        previous = {}  # dictionary that stores for each vertex the previous vertex from the path
        m_inf = float('-inf')
        for vertex in topologicalOrderList:  # initialize all the values of the dictionaries
            distance[vertex] = m_inf
            previous[vertex] = -1
        distance[beginVertex] = 0

        for vertex in topologicalOrderList:  # go through all the vertices
            if vertex == endVertex:  # stop the loop if we get to the end vertex
                break
            for otherVertex in self._outDict[vertex]:  # parse the outbound vertices of the current vertex
                if distance[otherVertex] < distance[vertex] + self._costDict[(vertex, otherVertex)]:
                    # if the cost is greater update the dictionary
                    distance[otherVertex] = distance[vertex] + self._costDict[(vertex, otherVertex)]
                    previous[otherVertex] = vertex

        return distance[endVertex], previous


class UI:
    def __init__(self):
        self._graphs = []
        self._currentGraph = None

    def createRandomGraphUI(self):
        vertices = int(input("Enter the number of vertices: "))
        edges = int(input("Enter the number of edges: "))
        graph = self.createRandomGraph(vertices, edges)
        if self._currentGraph is None:
            self._currentGraph = 0
        self._graphs.append(graph)
        self._currentGraph = len(self._graphs) - 1

    @staticmethod
    def createRandomGraph(vertices, edges):
        if edges > vertices * vertices:
            raise ValueError("Too many edges !")
        graph = DirectedGraph(vertices, 0)
        i = 0
        while i < edges:
            x = random.randint(0, vertices - 1)
            y = random.randint(0, vertices - 1)
            cost = random.randint(0, 100)
            if graph.addEdge(x, y, cost):
                i += 1
        return graph

    def readGraphFromTextFileUI(self):
        file = input("Write the name of the file: ")
        if self._currentGraph is None:
            self._currentGraph = 0
        graph = readGraphFromTextFile(file)
        self._graphs.append(graph)
        self._currentGraph = len(self._graphs) - 1

    def writeGraphToTextFileUI(self):
        current_graph = self._graphs[self._currentGraph]
        file = "outputgraph" + str(self._currentGraph) + ".txt"
        writeGraphToTextFile(current_graph, file)

    def getNumberOfVerticesUI(self):
        numberOfVertices = self._graphs[self._currentGraph].numberOfVertices
        print("The number of vertices of the current graph is " + str(numberOfVertices))

    def listAllInboundVertices(self):
        for x in self._graphs[self._currentGraph].parseTheSetOfVertices():
            line = str(x) + ": "
            for y in self._graphs[self._currentGraph].parseInboundEdges(x):
                line = line + str(y) + ", "
            print(line)

    def listAllOutboundVertices(self):
        for x in self._graphs[self._currentGraph].parseTheSetOfVertices():
            line = str(x) + ":"
            for y in self._graphs[self._currentGraph].parseOutboundEdges(x):
                line = line + str(y) + ", "
            print(line)

    def checkIfThereIsEdgeUI(self):
        x = int(input("Write the first vertex: "))
        y = int(input("Write the second vertex: "))
        edge = self._graphs[self._currentGraph].checkIfThereIsEdge(x, y)
        if edge is not False:
            print("There is an edge between " + str(x) + " and " + str(y) + " and its cost is " + str(edge))
        else:
            print("There is no edge between " + str(x) + " and " + str(y))

    def printInDegreeUI(self):
        x = int(input("Write the vertex: "))
        inDegree = self._graphs[self._currentGraph].getInDegree(x)
        if inDegree == -1:
            print("This vertex does not exist!")
        else:
            print("The in degree of the vertex " + str(x) + " is: " + str(inDegree))

    def printOutDegreeUI(self):
        x = int(input("Write the vertex: "))
        outDegree = self._graphs[self._currentGraph].getOutDegree(x)
        if outDegree == -1:
            print("This vertex does not exist!")
        else:
            print("The out degree of the vertex " + str(x) + " is: " + str(outDegree))

    def listInboundEdges(self):
        vertex = int(input("Write the vertex: "))
        print(str(vertex) + " :")
        for x in self._graphs[self._currentGraph].parseInboundEdges(vertex):
            print("(" + str(x) + ", " + str(vertex) + ")")

    def listOutboundEdges(self):
        vertex = int(input("Write the vertex: "))
        print(str(vertex) + " :")
        for x in self._graphs[self._currentGraph].parseOutboundEdges(vertex):
            print("(" + str(vertex) + ", " + str(x) + ")")

    def modifyCostOfAGivenEdge(self):
        x = int(input("Write the first vertex: "))
        y = int(input("Write the second vertex: "))
        cost = int(input("Write the new cost of the edge: "))
        result = self._graphs[self._currentGraph].modifyEdgeCost(x, y, cost)
        if result is False:
            print("There is no edge between " + str(x) + " and " + str(y))
        else:
            print("Cost modified successfully!")

    def addEdgeUI(self):
        x = int(input("Write the first vertex: "))
        y = int(input("Write the second vertex: "))
        cost = int(input("Write the cost of the edge: "))
        result = self._graphs[self._currentGraph].addEdge(x, y, cost)
        if result is False:
            print("There already exists an edge between these vertices!")
        else:
            print("Edge added successfully!")

    def removeEdgeUI(self):
        x = int(input("Write the first vertex: "))
        y = int(input("Write the second vertex: "))
        result = self._graphs[self._currentGraph].removeEdge(x, y)
        if result is False:
            print("There is no edge between these vertices!")
        else:
            print("Edge removed successfully!")

    def addVertexUI(self):
        x = int(input("Write the vertex: "))
        result = self._graphs[self._currentGraph].addVertex(x)
        if result is False:
            print("This vertex already exists!")
        else:
            print("Vertex added successfully!")

    def removeVertexUI(self):
        x = int(input("Write the vertex: "))
        result = self._graphs[self._currentGraph].removeVertex(x)
        if result is False:
            print("This vertex does not exist!")
        else:
            print("Vertex removed successfully!")

    def copyCurrentGraphUI(self):
        copy = self._graphs[self._currentGraph].copyGraph()
        self._graphs.append(copy)
        print("Graph copied successfully!")

    def parseAllVerticesUI(self):
        for vertex in self._graphs[self._currentGraph].parseTheSetOfVertices():
            print(vertex)

    def lowestCostWalkUI(self):
        s = int(input("Starting vertex:"))
        t = int(input("End vertex:"))
        prev = [-1] * self._graphs[self._currentGraph].numberOfVertices
        cost = self._graphs[self._currentGraph].lowestCostWalk(s, t, prev)
        if cost == -1:
            print("Negative cost cycles are accessible from the starting vertex")
        else:
            print("Cost of lowest cost path: " + str(cost))
            res = "Lowest cost path: "
            stack = []
            while prev[t] != -1:
                stack.append(t)
                t = prev[t]
            stack.append(s)
            while len(stack) > 1:
                res = res + str(stack.pop()) + "->"
            res = res + str(stack.pop())
            print(res)

    def topologicalSortUI(self):
        sortedList = self._graphs[self._currentGraph].topologicalSort()
        if len(sortedList) == 0:
            print("The current graph is not a DAG!")
        else:
            print("The current graph is a DAG\nWe have the following topological sort:")
            for vertex in sortedList:
                print(str(vertex) + " ")
            print("\n")
            beginVertex = int(input("Enter source vertex:"))
            endVertex = int(input("Enter end vertex:"))
            if beginVertex not in self._graphs[self._currentGraph].vertices or endVertex not in self._graphs[self._currentGraph].vertices:
                raise ValueError("One/both vertices do not exist!")
            else:
                distance, previous = self._graphs[self._currentGraph].highestCostPath(beginVertex, endVertex)
                if distance == float('-inf'):
                    raise ValueError("There is no walk from " + str(beginVertex) + " to " + str(endVertex))
                path = []
                vertex = endVertex
                path.append(vertex)
                while previous[vertex] != -1:
                    path.append(previous[vertex])
                    vertex = previous[vertex]
                print("The cost of the highest cost path is: " + str(distance))
            print("The path is: ")
            for index in range(len(path) - 1, -1, -1):
                print(str(path[index]) + " ")
            print("\n")

    @staticmethod
    def printMenu():
        print("--- OPTIONS MENU ---")
        print("1: generate a random graph")
        print("2: read a graph from a text file")
        print("3: write a graph to a text file")
        print("4: print the number of vertices")
        print("5: list all inbound vertices of the graph")
        print("6: list all outbound vertices of the graph")
        print("7: check if there is edge between two given vertices")
        print("8: print in degree of a given vertex")
        print("9: print out degree of a given vertex")
        print("10: list the inbound edges of a given vertex")
        print("11: list the outbound edges of a given vertex")
        print("12: modify the cost of a given edge")
        print("13: add an edge")
        print("14: remove an edge")
        print("15: add a vertex")
        print("16: remove a vertex")
        print("17: copy graph")
        print("18: parse all vertices")
        print("19: Check if the graph is a DAG; If the graph is a DAG, find a highest cost path between 2 vertices.")

        print("0: exit")

    def start(self):
        print("WELCOME TO MY GRAPH PROGRAM")
        while True:
            try:
                self.printMenu()
                option = input("Please enter your option: ").strip()
                if option == "0":
                    return
                elif option == "1":
                    self.createRandomGraphUI()
                elif option == "2":
                    self.readGraphFromTextFileUI()
                elif option == "3":
                    self.writeGraphToTextFileUI()
                elif option == "4":
                    self.getNumberOfVerticesUI()
                elif option == "5":
                    self.listAllInboundVertices()
                elif option == "6":
                    self.listAllOutboundVertices()
                elif option == "7":
                    self.checkIfThereIsEdgeUI()
                elif option == "8":
                    self.printInDegreeUI()
                elif option == "9":
                    self.printOutDegreeUI()
                elif option == "10":
                    self.listInboundEdges()
                elif option == "11":
                    self.listOutboundEdges()
                elif option == "12":
                    self.modifyCostOfAGivenEdge()
                elif option == "13":
                    self.addEdgeUI()
                elif option == "14":
                    self.removeEdgeUI()
                elif option == "15":
                    self.addVertexUI()
                elif option == "16":
                    self.removeVertexUI()
                elif option == "17":
                    self.copyCurrentGraphUI()
                elif option == "18":
                    self.parseAllVerticesUI()
                elif option == "19":
                    self.topologicalSortUI()
                else:
                    print("Invalid option ! Try again !")

            except ValueError as ve:
                print(str(ve))


def readGraphFromTextFile(file):
    f = open(file, "r")
    line = f.readline()
    vertices, edges = line.strip().split(" ")
    graph = DirectedGraph(int(vertices), int(edges))
    line = f.readline()
    for vertex in range(int(vertices)):
        graph.vertices.append(vertex)
    while len(line) > 0:
        splittedLine = line.strip().split(" ")
        if len(splittedLine) == 1:
            graph.inDict[int(splittedLine[0])] = []
            graph.outDict[int(splittedLine[0])] = []
        else:
            graph.inDict[int(splittedLine[1])].append(int(splittedLine[0]))
            graph.outDict[int(splittedLine[0])].append(int(splittedLine[1]))
            graph.costDict[(int(splittedLine[0]), int(splittedLine[1]))] = int(splittedLine[2])
        line = f.readline()
    f.close()
    return graph


def writeGraphToTextFile(graph, file):
    f = open(file, "w")
    line = str(graph.numberOfVertices) + " " + str(graph.numberOfEdges) + "\n"
    f.write(line)
    if len(graph.inDict) == 0 and len(graph.outDict) == 0:
        raise ValueError("You don't have any vertices and edges to write in the file !")
    for edge in graph.costDict.keys():
        line = str(edge[0]) + " " + str(edge[1]) + " " + str(graph.costDict[edge]) + "\n"
        f.write(line)
    for vertex in graph.inDict.keys():
        if len(graph.inDict[vertex]) == 0 and len(graph.outDict[vertex]) == 0:
            line = vertex + "\n"
            f.write(line)
    f.close()

ui = UI()
ui.start()