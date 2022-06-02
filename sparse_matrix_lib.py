# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
class sparseMatrix:
    so_hang = 1
    so_cot  = 1
    row_set =[]
    def __init__(self, so_row,so_col):
        self.so_hang = so_row
        self.so_cot = so_col
        for i in range(so_row):
            self.row_set.append({})
       
    def construct(self,A):
        self.so_hang, self.so_cot = A.shape
        self.row_set = []
        for i in range(0,self.so_hang):
            self.row_set.append({})
            for j in range(0,self.so_cot):
                if(A[i,j]!=0):
                    self.row_set[i][j] = A[i,j]
    def update(self,vi_tri_hang, vi_tri_cot, gia_tri):
        if(self.row_set[vi_tri_hang].get(vi_tri_cot)==None):
            self.row_set[int(vi_tri_hang)][int(vi_tri_cot)] = gia_tri
        else:
            self.row_set[int(vi_tri_hang)][int(vi_tri_cot)] +=gia_tri
    def mul_vector(self, b):
        n = b.shape[0]
        ans = np.zeros(n)
        for i in range(0,n):
            hang_i_items = self.row_set[i].items()
            for key, value in hang_i_items:
                ans[i] += b[int(key)] * value
        return ans




