def d(formula):
    print('at what value would you like to find the derivative.')
    x = int(input(':'))
    x = x + 0.0001
    a = eval(formula)
    x = x - 0.0002
    b = eval(formula)
    return (a-b)/0.0002
    
def ad(formula):
     print('first bound')
     a = int(input(':'))
     print('second bound')
     b = int(input(':'))
     x = a
     n = eval(formula)
     x = b
     m = eval(formula)
     return (m-n)/(b-a)

    
    