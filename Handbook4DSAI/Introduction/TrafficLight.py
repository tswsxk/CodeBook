# coding: utf-8
# 2019/9/16 @ tongshiwei

import time

GREEN = 17
RED = 20
YELLOW = 3

ZFILL_WIDTH = max(len(str(GREEN)), len(str(RED)), len(str(YELLOW)))


def flush_print(*values, **kwargs):
    sep = kwargs.get('sep', "")
    end = kwargs.get('end', "")
    print('\r', *values, sep=sep, end=end, flush=True)


def traffic_light():
    count = 0
    while True:
        count = count % (GREEN + YELLOW + RED)
        if count < GREEN:
            flush_print("\033[32m● %s" % str(GREEN - count).zfill(ZFILL_WIDTH))
        elif count < GREEN + YELLOW:
            flush_print("\033[33m● %2s" % str(GREEN + YELLOW - count).zfill(ZFILL_WIDTH))
        elif count < GREEN + YELLOW + RED:
            flush_print("\033[31m● %2s" % str(GREEN + YELLOW + RED - count).zfill(ZFILL_WIDTH))
        count += 1
        time.sleep(1)


if __name__ == '__main__':
    traffic_light()
