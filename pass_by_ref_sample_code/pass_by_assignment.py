# pass_by_assginment.py

def f(fx):
    #print(f'Start  f(x):  fx={fx}')
    print(f'fx = {fx} / id(fx) = {id(fx)}')
    fx = 10
    print(f'fx = {fx} / id(fx) = {id(fx)}')

x = 5
print(f'x = {x} / id(fx) = {id(x)}')
f(x)
print(f'x = {x} / id(fx) = {id(x)}')