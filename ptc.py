import math
import os
import random
import re
import sys
# Complete the 'gridSearch' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
def find(st, s_st):
    index = []
    L = len(st)
    l = len(s_st)
    for i in range(L-l+1):
        if(st[i:i+l] == s_st):
            index.append(i)
    return index
def gridSearch(G, P):
    # Write your code here
    R = len(G)
    C = len(G[0])
    r = len(P)
    c = len(P[0])
    for i in range(R-r+1):
        indexes = find(G[i], P[0])
        if indexes:
            for j in indexes:
                for k in range(i+1, i+r):
                    if(P[k-i] != G[k][j:j+c]):
                        break
                else:
                    return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        second_multiple_input = input().rstrip().split()
        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        result = gridSearch(G, P)
        fptr.write(result + '\n')
    fptr.close()