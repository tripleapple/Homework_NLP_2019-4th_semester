print('test module output')
def square(x):
    return x**2
def absolute(x):
    if x>=0:
        return x
    else:
        return -x
def prime(x):
    check_num=int(x**0.5+1)
    for i in range(2,check_num):
        x=x*1.0
        if x%i==0.0:
            return False
    return True
if __name__=='__main__':
    absolute(5)