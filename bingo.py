#!/usr/bin/python3
# coding:utf-8

import math
import random

try:
    import Tkinter as tkinter
except ImportError:
    import tkinter

try:
    import tkFont as font
except ImportError:
    from tkinter import font


def eratostenes(num):
    # 素数かどうか判定、素数ならTrue、そうでなければFalseを返す
    if num == 1:
        return False  # 1は素数ではないことにする

    m = int(math.sqrt(num)+1)  # この数までで探索する、もう少し少なくても可？
    for i in range(2, m):
        if num == num // i * i:
            return False
    return True


def prime_list_gen(max=500):
    # maxで指定された数までの素数のリストを返す
    return [i for i in range(1, max + 1) if eratostenes(i)]  # 素数ならリストに追加


prime_list = prime_list_gen()
# print(prime_list)
for i in range(1, 5200):
    random.shuffle(prime_list)

master = tkinter.Tk()
master.title(u"prime number bingo!")
master.geometry("600x600")
num_show = tkinter.Label(text=u'prime\nnumber\nbingo',
                         font="Helvetica 100")
button_next = tkinter.Button(text=u'next')


def update_num(event):
    random.shuffle(prime_list)
    choice = prime_list[random.randint(0, len(prime_list)-1)]
    prime_list.remove(choice)
    num_show.config(text=str(choice), font="Helvetica 250")
    print(choice)


button_next.bind("<Button-1>", update_num)
num_show.pack()
button_next.pack()
master.mainloop()
