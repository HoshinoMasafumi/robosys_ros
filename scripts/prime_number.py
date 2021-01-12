#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

n = 0

def cb(message):
    global n
    n = message.data
    if (n % 1)!=0:
        print(n, "is a fraction.")
    elif n < 0:
        print(n, "This is a negative number.")
    elif judg_prime(n):
        print(n,"is not prime number.")
        #factors = prime_factor_decomposition(n)
        print(n,"=",end="")
        #print(*factors,sep = " * ")
        print(*prime_factor_decomposition(n),sep="*")
    else :
        print(n, "is rime number!!!!!")


def judg_prime(n):
    n = int(n)
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def prime_factor_decomposition(n):
    factor = []

    i = 2
    while n >= i:
        if(n % i == 0):
            n /= i
            factor.append(i)
            i = 1
        i+=1
    return factor



if __name__ == '__main__':
    rospy.init_node('prime_number')
    sub = rospy.Subscriber('number', Float64, cb)
    rospy.spin()
