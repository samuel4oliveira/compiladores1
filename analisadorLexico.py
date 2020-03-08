def analisador_lexico(pathEntrada):
    palavrasReservadas = {
        'var':'declaracao',
        ':' : 'dois pontos',
        ',':'virgula',
        'integer':'tipo_real',
        'real':'tipo_integer',
        ';':'ponto e virgula',
        ':=':'atribuicao',
        'if':'condicional',
        'then':'acao condicional',
        '+':'soma'
    }

    arquivo = open(pathEntrada).read()
    for x in palavrasReservadas:
        arquivo = arquivo.replace(x, " " + x + " ")
    arquivo = arquivo.replace(': =', ' := ')
    tokens = arquivo.split()

    print(tokens)

    resultado = []
    for token in tokens:
        if token in palavrasReservadas:
            resultado.append([token, palavrasReservadas[token]])
        elif token.isalpha():
            resultado.append([token, 'identificador'])
        else:
            raise ValueError("Erro Léxico, '" + token + "' não é uma palavra reservada ou identificador válido.")
    return resultado

for i in analisador_lexico('/home/samuel/Documents/ufmt/compiladores1/entrada.txt'): print(i)