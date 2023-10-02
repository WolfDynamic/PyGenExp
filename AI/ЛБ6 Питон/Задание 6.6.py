import random

def neuron_learning(f, w, symbol):
    y = {'в': 0, 'е': 0, 'с': 0, 'х': 0, 'н': 0, 'т': 0, 'о': 0, 'р': 0, 'ь': 0, 'з': 0, 'у': 0, 'п': 0, 'а': 0,
         'б': 0, 'г': 0, 'ч': 0}
    p = 25
    for k in f.keys():
        s = 0
        for j in range(15):
            s += f[k][j] * w[j]
        if s < p:
            y[k] = 0
        else:
            y[k] = 1
    if y[symbol] == 1 and sum(y.values()) == 1:
        return y
    else:
        for k in f.keys():
            if y[k] == 0 and k == symbol:
                w = [i + j for i, j in zip(f[k], w)]
            elif y[k] == 1 and k != symbol:
                w = [j - i for i, j in zip(f[k], w)]
        return neuron_learning(f, w, symbol)


f = {'в': [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
     'е': [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
     'с': [1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
     'х': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
     'н': [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
     'т': [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
     'о': [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
     'р': [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
     'ь': [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
     'з': [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
     'у': [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
     'п': [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
     'а': [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
     'б': [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
     'г': [1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
     'ч': [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]}

w = [random.randint(0, 10) for i in range(15)]
print('Какой символ будем угадывать?')
print('в е с х н т о р ь з у п а б г ч')
symbol = input()
Y = neuron_learning(f, w, symbol)
# Вывод результата
for k in Y.keys():
    print('Знак «', k, '» :', 'y =', Y[k])
