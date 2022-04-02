from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED
import time


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times



if __name__ == '__main__':

    # executor = ThreadPoolExecutor(max_workers=2)
    # task1 = executor.submit(get_html, (3))
    # task2 = executor.submit(get_html, (2))
    # print(task1.done())
    # print(task2.cancel())
    # print(task1.result())

    # executor = ThreadPoolExecutor(max_workers=2)
    # urls = [3, 2, 4]
    # all_task = [executor.submit(get_html,(url)) for url in urls]
    # for future in as_completed(all_task):
    #     data = future.result()
    #     print("in main: get page {}s sucess".format(data))

    # urls = [3, 2, 4]i
    # executor = ThreadPoolExecutor(max_workers=2)
    # for data in executor.map(get_html, urls):
    #     print("get {} page".format(data))

    executor = ThreadPoolExecutor(max_workers=2)
    urls = [3, 2, 4]
    all_task = [executor.submit(get_html, (url)) for url in urls]
    wait(all_task, return_when=ALL_COMPLETED)
    print("main")
