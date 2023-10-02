def neuron1(x1, x2):
    w1 = 0.5
    w2 = -0.5
    teta = 0.5
    s = x1*w1+x2*w2
    if s<teta:
        i = 0
    else:
        i = 1
    return i

def neuron2(x3, x4):
    w1 = -0.5
    w2 = 0.5
    teta = 0.5
    s = x3*w1+x4*w2
    if s<teta:
        j = 0
    else:
        j = 1
    return j

def neuron3(y1, y2):
    w1 = 1
    w2 = 1
    teta = 0.5
    s = y1*w1+y2*w2
    if s<teta:
        y3 = 0
    else:
        y3 = 1
    return y3
print('Результат исключающего ИЛИ:', neuron3(neuron1(int(input()),int(input())),neuron2(int(input()),int(input()))))