def conjunction(x1, x2):
    w1=1
    w2=1
    teta=2
    s=x1*w1+x2*w2
    if s<teta:
        y = 0
    else:
        y = 1
    return y
print('Результат конъюнкции:', conjunction(int(input()),int(input())))