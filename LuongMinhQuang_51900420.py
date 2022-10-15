from typing import Deque
from queue import PriorityQueue

def Heuristic(start, end):
    q = PriorityQueue()
    v = {}
    q.put((diadiem[start], 0, start, [start]))
    while not None:
        (a, gt, dinh, arr) = q.get()
        if dinh == end:
            return a, gt, arr
        for i in khoangcach[dinh]:
            n = gt + khoangcach[dinh][i]
            a = diadiem[i]
            v[start] = diadiem[start]
            if not i in v or v[i] >= a:
                v[i] = a
                q.put((a, n, i, arr + [i]))


def a_star(start, end):
    q = PriorityQueue()
    v = {}
    q.put((diadiem[start], 0, start, [start]))
    while not None:
        (a, gt, dinh, arr) = q.get()
        if dinh == end:
            return a, gt, arr
        for i in khoangcach[dinh]:
            n = gt + khoangcach[dinh][i]
            a = n + diadiem[i]
            v[start] = diadiem[start]
            if not i in v or v[i] >= a: 
                v[i] = a
                q.put((a, n, i, arr + [i]))

# Cau 2 
# BFS
def __init__(self, row, col): 
        self.ROW = row 
        self.COL = col 
        

def s(self, i, j, v):
    r = len(v)
    c = len(v[0])
    return (i >= 0 and i < r and j >= 0 and j < c and self[i][j] == 1 and not v[i][j])
 
 
def BFS(self,v,i,j):
    row = [-1, -1, -1, 0, 1, 0, 1, 1]
    col = [-1, 1, 0, -1, -1, 1, 0, 1]
    queue = Deque()
    queue.append((i, j))
    
    while queue:
        i, j = queue.pop()
        for k in range(len(row)):
            if s(self, i + row[k], j + col[k], v):
                v[i + row[k]][j + col[k]] = True
                queue.append((i + row[k], j + col[k]))


if __name__ == '__main__':
    # Cau 1 
    # Du lieu 
    khoangcach = {"Arad" : {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},"Bucharest" : {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85  },"Craiova" : {"Pitesti": 138, "Drobeta": 120, "Rimnicu Vilcea": 146  },
     "Drobeta" : {"Mehadia": 75 , "Craiova": 120  },"Eforie" : {"Hirsova": 86 },"Fagaras" : {"Sibiu": 99, "Bucharest": 211 },"Giurgiu" : {"Bucharest": 90 },"Hirsova" : {"Eforie": 86, "Urziceni": 98 },
     "Iasi" : {"Neamt": 87, "Vaslui": 92 },"Lugoj" : {"Timisoara": 111, "Mehadia": 70 },"Mehadia" : {"Lugoj": 70, "Drobeta": 75 },"Neamt" : {"Iasi": 87 },"Oradea" : {"Zerind": 71, "Sibiu": 151 },
     "Pitesti" : {"Craiova": 138, "Bucharest": 101, "Rimnicu Vilcea": 97 },"Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146 },"Sibiu" : {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80 },
     "Timisoara" : {"Arad": 118, "Lugoj": 111 },"Urziceni" : {"Bucharest": 85, "Hirsova": 98, "Vaslui":  142 },"Vaslui" : {"Urziceni": 142, "Iasi": 92 },"Zerind" : {"Oradea": 71, "Arad": 75 }}

    diadiem = {"Arad" : 366 , "Bucharest" : 0,"Craiova" : 160,"Drobeta" : 242,"Eforie" : 161,
                     "Fagaras" : 176,"Giurgiu" : 77,"Hirsova" : 151,"Iasi" : 226,"Lugoj" : 244,
                     "Mehadia" : 241,"Neamt" : 234,"Oradea" : 380,"Pitesti" : 100,"Rimnicu Vilcea" : 193,
                     "Sibiu" : 253,"Timisoara" : 329,"Urziceni" : 80,"Vaslui" : 199,"Zerind" : 374,}
    # A*
    diembatdau = "Arad"
    diemketthuc = "Bucharest" 

    print("--Heuristic")
    a,gt,optimal_path = Heuristic(diembatdau,diemketthuc)
    for i in optimal_path:
        print(i,end = ' ')
    print('\nKhoang cach :', gt)
    print("")
    print("--A*")
    a,gt,optimal_path = a_star(diembatdau,diemketthuc)
    for i in optimal_path:
        print(i,end = ' ')    
    print('\nKhoang cach :', gt)

    print("")
    # Cau 2 
    # Du lieu 
    self = [[1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]]

    #BFS
    k = [[False for j in range(len(self))] for i in range(len(self[0]))]
    count = 0
    for i in range(len(self[0])):
        for j in range(len(self)):
            if self[i][j] == 1 and  k[i][j] == False:
                BFS(self, k, i, j)
                count = count + 1
    print("BFS :", count)