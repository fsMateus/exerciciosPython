def validate_cpf(cpf):
    
    if len(cpf) < 11:
        return False    
    
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    
    calc = lambda t: int(t[1]) * (t[0] + 2)
    d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
    d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
    return str(d1) == cpf[-2] and str(d2) == cpf[-1]

cpf = input('digite seu cpf (xxx.xxx.xxx-xx): ')
cpf = cpf.replace('.','')
cpf = cpf.replace('-','')

if validate_cpf(cpf):
    print('CPF válido')
else:
    print('CPF inválido')