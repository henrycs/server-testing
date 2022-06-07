import logging
from servertester.mem_case_test.memtest_0512_d3 import run_mem_test_cases
#from servertester.xd_xr.xdxr_0512_d2_1 import run_mem_test_cases
#from servertester.casetest.singlecase import run_mem_test_cases


logger = logging.getLogger(__name__)


def init_logging(level=logging.INFO):
    logger = logging.getLogger()

    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="---%(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(level)



if __name__ == "__main__":
    init_logging(logging.DEBUG)

    # 5.10的测试用例要重新整理，有的股票清仓，有的无交易，有的部分成交，有的全部成交，间隔交替
    run_mem_test_cases(stage=1)