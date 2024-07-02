#Ines Ji 99238

#TAD posicao
#cria_posicao: str x str -> posicao
#cria_copia_posicao: posicao -> posicao
#obter_pos_c: posicao -> str
#obter_pos_l: posicao -> str
#eh_posicao: universal -> booleano
#posicoes_iguais: posicao x posicao -> booleano
#posicao_para_str: posicao -> str
#obter_posicoes_adjacentes: posicao -> tuplo de posicoes
#Representacao interna do TAD posicao: dicionario com duas chaves, 'c' (coluna)
#e 'l' (linha), em que os valores dessa chaves representam a coluna e a linha 
#da posicao e sao representados por cadeias de caracteres -> {'c': c, 'l': l}
#(c e l sao argumentos da cria_posicao).

def cria_posicao(c,l):
    #str x str -> posicao
    """Recebe duas cadeias de carateres correspondentes a coluna c e a linha l 
    de uma posicao e devolve a posicao correspondente. O construtor verifica a 
    validade dos seus argumentos e gera um erro caso algum argumento nao seja 
    valido."""
    if (type(c) != str or type(l) != str or c not in ('a', 'b', 'c') or 
        l not in ('1', '2', '3')):
        raise ValueError('cria_posicao: argumentos invalidos')
    return {'c': c, 'l': l}

def cria_copia_posicao(p):
    #posicao -> posicao
    """Recebe uma posicao e devolve uma copia nova da posicao."""
    return {'c': p['c'], 'l': p['l']}

def obter_pos_c(p):
    #posicao -> str
    """Recebe uma posicao e devolve a componente coluna da posicao p."""
    return p['c']

def obter_pos_l(p):
    #posicao -> str
    """Recebe uma posicao e devolve a componente linha da posicao p."""  
    return p['l']

def eh_posicao(arg):
    #universal -> booleano
    """Recebe um argumento e devolve True caso o argumento seja um TAD posicao 
    e False caso contrario."""
    return (isinstance(arg, dict) and len(arg) == 2 and 'c' in arg and 'l' in 
            arg and arg['c'] in ('a', 'b', 'c') and arg['l'] in ('1','2','3'))

def posicoes_iguais(p1,p2):
    #posicao x posicao -> booleano
    """Recebe duas posicoes (p1, p2) e devolve True apenas se as p1 e p2 forem 
    TAD posicoes e se forem iguais."""
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

def posicao_para_str(p):
    #posicao -> str
    """Recebe uma posicao e devolve a cadeia de caracteres 'cl' que representam 
    o argumento, sendo os valores c e l as componentes coluna e linha de p."""
    return obter_pos_c(p) + obter_pos_l(p)

def obter_posicoes_adjacentes(p):
    #posicao -> tuplo de posicoes
    """Recebe uma posicao e devolve um tuplo com as posicoes adjacentes a 
    posicao p de acordo com a ordem de leitura do tabuleiro."""
    adj = (cria_posicao('b', '2'),)
    if obter_pos_l(p) == '1':
        adj = (cria_posicao('b', '1'),) + adj
        if obter_pos_c(p) == 'a':
            adj = (adj[0],) + (cria_posicao('a', '2'),) + (adj[1],)
        elif obter_pos_c(p) == 'c':
            adj = adj + (cria_posicao('c', '2'),) 
        elif obter_pos_c(p) == 'b':
            adj = ((cria_posicao('a', '1'),) + (cria_posicao('c', '1'),) 
                    + (adj[1],))
    if obter_pos_l(p) == '3':
        adj = adj + (cria_posicao('b', '3'),)
        if obter_pos_c(p) == 'a':
            adj = (cria_posicao('a', '2'),) + adj
        elif obter_pos_c(p) == 'c':
            adj = (adj[0],) + (cria_posicao('c', '2'),) + (adj[1],)  
        elif obter_pos_c(p) == 'b':
            adj = ((adj[0],) + (cria_posicao('a', '3'),) + 
                    (cria_posicao('c', '3'),))       
    if obter_pos_l(p) == '2':
        adj = ((cria_posicao(obter_pos_c(p), '1'),) + (adj[0],) 
                + (cria_posicao(obter_pos_c(p), '3'),))
    if obter_pos_c(p) == 'b' and obter_pos_l(p) == '2':
        adj = ()
        for l in ('1', '2', '3'):
            for c in ('a', 'b', 'c'):
                if l != '2' or c != 'b':
                    adj = adj + (cria_posicao(c,l),)    
    return adj
        
#TAD peca
#cria_peca: str -> peca
#cria_copia_peca: peca -> peca 
#eh_peca: universal -> booleano
#pecas_iguais: peca x peca -> booleano
#peca_para_str: peca -> str
#peca_para_inteiro: peca -> inteiro
#Representacao interna do TAD peca: uma lista com os valores 1, -1 e 0 que 
#representam o jogador 'X', 'O' e uma peca livre(' ') respetivamente -> [1], 
#[-1], [0].

def cria_peca(s):
    #str -> peca
    """Recebe uma cadeia de carateres correspondente ao identificador de um dos 
    dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devolve a peca 
    correspondente. O construtor verifica a validade dos seus argumentos, e 
    gera um erro caso o seu argumento nao seja valido."""
    
    if not isinstance(s, str) or s not in ('O', 'X', ' '):
        raise ValueError ('cria_peca: argumento invalido')
    d = {'X': 1, 'O': -1, ' ': 0}
    return [d[s]]

def cria_copia_peca(j):
    #peca -> peca 
    """Recebe uma peca e devolve uma copia nova da peca."""
    return [j[0]]

def eh_peca(arg):
    #universal -> booleano
    """Recebe um argumento e devolve True caso o argumento seja um TAD peca e 
    Falso caso contrario."""
    return isinstance(arg, list) and len(arg) == 1 and arg[0] in (1, -1, 0)    

def pecas_iguais(j1, j2):
    #peca x peca -> booleano
    """Recebe duas pecas (j1, j2) e devolve True apenas se j1 e j2 forem TAD 
    pecas e forem iguais."""
    return eh_peca(j1) and eh_peca(j2) and j1 == j2

def peca_para_str(j):
    #peca -> str
    """Recebe uma peca e devolve a cadeia de caracteres que representa o 
    jogador dono dessa peca, isto e, '[X]', '[O]' ou '[ ]'."""
    d = {1: '[X]', -1:'[O]', 0: '[ ]'}
    return d[j[0]]

def peca_para_inteiro(j):
    #peca -> inteiro
    """Recebe uma peca e devolve um inteiro de valor 1, -1 ou 0, dependendo se 
    a peca recebida e do jogador 'X', 'O' ou livre, respetivamente."""    
    if peca_para_str(j) == '[X]':
        return 1
    elif peca_para_str(j) == '[O]':
        return -1
    elif peca_para_str(j) == '[ ]':
        return 0

#TAD tabuleiro
#cria_tabuleiro: {} -> tabuleiro
#cria_copia_tabuleiro: tabuleiro -> tabuleiro
#obter_peca: tabuleiro x posicao -> peca
#obter_vetor: tabuleiro x str -> tuplo de pecas
#coloca_peca: tabuleiro x peca x posicao -> tabuleiro
#remove_peca: tabuleiro x posicao -> tabuleiro
#move_peca: tabuleiro x posicao x posicao -> tabuleiro
#eh_tabuleiro: universal -X booleano
#eh_posicao_livre: tabuleiro x posicao -> booleano
#tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
#tabuleiro_para_str: tabuleiro -> str
#tuplo_para_tabuleiro: tuplo -> tabuleiro
#obter_ganhador: tabuleiro -> peca
#obter_posicoes_livres: tabuleiro -> tuplo de posicoes
#obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
#Representacao interna do TAD tabuleiro: um dicionario com nove chaves, cada 
#chave representa uma posicao em cadeia de caracteres 'cl' (c refere-se a 
#coluna e l a linha da posicao), enquanto os valores das chaves sao as 
#pecas que ocupam essa posicao (TAD pecas) -> {'a1' : TAD peca, 'b1' : TAD peca,
#'c1' : TAD peca, 'a2' : TAD peca, 'b2' : TAD peca, 'c2' : TAD peca, 'a3' : 
#TAD peca, 'b3' : TAD peca, 'c3' : TAD peca}.

def cria_tabuleiro():
    #{} -> tabuleiro
    """Devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes ocupadas por 
    pecas de jogador."""
    return {'a1' : cria_peca(' '), 'b1' : cria_peca(' '), 'c1' : cria_peca(' '),
            'a2' : cria_peca(' '), 'b2' :cria_peca(' '), 'c2' : cria_peca(' '), 
            'a3' : cria_peca(' '), 'b3' : cria_peca(' '), 'c3' : cria_peca(' ')}

def cria_copia_tabuleiro(t):
    #tabuleiro -> tabuleiro
    """Recebe um tabuleiro e devolve uma copia nova do tabuleiro."""
    return {'a1' : t['a1'], 'b1' : t['b1'], 'c1' : t['c1'], 'a2' : t['a2'],
           'b2' : t['b2'], 'c2' : t['c2'], 'a3' : t['a3'], 'b3' : t['b3'],
           'c3' : t['c3']}

def obter_peca(t,p):
    #tabuleiro x posicao -> peca
    """Recebe um tabuleiro e uma posicao e devolve a peca que ocupa essa 
    posicao do tabuleiro. Se a posicao nao estiver ocupada, devolve uma peca 
    livre."""
    return t[posicao_para_str(p)]
            
def obter_vetor(t,s):
    #tabuleiro x str -> tuplo de pecas
    """Recebe uma cadeia de caracteres que representa uma linha/coluna e devolve
    todas as pecas da linha/coluna especificada pelo argumento num tuplo."""
    vect = ()
    if s in ('1', '2', '3'):
        for c in ('a', 'b', 'c'):
            vect = vect + (obter_peca(t, cria_posicao(c, s)),) 
    if s in ('a', 'b', 'c'):
        for l in ('1', '2', '3'):
            vect = vect + (obter_peca(t, cria_posicao(s, l)),) 
    return vect

def coloca_peca(t, j, p):
    #tabuleiro x peca x posicao -> tabuleiro
    """Recebe um tabuleiro, uma peca e uma posicao e modifica destrutivamente o 
    tabuleiro t, colocando a peca j na posicao p, e devolve o proprio tabuleiro.
    """
    t[posicao_para_str(p)] = j
    return t
    
def remove_peca(t, p):
    #tabuleiro x posicao -> tabuleiro
    """Recebe um tabuleiro e uma posicao e modifica destrutivamente o tabuleiro 
    t, removendo a peca na posicao j, e devolve o proprio tabuleiro."""
    coloca_peca(t, cria_peca(' '), p)    
    return t

def move_peca(t, p1, p2):
    #tabuleiro x posicao x posicao -> tabuleiro
    """Recebe um tabuleiro e duas posicoes (p1, p2) e modifica destrutivamente 
    o tabuleiro t, movendo a peca que se encontra na posicao p1 para a 
    posicao p2, e devolve o proprio tabuleiro."""
    peca = obter_peca(t, p1)
    remove_peca(t, p1)
    coloca_peca(t, peca, p2)
    return t

def eh_tabuleiro(arg):
    #universal -> booleano
    """Recebe um argumento e devolve True caso o argumento seja um TAD 
    tabuleiro. Um tabuleiro valido tem no maximo 3 pecas de cada jogador, 
    a diferenca entre o numero de pecas colocadas no tabuleiro entre os dois 
    jogadores nao pode ser mais que 1, e apenas pode existir um ganhador 
    em simultaneo. Caso contrario devolve False."""
    acum = 0
    x = o = 0
    if not isinstance(arg, dict):
        return False
    for c in ('a', 'b', 'c'):
        for l in ('1', '2', '3'):
            if pecas_iguais(obter_peca(arg, cria_posicao(c,l)), cria_peca('X')):
                x = x + 1
            if pecas_iguais(obter_peca(arg, cria_posicao(c,l)), cria_peca('O')):
                o = o + -1
    #x e o verificam o numero de pecas de cada jogador             
    if x > 3 or o < -3 or (x + o) > 1 or (x + o) < -1 :
        return False
    if len(tuplo_vict(arg)) > 1:
        return False           
    return True    

def eh_posicao_livre(t,p):
    #tabuleiro x posicao -> booleano
    """Recebe um tabuleiro e uma posicao e devolve True apenas se a posicao 
    recebida corresponder a uma posicao livre do tabuleiro, caso contrario 
    devolve False."""
    return pecas_iguais(t[posicao_para_str(p)], cria_peca(' '))

def tabuleiros_iguais(t1, t2):
    #tabuleiro x tabuleiro -> booleano
    """Recebe dois tabuleiros (t1, t2) e devolve True apenas se t1 e t2 forem 
    TAD tabuleiros e forem iguais."""
    for l in ('1', '2', '3'): #verifica peca uma a uma de tal forma que 
        for c in ('a', 'b', 'c'): #verifique que t1 == t2
            if (not eh_tabuleiro(t1) or not eh_tabuleiro(t2) or not 
                pecas_iguais(t1[posicao_para_str(cria_posicao(c, l))], 
                             t2[posicao_para_str(cria_posicao(c, l))])):
                return False
    return True

def tabuleiro_para_str(t):
    #tabuleiro -> str
    """Recebe um tabuleiro e devolve a cadeia de caracteres que representa o 
    tabuleiro."""
    cont = 0
    tab ='   a   b   c\n1 '   
    for s in ('1', '2', '3'):
        for i in range(0,3):
            tab = tab + peca_para_str((obter_vetor(t, s)[i])) + '-'
        tab = tab[0:len(tab)-1] #para eliminar o ultimo '-'
        if s == '1':
            tab = tab + '\n   | \\ | / |\n2 '
        elif s == '2':
            tab = tab + '\n   | / | \\ |\n3 ' 
    return tab

def tuplo_para_tabuleiro(t):
    #tuplo -> tabuleiro 
    """Recebe um tuplo com 3 tuplos, cada um deles contendo 3 valores inteiros 
    iguais a 1, -1 ou 0 (em que o jogador e 'X', 'O' ou peca livre 
    respetivamente) e devolve o tabuleiro respetivo."""
    tab = cria_tabuleiro()
    l = {0: '1', 1: '2', 2: '3'} #indice do tuplo correspondente a linha do tab
    c = {0: 'a', 1: 'b', 2: 'c'} #ind. correspondente a coluna
    j = {1: 'X', -1: 'O', 0: ' '}
    for i in range(0,3):
        for e in range(0,3):
            tab[posicao_para_str(cria_posicao(c[e],l[i]))] = cria_peca(j[t[i]
                                                                         [e]])
    return tab
   
def obter_ganhador(t):
    #tabuleiro -> peca
    """Recebe um tabuleiro e devolve uma peca do jogador que tenha as suas 3 
    pecas em linha na vertical ou na horizontal no tabuleiro. Se nao existir 
    nenhum ganhador, devolve uma peca livre."""
    if len(tuplo_vict(t)) != 0:
        return tuplo_vict(t)[0]
    return cria_peca(' ')

def obter_posicoes_livres(t):
    #tabuleiro -> tuplo de posicoes
    """Recebe um tabuleiro e devolve um tuplo com as posicoes nao ocupadas 
    pelas pecas de qualquer um dos dois jogadores na ordem de leitura do 
    tabuleiro."""
    tup = ()
    
    for l in ('1', '2', '3'):
        for c in ('a', 'b', 'c'):    
            if eh_posicao_livre(t,cria_posicao(c,l)):
                tup = tup + (cria_posicao(c,l),)
    return tup

def obter_posicoes_jogador(t,j):
    #tabuleiro x peca -> tuplo de posicoes
    """Recebe um tabuleiro e uma peca e devolve um tuplo com as posicoes 
    ocupadas pelas pecas j (de um dos dois jogadores) na ordem de leitura do 
    tabuleiro."""
    tup = ()
    for l in ('1', '2', '3'):
        for c in ('a', 'b', 'c'):
            if pecas_iguais(obter_peca(t, cria_posicao(c,l)), j):
                tup = tup + (cria_posicao(c,l),)
    return tup

def obter_movimento_manual(t,j):
    #tabuleiro x peca -> tuplo de posicoes
    """Funcao auxiliar que recebe um tabuleiro e uma peca de um jogador, e 
    devolve um tuplo com uma ou duas posicoes que representam uma posicao ou um 
    movimento introduzido manualmente pelo jogador. A funcao apresenta uma 
    mensagem 'Turno do jogador. Escolha uma posicao(ou movimento): ', 
    dependendo da fase do jogo, para pedir ao utilizador para introduzir uma 
    posicao ou movimento. Se o valor introduzido nao corresponder a uma posicao 
    ou movimento validos, a funcao gera um erro."""
    if len(obter_posicoes_jogador(t,j)) < 3:
        pos = str(input("Turno do jogador. Escolha uma posicao: "))
        if (len(pos) != 2 or pos[0] not in ('a', 'b', 'c') or pos[1] not in 
            ('1','2','3')):
            raise ValueError('obter_movimento_manual: escolha invalida')  
        p = cria_posicao(pos[0], pos[1])
        if not eh_posicao(p) or not eh_posicao_livre(t, p):
            raise ValueError('obter_movimento_manual: escolha invalida')
        return (p,)
    mov = str(input("Turno do jogador. Escolha um movimento: "))
    if (len(mov) != 4 or mov[0] and mov[2] not in ('a', 'b', 'c') or mov[1] and 
        mov[3] not in ('1','2','3') or not eh_pos_jogador(t, 
        cria_posicao(mov[0], mov[1]), j)):
        raise ValueError('obter_movimento_manual: escolha invalida')
    m1 = cria_posicao(mov[0], mov[1])
    m2 = cria_posicao(mov[2], mov[3])
    for pos in obter_posicoes_jogador(t, j): #verifica se existem posicoes adj.
        for p in obter_posicoes_adjacentes(pos): #livres as do jogador, em
            if eh_posicao_livre(t, p): #caso de m2 = m1
                if not eh_pos_adjacente(m1, m2) or not eh_posicao_livre(t, m2):
                    raise ValueError('obter_movimento_manual: escolha invalida')
    return (m1,) + (m2,)

def obter_movimento_auto(t,j,modo):
    #tabuleiro x peca x str -> tuplo de posicoes
    """Funcao auxiliar que recebe um tabuleiro, uma peca de um jogador e uma 
    cadeia de carateres que representa o nivel de dificuldade do jogo, e devolve
    um tuplo com uma ou duas posicoes que representam uma posicao ou um 
    movimento escolhido automaticamente. Na fase de colocacao, o tuplo contem 
    apenas a posicao escolhida automaticamente para onde colocar a nova peca, 
    de acordo com os criterios (vitoria, bloqueio, centro, canto vazio e 
    lateral vazia). Na fase de movimento, o tuplo contem a posicao de origem da 
    peca a movimentar e a posicao de destino. A escolha automatica do movimento 
    depende do nivel de dificuldade escolhido."""
    if len(obter_posicoes_jogador(t,j)) < 3: 
        return (victoria(t,j) or bloqueio(t,j) or centro(t) or canto_vazio(t) 
                or lateral_vazia(t))
    if modo == 'facil':
        return facil(t,j)
    elif modo == 'normal':
        return minimax(t, j, 1, ())[1][0]
    elif modo == 'dificil':
        return minimax(t, j, 5, ())[1][0]

def victoria(t,j):
    #tabuleiro x peca -> tuplo de posicoes
    """Recebe um tabuleiro e uma peca de um jogador, e verifica se o jogador 
    tem duas das suas pecas e uma posicao livre numa linha/coluna do tabuleiro. 
    Se tal acontecer, devolve a posicao livre num tuplo (ganhando o jogo)."""
    for p in obter_posicoes_livres(t):
        copyt = cria_copia_tabuleiro(t)
        coloca_peca(copyt, j, p)
        if pecas_iguais(obter_ganhador(copyt), j):
            return (p,)

def bloqueio(t,j):
    #tabuleiro x peca -> tuplo de posicoes
    """Recebe um tabuleiro e uma peca de um jogador e verifica se o oponente 
    tem duas das suas pecas e uma posicao livre numa linha/coluna/diagonal do 
    tabuleiro. Se tal acontecer, devolve a posicao livre num tuplo (bloqueando 
    o oponente)."""
    if j == cria_peca('X'):
        advers = cria_peca('O')
    else:
        advers = cria_peca('X')
    if victoria(t, advers):
        return victoria(t, advers)

def centro(t):
    #tabuleiro -> tuplo de posicoes
    """recebe um tabuleiro e verifica se a posicao central encontra-se livre, 
    e se estiver devolve a mesma num tuplo."""    
    if eh_posicao_livre(t, cria_posicao('b', '2')):
        return (cria_posicao('b', '2'),) 

def canto_vazio(t):
    #tabuleiro -> tuplo de posicoes
    """Recebe um tabuleiro e verifica em ordem se os cantos estao livres, 
    devolvendo o primeiro que se encontrar livre num tuplo."""    
    cantos = ('a1', 'c1', 'a3', 'c3')
    for e in cantos:
        if eh_posicao_livre(t, cria_posicao(e[0], e[1])):
            return (cria_posicao(e[0], e[1]),)

def lateral_vazia(t):
    #tabuleiro -> tuplo de posicoes
    """Recebe um tabuleiro e verifica em ordem se as laterais estao livres, 
    devolvendo a primeira que se encontrar livre num tuplo."""    
    laterais = ('b1', 'a2', 'c2', 'b3')
    for e in laterais:
        if eh_posicao_livre(t, cria_posicao(e[0], e[1])):
            return (cria_posicao(e[0], e[1]),)        
                                    
def facil(t, j):
    #tabuleiro x peca -> tuplo de posicoes
    """Recebe um tabuleiro e uma peca de um jogador e devolve um tuplo com a 
    posicao da peca a movimentar e a posicao destino. A peca a movimentar e 
    sempre a que ocupa a primeira posicao em ordem de leitura do tabuleiro e 
    que tenha alguma posicao adjacente livre. A posicao de destino e a primeira 
    posicao adjacente livre. Se nao for possivel movimentar nenhuma peca por 
    estarem todas bloqueadas, a funcao devolve como movimento a posicao da 
    primeira peca do jogador correspondente seguida da mesma posicao que 
    ocupa."""
    pos_jog = obter_posicoes_jogador(t,j)
    for p_inicial in pos_jog:
        for p_final in obter_posicoes_adjacentes(p_inicial):
            if eh_posicao_livre(t, p_final):
                return (p_inicial,) + (p_final,)
    #Caso nao seja possivel movimentar nenhuma peca:            
    return (pos_jog[0],) + (pos_jog[0],)

def minimax(t, j, prof, seq_m):
    #tabuleiro x peca x inteiro x tuplo de posicoes -> tuplo 
    """Recebe um tabuleiro, uma peca do jogador, a profundidade da recursividade
    e a sequencia de movimentos realizados (que e atualizada na chamada a funcao
    recursiva) e devolve o valor do tabuleiro (1 se ganhador for 'X', -1 se for
    'O' e 0 se nao houver) e a sequencia de movimentos atualizada num tuplo. 
    Este algoritmo escolhe o melhor movimento para o proprio assumindo que o 
    adversario ira escolher o pior possivel."""
    valor_tab = peca_para_inteiro(obter_ganhador(t))
    if not pecas_iguais(obter_ganhador(t), cria_peca(' ')) or prof == 0:
        return valor_tab, seq_m
    d = {'[X]': 'O', '[O]': 'X'}
    adv = cria_peca(d[peca_para_str(j)])
    melhor_res = peca_para_inteiro(adv)
    melhor_seq_mov = ()
    for pos_i in obter_posicoes_jogador(t,j):
        for pos_f in obter_posicoes_adjacentes(pos_i):
            if eh_posicao_livre(t, pos_f):
                tab = cria_copia_tabuleiro(t)
                novo_mov = ((pos_i, pos_f),)
                move_peca(tab, pos_i, pos_f)
                novo_res, nova_seq_mov = minimax(tab, adv, prof-1, 
                                                     (seq_m + novo_mov))
                if ((not melhor_seq_mov) or (pecas_iguais(j,cria_peca('X')) 
                    and novo_res > melhor_res) or (pecas_iguais(j, 
                    cria_peca('O')) and novo_res < melhor_res)):
                    melhor_res, melhor_seq_mov = novo_res, nova_seq_mov  
    return melhor_res, melhor_seq_mov         

def moinho(jog, modo):
    #str x str -> str
    """Funcao principal que permite jogar um jogo completo do jogo do moinho de 
    um jogador contra o computador. Recebe duas cadeias de caracteres 
    (representacao externa da peca com o jogador humano deseja jogar, '[X]' 
    ou '[O]' e o segundo argumento selecciona o nivel de dificuldade do jogo) e 
    devolve a representacao externa da peca ganhadora ('[X]' ou '[O]'). Se algum
    dos argumentos dados for invalido, a funcao gera um erro."""
    if jog not in ('[X]', '[O]') or modo not in ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade', modo+'.')
    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))
    d = {'[X]': '[O]', '[O]': '[X]'}
    cont = {'[X]': 1, '[O]': 2} #Para saber quem comeca, ou seja, quem tem 'X'
    adv = cria_peca(d[jog][1])
    j = cria_peca(jog[1])
    while pecas_iguais(obter_ganhador(t),cria_peca(' ')):
        if cont[jog] % 2 != 0:
            p = obter_movimento_manual(t,j)
            if len(obter_posicoes_jogador(t,j)) < 3:
                t = coloca_peca(t,j,p[0])
            else:
                t = move_peca(t,p[0],p[1])
        if cont[jog] % 2 == 0:
            print('Turno do computador ('+modo+'):')
            p = obter_movimento_auto(t, adv, modo)
            if len(obter_posicoes_jogador(t,adv)) < 3:
                t = coloca_peca(t,adv,p[0])
            else:
                t = move_peca(t,p[0],p[1])
        print(tabuleiro_para_str(t))
        cont[jog] = cont[jog] + 1 #Turno do outro jogador no proximo loop   
        if pecas_iguais(obter_ganhador(t), j): 
            return peca_para_str(j)            
        if pecas_iguais(obter_ganhador(t), adv): 
            return peca_para_str(adv)

def tuplo_vict(t):
    #tabuleiro -> tuplo
    """Recebe um tabuleiro e devolve um tuplo com uma peca do(s) jogador(es) 
    que tiverem 3 pecas em linha/coluna, isto e que ganharam o jogo. Caso nao 
    haja nenhum, devolve um tuplo vazio."""
    tup = ()
    for s in ('1', '2', '3', 'a', 'b', 'c'):
        if (pecas_iguais(obter_vetor(t,s)[0], obter_vetor(t,s)[1]) and 
            pecas_iguais(obter_vetor(t,s)[1], obter_vetor(t,s)[2]) and not 
            pecas_iguais(obter_vetor(t,s)[0], cria_peca(' '))):
            tup = (obter_vetor(t,s)[0],) + tup
    return tup

def eh_pos_adjacente(p_ini, p_adj):
    #posicao x posicao -> booleano
    """Recebe duas posicoes e devolve True se a segunda posicao for adjacente a 
    primeira, caso contrario retorna False."""
    for pos in obter_posicoes_adjacentes(p_ini):
        if posicoes_iguais(pos, p_adj):
            return True   
    return False

def eh_pos_jogador(t, p_jog, j):
    #tabuleiro x posicao x peca -> booleano
    """Recebe um tabuleiro, uma posicao e uma peca e devolve True se a posicao 
    for uma posicao da peca no tabuleiro, caso contrario devolve False."""
    for pos in obter_posicoes_jogador(t, j):
        if posicoes_iguais(pos, p_jog):
            return True
    return False