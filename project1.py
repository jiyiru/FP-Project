#99238 Ines Ye Ji


def eh_tabuleiro(tab):
    
    #universal -> booleano
    """Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu 
    argumento corresponder a um tabuleiro e False caso contrario."""
    
    if type(tab) != tuple or len(tab) != 3:
        return False  
   
    for elemento in tab: 
        if type(elemento) != tuple or len (elemento) != 3:
            return False
        
        for e in elemento: 
            if type(e) != int:
                return False            
            if e != -1 and e != 0 and e != 1: 
                return False     
   
    return True

 
    
def eh_posicao(p):
    
    #universal -> booleano
    """Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu 
    argumento corresponder a uma posicao (de 1 a 9) e False caso contrario."""
    
    if type(p) != int or p not in range(1,10):
        return False
    
    else:
        return True
    
    
   
def eh_jogador(jog):
    
    #universal -> booleano
    """Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu
    argumento corresponder a um jogador (-1 ou 1) e False caso contrario."""
    
    if type(jog) != int or (jog != 1 and jog != -1):
        return False
    
    else:
        return True
    
    
    
def eh_modo(modo):
    
    #universal -> booleano
    """Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu
    argumento corresponder a um modo do jogo, isto e, a estrategia usada 
    ("basico", "normal" ou "perfeito") e False caso contrario."""
    
    if modo == 'basico' or modo == 'normal' or modo == 'perfeito':
        return True
    
    else:
        return False
    
    
    
def obter_coluna(tab, col):
    
    #tabuleiro x inteiro -> vector
    """Esta funcao recebe um tabuleiro e um inteiro com valor de 1 a 3 que 
    representa o numero da coluna, e devolve um vector com os valores dessa 
    coluna. Se algum dos argumentos dados for invalido, a funcao gera 
    um erro."""
    
    coluna = ()
    
    if not eh_tabuleiro(tab) or type(col) != int or col not in range(1,4):
        raise ValueError ("obter_coluna: algum dos argumentos e invalido")
    
    for i in range(0,3): #Colunas sao formadas por um elemento de cada
        #tuplo (linha) na posicao col
        e = col - 1 #O indice dos tuplos comeca do 0 
        coluna = coluna + (tab[i][e],) 

    return coluna



def obter_linha(tab, lin):
    
    #tabuleiro x inteiro -> vector
    """Esta funcao recebe um tabuleiro e um inteiro com valor de 1 a 3 que 
    representa o numero da linha, e devolve um vector com os valores dessa 
    linha. Se algum dos argumentos dados for invalido, a funcao gera 
    um erro."""
    
    if not eh_tabuleiro(tab) or type(lin) != int or lin not in range(1,4):
        raise ValueError ("obter_linha: algum dos argumentos e invalido")
    
    e = lin - 1 #O indice dos tuplos comeca do 0
    linha = tab[e] #Cada tuplo do tuplo tab e uma linha
   
    return linha



def obter_diagonal(tab, dia):
    
    #tabuleiro x inteiro -> vector
    """Esta funcao recebe um tabuleiro e um inteiro com valor de 1 a 2 que 
    representa o numero da diagonal, e devolve um vector com os valores dessa 
    diagonal. Se algum dos argumentos dados for invalido, a funcao gera 
    um erro."""
   
    if dia not in range(1,3) or not eh_tabuleiro(tab) or type(dia) != int:
        raise ValueError ("obter_diagonal: algum dos argumentos e invalido")
    
    if dia == 1: #Diagonal descendente da esquerda para a direita
        diagonal = (tab[0][0],) + (tab[1][1],) + (tab[2][2],)
    
    if dia == 2: #Diagonal ascendente da esquerda para a direita
        diagonal = (tab[2][0],) + (tab[1][1],) + (tab[0][2],)
    
    return diagonal
    
       
    
def tabuleiro_str(tab):
    
    #tabuleiro -> cadeia de caracteres
    """Esta funcao recebe um tabuleiro e devolve a cadeia de caracteres que o 
    representa ("a representacao para os nossos olhos"). Se o argumento dado 
    for invalido, a funcao gera um erro."""
    
    tabuleiro = ''
    
    if not eh_tabuleiro(tab):
        raise ValueError ("tabuleiro_str: o argumento e invalido")
   
    for i in range(len(tab)):
        for e in tab[i]:
            
            d = {-1: " O ", 1: " X ", 0: "   "}
            
            tabuleiro = tabuleiro + d[e] + "|"
        tabuleiro = tabuleiro[0:len(tabuleiro)-1] 
        #Para retirar o "|" que esta a mais no fim antes de '\n-----------\n'
        
        tabuleiro = tabuleiro + '\n-----------\n' 
    tabuleiro = tabuleiro[0:len(tabuleiro)-13] 
    #Para retirar o '\n-----------\n' que esta a mais no fim do tabuleiro           
    
    return tabuleiro



def eh_posicao_livre(tab, p):
    
    #tabuleiro x posicao -> booleano
    """Esta funcao recebe um tabuleiro e uma posicao, e devolve True se a 
    posicao corresponder a uma posicao livre do tabuleiro e False caso 
    contrario. Se algum dos argumentos dados for invalido, a funcao gera 
    um erro."""
    
    if not eh_tabuleiro(tab) or not eh_posicao(p):
        raise ValueError ("eh_posicao_livre: algum dos argumentos e invalido")
    
    if jog_da_posicao(tab, p) == 0:
        return True
    
    else:
        return False
    
    
    
def jog_da_posicao(tab, p):
    
    #tabuleiro x posicao -> inteiro
    """Esta funcao recebe um tabuleiro e uma posicao e devolve o valor (jogador) 
    que se encontra nessa posicao."""
    
    jog = {1 : tab[0][0], 2: tab[0][1], 3 : tab[0][2], 4 : tab[1][0], 
           5 : tab[1][1], 6 : tab[1][2], 7 : tab[2][0], 8 : tab[2][1], 
           9 : tab[2][2]}
    
    return jog[p] 



def obter_posicoes_livres(tab):
    
    #tabuleiro -> vector
    """Esta funcao recebe um tabuleiro, e devolve o vector ordenado com todas 
    as posicoes livres do tabuleiro. Se o argumento dado for invalido, a funcao 
    deve gerar um erro."""
    
    livres = ()
    
    if not eh_tabuleiro(tab):
        raise ValueError("obter_posicoes_livres: o argumento e invalido")
    
    for p in range(1,10):
        if eh_posicao_livre(tab, p):
            livres = livres + (p,)
    
    return livres



def jogador_ganhador(tab):
    
    #tabuleiro -> inteiro
    """Esta funcao recebe um tabuleiro, e devolve um valor inteiro a indicar o 
    jogador que ganhou a partida no tabuleiro sendo o valor igual a 1 se o 
    jogador que joga com 'X' ganhou, -1 se o jogador que joga com 'O' ganhou, 
    ou 0 se nenhum jogador ganhou. Se o argumento dado for invalido, a funcao 
    deve gerar um erro."""
    
    if not eh_tabuleiro(tab):
        raise ValueError("jogador_ganhador: o argumento e invalido")    
    
    #Procurar se existem tres elementos iguais nas colunas/linhas/diagonais e 
    #que nao sejam 0
    
    for col in range(1,4):
        if (obter_coluna(tab, col)[0] == obter_coluna(tab, col)[1] == 
            obter_coluna(tab, col)[2]) and (obter_coluna(tab, col)[0] != 0):
            return obter_coluna(tab, col)[0]
    
    for lin in range(1,4):
        if (obter_linha(tab, lin)[0] == obter_linha(tab, lin)[1] == 
            obter_linha(tab, lin)[2]) and (obter_linha(tab, lin)[0] != 0):
            return obter_linha(tab, lin)[0]
        
    for dia in range(1,3):
        if ((obter_diagonal(tab, dia)[0] == obter_diagonal(tab, dia)[1] == 
            obter_diagonal(tab, dia)[2]) and 
            (obter_diagonal(tab, dia)[0] != 0)):
            return obter_diagonal(tab, dia)[0]
    
    else:
        return 0
    
        
        
def marcar_posicao(tab, jog, p):
    
    #tabuleiro x inteiro x posicao -> tabuleiro
    """Esta funcao recebe um tabuleiro, um inteiro identificando um jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e uma posicao livre, e 
    devolve um tabuleiro modificado com uma nova marca do jogador na posicao 
    escolhida. Se algum dos argumentos dados for invalido, a funcao gera um 
    erro."""
   
    linha = ()
    novotab = ()
    
    if (not eh_tabuleiro(tab) or not eh_jogador(jog) or not eh_posicao(p) or 
        not eh_posicao_livre(tab, p)):
        raise ValueError("marcar_posicao: algum dos argumentos e invalido")      
    
    for posicao in range(1,10):
        if posicao == p:
            #Adiciona-se ao tuplo a marca do jogador na posicao escolhida
            linha = linha + (jog,) 
        else:
            #Adiciona-se as marcas originais
            linha = linha + (jog_da_posicao(tab, posicao),)
        if posicao == 3 or posicao == 6 or posicao == 9:
            #O tabuleiro e formado por 3 tuplos de 3
            novotab = novotab + (linha,)
            linha = ()
            
    return novotab
            


def escolher_posicao_manual(tab):
    
    #tabuleiro -> posicao
    """Esta funcao realiza a leitura de uma posicao introduzida manualmente por 
    um jogador e devolve essa posicao. Se o argumento dado for invalido, a 
    funcao gera um erro. A funcao apresenta a mensagem 'Turno do jogador. 
    Escolha uma posicao livre: ', para pedir ao utilizador para introduzir uma 
    posicao. Se o valor introduzido nao corresponder a uma posicao livre do 
    tabuleiro, a funcao gera um erro."""
    
    if not eh_tabuleiro(tab):
        raise ValueError ("escolher_posicao_manual: o argumento e invalido")
    
    posicao = int(input("Turno do jogador. Escolha uma posicao livre: "))
    
    if not eh_posicao(posicao) or not eh_posicao_livre(tab, posicao):
        raise ValueError ("escolher_posicao_manual: " 
                          "a posicao introduzida e invalida")
    
    return posicao
    


def escolher_posicao_auto(tab, jog, modo):
    
    #tabuleiro x inteiro x cadeia de caracteres -> posicao
    """Esta funcao recebe um tabuleiro, um inteiro identificando um jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e uma cadeia de carateres 
    que corresponde ao modo (estrategia) selecionado, e devolve a posicao 
    escolhida automaticamente de acordo com o modo de jogo seleccionado. Se 
    algum dos argumentos dados for invalido, a funcao gera um erro."""
    
    if not eh_tabuleiro(tab) or not eh_jogador(jog) or not eh_modo(modo):
        raise ValueError ("escolher_posicao_auto: "
                          "algum dos argumentos e invalido")
    
    if modo == 'basico':
        return basico(tab)
    
    if modo == 'normal':
        return normal(tab, jog)
    
    if modo == 'perfeito':
        return perfeito(tab, jog)
    
    

def basico(tab):
    
    #tabuleiro -> posicao
    """Esta funcao recebe um tabuleiro e devolve a posicao escolhida de acordo 
    com o modo "basico", atraves da consideracao em ordem dos criterios 
    5,7,8."""
    
    if centro(tab):
        return centro(tab)
    
    elif canto(tab):
        return canto(tab)
    
    else:
        return lateral(tab)
    
    
    
def normal(tab, jog):
    
    #tabuleiro x inteiro -> posicao 
    """Esta funcao recebe um tabuleiro e um inteiro que identifica um jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e devolve a posicao 
    escolhida de acordo com o modo "normal", atraves da consideracao em ordem 
    dos criterios 1,2,5,6,7,8."""
    
    if victoria(tab, jog):
        return victoria(tab, jog)
    
    elif bloqueio(tab, jog):
        return bloqueio(tab, jog)
    
    elif centro(tab):
        return centro(tab)
    
    elif canto_oposto(tab, jog):
        return canto_oposto(tab, jog)
    
    elif canto(tab):
        return canto(tab)
    
    else:
        return lateral(tab)       
    
    
    
def perfeito(tab, jog):
    
    #tabuleiro x inteiro -> posicao
    """Esta funcao recebe um tabuleiro e um inteiro que identifica um jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e devolve a posicao 
    escolhida de acordo com o modo "perfeito", atraves da consideracao em ordem 
    dos criterios 1,2,3,4,5,6,7,8."""
    
    if victoria(tab, jog):
        return victoria(tab, jog)
    
    elif bloqueio(tab, jog):
        return bloqueio(tab, jog)
    
    elif bifurcacao(tab,jog):
        return bifurcacao(tab,jog)
        
    elif bloqueio_bifurcacao(tab,jog):
        return bloqueio_bifurcacao(tab,jog)
    
    elif centro(tab):
        return centro(tab)
    
    elif canto_oposto(tab, jog):
        return canto_oposto(tab, jog)
    
    elif canto(tab):
        return canto(tab)
    
    else:
        return lateral(tab)    
    
    
    
def victoria (tab, jog):
    
    #tabuleiro x inteiro -> posicao
    """Esta funcao recebe um tabuleiro e um inteiro que identifica um jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e verifica se o jogador tem 
    duas das suas pecas e uma posicao livre numa linha/coluna/diagonal do 
    tabuleiro. Se tal acontecer, devolve a posicao livre (ganhando o jogo)."""
    
    tipos = ((0, jog, jog), (jog, 0, jog), (jog, jog, 0))
    
    linha_p = { 1 : (1, 2, 3), 2 : (4, 5, 6), 3 : (7, 8, 9)}
    coluna_p = { 1 : (1, 4, 7), 2: (2, 5, 8), 3 : (3, 6, 9)}
    diagonal_p = { 1 : (1, 5, 9), 2 : (7, 5, 3)}    
    
    for n in range (1,4):
        for i in range(0,3):
            if obter_linha(tab, n) == tipos[i]:
                for zero_p in range(0,3):
                    if tipos[i][zero_p] == 0: 
                        return linha_p[n][zero_p] 
    #Correspondencia do zero (posicao livre) com o numero da posicao 
    #(que se encontra no dicionario)
            if obter_coluna(tab, n) == tipos[i]:
                for zero_p in range(0,3):
                    if tipos[i][zero_p] == 0:
                        return coluna_p[n][zero_p]
                    
    for n in range(1,3):
        for i in range(0,3):
            if obter_diagonal(tab, n) == tipos[i]:
                for zero_p in range(0,3):
                    if tipos[i][zero_p] == 0:
                        return diagonal_p[n][zero_p]

    
    
def bloqueio(tab, jog):
    
    #tabuleiro x inteiro -> posicao
    """Esta funcao recebe um tabuleiro e um inteiro que identifica um jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e verifica se o oponente 
    tem duas das suas pecas e uma posicao livre numa linha/coluna/diagonal do 
    tabuleiro. Se tal acontecer, devolve a posicao livre (bloqueando 
    o oponente)."""    
    
    if jog == -1:
        advers = 1
    else:
        advers = -1
    
    if victoria(tab, advers):
        return victoria(tab, advers)
    
    
    
def bifurcacao (tab, jog):
    
    #tabuleiro x inteiro -> posicao
    """Esta funcao recebe um tabuleiro e um inteiro que identifica um jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e verifica se o jogador tem 
    linhas/colunas/diagonais que se intersectam, onde cada uma apenas contem uma 
    das suas pecas e se a posicao de intersecao estiver livre entao marca nessa 
    posicao (criando duas formas de vencer na jogada seguinte)."""     
    
    if intersecao(tab,jog) != ():
        return min(intersecao(tab,jog))   
    
    
    
def intersecao(tab, jog):
    
    #tabuleiro x inteiro -> vector
    """Esta funcao recebe um tabuleiro e um inteiro que identifica um jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e verifica se o jogador tem 
    linhas/colunas/diagonais onde contem apenas uma das suas pecas e encontra 
    a intersecao dessas linhas/colunas/diagonais. Se as posicoes de intersecao 
    estiverem livres devolve essas posicoes num vector."""    
    
    intersecao = ()
    soma = ()
    
    tipos = ((jog,0,0), (0,jog,0), (0,0,jog)) 
    
    #Dicionarios que correspondem o numero da linha/coluna/diagonal com as 
    #posicoes existentes nela 
    linha_p = {1 : (1, 2, 3), 2 : (4, 5, 6), 3 : (7, 8, 9)}
    coluna_p = {1 : (1, 4, 7), 2: (2, 5, 8), 3 : (3, 6, 9)}
    diagonal_p = {1 : (1, 5, 9), 2 : (7, 5, 3)}
    
    for n in range (1,4):
        for i in range(0,3):
            if obter_linha(tab, n) == tipos[i]:
                soma = soma + linha_p[n] 
            if obter_coluna(tab, n) == tipos[i]:
                soma = soma + coluna_p[n]
                
    for n in range(1,3):
        for i in range(0,3):
            if obter_diagonal(tab, n) == tipos[i]:
                soma = soma + diagonal_p[n]
    #Ver as intersecoes (posicoes em comum entre as linhas/colunas/diagonais)
    for e in elemento_repetido(soma):
        if eh_posicao_livre(tab, e):
            intersecao = intersecao + (e,)
    return intersecao 



def elemento_repetido(t):
    
    #tuplo -> tuplo
    """Esta funcao recebe um tuplo e devolve em tuplo um elemento cada dos que 
    se encontram repetidos."""
    
    soma = ()
    e_r = ()
    
    for e in t:
        if e in soma and e not in e_r:
            e_r = e_r + (e,)
        soma = soma + (e,)
    
    return e_r



def bloqueio_bifurcacao(tab, jog):
    
    #tabuleiro x inteiro -> posicao
    """Esta funcao recebe um tabuleiro e um inteiro que identifica um jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e verifica se o oponente 
    tem bifurcacoes e dependendo do numero de bifurcacoes a funcao vai funcionar 
    de maneira diferente. 
    Se tiver quatro bifurcacoes, devolve a primeira intersecao (posicao de 
    bifurcacao) livre que esteja numa linha/diagonal/coluna de uma das 
    pecas do jogador. Se tiver duas ou tres, devolve a primeira posicao 
    livre que nao seja intersecao e que se encontre numa linha/diagonal/coluna
    de uma das pecas do jogador. 
    Se tiver uma, devolve a posicao da unica intersecao que existe."""

    e_c = ()
    
    if jog == 1:
        advers = -1
    else:
        advers = 1
    
    if len(intersecao(tab, advers)) == 4:
        for e in posicoes_do_jogador(tab, jog):
            e_c = e_c + elemento_comum(pertence(e),intersecao(tab, advers)) 
        return min(e_c)
    #pertence(e) -> posicoes de lin/col/dia em que ha pecas do jogador  
    if len(intersecao(tab, advers)) > 1 and len(intersecao(tab, advers)) < 4: 
        for e in posicoes_do_jogador(tab, jog):
            e_c = e_c + elemento_comum(pertence(e), obter_posicoes_livres(tab))
        jogada = elementos_dif(e_c, intersecao(tab, advers))
        return min(jogada)
    
    if len(intersecao(tab, advers)) == 1:
        return min(intersecao(tab, advers))



def elemento_comum(t1, t2):
    
    #tuplo x tuplo -> tuplo
    """Esta funcao recebe dois tuplos e compara-os, devolvendo os seus elementos 
    em comum num tuplo."""
    
    soma =()
    t = t1 + t2
    
    for e in t:
        if e in t1 and e in t2:
            if e not in soma:
                soma = soma + (e,)
    
    return soma



def pertence(p):
    
    #posicao -> vector
    """Esta funcao recebe uma posicao e devolve um vector com todas as posicoes 
    das colunas/linhas/diagonais as quais essa posicao pertence."""
    
    res = ()
    
    linha_p = { 1 : (1, 2, 3), 2 : (4, 5, 6), 3 : (7, 8, 9)}
    coluna_p = { 1 : (1, 4, 7), 2 : (2, 5, 8), 3 : (3, 6, 9)}
    diagonal_p = { 1 : (1, 5, 9), 2 : (7, 5, 3)}
    
    for i in range(1,4):
        if p in linha_p[i]:
            res = res + linha_p[i]
        if p in coluna_p[i]:
            res = res + coluna_p[i]
            
    for i in range(1,3):
        if p in diagonal_p[i]:
            res = res + diagonal_p[i]
            
    return res
        


def posicoes_do_jogador(tab, jog):
    
    #tabuleiro x inteiro -> vector
    """Esta funcao recebe um tabuleiro e um inteiro que identifica o jogador 
    (1 para o jogador 'X' ou -1 para o jogador 'O') e devolve um vector com as 
    posicoes do jogador."""
    
    posicoes = ()
    
    for p in range (1,10):
        if jog_da_posicao(tab, p) == jog:
            posicoes = posicoes + (p,)
    return posicoes



def elementos_dif(t1,t2):
    
    #tuplo x tuplo -> tuplo
    """Esta funcao recebe dois tuplos e compara-os, devolvendo os seus elementos 
    diferentes num tuplo."""
    
    res = ()
    t = t1 + t2
    
    for e in t:
        if e in t1 and e not in t2:
            res = res + (e,)
        elif e not in t1 and e in t2:
            res = res + (e,)
    return res  



def centro(tab):
    
    #tabuleiro -> posicao
    """Esta funcao recebe um tabuleiro e verifica se a posicao central (5) 
    encontra-se livre, e se estiver devolve a mesma."""
    
    if eh_posicao_livre(tab, 5):
        return 5
    
    
    
def canto_oposto(tab, jog):
    
    #tabuleiro x inteiro -> posicao
    """Esta funcao recebe um tabuleiro e um inteiro que identifica um jogador 
    (1 para jogador 'X' e -1 para jogar 'O') e verifica se o adversario jogou 
    num canto e se tal acontecer, verifica se o canto diagonalmente oposto esta
    livre e devolve esse canto."""
    
    if jog == -1:
        advers = 1
    else:
        advers = -1
    
    cantos = ((9, 1), (7, 3), (3, 7), (1, 9))
    
    for i in range(len(cantos)):
        if (advers == jog_da_posicao(tab, cantos[i][0]) and 
            eh_posicao_livre(tab, cantos[i][1])):
            return cantos[i][1]



def canto(tab):
    
    #tabuleiro -> posicao
    """Esta funcao recebe um tabuleiro e verifica em ordem se os cantos estao 
    livres, devolvendo o primeiro que se encontrar livre."""
    
    cantos = (1, 3, 7, 9)
    for p in cantos:
        if eh_posicao_livre(tab, p):
            return p



def lateral(tab):
    
    #tabuleiro -> posicao
    """Esta funcao recebe um tabuleiro e verifica em ordem se as laterais estao 
    livres, devolvendo a primeira que se encontrar livre."""
    
    laterais = (2, 4, 6, 8)
    for p in laterais:
        if eh_posicao_livre(tab, p):
            return p


                   
def jogo_do_galo(jog, modo):
    
    #cadeia de caracteres x cadeia de caracteres -> cadeia de caracteres
    """Esta funcao corresponde a funcao principal que permite jogar um jogo 
    completo de Jogo do Galo de um jogador contra o computador. O jogo comeca 
    sempre com o jogador 'X' a marcar uma posicao livre e termina quando um dos 
    jogadores vence ou, se nao existirem posicoes livres no tabuleiro. A funcao 
    recebe duas cadeias de caracteres (a marca que o ultizador quer usar e modo 
    de jogo do computador) e devolve o jogador que ganhou ('X' ou 'O') ou 
    'EMPATE'."""
    
    valor = {'O' : -1 , 'X' : 1}
    
    if not eh_jogador(valor[jog]) or not eh_modo(modo):
        raise ValueError ("jogo_do_galo: algum dos argumentos e invalido")
     
    print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com", "'" + jog + "'.")

    tab = ((0,0,0), (0,0,0), (0,0,0))
        
    if valor[jog] == 1:       
        return manual_primeiro(tab, modo)
    
    else:
        return auto_primeiro(tab, modo)
        
        
        
def manual_primeiro(tab, modo):
    
    #tabuleiro x inteiro x cadeia de caracters -> cadeia de caracteres
    """Esta funcao e uma subdivisao da funcao jogo_do_galo em que o utilizador 
    escolheu a marca 'X'. Recebe dois argumentos, um tabuleiro e o modo de jogo 
    do computador e devolve o jogador que ganhou ('X' ou 'O') ou 'EMPATE'."""
    
    while len(obter_posicoes_livres(tab)) != 0:
        
        jog = 1
        advers = -1
        
        p = escolher_posicao_manual(tab)
        tab = marcar_posicao(tab, jog, p)
        print(tabuleiro_str(tab))
        
        if jogador_ganhador(tab) == 1:
            return 'X'
        if jogador_ganhador(tab) == -1:
            return 'O'
        
        if len(obter_posicoes_livres(tab)) == 0:
            return 'EMPATE'   
        
        print("Turno do computador", "("+modo+"):")  
        p = escolher_posicao_auto(tab, advers, modo)
        tab = marcar_posicao(tab, advers, p)    
        print(tabuleiro_str(tab))
        
        if jogador_ganhador(tab) == 1:
            return 'X'
        if jogador_ganhador(tab) == -1:
            return 'O'
        
        
        
def auto_primeiro(tab, modo):
    
    #tabuleiro x inteiro x cadeia de caracters -> cadeia de caracteres
    """Esta funcao e uma subdivisao da funcao jogo_do_galo em que o utilizador 
    escolheu a marca 'O'. Recebe dois argumentos, um tabuleiro e o modo de jogo 
    do computador e devolve o jogador que ganhou ('X' ou 'O') ou 'EMPATE'.""" 
    
    while len(obter_posicoes_livres(tab)) != 0: 
        
        jog = -1
        advers = 1
        
        print("Turno do computador", "("+modo+"):")  
        p = escolher_posicao_auto(tab, advers, modo)
        tab = marcar_posicao(tab, advers, p)    
        print(tabuleiro_str(tab))
        
        if jogador_ganhador(tab) == 1:
            return 'X'
        if jogador_ganhador(tab) == -1:
            return 'O'
        
        if len(obter_posicoes_livres(tab)) == 0:
            return 'EMPATE'           
        
        p = escolher_posicao_manual(tab)
        tab = marcar_posicao(tab, jog, p)
        print(tabuleiro_str(tab))
        
        if jogador_ganhador(tab) == 1:
            return 'X'
        if jogador_ganhador(tab) == -1:
            return 'O'
