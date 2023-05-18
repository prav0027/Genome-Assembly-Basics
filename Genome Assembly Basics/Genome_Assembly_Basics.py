##def stringComposition(k, genome):
##    result = []
##    for i in range(len(genome)-k+1):
##        result.append(genome[i:i+k])
##    return result

##def stringReconstruction(reads):
##    readsList = reads.split()
##    result = readsList[0]
##    for i in readsList:
##        if i!=result:
##            result+=i[-1]
##    return result


##def overlapGraph(readsList):
##    #readsList = reads.split()
##    result = ""
##    for i in readsList:
##        resultsList = []
##        compareVal = i[1:]
##        for k in readsList:
##            if k!=i:
##                if compareVal == k[:-1]:
##                    resultsList.append(k)
##        if len(resultsList)>0:
##            if result=="":
##                result = i+":"
##                for n in resultsList:
##                    result=result+" "+n
##            else:
##                result = result+"\n"+i+":"
##                for n in resultsList:
##                    result=result+" "+n

##    return result

##def deBruijnGraph(k, genome):
##    result = dict()
##    readsList = stringComposition(k-1, genome)
##    for i in range(len(readsList)):
##        compareString = readsList[i]
##        genomeCompare = genome[i+1:i+k]
##        if genomeCompare[:-1] == compareString[1:]:
##            if compareString in list(result.keys()):
##                resultTemp = result[compareString]
##                resultTemp.append(genomeCompare)
##                result[compareString] = resultTemp
##            else:
##                resultTemp = list()
##                resultTemp.append(genomeCompare)
##                result[compareString] = resultTemp

##    return result

##def printDeBruijnGraph(result):
##    for i in list(result.keys()):
##        printTemp = i + ":"
##        for n in result[i]:
##            printTemp = printTemp + " "+n
##        print(printTemp)

##def walkingDeBruijn(reads):
##    readsList = reads.split()
##    result = dict()
##    for i in readsList:
##        iPrefix = i[:-1]
##        if i[:-1] in list(result.keys()):
##            resultTemp = result[iPrefix]
##            resultTemp.append(i[1:])
##            result[iPrefix] = resultTemp
##        else:
##            resultTemp = list()
##            resultTemp.append(i[1:])
##            result[iPrefix] = resultTemp

##    return result


#class EulerianCycle:
#    def __init__(self):
#        self.adj = []
#        self.n = None
#        self.nUnEdges = 0 # number of explored edges
#        #self.edgesExplored = []
#        self.nodesWUE = dict() # key: node with unused edges; value: the position of such node in the current path
#        self.outDeg = []
#        self.adjCurPos = []
#        self.path = []
#        self._input()
#        self.calculateEulerianCycle()
#        self.printPath()

#    def _input(self):
#        with open('euler.txt', 'r') as file:
#            dataString = file.read()
#        data = list(dataString.strip().split())
#        self.n = len(data) // 3
#        self.adj = [[]] * self.n
#        self.unusedEdges = [[]] * self.n
#        self.outDeg = [None] * self.n
#        self.adjCurPos = [0] * self.n
#        for i in range(self.n):
#            curIn = int(data[i*3])
#            self.adj[curIn] = list(map(int, data[i*3+2].split(',')))
#            l = len(self.adj[curIn])
#            self.outDeg[curIn] = l
#            self.nUnEdges += l
    
#    def explore(self, s):
#        self.path.append(s)
#        curPos = self.adjCurPos[s]
#        curMaxPos = self.outDeg[s]
#        while curPos < curMaxPos:
#            self.adjCurPos[s] = curPos + 1
#            if curPos + 1 < curMaxPos:
#                self.nodesWUE[s] = len(self.path) - 1
#            else:
#                if s in self.nodesWUE:
#                    del self.nodesWUE[s]
#            v = self.adj[s][curPos]
#            self.path.append(v)
#            s = v
#            curPos = self.adjCurPos[s]
#            curMaxPos = self.outDeg[s]
#            self.nUnEdges -= 1
#        return

#    def updatePath(self, startPos):
#        l = len(self.path) - 1
#        #print(self.path[startPos:l])
#        #print(self.path[:startPos])
#        self.path = self.path[startPos:l] + self.path[:startPos]
#        for node, pos in self.nodesWUE.items():
#            if pos < startPos:
#                self.nodesWUE[node] = pos + l - startPos
#            else:
#                self.nodesWUE[node] = pos - startPos
#        return

#    def calculateEulerianCycle(self):
#        self.explore(0)
#        while self.nUnEdges > 0:
#            node, pos = self.nodesWUE.popitem()
#            self.updatePath(pos)
#            self.explore(node)
#        return self.path

#    def printPath(self):
#        pathCopy = self.path
#        resultTemp = list()
#        copyChar = pathCopy[0]
#        indexSecondOcc = [i for i, n in enumerate(pathCopy) if n == copyChar][1]
#        print(indexSecondOcc)
#        for k in range(indexSecondOcc, len(pathCopy)):
#            resultTemp.append(pathCopy[k])
#        for l in range(1, indexSecondOcc):
#            resultTemp.append(pathCopy[l])
#        resultTemp.append(copyChar)
#        print(' '.join([str(node) for node in resultTemp]))
#        #print("done")
#        #print(' '.join([str(node) for node in self.path]))       

#class EulerianPath:
#    def __init__(self):
#        self.adj = []
#        self.n = None
#        self.nUnEdges = 0 # number of explored edges
#        self.nodesWUE = dict() # key: node with unused edges; value: the position of such node in the current path
#        self.inDeg = []
#        self.outDeg = []
#        self.adjCurPos = []
#        self.path = []
#        self.unbalancedNode = []
#        self._input()
#        self.calculateEulerianPath()
#        self.printPath()
#        self.saveResult()

#    def _input(self):
#        with open('euler.txt', 'r') as file:
#            dataString = file.read()
#        data = list(dataString.strip().split())
#        curMax = 0
#        for i in range(len(data) // 3):
#            curMax = max(int(data[i*3]), curMax, max(list(map(int, data[i*3+2].split(',')))))
#        self.n = curMax + 1
#        self.adj = [[]] * self.n
#        self.unusedEdges = [[]] * self.n
#        self.inDeg = [0] * self.n
#        self.outDeg = [0] * self.n
#        self.adjCurPos = [0] * self.n
#        for i in range(len(data) // 3):
#            curIn = int(data[i*3])
#            self.adj[curIn] = list(map(int, data[i*3+2].split(',')))
#            for v in self.adj[curIn]:
#                self.inDeg[v] += 1
#            l = len(self.adj[curIn])
#            self.outDeg[curIn] = l
#            self.nUnEdges += l
    
#    def addEdge(self):
#        for v in range(self.n):
#            if self.inDeg[v] != self.outDeg[v]:
#                if self.inDeg[v] < self.outDeg[v]:
#                    self.unbalancedNode.append(v)
#                else:
#                    self.unbalancedNode.insert(0, v)
#        if len(self.unbalancedNode) > 0:
#            self.adj[self.unbalancedNode[0]].append(self.unbalancedNode[1])
#            self.outDeg[self.unbalancedNode[0]] += 1
#            self.inDeg[self.unbalancedNode[1]] += 1
    
#    def explore(self, s):
#        self.path.append(s)
#        curPos = self.adjCurPos[s]
#        curMaxPos = self.outDeg[s]
#        while curPos < curMaxPos:
#            self.adjCurPos[s] = curPos + 1
#            if curPos + 1 < curMaxPos:
#                self.nodesWUE[s] = len(self.path) - 1
#            else:
#                if s in self.nodesWUE:
#                    del self.nodesWUE[s]
#            v = self.adj[s][curPos]
#            self.path.append(v)
#            s = v
#            curPos = self.adjCurPos[s]
#            curMaxPos = self.outDeg[s]
#            self.nUnEdges -= 1
#        return

#    def updatePath(self, startPos):
#        l = len(self.path) - 1
#        self.path = self.path[startPos:l] + self.path[:startPos]
#        for node, pos in self.nodesWUE.items():
#            if pos < startPos:
#                self.nodesWUE[node] = pos + l - startPos
#            else:
#                self.nodesWUE[node] = pos - startPos
#        return

#    def calculateEulerianCycle(self):
#        self.explore(0)
#        while self.nUnEdges > 0:
#            node, pos = self.nodesWUE.popitem()
#            self.updatePath(pos)
#            self.explore(node)
#        return self.path
    
#    def calculateEulerianPath(self):
#        self.addEdge()
#        self.calculateEulerianCycle()
#        if len(self.unbalancedNode) > 0:
#            for i in range(len(self.path)-1):
#                if self.path[i] == self.unbalancedNode[0] and self.path[i+1] == self.unbalancedNode[1]:
#                    self.updatePath(i+1)
#                    break
#        return           

#    def printPath(self):
#        print(' '.join([str(node) for node in self.path]))     

#    def saveResult(self):
#        f = open('result.txt', 'w')
#        f.write(' '.join([str(node) for node in self.path]))

#if __name__ == "__main__":
#    EulerianPath()

class EulerianPath:
    def __init__(self, adj):
        self.adj = adj
        self.updateAdj()

    def updateAdj(self):
        self.n = len(self.adj)
        self.nUnEdges = 0 # number of unexplored edges
        self.nodesWUE = dict() # key: node with unused edges; value: the position of such node in the current path
        self.inDeg = dict()
        self.outDeg = dict()
        self.adjCurPos = dict()
        self.path = []
        self.unbalancedNode = []
        for w, vList in self.adj.items():
            self.inDeg[w] = self.inDeg.get(w, 0)
            for v in vList:
                self.inDeg[v] = self.inDeg.get(v, 0) + 1
            l = len(vList)
            self.outDeg[w] = l
            self.nUnEdges += l
            self.adjCurPos[w] = 0

    def _input(self):
        data = list(sys.stdin.read().strip().split())
        curMax = 0
        for i in range(len(data) // 3):
            curMax = max(int(data[i*3]), curMax, max(list(map(int, data[i*3+2].split(',')))))
        self.n = curMax + 1
        self.adj = [[]] * self.n
        self.unusedEdges = [[]] * self.n
        self.inDeg = [0] * self.n
        self.outDeg = [0] * self.n
        self.adjCurPos = [0] * self.n
        for i in range(len(data) // 3):
            curIn = int(data[i*3])
            self.adj[curIn] = list(map(int, data[i*3+2].split(',')))
            for v in self.adj[curIn]:
                self.inDeg[v] += 1
            l = len(self.adj[curIn])
            self.outDeg[curIn] = l
            self.nUnEdges += l
    
    def addEdge(self):
        if type(self.adj) is dict:
            for v in self.adj.keys():
                if self.inDeg[v] != self.outDeg[v]:
                    if self.inDeg[v] < self.outDeg[v]:
                        self.unbalancedNode.append(v)
                    else:
                        self.unbalancedNode.insert(0, v)
            if len(self.unbalancedNode) > 0:
                self.adj[self.unbalancedNode[0]].append(self.unbalancedNode[1])
                self.outDeg[self.unbalancedNode[0]] += 1
                self.inDeg[self.unbalancedNode[1]] += 1
            return    
        for v in range(self.n):
            if self.inDeg[v] != self.outDeg[v]:
                if self.inDeg[v] < self.outDeg[v]:
                    self.unbalancedNode.append(v)
                else:
                    self.unbalancedNode.insert(0, v)
        if len(self.unbalancedNode) > 0:
            self.adj[self.unbalancedNode[0]].append(self.unbalancedNode[1])
            self.outDeg[self.unbalancedNode[0]] += 1
            self.inDeg[self.unbalancedNode[1]] += 1
        return
    
    def explore(self, s):
        self.path.append(s)
        curPos = self.adjCurPos[s]
        curMaxPos = self.outDeg[s]
        while curPos < curMaxPos:
            self.adjCurPos[s] = curPos + 1
            if curPos + 1 < curMaxPos:
                self.nodesWUE[s] = len(self.path) - 1
            else:
                if s in self.nodesWUE:
                    del self.nodesWUE[s]
            v = self.adj[s][curPos]
            self.path.append(v)
            s = v
            curPos = self.adjCurPos[s]
            curMaxPos = self.outDeg[s]
            self.nUnEdges -= 1
        return

    def updatePath(self, startPos):
        l = len(self.path) - 1
        self.path = self.path[startPos:l] + self.path[:startPos]
        for node, pos in self.nodesWUE.items():
            if pos < startPos:
                self.nodesWUE[node] = pos + l - startPos
            else:
                self.nodesWUE[node] = pos - startPos
        return

    def calculateEulerianCycle(self):
        if type(self.adj) is dict:
            w, vList = self.adj.popitem()
            self.adj[w] = vList
            self.explore(w)
        else:
            self.explore(0)
        while self.nUnEdges > 0:
            node, pos = self.nodesWUE.popitem()
            self.updatePath(pos)
            self.explore(node)
        return self.path
    
    def calculateEulerianPath(self):
        self.addEdge()
        self.calculateEulerianCycle()
        if len(self.unbalancedNode) > 0:
            for i in range(len(self.path)-1):
                if self.path[i] == self.unbalancedNode[0] and self.path[i+1] == self.unbalancedNode[1]:
                    self.updatePath(i+1)
                    break
        return self.path          

    def printPath(self):
        print('->'.join([str(node) for node in self.path]))     

    def saveResult(self):
        f = open('result.txt', 'w')
        f.write('->'.join([str(node) for node in self.path]))

class StringReconstruction:
    def __init__(self):
        self.adj = self.readData()
        self.path = EulerianPath(self.adj).calculateEulerianPath()
        print(self.reconstructFromPath(self.path))

    def readData(self):
        with open('data.txt', 'r') as file:
            dataString = file.read()
        data = list(dataString.strip().split())
        adj = self.DeBrujin(int(data[0]), data[1:]) 
        return adj
    
    def DeBrujin(self, k, patterns):
        adjdb = dict()
        for p in patterns:
            if p[:k-1] in adjdb:
                adjdb[p[:k-1]].append(p[1:])
            else:
                adjdb[p[:k-1]] = []
                adjdb[p[:k-1]].append(p[1:])
            if p[1:] not in adjdb:
                adjdb[p[1:]] = []
        return adjdb

    def reconstructFromPath(self, path):
        return path[0] + ''.join(seq[-1] for seq in path[1:])

if __name__ == "__main__":
    StringReconstruction()