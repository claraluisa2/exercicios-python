def converteNotacao(hora,minuto):
    if hora>12:
        hora = hora - 12
        return hora, minuto, 'P'
    else:
        return hora, minuto, 'A'
    
hora, minuto, notacao = converteNotacao(14,25)

def imprime(hora, minuto, notacao):
    if notacao == 'P':
        print(f"{hora}:{minuto}PM")
    else:
        print(f"{hora}:{minuto}AM")


imprime(hora, minuto, notacao)


