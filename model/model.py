import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMap = {}
        for n in self._nodes:
            self._idMap[n.id] = n

    def buildGraph(self, year, diff):
        self._graph.clear()
        self._graph.add_nodes_from(self._nodes)
        edges = DAO.getAllEdges(self._idMap)
        for e in edges:
            self._graph.add_edge(e[0], e[1], weight=0)
        weights = DAO.getWeights(year, diff)
        for e in weights:
            v = self._idMap[e[0].upper()]
            u = self._idMap[e[1].upper()]
            if self._graph.has_edge(v, u):
                self._graph[v][u]["weight"] += 1

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getWeightNeighbors(self):
        result = {}
        for n in self._nodes:
            weight = 0
            for v in self._graph.neighbors(n):
                weight += self._graph[v][n]["weight"]
            result[n] = weight
        return result
