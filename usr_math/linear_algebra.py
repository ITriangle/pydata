#!/usr/bin/env python
# coding=utf-8


import numpy

if __name__ == '__main__':
    # 1. 矩阵的转置 Matrix Transpose
    m = numpy.mat([[1, 2], [3, 4]])
    print("Matrix.Transpose:")
    print(m.T)

    # 2. 矩阵的乘法 Matrix Multiplication

    a = numpy.mat([1, 2])
    b = numpy.mat([[10], [20]])
    print("Matrix Multiplication")
    print(a * b)
    print("Matrix Multiplication")
    print(a.T * b.T)


    a = numpy.mat([[1, 2], [3, 4]])
    b = numpy.mat([[10, 20], [30, 40]])
    print("Matrix Multiplication")
    print(a * b)

    # 3. 矩阵的内积 Matrix inner ： 矢量的降维运算，变成一个数
    x = numpy.mat([[1, 2], [3, 4]])
    y = numpy.mat([10, 20])
    print("Matrix inner:")
    print(numpy.inner(x, y))

    # 4. 矩阵的外积 Matrix outer ： 矢量的升维运算， mm维矢量和nn维矢量的外积是m∗nm∗n为矩阵
    x = numpy.mat([[1, 2], [3, 4]])
    y = numpy.mat([10, 20])
    print("Matrix outer:")
    print(numpy.outer(x, y))

    # 5. 矩阵的元素积 element-wise product/
    x = numpy.array([1, 3])
    y = numpy.array([10, 20])
    print("Array element-wise product:")
    print(x * y)

    # 6. 矩阵的相加
    x = numpy.mat([[1, 2], [3, 4]])
    y = numpy.mat([[10, 20], [30, 40]])
    print("Matrix Add :")
    print(x + y)

    # 7. 矩阵的相减
    x = numpy.mat([[1, 2], [3, 4]])
    y = numpy.mat([[10, 20], [30, 40]])
    print("Matrix Sub :")
    print(x - y)

    pass