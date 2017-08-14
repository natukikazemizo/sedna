#!BPY
# -*- coding: UTF-8 -*-
#
# Debug All Utilities
#
#
#
# 2017.08.14 Natukikazemizo

import importlib
import os

import utils_converter
import utils_log

#reload all user pythons
importlib.reload(utils_converter)
importlib.reload(utils_log)

#constants
PY_NAME = "utils_0000_debug_all"

def print_arg_and_result(func, *arg):
    print("### CHECK ###")
    print(*arg)
    print(func(*arg))


# debug utils_log
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))
logger.start()
logger.log("log TEST")
logger.detailtime_log("detailtime_log TEST")
logger.info("info LOG TEST")
logger.warn("warn LOG TEST")
logger.err("err LOG TEST")

# debug utils_convertert
## cnv_l_2_r
STRING_DOT_L_DOT = "HOGE.L.Fr"
STRING_DOT_L_UNDER_BAR = "HOGE.L_BK"
STRING_DOT_L_END = "HOGE.L"
STRING_DOT_L_NAME = "HOGE.LONG"

print_arg_and_result(utils_converter.cnv_l_2_r, STRING_DOT_L_DOT)
print_arg_and_result(utils_converter.cnv_l_2_r, STRING_DOT_L_UNDER_BAR)
print_arg_and_result(utils_converter.cnv_l_2_r, STRING_DOT_L_END)
print_arg_and_result(utils_converter.cnv_l_2_r, STRING_DOT_L_NAME)


# debug utils_log
logger.end()



