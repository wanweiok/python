from functools import reduce

if __name__ == '__main__':
    for i in map(lambda x: x*x, range(10)):
        print(i)

    for i in filter(lambda x: x % 3 == 0, range(10)):
        print(i)

    res = reduce(lambda x, y: x+y, range(11))
    print(res)
    print(reduce(lambda a, b: '{},{}'.format(a,b),range(11)))

    a = [('b', 3), ('a', 2), ('d', 4), ('c', 1)]
    print(sorted(a, key=lambda x: x[1]))

    import sys
    from tkinter import Button, mainloop
    x = Button(text='Press me', command=(lambda: sys.stdout.write('Hello,World\n')))
    x.pack()
    x.mainloop()