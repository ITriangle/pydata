#!/usr/bin/env python
# coding=utf-8

import sys
import os
import logging

import traceback
import time


reload(sys)
sys.setdefaultencoding("utf-8")


logger = logging.getLogger("python math")
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)



def problem(x):
    e = 2.71828182845904590
    return x**3 + 2*x + e**x - 3

def error(x):
    return (problem(x)-0)**2

def derivative_descent(x):
    delta = 0.00000001
    derivative = (error(x + delta) - error(x - delta)) / (delta * 2)

    alpha = 0.01
    x = x - derivative * alpha
    return x

if __name__ == '__main__':


    logger.debug('often makes a very good meal of %s', 'visiting tourists')

    x = 0.0
    for i in range(50):
        x = derivative_descent(x)
        print('x = {:6f}, problem(x) = {:6f}'.format(x, problem(x)))

    pass