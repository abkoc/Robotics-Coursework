from collections import deque
 
class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        H = {
            'A': 8,
            'B': 3,
            'C': 7,
            'D': 0
        }
 
        return H[n]
 
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a list of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
        # node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been already inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            print(f"\n\n Nodes to be compared {open_lst}")
            for v in par:
                print(f"\n Former node of {v} in shortest path : {par[v]}")
                print(f" Shortest distance {start}-{v}       : {poo[v]}")

            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                print(f"Estimate {v} : Distance from start to {v} + H({v}) = \
                {poo[v]} + {self.h(v)} = {poo[v] + self.h(v)}")
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return None

            # Indicate the expanded path at each step
            print(f"\n          Expanded node : {n}")
            expanded_path = []
            expanded_node = n
            while par[expanded_node] != expanded_node:
                expanded_path.append(expanded_node)
                expanded_node = par[expanded_node]
 
            expanded_path.append(start)
            expanded_path.reverse()
            print('             Expanded Path : {}'.format(expanded_path))
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

 
        print('Path does not exist!')
        return None


""" Main Code """

adjac_lis = {
    'A': [('B', 4), ('C', 1)],
    'B': [('C', 2), ('D', 6)],
    'C': [('B', 2), ('D', 9)]
}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('A', 'D')
