# -*- coding: utf-8 -*-
# @Author   : henry
# @Time     : 2022-03-09 15:08
import logging
from generators.entrusts import Entrust, OrderSide, OrderStatus, OrderType, TestAction, TestCase, get_action
from generators.executor import run_stages_in_case

from test_basic import *
from test_buy import *
from test_buy_sequence import *
from test_cancel import *
from test_positions import *
from test_sell import *
from test_sell_sequence import *



def run_test_cases():
    # testcase_f01_01()
    #testcase_f02_32()
    testcase_f03_03()
    #testcase_f04_03()
    #testcase_f05_04()
    # testcase_f06_03()
    # testcase_f07_03()
    
    #testcase_f20_01_04()
    #testcase_f40_11_14()

    input("next step: query account info")
    testcase_f01_01()




def run_file_testcases():
    run_test_cases()