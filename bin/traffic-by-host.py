#!/usr/bin/env python

import sys


def analyze(stream):
    services = {}
    line = stream.readline()
    while line:
        arr = line.split()
        src = arr[2].split('.')
        sip = '.'.join(src[0:4])
        sport = src[-1]
        arr[4] = arr[4][:-1]
        dst = arr[4].split('.')
        dip = '.'.join(dst[0:4])
        dport = dst[-1]
        flags = arr[6][:-1]
        length = int(arr[-1])

        print sip, sport,dip,dport

        if flags == '[S]':
            services.setdefault(arr[4], [0, 0])  # send, recive
        elif arr[2] in services:
            traffic = services.get(arr[2])
            traffic[0] += length
        elif arr[4] in services:
            traffic = services.get(arr[4])
            traffic[1] += length
        else:
            print 'bad line ' + line

        line = stream.readline()
    return services


if __name__ == '__main__':
    services =  analyze(sys.stdin)
    for key, value in services.items():
        print '%s: %s %s' % (key, value[0], value[1])

