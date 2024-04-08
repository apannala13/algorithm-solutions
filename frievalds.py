"""
Frievalds algorithm implementation.
Given three matrices, A, B, C,
verify A x B == C.. 
generates a random vector r of dimension n * 1,
n being # of columns in B and rows in A.
A (B * r) == C * r
"""
from random import randint
from sys import stdin

class Frievalds:
    def __init__(self, n):
        self.n = n #size of matrices to verify

    def readarray(self, typ, line):
        return list(map(typ, line.split()))
    
    #read in square matrix from a list of string lines
    def readmatrix(self, lines):
        M = [] #initialize matrix list 
        for line in lines: 
            row = self.readarray(int, line) #convert to integers
            assert len(row) == self.n, f'Length of {self.n} is off'
            M.append(row)
        return M

    #multiply matrix M by vector v
    def mult(self, M, v):
        return [sum(M[i][j] * v[j] for j in range(self.n)) for i in range(self.n)]

    def frievalds(self, A, B, C):
        x = [randint(0, 100000) for _ in range(self.n)] #generate random vector
        ABx = self.mult(A, self.mult(B, x)) #calculate A*(B*x) 
        Cx = self.mult(C, x) #calculate C*x
        return True if Abx == Cx else False

if __name__ == "__main__":
    n = 3  
    f = Frievalds(n) #matrix size 3 
    A = f.readmatrix(["1 2 3", "4 5 6", "7 8 9"]) #define matrix A
    B = f.readmatrix(["9 8 7", "6 5 4", "3 2 1"]) #define matrix B
    C = f.readmatrix(["30 24 18", "84 69 54", "138 114 90"])  #define matrix C 
    print(f"Frievald's test result: {f.frievalds(A, B, C)}") #call Frievalds
