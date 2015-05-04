__author__ = 'zephyros'
class PageRank:
    def __init__(self, graph, d, t):
        self.graph = graph
        self.nodeNum = len(graph)
        self.damping = d
        self.iterationTimes = t

    def rank(self):
        lastScores = [1 for i in range(self.nodeNum)]
        scores = [1 for i in range(self.nodeNum)]
        for i in range(self.iterationTimes):
            print(scores)
            for i in range(self.nodeNum):
                inEdges = self.getInEdge(i)
                temp = 0
                for inEdge in inEdges:
                    index = inEdge[0]
                    outDegree =len(self.getOutEdge(index))
                    temp += lastScores[index] / outDegree
                scores[i] = self.damping * (temp + 1)
            for i in range(self.nodeNum):
                lastScores[i] = scores[i]
        return scores

    def getOutEdge(self, index):
        edges = []
        for i in range(self.nodeNum):
            weight = self.graph[index][i]
            if weight > 0:
                edges.append([i, weight])
        return edges

    def getInEdge(self, index):
        edges = []
        for i in range(self.nodeNum):
            weight = self.graph[i][index]
            if weight > 0:
                edges.append([i, weight])
        return edges

if __name__ == "__main__":
    g = [[0, 1, 1], [0, 0, 1], [1, 0 , 0]]
    pr = PageRank(g, 0.5, 100)
    print(pr.rank())


