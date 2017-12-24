#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np


if __name__ == '__main__':

    # 元组，列表 为向量，或者矩阵
    arr1 = np.array([1,3,5,7,9])
    print(arr1)

    arr2 = np.array((2,4,5,6,10))
    print(arr2)

    arr3 = np.array([
        [1,2,3,4]
        ,[5,6,7,8]
        ,[9,2,4,5]
    ])
    print(arr3)

    print(arr1.shape)
    print(arr3.shape)


    print(arr3[1,:])

    print(arr3[:,1])
    print(arr3[[0,1],:],'\n')

    pass
