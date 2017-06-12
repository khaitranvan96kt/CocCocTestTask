#!/usr/bin/ python
# -*- coding: utf-8 -*-

import os
import sys
import operator

r = []
p = []
n = 0
zombies = []


class Zombie:

    def __init__(self, index, time, heigth):
        self.index = index
        self.time = time
        self.heigth = heigth


def _compare(x, y):
    if x.time > y.time:
        return 1
    elif x.time == y.time:
        return 0
    else:
        return -1


def Read_File(filename='input.txt'):
    f = open(filename, 'r', 1)
    n = int(f.readline())
    string_r = f.readline()
    r = map(int, string_r.split())
    string_p = f.readline()
    p = map(int, string_p.split())

    print 'n = %s' % n
    print 'r = %s' % r
    print 'p = %s' % p

    for i in range(0, n):
        Z = Zombie(i + 1, r[i], p[i])
        zombies.append(Z)
    zombies.sort(_compare)
    # for x in zombies:
    #     print '(index,r,p) = (%s,%s,%s)' % (x.index, x.time, x.heigth)
    Calcu(n, r, p, zombies)


def Calcu(n, r, p, zombies):
    c_min = 0
    i = 1
    kq_hit = []
    while len(zombies) != 0:
        sum_vt_min = 0
        for j in zombies:
            if j.time <= i:
                sum_vt_min += 1
            else:
                break
        if sum_vt_min == 0:
            kq_hit.append(0)
            i += 1
            continue
        # print 'sum_vt_min = %s' % sum_vt_min
        p_min_in_i = zombies[0].heigth
        index_min = 0
        for index, j in enumerate(zombies[:sum_vt_min]):
            if j.heigth < p_min_in_i:
                p_min_in_i = j.heigth
                index_min = index
        # print '(p_min_in_i,index_min) = (%s,%s)' % (p_min_in_i, index_min)
        hit = zombies[index_min].index
        kq_hit.append(hit)
        zombies[index_min].heigth -= 1
        if zombies[index_min].heigth == 0:
            zombies.pop(index_min)
            c_min += i
        i += 1
    # print '\n%s' % c_min
    # for hit in kq_hit:
    #     print '%s ' % hit,
    OutFile(c_min, kq_hit)


def OutFile(c_min, kq_hit):
    f = open('output.txt', 'w', 1)
    f.write(str(c_min) + '\n')
    for hit in kq_hit:
        f.write(str(hit) + ' ')


if __name__ == '__main__':
    Read_File()
