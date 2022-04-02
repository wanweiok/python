import time

import schedule,datetime


def job_test():
    print(datetime.datetime.now())


def job_test_2(name):
    print(datetime.datetime.now())
    print(name)


if __name__ == '__main__':
    schedule.every(3).seconds.do(job_test)
    name = "myJob"
    schedule.every().hour.do(job_test_2, name)
    schedule.every(2).days.at("08:00").do(job_test)
    schedule.every().wednesday.at("13:15").do(job_test)

    while True:
        schedule.run_pending()
        time.sleep(1)