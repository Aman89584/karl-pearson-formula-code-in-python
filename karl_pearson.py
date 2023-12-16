#kurl pearson coefficient of co-relation


import math

# taking value input of x
n1 = int(input("Enter Your n no. of value you want to insert in X:- "))
x = []
y = []
x_sqr = []
y_sqr = []
def input_xy_value(n):
    for i in range (0,n):
        ele1 = int(input("Enter X values:-"))
        x.append(ele1)
        x_sqr.append(ele1**2)
        ele2 = int(input("Enter Y values:-"))
        y.append(ele2)
        y_sqr.append(ele2**2)
input_xy_value(n1)



#taking addition of two values x and y
def add_two_matrix(x,y):
    add = []
    for i in range (0,len(x)):
        for j in range(0,len(y)):
            sums = x[i]*y[i]
        add.append(sums)
    return add
result = add_two_matrix(x,y)



# function to add list
def adds(value):
    sums = 0
    for i in range(0,len(value)):
        sums += value[i]
    return sums

#kurl pearson formula to find the cofficient of co-relation between x and y

def final_answer(x,y,xy,x_2,y_2):
    final_numerator = n1*xy - x*y
    final_denominator = float("{:.3f}".format(math.sqrt((n1*x_2)-(x**2))))*float("{:.3f}".format(math.sqrt((n1*y_2)-(y**2))))
    return float("{:.3f}".format(final_numerator/final_denominator)) 

#final answer 

print(final_answer(adds(x),adds(y),adds(result),adds(x_sqr),adds(y_sqr)))