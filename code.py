def calc_hypo(a,b):
    if type(a) not in (float,int) or type(b) not in (float,int):
        print('Wrong argument type!')
        return False
    if a < 0 or b < 0:
        print('Argument negative!')
        return False
    hypo = (a**2 + b**2)**(1/2)
    return hypo

