import random
import math
from math import radians, sin, cos, sqrt, atan
import heapq
class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict
        self.directed = directed
        if not directed:
            self.make_undirected()
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)
    def connect(self, A, B, distance=1):
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)
    def connect1(self, A, B, distance):
        self.graph_dict.setdefault(A, {})[B] = distance

    # method to get the links of a node
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
    def cost(self, current, next):
        return self.graph_dict[current][next]
    def heuristic(self, goal, node):
        locs = getattr(self, 'locations', None)
        if locs:
            return int(haversine(locs[goal], locs[node]))
        else:
            return 0
    def neighbors(self, node):
        return self.graph_dict[node].keys()
def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)
def haversine(coord1, coord2):
    R = 6371
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
    return 2 * R * atan(sqrt(a))
class PriorityQueue:
    # constructor
    def __init__(self):
        self.elements = []
    def empty(self):
        return len(self.elements) == 0
    def put(self, item, priority):
        self.elements.append((item, priority))
        self.elements.sort(key=lambda x: x[1])
    def get(self):
        return self.elements.pop(0)[0]
class SimpleProblemSolvingAgent:
    def __init__(self, graph, start_city, goal_city):
        self.start_city = start_city
        self.goal_city = goal_city
        self.graph = graph
        self.heuristics = {}
        for city in self.graph.nodes():
            self.heuristics[city] = self.graph.heuristic(self.goal_city, city)
    def search(self, strategy):
        if strategy == 'greedy_best_first':
            return self.greedy_best_first_search()
        elif strategy == 'a_star':
            return self.a_star_search()
        elif strategy == 'hill_climbing':
            return self.hill_climbing_search()
        elif strategy == 'simulated_annealing':
            return self.simulated_annealing_search()
        else:
            return "Invalid strategy"
    def greedy_best_first_search(self):
        # create a priority queue
        frontier = [(self.heuristics[self.start_city], self.start_city)]
        heapq.heapify(frontier)
        cost = 0
        came_from = {self.start_city: None}

        while frontier:
            current = heapq.heappop(frontier)[1]
            closest = None
            if current == self.goal_city:
                break
            for next in self.graph.neighbors(current):
                if next not in came_from:
                    if closest is None or self.heuristics[next] < self.heuristics[closest]:
                        closest = next
            if closest:
                heapq.heappush(frontier, (self.heuristics[closest], closest))
                came_from[closest] = current, self.graph.cost(current, closest)
        path = self.reconstruct_path(came_from)
        cost = self.calculate_cost(path)
        return path, cost
    
    def a_star_search(self):
        frontier = PriorityQueue()
        frontier.put(self.start_city, 0)
        came_from = {self.start_city: None}
        cost_so_far = {self.start_city: 0}
        path = []
        cost = 0
        while not frontier.empty():
            current = frontier.get()
            if current == self.goal_city:
                break
            for next in self.graph.neighbors(current):
                new_cost = cost_so_far[current] + self.graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristics[next]
                    frontier.put(next, priority)
                    came_from[next] = current, self.graph.cost(current, next)
        path = self.reconstruct_path(came_from)
        cost = self.calculate_cost(path)
        return path, cost
    def hill_climbing_search(self):
        current = self.start_city
        path = [current]
        cost = 0
        tried = []
        while current != self.goal_city:
            neighbors = list(self.graph.neighbors(current))
            next = None
            next_cost = 0
            best_cost = float('inf')
            best_neighbor = None
            if current == self.start_city:
                for city in tried:
                    if city in neighbors:
                        neighbors.remove(city)
                        cost = 0
                        path = [self.start_city]
            for neighbor in neighbors:
                if neighbor == self.goal_city:
                    best_neighbor = neighbor
                    best_cost = self.graph.cost(current, neighbor)
                    break
                if neighbor in tried:
                    continue
                if neighbor in path:
                    continue
                if len(list(self.graph.neighbors(neighbor))) == 1:
                    continue
                next_cost = self.graph.cost(current, neighbor)
                if next_cost < best_cost:
                    best_cost = next_cost
                    best_neighbor = neighbor
            if best_neighbor:
                tried.append(best_neighbor)
            else:
                tried.append(current)
                current = path[-2]
                path.pop()
                continue
            
            if best_neighbor:
                current = best_neighbor
                path.append(current)
                cost += best_cost
            else:
                break     
        return path, cost
    def simulated_annealing_search(self):
        # higher number of iterations increases precision
        number_of_iterations = 10
        T = 100
        T_min = 0.00001
        alpha = 0.9
        def simulated_annealing(T, T_min, alpha):
            current = self.start_city
            path = [current]
            cost = 0
            while T > T_min:
                neighbors = list(self.graph.neighbors(current))
                next = random.choice(neighbors)
                if next in path and len(neighbors) > 1:
                    neighbors.remove(next)
                    next = random.choice(neighbors)
                if next in path and len(neighbors) == 1:
                    break
                next_cost = self.graph.cost(current, next)
                delta = next_cost - cost
                if delta < 0 or math.exp(-delta/T) > random.random():
                    path.append(next)
                    cost += next_cost
                    current = next
                if current == self.goal_city:
                    break
                else:
                    T *= alpha
            if current != self.goal_city:
                return path, float('inf')
            else:
                return path, cost
        for i in range(number_of_iterations):
            path, cost = simulated_annealing(T, T_min, alpha)
            if i == 0:
                best_path = path
                best_cost = cost
            else:
                if cost < best_cost:
                    best_path = path
                    best_cost = cost
        return best_path, best_cost  
    def reconstruct_path(self, came_from):
        current = self.goal_city
        total_path = [current]
        while current != self.start_city:
            current, cost = came_from[current]
            total_path.append(current)
        return total_path[::-1]
    def calculate_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self.graph.cost(path[i], path[i + 1])
        return cost