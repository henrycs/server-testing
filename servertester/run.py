import logging
#from servertester.casetest.singlecase import run_mem_test_cases
from servertester.mem_case_test.memtest_0512_d3 import run_mem_test_cases


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

    run_mem_test_cases(stage=3)