from cgi import print_exception
# import random
from numpy import random


N = [10**k for k in range(4,10)]
for n in N:
    mypi = 0

    pi_list = []
    for k in range(4*n):
        x = random.rand()
        y = random.rand()
        radius_2 = x*x + y*y
        if radius_2 <= 1:
            # pi_list.append(radius_2)
        # if (x*x + y*y) <= 1:
            mypi += 1
    # pi_list = np.array(pi_list)
    # mypi = len(pi_list)
    print('N =', n, "\tThe value of pi is: ", float(mypi)/n, ".\n")
    