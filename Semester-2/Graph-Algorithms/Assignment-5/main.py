import copy
import random


class UndirectedGraph:
    def __init__(self, numberOfVertices, numberOfEdges):
        self._numberOfVertices = numberOfVertices
        self._numberOfEdges = numberOfEdges
        self._verticesList = []
        self._edgesDict = {}
        for vertex in range(self._numberOfVertices):
            self._edgesDict[vertex] = []
            self._verticesList.append(vertex)

    @property
    def numberOfVertices(self):
        return self._numberOfVertices

    @property
    def numberOfEdges(self):
        return self._numberOfEdges

    @property
    def verticesList(self):
        return self._verticesList

    @property
    def edgesDict(self):
        return self._edgesDict

    @numberOfEdges.setter
    def numberOfEdges(self, value):
        self._numberOfEdges = value

    def parseVertices(self):
        for v in self._verticesList:
            yield v

    def parseEdges(self, x):
        for y in self._edgesDict[x]:
            yield y

    def addVertex(self, x):
        """
            This function adds a given vertex to the undirected graph if it does not already exist.
        :param x: the given vertex
        :return: False if the vertex already exists, True if it does not exist
        """
        if x in self._verticesList:
            return False

        self._verticesList.append(x)
        self._edgesDict[x] = []
        self._numberOfVertices += 1
        return True

    def removeVertex(self, x):
        """
            This function removes a given vertex from the undirected graph if it exists.
        :param x: the given vertex
        :return: True if the vertex exists and it is removed, False if it does not exist
        """
        if x not in self._verticesList or x not in self._edgesDict.keys():
            return False

        self._verticesList.remove(x)
        self._edgesDict.pop(x)
        self._numberOfVertices -= 1
        for vertex in self._edgesDict.keys():
            if x in self._edgesDict[vertex]:
                self._edgesDict[vertex].remove(x)
                self._numberOfEdges -= 1
        return True

    def degree(self, x):
        """
            This function returns the degree of a given vertex.
        :param x: the given vertex
        :return: the degree of the vertex if it exists, -1 if it does not exist
        """
        if x not in self._verticesList:
            return -1
        return len(self._edgesDict[x])

    def addEdge(self, x, y):
        """
            This function adds a given edge to the undirected graph.
        :param x: the first vertex
        :param y: the second vertex
        :return: True if the vertices exist and the edge does not already exist and the edge is added, False if the edge
        cannot be added (if one of the vertices does not exist or if the edge already exists)
        """
        if x not in self._verticesList or y not in self._verticesList:  # one of the vertices does not exist
            return False
        if x == y:
            return False
        if x in self._edgesDict[y] or y in self._edgesDict[x]:  # the edge already exists
            return False
        self._edgesDict[x].append(y)
        self._edgesDict[y].append(x)
        self._numberOfEdges += 1
        return True

    def removeEdge(self, x, y):
        """
            This function removes a given edge from the undirected graph if it exists.
        :param x: the first vertex
        :param y: the second vertex
        :return: True if the vertices and the edge exist and the edge is removed, False if one the vertices do not
        exist or if the edge does not exist
        """
        if x not in self._verticesList or y not in self._verticesList:  # one of the vertices does not exist
            return False
        if x not in self._edgesDict[y] or y not in self._edgesDict[x]:  # the edge does not exist
            return False
        self._edgesDict[x].remove(y)
        self._edgesDict[y].remove(x)
        self._numberOfEdges -= 1
        return True

    def findIfEdge(self, x, y):
        """
            This function checks if there is an edge between two given vertices.
        :param x: the first vertex
        :param y: the second vertex
        :return: True if the edge exists, False if one of the vertices do not exist or if the edge does not exist
        """
        if x not in self._verticesList or y not in self._verticesList:
            return False
        if x in self._edgesDict[y] and y in self._edgesDict[x]:
            return True
        return False

    def makeCopy(self):
        """
            This function makes a copy of the graph.
        :return: the copy of the graph
        """
        return copy.deepcopy(self)

    def depthFirstTraversal(self, vertex, visited, cc):
        """
            This function traverses the graph with a depth-first algorithm for a given vertex
        :param vertex: the given vertex
        :param visited: a dictionary where we mark the visited vertices
        :param cc: the connected component list for the given graph
        :return: the connected component with the given vertex as a starting point
        """
        visited[vertex] = True
        cc.append(vertex)
        for v in self._edgesDict[vertex]:
            if visited[v] is False:
                cc = self.depthFirstTraversal(v, visited, cc)
        return cc

    def findConnectedComponents(self):
        """
            This function finds all the connected components of the graph.
        :return: the list with the connected components
        """
        visited = {}
        allConnected = []  # the list with all the connected components
        for vertex in self._verticesList:
            visited[vertex] = False
        for vertex in self._verticesList:
            if visited[vertex] is False:
                cc = []
                allConnected.append(self.depthFirstTraversal(vertex, visited, cc))
        return allConnected

    def isSafe(self, v, pos, path):
        if v not in self._edgesDict[path[pos - 1]]:
            return False
        for vertex in path:
            if vertex == v:
                return False
        return True

    def hamiltonianCycleUtil(self, path, pos):
        if pos == self._numberOfVertices:
            if path[0] in self._edgesDict[path[pos - 1]]:
                return True
            else:
                return False

        for v in range(1, self._numberOfVertices):
            if self.isSafe(v, pos, path) is True:
                path[pos] = v
                if self.hamiltonianCycleUtil(path, pos+1) is True:
                    return True
                path[pos] = -1
        return False

    def hamiltonianCycle(self):
        path = [-1] * self._numberOfVertices
        path[0] = 0
        if self.hamiltonianCycleUtil(path, 1) is False:
            return False, [-1]
        return True, path


class UI:
    def __init__(self):
        self._graphs = []
        self._currentGraph = None

    def createRandomGraphUI(self):
        """
            This function creates a random graph with the number of vertices and edges given by the user and adds it to
        the graphs list.
        """
        vertices = int(input("Enter the number of vertices: "))
        edges = int(input("Enter the number of edges: "))
        graph = self.createRandomGraph(vertices, edges)
        if self._currentGraph is None:
            self._currentGraph = 0
        self._graphs.append(graph)
        self._currentGraph = len(self._graphs) - 1

    @staticmethod
    def createRandomGraph(vertices, edges):
        """
            This function creates a random graoh with the given number of vertices and edges.
        :param vertices: the number of vertices
        :param edges: the number of edges
        :return: the randomly created graph
        """
        if edges > vertices * vertices:
            raise ValueError("Too many edges !")
        graph = UndirectedGraph(vertices, 0)
        i = 0
        while i < edges:
            x = random.randint(0, vertices - 1)
            y = random.randint(0, vertices - 1)
            if graph.addEdge(x, y):
                i += 1
        return graph

    def readGraphFromTextFileUI(self):
        """
            This function reads a graph from a text file with the name given by the user and adds it to the graphs list
        """
        file = input("Write the name of the file: ")
        if self._currentGraph is None:
            self._currentGraph = 0
        graph = readGraphFromFile(file)
        self._graphs.append(graph)
        self._currentGraph = len(self._graphs) - 1

    def writeGraphToTextFileUI(self):
        """
            This function writes the current graph to a text file.
        """
        current_graph = self._graphs[self._currentGraph]
        file = "outputgraph" + str(self._currentGraph) + ".txt"
        writeGraphToFile(file, current_graph)

    def getNumberOfVerticesUI(self):
        """
            This function prints the number of vertices of the current graph.
        """
        numberOfVertices = self._graphs[self._currentGraph].numberOfVertices
        print("The number of vertices of the current graph is " + str(numberOfVertices))

    def checkIfThereIsEdgeUI(self):
        """
            This function checks if there is edge between two vertices given by the user and prints a message.
        """
        x = int(input("Write the first vertex: "))
        y = int(input("Write the second vertex: "))
        edge = self._graphs[self._currentGraph].findIfEdge(x, y)
        if edge is not False:
            print("There is an edge between " + str(x) + " and " + str(y))
        else:
            print("There is no edge between " + str(x) + " and " + str(y))

    def printDegreeUI(self):
        """
            This function prints the degree of a vertex given by the user.
        :return:
        """
        x = int(input("Write the vertex: "))
        degree = self._graphs[self._currentGraph].degree(x)
        if degree == -1:
            print("This vertex does not exist!")
        else:
            print("The degree of the vertex " + str(x) + " is: " + str(degree))

    def listBoundEdges(self):
        """
            This function prints the edges of a vertex given by the user.
        """
        vertex = int(input("Write the vertex: "))
        print(str(vertex) + " :")
        for x in self._graphs[self._currentGraph].parseEdges(vertex):
            print("(" + str(x) + ", " + str(vertex) + ")")

    def listAllBoundEdges(self):
        """
            This function prints the edges of all vertices of the current graph.
        """
        for x in self._graphs[self._currentGraph].parseVertices():
            line = str(x) + " :"
            for y in self._graphs[self._currentGraph].parseEdges(x):
                line = line + " " + str(y)
            print(line)

    def addEdgeUI(self):
        """
            This function adds an edge given by the user.
        """
        x = int(input("Write the first vertex: "))
        y = int(input("Write the second vertex: "))
        result = self._graphs[self._currentGraph].addEdge(x, y)
        if result is False:
            print("There already exists an edge between these vertices!")
        else:
            print("Edge added successfully!")

    def removeEdgeUI(self):
        """
            This function removes an edge given by the user.
        """
        x = int(input("Write the first vertex: "))
        y = int(input("Write the second vertex: "))
        result = self._graphs[self._currentGraph].removeEdge(x, y)
        if result is False:
            print("There is no edge between these vertices!")
        else:
            print("Edge removed successfully!")

    def addVertexUI(self):
        """
            This function adds a vertex given by the user.
        """
        x = int(input("Write the vertex: "))
        result = self._graphs[self._currentGraph].addVertex(x)
        if result is False:
            print("This vertex already exists!")
        else:
            print("Vertex added successfully!")

    def removeVertexUI(self):
        """
            This function removes a vertex given by the user.
        """
        x = int(input("Write the vertex: "))
        result = self._graphs[self._currentGraph].removeVertex(x)
        if result is False:
            print("This vertex does not exist!")
        else:
            print("Vertex removed successfully!")

    def copyCurrentGraphUI(self):
        """
            This function copies the current graph.
        """
        copyG = self._graphs[self._currentGraph].copyGraph()
        self._graphs.append(copyG)
        print("Graph copied successfully!")

    def parseAllVerticesUI(self):
        """
            This function prints all the vertices of the current graph.
        """
        for vertex in self._graphs[self._currentGraph].parseTheSetOfVertices():
            print(vertex)

    def findConnectedComponentsUI(self):
        """
            This function prints the connected components of the current graph.
        """
        connectedComponents = self._graphs[self._currentGraph].findConnectedComponents()
        for cc in connectedComponents:
            print(cc)

    def hamiltonianCycleUI(self):
        hasHamCycle, path = self._graphs[self._currentGraph].hamiltonianCycle()
        if hasHamCycle is False:
            print("The graph does not have any hamiltonian cycle")
        else:
            print("The hamiltonian cycle of the graph is : \n")
            for vertex in path:
                print(str(vertex) + " ")
            print(str(path[0]))

    @staticmethod
    def printMenu():
        """
            This function prints the options menu.
        """
        print("--- OPTIONS MENU ---")
        print("1: generate a random graph")
        print("2: read a graph from a text file")
        print("3: write a graph to a text file")
        print("4: print the number of vertices")
        print("5: list the bound edges of a vertex")
        print("6: list all bound vertices of the graph")
        print("7: check if there is edge between two given vertices")
        print("8: print the degree of a given vertex")
        print("9: add an edge")
        print("10: remove an edge")
        print("11: add a vertex")
        print("12: remove a vertex")
        print("13: copy graph")
        print("14: parse all vertices")
        print("15: get connected components using a depth-first traversal")
        print("16: hamiltonian cycle")
        print("0: exit")

    def start(self):
        """
            This function starts the application.
        """
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
                    self.listBoundEdges()
                elif option == "6":
                    self.listAllBoundEdges()
                elif option == "7":
                    self.checkIfThereIsEdgeUI()
                elif option == "8":
                    self.printDegreeUI()
                elif option == "9":
                    self.addEdgeUI()
                elif option == "10":
                    self.removeEdgeUI()
                elif option == "11":
                    self.addVertexUI()
                elif option == "12":
                    self.removeVertexUI()
                elif option == "13":
                    self.copyCurrentGraphUI()
                elif option == "14":
                    self.parseAllVerticesUI()
                elif option == "15":
                    self.findConnectedComponentsUI()
                elif option == "16":
                    self.hamiltonianCycleUI()

            except ValueError as ve:
                print(str(ve))


def readGraphFromFile(file):
    """
        This function reads a graph from a given file
    :param file: the given file
    :return: the graph
    """
    f = open(file, "r")
    line = f.readline()
    vertices, edges = line.strip().split(" ")
    graph = UndirectedGraph(int(vertices), 0)
    line = f.readline().strip()
    while len(line) > 0:
        splittedLine = line.split(" ")
        if len(splittedLine) != 1 and int(splittedLine[0]) != int(splittedLine[1]):
            if int(splittedLine[0]) not in graph.edgesDict[int(splittedLine[1])]:
                graph.numberOfEdges += 1
                graph.edgesDict[int(splittedLine[1])].append(int(splittedLine[0]))
            if int(splittedLine[1]) not in graph.edgesDict[int(splittedLine[0])]:
                graph.edgesDict[int(splittedLine[0])].append(int(splittedLine[1]))
        line = f.readline().strip()
    f.close()
    return graph


def writeGraphToFile(file, graph):
    """
        This function writes a given graph to a given file.
    :param file: the file
    :param graph: the graph
    """
    f = open(file, "w")
    line = str(graph.numberOfVertices) + " " + str(graph.numberOfEdges) + "\n"
    f.write(line)
    if len(graph.verticesList) == 0 and len(graph.edgesDict) == 0:
        raise ValueError("There is nothing to be written in the file !")
    writtenEdges = []
    for vertex in graph.verticesList:
        if len(graph.edgesDict[vertex]) != 0:
            for vertex2 in graph.edgesDict[vertex]:
                if [vertex, vertex2] not in writtenEdges and [vertex2, vertex] not in writtenEdges:
                    line = str(vertex) + " " + str(vertex2) + "\n"
                    f.write(line)
        else:
            line = str(vertex) + "\n"
            f.write(line)
    f.close()


ui = UI()
ui.start()
