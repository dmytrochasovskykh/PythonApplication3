import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
from math import radians, modf

def FizzBall():
# Output numbers from 1 to x. 
# If the number is divisible by 3, replace it with “Fizz”. 
# If it is divisible by 5, replace it with “Buzz”. 
# If it is divisible by 3 and 5 replace it with “FizzBuzz”. '''
    print("Enter the number please: ");
    number = int(input());
    for i in range(1,number+1):
        tup1 = modf(i/3);
        tup2 = modf(i/5);
        if (tup1[0] == 0 and tup2[0] == 0):
            print("FizzBuzz");
        elif (tup1[0] == 0):
            print("Fizz");
        elif (tup2[0] == 0):
            print("Buzz");
        else:
            print(i);


def main():  
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()



#main()
FizzBall()
