"""High-level functions for using multiple threads of execution."""

import logging
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Tuple
import time


_MAX_WORKERS = max(10, os.cpu_count() or 1)
"""Maximum number of workers used in :func:`run_parallel`."""


def run_parallel(*funcs: Callable[[], Any]) -> Tuple[Any, ...]:
    max_workers = min(len(funcs), _MAX_WORKERS)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        logging.info("Starting parallel execution (%s workers)", max_workers)
        func_futures = [executor.submit(f) for f in funcs]

        return tuple(fut.result() for fut in func_futures)


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


if __name__ == '__main__':
    res = run_parallel(lambda: get_html(2), lambda: get_html(3))
    print("main:" + res.__str__())
