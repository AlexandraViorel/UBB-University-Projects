import copy
import random


class DirectedGraph:
    def __init__(self, numberOfVertices, numberOfEdges):
        self._numberOfVertices = numberOfVertices
        self._numberOfEdges = numberOfEdges
        self._inDict = {}
        self._outDict = {}
        self._costDict = {}
        for i in range(self.numberOfVertices):
            self.inDict[i] = []
            self.outDict[i] = []

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
        self._numberOfVertices += 1
        return True

    def removeVertex(self, x):
        if x not in self.inDict.keys() and x not in self.outDict.keys():
            return False
        self.inDict.pop(x)
        self.outDict.pop(x)
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

            except ValueError as ve:
                print(str(ve))


def readGraphFromTextFile(file):
    f = open(file, "r")
    line = f.readline()
    vertices, edges = line.strip().split(" ")
    graph = DirectedGraph(int(vertices), int(edges))
    line = f.readline()
    while len(line) > 0:
        splittedLine = line.strip().split(" ")
        if len(splittedLine) == 1:
            graph.inDict[int(splittedLine[0])] = []
            graph.outDict[int(splittedLine[0])] = []
        else:
            graph.inDict[int(splittedLine[1])].append(int(splittedLine[0]))
            graph.outDict[int(splittedLine[0])] = [int(splittedLine[1])]
            graph.costDict[(int(splittedLine[0]), splittedLine[1])] = splittedLine[2]
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