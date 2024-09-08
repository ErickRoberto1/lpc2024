cpf = input("CPF no formato xxx.xxx.xxx-xx: ").strip()

def verificar_cpf(cpf):

    cpf = cpf.replace('.', '').replace('-', '')

    digitos = [int(digito) for digito in cpf]
    
    # Cálculo do primeiro dígito verificador
    soma = sum(digitos[i] * (10 - i) for i in range(9))
    resto_divisao = soma % 11
    primeiro_digito = 0 if resto_divisao < 2 else 11 - resto_divisao

    if primeiro_digito != digitos[9]:
        return False
    
    # Cálculo do segundo dígito verificador
    soma = sum(digitos[i] * (11 - i) for i in range(10))
    resto_divisao = soma % 11
    segundo_digito = 0 if resto_divisao < 2 else 11 - resto_divisao

    if segundo_digito != digitos[10]:
        return False

    return True

if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    resultado = verificar_cpf(cpf)
    print('CPF válido' if resultado else 'CPF inválido')
else:
    print('Formato inválido')
