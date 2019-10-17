import itertools
import numpy as np
import time

wlx, wly = 0, 0     
steps = []


def aiwater(deep=6):
    global wlx
    global wly
    global steps
    # for j in range(1, deep+1):
    for i in list(itertools.product([1, 2, 3, 4, 5, 6, 7, 8], repeat=deep)):
        s = True
        wlx, wly = 0, 0
        step = []
        if i[0] == 1 or i[0] == 2:
            for num in i:
                if wlx != 2:
                    if s is True:

                        if num == 1:
                            if wlx < 4:
                                wlx = 4
                                step.append(num)
                            else:
                                s = False

                        elif num == 2:
                            if wly < 3:
                                wly = 3
                                step.append(num)
                            else:
                                s = False

                        elif num == 3:
                            if wlx > 0:
                                wlx = 0
                                step.append(num)
                            else:
                                s = False

                        elif num == 4:
                            if wly > 0:
                                wly = 0
                                step.append(num)
                            else:
                                s = False

                        elif num == 5:
                            if wlx+wly >= 4 and wly > 0:
                                wly = wly - (4-wlx)
                                wlx = 4
                                step.append(num)
                                if wlx == 2:
                                    if step not in steps:
                                        steps.append(step)
                                    s = False
                                    continue

                            else:
                                s = False

                        elif num == 6:
                            if wlx+wly >= 3 and wlx > 0:
                                wlx = wlx - (3-wly)
                                wly = 3
                                step.append(num)
                                if wlx == 2:
                                    if step not in steps:
                                        steps.append(step)
                                    s = False
                                    continue

                            else:
                                s = False

                        elif num == 7:
                            if wlx+wly <= 4 and wly > 0:
                                wlx = wlx + wly
                                wly = 0
                                step.append(num)
                                if wlx == 2:
                                    if step not in steps:
                                        steps.append(step)
                                    s = False
                                    continue

                            else:
                                s = False

                        elif num == 8:
                            if wlx+wly <= 3 and wlx > 0:
                                wly = wlx + wly
                                wlx = 0
                                step.append(num)
                                if wlx == 2:
                                    if step not in steps:
                                        steps.append(step)
                                    s = False
                                    continue

                            else:
                                s = False

                        else:
                            pass
        else:
            pass


if __name__ == '__main__':
    s1 = time.time()
    aiwater(8)
    s2 = time.time()
    print(np.array(steps))
    print(s2 - s1)







