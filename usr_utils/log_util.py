#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import
from __future__ import division


import sys
import os
import logging


reload(sys)
sys.setdefaultencoding("utf-8")


rootLogger = logging.getLogger("python data math")
rootLogger.setLevel(logging.INFO)
rootLogger.setLevel(logging.DEBUG)

'''日志格式'''
logFormatter = logging.Formatter('%(asctime)s [%(levelname)s] (%(pathname)s:%(lineno)d@%(funcName)s) -> %(message)s')

'''控制台日志输出'''
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


'''写日志文件'''
fileHandler = logging.FileHandler(os.path.join(LOG_DIR_PATH, 'log.log'))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

'''每天凌晨生成一个新的日志文件'''
# every_log_path = os.path.join(ROOT_DIR, "log")
# if not os.path.exists(every_log_path):
#     os.makedirs(every_log_path)
# log_file = os.path.join(every_log_path, "{}_log.log".format(os.getpid()))
# every_day_handler = logging.handlers.TimedRotatingFileHandler(log_file, 'midnight', 1)
# every_day_handler.setFormatter(logFormatter)
# rootLogger.addHandler(every_day_handler)