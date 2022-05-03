# from python cookbook capter 1
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
name2, *_, date2 = data
from collections import deque

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        print(self._queue)

    def pop(self):
        return heapq.heappop(self._queue)[-1]

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    # with open('private.py') as f:
    #     for line, prevlines in search(f, 'python', 5):
    #         for pline in prevlines:
    #             print(pline, end='')
    #         print(line, end='')
    #         print('-'*20)

    # import heapq
    # portfolio = [
    #     {'name': 'IBM', 'shares': 100, 'price': 91.1},
    #     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    #     {'name': 'FB', 'shares': 200, 'price': 21.09},
    #     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    #     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    #     {'name': 'ACME', 'shares': 75, 'price': 115.65}
    # ]
    # cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    # expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    # print(cheap)
    # print(expensive)

    # class Item:
    #     def __init__(self, name):
    #         self.name = name
    #
    #     def __repr__(self):
    #         return 'Item({!r})'.format(self.name)
    #
    # q = PriorityQueue()
    # q.push(Item('foo'), 1)
    # q.push(Item('bar'), 5)
    # q.push(Item('spam'), 4)
    # q.push(Item('grok'), 1)
    # print(q.pop())

    # from collections import defaultdict
    #
    # d = defaultdict(list)
    # d['a'].append(1)
    # d['a'].append(2)
    # d['a'].append(2)
    # d['b'].append(4)
    # print(d)
    # d = defaultdict(set)
    # d['a'].add(1)
    # d['a'].add(2)
    # d['a'].add(2)
    # d['b'].add(4)
    # print(d)

    # prices = {
    #     'ACME': 45.23,
    #     'AAPL': 612.78,
    #     'IBM': 205.55,
    #     'HPQ': 37.20,
    #     'FB': 10.75
    # }
    # min_price = min(zip(prices.values(), prices.keys()))
    # print(min_price)
    # max_price = max(zip(prices.values(), prices.keys()))
    # print(max_price)

    # words = [
    #     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    #     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    #     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    #     'my', 'eyes', "you're", 'under'
    # ]
    # from collections import Counter
    #
    # word_counts = Counter(words)
    # # 出现频率最高的3 个单词
    # top_three = word_counts.most_common(3)
    # print(top_three)
    # # Outputs [('eyes', 8), ('the', 5), ('look', 4)]

    # rows = [
    #     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    #     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    #     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    #     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    # ]
    #
    # from operator import itemgetter
    #
    # rows_by_fname = sorted(rows, key=itemgetter('fname'))
    # rows_by_uid = sorted(rows, key=itemgetter('uid'))
    # print(rows_by_fname)
    # print(rows_by_uid)

    # rows = [
    #     {'address': '5412 N CLARK', 'date': '07/01/2012'},
    #     {'address': '5148 N CLARK', 'date': '07/04/2012'},
    #     {'address': '5800 E 58TH', 'date': '07/02/2012'},
    #     {'address': '2122 N CLARK', 'date': '07/03/2012'},
    #     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    #     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    #     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    #     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    # ]
    # from operator import itemgetter
    # from itertools import groupby
    #
    # # Sort by the desired field first
    # rows.sort(key=itemgetter('date'))
    # # Iterate in groups
    # for date, items in groupby(rows, key=itemgetter('date')):
    #     print(date)
    #     for i in items:
    #         print(' ', i)

    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))