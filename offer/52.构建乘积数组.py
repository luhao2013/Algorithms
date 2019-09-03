"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""


# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if len(A)<1:
            return A
        toright = [1] * len(A)
        toleft = [1] * len(A)
        for i in range(1, len(A)):
            toright[i] = A[i-1] * toright[i-1]
        for i in range(len(A)-2, -1, -1):
            toleft[i] = A[i+1] * toleft[i+1]
        for i in range(len(A)):
            A[i] = toleft[i] * toright[i]
        return A
