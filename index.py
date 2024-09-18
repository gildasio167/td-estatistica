from math import *

def questao1():
    print("Você escolheu a Questão 1.\n")
    print("Quantas palavras contendo 3 letras diferentes podem ser formadas com um alfabeto de 26 letras?\n")
    num_palavras = 26 * 25 * 24
    print("Número de palavras com 3 letras diferentes:", num_palavras)

def questao2():
    print("Você escolheu a Questão 2.")
    # Definindo o número de alternativas por questão e o número de questões
    num_alternativas = 5
    num_questoes = 10

    # Calculando o número de gabaritos possíveis
    num_gabaritos = num_alternativas ** num_questoes

    # Exibindo o resultado
    print(f"O número de gabaritos possíveis é: {num_gabaritos}")


def questao3():
    print("Você escolheu a Questão 3.")
    # Código da questão 3

    # Número de opções para cada posição
    opcoes_primeiro_digito = 9
    opcoes_segundo_digito = 9
    opcoes_terceiro_digito = 8
    opcoes_quarto_digito = 7

    # Calculando o total de números com algarismos distintos
    total_numeros = opcoes_primeiro_digito * opcoes_segundo_digito * opcoes_terceiro_digito * opcoes_quarto_digito

    # Exibindo o resultado
    print(f"O número de inteiros entre 1000 e 9999 cujos algarismos são distintos é: {total_numeros}")


def questao4():
    print("Você escolheu a Questão 4.")
    # Código da questão 4

    # Número de membros do conselho
    num_membros = 12

    # Calculando o número de maneiras de escolher um presidente e um secretário
    num_maneiras = num_membros * (num_membros - 1)

    # Exibindo o resultado
    print(f"O número de modos diferentes de escolher um presidente e um secretário é: {num_maneiras}")


def questao5():
    print("Você escolheu a Questão 5.")
    # Código da questão 5
    import math

    # Número total de cadeiras e pessoas
    num_cadeiras = 5
    num_pessoas = 3

    # Calculando combinações e permutações
    combinacoes = math.comb(num_cadeiras, num_pessoas)
    permutacoes = math.factorial(num_pessoas)

    # Número total de maneiras
    total_maneiras = combinacoes * permutacoes

    # Exibindo o resultado
    print(f"O número de modos diferentes de 3 pessoas se sentarem em 5 cadeiras em fila é: {total_maneiras}")

def questao6():
    print("Você escolheu a Questão 6.")
    # Código da questão 6

    # Quantos número de quatro dígitos são maiores que 2400 e:
    # a) têm todos os dígitos diferentes?   
    # b) não têm dígitos iguais a 3,5 ou 6
    # c) têm as prioridades a) e b) simultaneamente

    # a) têm todos os dígitos diferentes
    # Número de opções para cada posição

    print("Quantos número de quatro dígitos são maiores que 2400 e: \n")
    
    from itertools import permutations

    def count_unique_numbers_greater_than_2400():
        count = 0
        for num in permutations('0123456789', 4):
            num_str = ''.join(num)
            if int(num_str) > 2400:
                count += 1
        return count

    print(" a) têm todos os dígitos diferentes", count_unique_numbers_greater_than_2400())

    
    def count_numbers_without_3_5_6_greater_than_2400():
        valid_digits = '0124789'
        count = 0
        for num in permutations(valid_digits, 4):
            num_str = ''.join(num)
            if int(num_str) > 2400:
                count += 1
        return count    

    print("\n b) não têm dígitos iguais a 3,5 ou 6 ", count_numbers_without_3_5_6_greater_than_2400())

    def count_unique_numbers_without_3_5_6_greater_than_2400():
        valid_digits = '0124789'
        count = 0
        for num in permutations(valid_digits, 4):
            num_str = ''.join(num)
            if int(num_str) > 2400:
                count += 1
        return count

    print("\n c) têm as prioridades a) e b) simultaneamente ", count_unique_numbers_without_3_5_6_greater_than_2400())


def questao7():
    print("Você escolheu a Questão 7.")
    # Código da questão 7

    print("O conjunto A possui 4 elementos e o conjunto B possui 7 elementos. Quantas são as funções f : A ->B? Quantas são as funções injetoras f : A -> B?")

    import math

    num_elementos_A = 4
    num_elementos_B = 7

    # Número total de funções f: A -> B
    total_funcoes = num_elementos_B ** num_elementos_A

    # Número de funções injetoras f: A -> B
    num_funcoes_injetoras = math.perm(num_elementos_B, num_elementos_A)

    print("Número total de funções f: A -> B:", total_funcoes)
    print("Número de funções injetoras f: A -> B:", num_funcoes_injetoras)




def questao8():
    print("Você escolheu a Questão 8.")
    # Código da questão 8

    print("Quantos divisores e quantos divisores pares tem o número 360? Quantos são pares? \n") 

    def count_divisors(n):
        divisor_count = 0
        even_divisor_count = 0
        
        for i in range(1, n//2 + 1):
            if n % i == 0:  
                divisor_count += 1
                if i % 2 == 0: 
                    even_divisor_count += 1
        
        divisor_count += 1
        if n % 2 == 0:  
            even_divisor_count += 1
        
        return divisor_count, even_divisor_count

    number = 360
    total_divisors, even_divisors = count_divisors(number)
    print("Número total de divisores de", number, ":", total_divisors)
    print("Número total de divisores pares de", number, ":", even_divisors)


def questao9():
    print("Você escolheu a Questão 9.")
    # Código da questão 9

    print("Quantos números naturais de 4 dígitos têm pelo menos dois dígitos iguais?")

    def possui_dois_digitos_iguais(numero):
        digitos = [int(d) for d in str(numero)]
        return len(set(digitos)) < 4

    def contar_numeros_com_dois_digitos_iguais():
        contador = 0
        for numero in range(1000, 10000):
            if possui_dois_digitos_iguais(numero):
                contador += 1
        return contador

    total = contar_numeros_com_dois_digitos_iguais()
    print("Total de números naturais de 4 dígitos com pelo menos dois dígitos iguais:", total)


def questao10():
    print("Você escolheu a Questão 10.")
    # Código da questão 10

    print("Quantos subconjuntos possui um conjunto que tem n elementos? \n")

    def numero_de_subconjuntos(n):
        return 2 ** n

    # Exemplo com conjunto com 3 elementos
    n = 3
    subconjuntos = numero_de_subconjuntos(n)
    print("Número de subconjuntos:", subconjuntos)



def questao11():
    print("Você escolheu a Questão 11.")
    # Código da questão 11

    print("De quantos modos podemos arrumar 8 torres iguais em um tabuleiro de xadrez (8 x 8) de modo que não haja duas torres na mesma linha nem na mesma coluna? \n") 


    from itertools import permutations

    def contar_arranjos_torres():
        arranjos = permutations(range(8))
        
        # Contar o número de permutações onde nenhuma torre está na mesma linha
        contagem = 0
        for arranjo in arranjos:
            if len(set(arranjo)) == 8:  # Verificar se todas as linhas são diferentes
                contagem += 1
        
        return contagem

    num_arranjos = contar_arranjos_torres()
    print("Número de modos para arrumar 8 torres em um tabuleiro de xadrez: ", num_arranjos)


def questao12():
    print("Você escolheu a Questão 12.")
    # Código da questão 12

    print("Em uma banca há 5 exemplares iguais da revista A, 6 exemplares iguais da revista B e 10 exemplares iguais da revista C. Quantas coleções não vazias de revistas dessa banca é possivel formar? \n")

    def numero_de_colecoes(n_A, n_B, n_C):
        return (n_A + 1) * (n_B + 1) * (n_C + 1) - 1

    # Quantidades de exemplares de cada revista
    exemplares_A = 5
    exemplares_B = 6
    exemplares_C = 10

    # Calcular o número de coleções não vazias
    num_colecoes = numero_de_colecoes(exemplares_A, exemplares_B, exemplares_C)
    print("Número de coleções não vazias de revistas possíveis:", num_colecoes)


def questao13():
    print("Você escolheu a Questão 13.")
    # Código da questão 13

    print("De um baralho comum (52 cartas) sacam-se sucessivamente e sem reposição três cartas. Quantas são as extrações nas quais a primeira carta é de copas, a segunda é um rei e a terceira não é uma dama? \n")

    total_colecoes = 0

    # Caso 1: Primeira carta é um Rei de Copas
    # Uma possibilidade para o Rei de Copas
    # Três possibilidades para escolher um Rei após a primeira extração
    # 46 possibilidades para escolher uma carta que não seja uma Dama
    total_colecoes += 1 * 3 * 46

    # Caso 2: Primeira carta de copas não é um Rei de Copas
    # 11 possibilidades para escolher uma carta que não seja um Rei de Copas
    # Quatro possibilidades para escolher um Rei após a primeira extração
    # 46 possibilidades para escolher uma carta que não seja uma Dama
    total_colecoes += (52 - 4 - 1) // 4 * 4 * 46 

    # Caso 3: Primeira carta é uma Dama de Copas
    # Uma possibilidade para a Dama de Copas
    # Quatro possibilidades para escolher um Rei após a primeira extração
    # 47 possibilidades para escolher uma carta que não seja uma Dama
    total_colecoes += 1 * 4 * 47

    print("Total de coleções que atendem às condições especificadas:", total_colecoes)



def questao14():
    print("Você escolheu a Questão 14.")
    # Código da questão 14

    print("Quantos números diferentes podem ser formados multiplicando alguns (ou todos) dos números 1,5,6,7,7,9,9,9? \n")

    from itertools import combinations

    def contar_numeros_diferentes(numeros):
        produtos = set()
        for r in range(1, len(numeros) + 1):
            for comb in combinations(numeros, r):
                produto = 1
                for num in comb:
                    produto *= num
                produtos.add(produto)
        return len(produtos)

    numeros = [1, 5, 6, 7, 7, 9, 9, 9]

    total_numeros_diferentes = contar_numeros_diferentes(numeros)
    print("Número de números diferentes que podem ser formados:", total_numeros_diferentes)


def questao15():
    print("Você escolheu a Questão 15.")
    # Código da questão 15

    print("Um vagão de metrô tem 10 bancos individuais, sendo 5 de frente e 5 de costas. De 10 passageiros, 4 preferem sentar de frente, 3 preferem sentar de costas e os demais não têm preferência. De quantos modos os passageiros podem se sentar, respeitando-se as preferências? \n")

    import math

    def permutations(n, k):
        return math.factorial(n) // math.factorial(n - k)

    # Número total de passageiros
    total_passengers = 10
    front_facing = 4
    back_facing = 3

    no_preference = total_passengers - front_facing - back_facing

    ways_front_facing = permutations(5, front_facing)

    ways_back_facing = permutations(5, back_facing)

    total_ways = ways_front_facing * ways_back_facing * math.factorial(no_preference)

    print("Número total de maneiras:", total_ways)


def questao16():
    print("Você escolheu a Questão 16.")
    # Código da questão 16

    print("Há duas estradas principais da cidade A até a cidade B, ligadas por 10 estradas secundárias, como na Figura 2.2. Quantas rotas livres de auto-interseções há de A até B? \n")

    def count_routes(n):
        # Inicialmente, há uma única rota (não há movimentos)
        routes = 1
        # Para cada movimento adicional
        for i in range(n):
            
            routes *= 2
        
        return routes

    n = 11

    total_routes = count_routes(n)

    print("Número total de rotas:", total_routes)

def questao17():
    print("Você escolheu a Questão 17.")
    # Código da questão 17

    print("Quantos números inteiros entre 100 e 999 são ímpares e possuem três dígitos distintos? \n")

    def has_distinct_digits(number):
        digits = set(str(number))
        return len(digits) == 3

    count = 0

    for num in range(100, 1000):
        # Verificar se o número é ímpar e possui três dígitos distintos
        if num % 2 != 0 and has_distinct_digits(num):
            count += 1

    print("Número de inteiros ímpares entre 100 e 999 com três dígitos distintos:", count)


def questao18():
    print("Você escolheu a Questão 18.")
    # Código da questão 18

    print("Escrevem-se os inteiros de 1 até 222 222. Quantas vezes o algarismo zero é escrito? \n")

    # Contando o número de zeros nas unidades
    zeros_units = 222222 // 10

    # Contando o número de zeros nas dezenas
    zeros_tens = 222222 // 100 * 10

    # Contando o número de zeros nas centenas
    zeros_hundreds = 222222 // 1000 * 100

    # Contando o número de zeros nos milhares
    zeros_thousands = 222222 // 10000 * 1000

    # Contando o número de zeros nas dezenas de milhar
    zeros_ten_thousands = 222222 // 100000 * 10000

    # Totalizando o número de zeros
    total_zeros = zeros_units + zeros_tens + zeros_hundreds + zeros_thousands + zeros_ten_thousands

    print("O algarismo zero é escrito", total_zeros, "vezes.")


def questao19():
    print("Você escolheu a Questão 19.")
    # Código da questão 19

    print("Quantos são os números de 5 algarismos, na base 10:")

    def contar_numeros_com_2():
        contador = 0
        for numero in range(10000, 100000):
            if '2' in str(numero):
                contador += 1
        return contador

    def contar_numeros_sem_2():
        contador = 0
        for numero in range(10000, 100000):
            if '2' not in str(numero):
                contador += 1
        return contador

    numeros_com_2 = contar_numeros_com_2()
    numeros_sem_2 = contar_numeros_sem_2()

    print("a) Números de 5 algarismos com o algarismo 2:", numeros_com_2)
    print("b) Números de 5 algarismos sem o algarismo 2:", numeros_sem_2)


def questao20():
    print("Você escolheu a Questão 20.")
    # Código da questão 20

    print("Em um concurso há três candidatos e cinco examinadores, devendo cada examinador votar em um candidato. De quantos modos os votos podem ser distribuídos? \n")

    candidatos = 3
    examinadores = 5

    modos = candidatos ** examinadores
    print("Número total de modos de distribuir os votos:", modos)


def questao21():
    print("Você escolheu a Questão 21.")
    # Código da questão 21

    print("O código morse usa “palavras” contendo de 1 a 4 “letras”, as “letras” sendo ponto e traço. Quantas “palavras” existem no código morse? \n")

    total_palavras = sum([2**i for i in range(1, 5)])
    print("Número total de 'palavras':", total_palavras)



def questao22():
    print("Você escolheu a Questão 22.")
    # Código da questão 22

    print("Fichas podem ser azuis, vermelhas ou amarelas; circulares, retangulares ou triangulares; finas ou grossas. Quantos tipos de fichas existem? \n")

    cores = 3
    formas = 3
    espessuras = 2

    tipos_fichas = cores * formas * espessuras
    print("Número total de tipos de fichas:", tipos_fichas)


def questao23():
    print("Você escolheu a Questão 23.")
    # Código da questão 23

    print("Escrevem-se números de cinco dígitos (inclusive os começados por zero) em cartões. Como 0,1 e 8 não se alteram de cabeça para baixo e como 6 de cabeça para baixo se transforma em 9, um só cartão pode representar dois números (por exemplo, 06198 e 86190). Qual é o número mínimo de cartões para representar todos os números de cinco dígitos? \n")

    # Número total de números de cinco dígitos
    total_numeros = 10 ** 5

    # Número total de cartões do tipo (III) que exibem dois números diferentes quando virados de cabeça para baixo
    cartoes_tipo_III = (5 ** 5) - 75

    # Número de cartões que podem ser economizados (cada cartão do tipo III representa dois números diferentes)
    cartoes_economizados = cartoes_tipo_III // 2

    # Número mínimo de cartões necessário para representar todos os números de cinco dígitos
    numero_minimo_cartoes = total_numeros - cartoes_economizados

    print("O número mínimo de cartões necessário é:", numero_minimo_cartoes)


def questao24():
    print("Você escolheu a Questão 24.")
    # Código da questão 24

    print("No Senado Federal, o Distrito Federal e os 26 estados da federação têm 3 representantes cada. Deve-se formar uma comissão de modo que todos os estados e o Distrito Federal estejam representados por 1 ou 2 senadores. De quantos modos essa comissão pode ser formada? \n")

    num_estados = 27
    maneiras_senadores = 6  # 3*2 maneiras de escolher senadores

    # Número total de maneiras de formar a comissão
    numero_total_formas = maneiras_senadores ** num_estados

    print("O número total de modos que a comissão pode ser formada é:", numero_total_formas)


def questao25():
    print("Você escolheu a Questão 25.")
    # Código da questão 25

    def soma_divisores(n):
        soma = 0
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                soma += i
        return soma + n

    print("a) A soma dos divisores de 720 é:", soma_divisores(720))

    def decomposicoes_em_dois_inteiros(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1
                if n // i != i:
                    count += 1
        return count // 2

    print("b) 720 pode ser decomposto em um produto de dois inteiros positivos de", decomposicoes_em_dois_inteiros(720), "maneiras.")

    def decomposicoes_em_tres_inteiros(n):
        count = 0
        for i in range(1, int(n**(1/3)) + 1):
            if n % i == 0:
                for j in range(i, int((n/i)**0.5) + 1):
                    if (n / i) % j == 0:
                        count += 1
        return count

    print("c) 720 pode ser decomposto em um produto de três inteiros positivos de", decomposicoes_em_tres_inteiros(720), "maneiras.")

    print("d) 144 pode ser decomposto em um produto de dois inteiros positivos de", decomposicoes_em_dois_inteiros(144), "maneiras.")


def questao26():
    print("Você escolheu a Questão 26.")
    # Código da questão 26

    total_palavras = 26**5 #total

    # Número de palavras sem nenhuma letra A
    palavras_sem_A = 25**5

    # Número de palavras em que A é a letra inicial
    palavras_com_A_inicial = 26**4

    # Número de palavras em que A figura, mas não é a letra inicial
    palavras_com_A = total_palavras - palavras_sem_A - palavras_com_A_inicial

    print("O número de palavras de 5 letras distintas com A, mas não como a letra inicial, é:", palavras_com_A)


def permutacao(n):
  if(n == 0):
    return 1
  else:
    return n * permutacao(n - 1)


def questao27():
    print("Você escolheu a Questão 27.")
    # Código da questão 27

    print("Quantos são os anagramas da palavra CAPÍTULO: \n" )
    print("a) que começam com uma consoante e terminam com uma vogal? \n")  
    print("b) que têm as letras C, A e P juntas? \n")
    print("c) que têm as letras C, A, P juntas em qualquer ordem? \n")
    print("d) que têm as vogais e as consoantes intercaladas? \n")  
    print("e) que têm a letra C no 1º lugar e a letra A no 2º lugar? \n")
    print("f) que têm a letra C no 1º lugar ou a letra A no 2º lugar? \n")
    print("g) que têm a letra C no 1º lugar ou a letra A no 2º lugar ou a letra P no 3º lugar? \n")


    print("Item a)\n ")

    res = 4 * 4 *   permutacao(6) # Quatro possibilidades para ser consoante, quatro possibilidades para ser vogal e as demais letras

    print(res, "\n")

    print("Item b)\n ")

    res =  permutacao(6) #Como {C, A, P} é um bloco só, podemos tratá-lo como uma única letra, assim temos 6 letras para organizar 

    print(res, "\n")

    print("Item c)\n ")

    res =  permutacao(3) * permutacao(6) # Formas de organizar {C, A, P} e formas de organizar as demais letras

    print(res, "\n")

    print("Item d)\n ")

    res =  permutacao(4) * permutacao(4) # Cada consoante tem 4 possibilidades e cada vogal tem 4 possibilidades
    res = res * 2 # Multiplica-se para representar que podem ser vogais ou consoantes no começo

    print(res, "\n")

    print("Item e)\n ")

    res = 1 * 1 * permutacao(6) # Como C e A são fixos, temos apenas 6 letras para organizar

    print(res, "\n")

    print("Item f)\n ")

    res =  permutacao(7) + permutacao(7) - permutacao(6) #Calcula-se primeiramente os casos que C e A são definidos, sobrando 7 letras para organizar em cada caso,
                                                                #subtrai-se isso pelo número de casos com C na primeira posição e A na segunda posição 

    print(res, "\n")


    print("Item g)\n ")

    res =  permutacao(7) + permutacao(7) + permutacao(7) - permutacao(6) - permutacao(6) - permutacao(6) + permutacao(5) 
                                                            #Pelo princípio da inclusão exclusão, primeiro soma-se os casos que C, A e P são definidos, sobrando 7 letras para organizar em cada caso,
                                                            #subtrai-se isso pelo número de casos com C intersectando A, C intersectando P e A intersectando P, 
                                                            # e soma-se o número de casos com C intersectando A intersectando P 

    print(res, "\n")


def questao28():
    print("Você escolheu a Questão 28.")
    # Código da questão 28

    print("Permutam-se de todos os modos possíveis os algarismos 1,2,4,6,7 e escrevem-se os números assim formados em ordem crescente. \n" )

    print("a) Em que posição está o número 62417? \n")
    print("b) Qual o número que ocupa o 66º lugar? \n")
    print("c) qual o 200º algarismo escrito? \n")
    print("d) Qual a soma dos número assim formadas? \n")

    print("Item a)\n")

    res = 81 # Partindo se de que cada número tem a possibilidade de ser acompanhado por 4! algarismos, sabe-se que existe 24 possibilidades para cada número isoladamente
            # Assim números começados com 1, 2, ou 4 somam-se 72 posições. Começando a próxima rodada com os algarismos 61 e 3! para as demais possibilidades, temos 6 possibilidades
            # Assim, sabe-se que 72 + 6 = 78 posições. Contando a partir de números começados com 62, fica fácil ver que 62417 fica na posição 81

    print(res, "\n")

    print("Item b)\n")

    res = 46721 # Sabendo que 41 e 3! chega-se há 54 posições. Basta verificar os números iniciados por 42 e 46.

    print(res, "\n")

    print("Item c)\n")

    res = 1 # Dividindo 200 posições por 5 digitos, temos 40 posições para cada número. Assim, usando a mesma lógica dos itens passados
            # Vemos que o número na posição 40 é 26471, e o seu último número é 1.

    print(res, "\n")

    print("Item d)\n")

    dezenaMilhar = 24 * (10000 + 20000 + 40000 + 60000 + 70000) # 24 está em evidência, já que cada algarismo na dezena de milhar tem 24 possibilidades
    milhar = 24 * (1000 + 2000 + 4000 + 6000 + 7000) # 24 possibilidades para cada algarismo na casa do milhar
    centena = 24 * (100 + 200 + 400 + 600 + 700) # 24 possibilidades para cada algarismo na casa da centena
    dezena = 24 * (10 + 20 + 40 + 60 + 70) # 24 possibilidades para cada algarismo na casa da dezena
    unidade = 24 * (1 + 2 + 4 + 6 + 7) # 24 possibilidades para cada algarismo na casa da unidade
    res = dezenaMilhar + milhar + centena + dezena + unidade

    print(res, "\n")

def questao29():
    print("Você escolheu a Questão 29.")
    # Código da questão 29

    print("De quantos modos é possível sentar 7 pessoas em cadeiras em fila de modo que duas determinadas pessoas dessas 7 não fiquem juntas? \n")


    res = permutacao(7) - 2 * permutacao(6) # Calcula-se primeiro todas as posições possíveis, 
                                                # Subtrai-se os casos em que as pessoas A e B estão juntas,
                                                # Como A pode vir na frente de B e vice-versa, multiplica-se por 2!, para indicar que permutam entre si
    print(res, "\n")


def questao30():
    print("Você escolheu a Questão 30.")
    # Código da questão 30

    print("Se A é um conjunto com n elementos, quantas são as funções f : A —> A bijetoras? \n")

    def contar_funcoes_bijetoras(n):
        return permutacao(n)
    
    n = 5
    num_funcoes_bijetoras = contar_funcoes_bijetoras(n)
    print("Número de funções bijetoras f: A -> A:", num_funcoes_bijetoras)


def questao31():
    print("Você escolheu a Questão 31.")
    # Código da questão 31

    print("De quantos modos é possível colocar em uma prateleira 5 livros de matemática, 3 de física e 2 de estatística, de modo que os livros de um mesmo assunto permaneçam juntos? \n")


    res = permutacao(3) * permutacao(5) * permutacao(3) * permutacao(2) #Há 3! formas de organizar os blocos de matéria
                                                                                # Junte isso com a forma de permutar cada bloco de livros

    print(res, "\n")

def questao32():
    print("Você escolheu a Questão 32.")
    # Código da questão 32

    print("Quantas são as permutações dos números (1,2,..., 10) nas quais o 5 está situado à direita do 2 e à esquerda do 3, embora não necessariamente em lugares consecutivos? \n")

    res = permutacao(10) // permutacao(3) # De forma aleatória, há 10! possibilidades de organizar os números no total, 
                                            #mas com a restrição de {2, 3, 5} há 3! possibilidades de organizar essa divisão. Assim dividimos o total de possibilidades pela forma de organizar a restrição.

    print(res, "\n")


def questao33():
    print("Você escolheu a Questão 33.")
    # Código da questão 33

    print("De quantos modos podemos dividir 12 pessoas: \n")
    print("a) em dois grupos de 6? \n")
    print("b) em três grupos de 4? \n")
    print("c) em um grupo de 5 e um grupo de 7? \n")
    print("d) em seis grupos de 2? \n")
    print("e) em dois grupos de 4 e dois grupos de 2? \n")

    print("Item a)\n")

    res = permutacao(12) // (permutacao(6) * permutacao(6) * 2)

    print(res, "\n")

    print("Item b)\n")

    res = permutacao(12) // (permutacao(4) * permutacao(4) * permutacao(4) * permutacao(3))

    print(res, "\n")

    print("Item c)\n")

    res = permutacao(12) // (permutacao(5) * permutacao(7))

    print(res, "\n")

    print("Item d)\n")

    res = permutacao(12) // (permutacao(2) * permutacao(2) * permutacao(2) * permutacao(2) * permutacao(2) * permutacao(2) * permutacao(6)  )

    print(res, "\n")

    print("Item e)\n")

    res = permutacao(12) // (permutacao(2) * permutacao(2) * permutacao(4)**2 * 2**2)

    print(res, "\n")



def questao34():
    print("Você escolheu a Questão 34.")
    # Código da questão 34

    print("De quantos modos r rapazes e m moças podem se colocar em fila de modo que as moças fiquem juntas? \n")

    res = permutacao(5) * permutacao(5) * 2 # Há 5! formas de organizar os rapazes e 5! formas de organizar as moças
    
    print("foi usado r = 5")
    print("foi usado 2 para representar que as moças podem ficar na frente ou atrás dos rapazes")
    print(res, "\n")



def questao35():
    print("Você escolheu a Questão 35.")
    # Código da questão 35

    print("Delegados de 10 países devem se sentar em 10 cadeiras em fila. De quantos modos isso pode ser feito se os delegados do Brasil e de Portugal devem se sentar juntos e o do Iraque e o dos Estados Unidos não podem sentar juntos? \n")

    r = permutacao(2) * permutacao(9) - (2 * 2 * permutacao(8)) # Calcula-se todas as possibilidades de Brasil e Portugal como um bloco, lembrando de permutar entre eles
                                                                  # e subtrai-se as possibilidades de EUA e Irã como um bloco, assim como Brasil e Portugal, permutando-se entre eles
    print(r, "\n") # 725760   

def questao36():
    print("Você escolheu a Questão 36.")
    # Código da questão 36

    print("Um cubo de madeira tem uma face de cada cor. Quantos dados diferentes podemos formar gravando números de 1 a 6 sobre essas faces? \n")

    r = permutacao(6) # Possibilidades de faces do dado já que cada face é diferenciável por apresentar cores diferentes
    print(r, "\n") 

def questao37():
    print("Você escolheu a Questão 37.")
    # Código da questão 37

    print("Quantos dados diferentes podemos formar gravando números de 1 a 6 sobre as faces indistinguíveis de um cubo de madeira? \n")
    
    r = permutacao(6) // 24 # Há 4 possibilidades de escolhas para a face ficar de frente, já que a sua parte oposta é indiferenciável
                        # Como há 6 faces ao todo no cubo, temos que 6*4 = 24. Já que há 6! possibilidades de confecção do cubo em 6 grupos de 4 faces

    print(r, "\n")

def questao38():
    print("Você escolheu a Questão 38.")
    # Código da questão 38

    print("Resolva o problema anterior da questão 37 para: \n")
    print("a) números de 1 a 4, tetraedro regular \n")
    print("b) números de 1 a 8, octaedro regular \n")
    print("c) números de 1 a 12, dodecaedro regular \n")
    print("d) números de 1 a 20, icosaedro regular \n")
    print("e) números de 1 a 8, prisma hexagonal regular \n")
    print("f) números de 1 a 5, pirâmide quadrangular regular \n")


    print("Item a)\n")

    r = permutacao(4) // 12 

    print(r, "\n")

    print("Item b)\n")

    r = permutacao(8) // 24 

    print(r, "\n")

    print("Item c)\n")

    r = permutacao(12) // 60

    print(r, "\n")

    print("Item d)\n")

    r = permutacao(20) // 60 

    print(r, "\n")

    print("Item e)\n")

    r = permutacao(8) // 12 

    print(r, "\n")

    print("Item f)\n")

    r = permutacao(5) // 4 

    print(r, "\n")


def questao39():
    print("Você escolheu a Questão 39.")
    # Código da questão 39

    print("Um campeonato é disputado por 12 clubes em rodadas de 6 jogos cada. De quantos modos é possível selecionar os jogos de primeira rodada? \n ")

    r = permutacao(12) // (permutacao(2) * permutacao(10)) # Há 12 possibilidades para o primeiro jogo, 11 para o segundo, 10 para o terceiro, 9 para o quarto, 8 para o quinto e 7 para o sexto

    print(r, "\n")

def fatorial(n):
  if(n == 0):
    return 1
  else:
    return n * fatorial(n - 1)

def permSimples(m, p):
    return ((fatorial(m)) /( fatorial(p) * fatorial(m - p)) )


def questao40():
    print("Você escolheu a Questão 40.")
    # Código da questão 40

    print("Uma comissão formada por 3 homens e 3 mulheres deve ser escolhida em um grupo de 8 homens e 5 mulheres. \n ")
    print("a) Quantas comissões podem ser formadas? \n")
    print("b) Qual seria a resposta se um dos homens não aceitassem participar da comissão se nela estivesse determinada mulher? \n")


    a = permSimples(8, 3) * permSimples(5,3)
    print(f'a) {a} \n')


    caso1 = permSimples(7,3) * permSimples(4,3)

    caso2 = permSimples(7,2) * permSimples(4,3)

    caso3 = permSimples(7,3) * permSimples(4,2)

    b = caso1 + caso2 + caso3

    print(f'b) {b}\n')

def questao41():
    print("Você escolheu a Questão 41.")
    # Código da questão 41

    print("Para a seleção brasileira foram convocados dois goleiros, 6 zagueiros, 7 meios de campo e 4 atacantes. De quantos modos é possível escalar a seleção com 1 goleiro, 4 zagueiros, 4 meios de campo e 2 atacantes? \n ")

    r = permSimples(2,1) * permSimples(6,4) * permSimples(7,4) * permSimples(4,2)

    print(r, "\n")


def questao42():
    print("Você escolheu a Questão 42.")
    # Código da questão 42

    print("Tem-se 5 pontos sobre uma reta R e 8 pontos sobre uma reta R' paralela a R. Quantos quadriláteros convexos com vértices em 4 desses 13 pontos existem? \n")

    r = permSimples(5, 2) * permSimples(8, 2)

    print(r, "\n")

def questao43():
    print("Você escolheu a Questão 43.")
    # Código da questão 43

    print("Em um torneio no qual cada participante enfrenta todos os demais uma única vez, são jogadas 780 partidas. Quantos são os participantes? \n")

    r = 1 + math.sqrt(1 + 8 * 780) / 2

    print(r, "\n")


def questao44():
    print("Você escolheu a Questão 44.")
    # Código da questão 44

    print("Um homem tem 5 amigas e 7 amigos. Sua esposa tem 7 amigas e 5 amigos. De quantos modos eles podem convidar 6 amigas e 6 amigos, se cada um deve convidar 6 pessoas? \n")


    caso1 = permSimples(5, 5) * permSimples(7, 1) *  permSimples(5, 5) * permSimples(7, 1)

    caso2 = permSimples(5, 4) * permSimples(7, 2) * permSimples(5, 4) * permSimples(7, 2)

    caso3 = permSimples(5, 3) * permSimples(7,3) *  permSimples(5, 3) * permSimples(7,3)

    caso4 = permSimples(5, 2) * permSimples(7, 4) * permSimples(5, 2) * permSimples(7, 4)

    caso5 = permSimples(5, 1) * permSimples(7, 5) * permSimples(5, 1) * permSimples(7, 5)

    caso6 = permSimples(5, 0) * permSimples(7, 6) * permSimples(5, 0) * permSimples(7, 6)

    r = caso1 + caso2 + caso3 + caso4 + caso5 + caso6

    print(r, "\n")


def questao45():
    print("Você escolheu a Questão 45.")
    # Código da questão 45

    print("Quantos são os números naturais de 7 dígitos nos quais o dígito 4 figura exatamente 3 vezes e o dígito 8 exatamente 2 vezes? \n")


    # Escolhendo as casas:

    f = permSimples(7, 2) * permSimples(5, 3) * 8 ** 2

    # Numero de numeros comecando com zero

    z = permSimples(6, 2) * permSimples(4, 3) * 8

    # Excluindo os numeros começando com zero das possibilidades gerais

    r = f - z

    print(r, "\n")


def questao46():
    print("Você escolheu a Questão 46.")
    # Código da questão 46

    print("Quantos são os números naturais de 7 dígitos nos quais o dígito 4 figura pelo menos 3 vezes e o dígito 8 pelo menos 2 vezes? \n")


    # 4 exatamente tres vezes e 8 exatamente duas vezes

    caso1 = 12960

    # 4 exatamente quatro vezes e 8 duas vezes

    caso2 = (permSimples(7, 2) * permSimples(5, 4) * 8) - permSimples(6,4)

    #4 figura cinco vezes e 8 duas vezes

    caso3 = permSimples(7, 5) * permSimples(2, 2)

    # 4 figura tres vezes e 8 tres vezes

    caso4 = (permSimples(7, 3) * permSimples(4, 3) * 8) - (permSimples(6, 3))

    print(caso4)

    # 4 figura quatro vezes e 8 tres vezes

    caso5 = permSimples(7, 4)

    caso6 = permSimples(7, 3)

    r = caso1 + caso2 + caso3 + caso4 + caso5 + caso6

    print(r, "\n")


def questao47():
    print("Você escolheu a Questão 47.")
    # Código da questão 47

    print("De quantos modos é possível dividir 20 pessoas: \n")
    print("a) em dois grupos de 10? \n")
    print("b) em quatro grupos de 5? \n")
    print("c) em um grupo de 12 e um de 8? \n")
    print("d) em três grupos de 6 e um de 2? \n")

    print("Item a)\n")

    res = permSimples(20, 10) // 2

    print(res, "\n")

    print("Item b)\n")

    res = permSimples(20, 5) // (permSimples(5, 5) * permSimples(5, 5) * permSimples(5, 5) * permSimples(5, 5))

    print(res, "\n")

    print("Item c)\n")

    res = permSimples(20, 12) * permSimples(8, 8)

    print(res, "\n")

    print("Item d)\n")

    res = permSimples(20, 6) * permSimples(14, 6) * permSimples(8, 6) * permSimples(2, 2)

    print(res, "\n")




def questao48():
    print("Você escolheu a Questão 48.")
    # Código da questão 48

    print("De um baralho de pôquer (7,8,9,10, valete, dama, rei e ás, cada um desses grupos aparecendo em 4 naipes: copas, ouros, paus, espadas), sacam-se simultaneamente 5 cartas. \n")

    print("a) Quantas são as extrações possiveis? \n  Quantas são as extrações nas quais se formam. \n")
    print("b) um par(duas cartas em um mesmo grupo e as outras três em três outros grupos diferentes)? \n")
    print("c) dois pares(duas cartas em um grupo, duas em outro grupo e uma em um terceiro grupo)? \n")
    print("d) uma trinca(três cartas em um grupo e as outras duas em dois outros grupos diferentes) \n")
    print("e) um four (quatro cartas em um grupo e uma em outro grupo) \n")
    print("f) um full hand(três cartas em um grupo e duas em outro grupo)? \n")
    print("g) uma sequência(5 cartas de grupos consecutivos, não sendo todas do mesmo naipe)? \n")
    print("h) um flush(5 cartas do mesmo naipe, não formando uma sequência)? \n")
    print("i) um straight flush(5 cartas de grupos consecutivos e do mesmo naipe)? \n")
    print("j) um royal flush(10, valete, dama, rei e ás do mesmo naipe)? \n")

    print("Item a)\n")

    res = permSimples(52, 5)

    print(res, "\n")

    b = 8 * permSimples(4, 2) * permSimples(7,3) * (4 **3)

    print(f'b) {b}\n')

    c = permSimples(8, 2) * (permSimples(4, 2) **2 )* 6 * 4

    print(f'c) {c}\n')

    d = 8 * permSimples(4,3) * permSimples(7, 2 ) * (4 ** 2)
    
    print(f'd) {d}\n')

    e = 8 * 1 * 7 * 4

    print(f'e) {e}\n')

    f = 8 * permSimples(4, 3) * 7 * permSimples(4, 2)

    print(f'f) {f}\n')

    g = 4 * (4**5 - 4)

    print(f'g) {g}\n')

    h = (permSimples(8, 5) - 4) * 4

    print(f'h) {h}\n')

    i = 4 * 4

    print(f'i) {i}\n')

    j = 4

    print(f'j) {j}\n')


def questao49():
    print("Você escolheu a Questão 49.")
    # Código da questão 49

    print("Quantos são os anagramas da palavra CARAGUATATUBA? Quantos começam por vogal? \n")

    r = fatorial(13) / (fatorial(5) * fatorial(2)**2)

    print(f'a) {r}\n')

    va = fatorial(12) / (fatorial(4) * fatorial(2) * fatorial(2))

    vu = fatorial(12) / (fatorial(5) * fatorial(2))

    print(f'b) {va + vu}\n')


def questao50():
    print("Você escolheu a Questão 50.")
    # Código da questão 50

    print("Uma fila de cadeiras no cinema tem 20 poltronas. De quantos modos 6 casais podem se sentar nessas poltronas de modo que nenhum marido se sente separado de sua mulher? \n")

    r = permSimples(20, 2) * permSimples(18, 2) * permSimples(16, 2) * permSimples(14, 2) * permSimples(12, 2) * permSimples(10, 2)

    print(r, "\n")

def questao51():
    print("Você escolheu a Questão 51.")
    # Código da questão 51

    print("Nove cientistas trabalham num projeto sigiloso. Por questões de segurança, os planos são guardados em um cofre protegido por muitos cadeados de modo que só é possível abri-los todos se houver pelo menos 5 cientistas presentes. \n")

    print("a) Qual é o número mínimo possível de cadeados?\n ")
    print('b) Na situação do item a), quantas chaves cada cientista deve ter?\n')


    print("Item a)\n")

    r = 1 + permSimples(9, 5) + permSimples(9, 6) + permSimples(9, 7) + permSimples(9, 8) + permSimples(9, 9)

    print(r, "\n")

    print("Item b)\n")

    r = 1 + permSimples(8, 4) + permSimples(8, 5) + permSimples(8, 6) + permSimples(8, 7) + permSimples(8, 8)

    print(r, "\n")




def questao52():
    print("Você escolheu a Questão 52.")
    # Código da questão 52

    print("Depois de ter dado um curso, um professor resolve se despedir de seus 7 alunos oferecendo, durante 7 dias consecutivos, 7 jantares para 3 alunos cada. De quantos modos ele pode fazer os convites se ele não deseja que um mesmo par de alunos compareça a mais de um jantar? \n")

    convidados =( ( permSimples(6, 2) *  permSimples(4, 2) * 1 )/ fatorial(3) ) * 2

    r = fatorial(7) * convidados

    print(r, "\n")

def questao53():
    print("Você escolheu a Questão 53.")
    # Código da questão 53

    print("No quadro abaixo, de quantos modos é possível formar a palavra “MATEMÁTICA”, partindo de um M e indo sempre para a direita ou para baixo? \n")

    print("Veja o quadro no livro página 44 do pdf - questão 25 \n")


    r = fatorial(9) / (fatorial(3) * fatorial(2))

    print(r, "\n")




def questao54():
    print("Você escolheu a Questão 54.")
    # Código da questão 54

    print("De quantos modos 15 jogadores podem ser divididos em 3 times de basquetebol de 5 jogadores cada, denominados Esperança, Confiança e Vitória'? \n")

    r = permSimples(15, 5) * permSimples(10, 5) * permSimples(5, 5)

    print(r, "\n")


def questao55():
    print("Você escolheu a Questão 55.")
    # Código da questão 55

    print("Quantos são os jogos de um campeonato disputado por 20 clubes, no qual todos se enfrentam uma única vez? \n")

    r = permSimples(20, 2)

    print(r, "\n")



def questao56():
    print("Você escolheu a Questão 56.")
    # Código da questão 56

    print("Empregando dez consoantes e cinco vogais, calcule o número de palavras de seis letras que se podem formar sem usar consoantes nem vogais adjacentes: \n")

    print("a) Se são permitidas repetições; \n")
    print("b) Se não são permitidas repetições. \n")

    print("Item a)\n")

    r = 2 * (5 ** 6)

    print(r, "\n")

    print("Item b)\n")

    r = 2 * (5 * 4 * 5 * 4 * 5 * 4)

    print(r, "\n")

def questao57():
    print("Você escolheu a Questão 57.")
    # Código da questão 57

    print("Em uma escola, x professores se distribuem em 8 bancas examinadoras de modo que cada professor participa de exatamente duas bancas e cada duas bancas têm exatamente um professor em comum. \n")
    print("a) Calcule x. \n")
    print("b) Determine quantos professores há em cada banca. \n")

    print("Item a)\n")

    r = 8 * 2

    print(r, "\n")

    print("Item b)\n")

    r = 2 * 8

    print(r, "\n")




def questao58():
    print("Você escolheu a Questão 58.")
    # Código da questão 58

    print("uma permutação C de 500 por 1000 é divisivel por 7? \n")

    print("não \n")


def questao59():
    print("Você escolheu a Questão 59.")
    # Código da questão 59

    print("De quantos modos 5 meninos e 5 meninas podem formar uma roda de ciranda de modo que pessoas de mesmo sexo não fiquem juntas? \n")

    r = 2 * permSimples(5, 5) * permSimples(5, 5)

    print(r, "\n")


def questao60():
    print("Você escolheu a Questão 60.")
    # Código da questão 60

    print("De quantos modos n crianças podem formar uma roda de ciranda de modo que duas dessas crianças permaneçam juntas? E de modo que p(p < n) dessas crianças permaneçam juntas? \n")

    def roda_ciranda_duas_juntas(n):
        # de modo que duas delas permaneçam juntas na roda de ciranda
        return 2 * factorial(n - 2)

    def roda_ciranda_p_juntas(n, p):
        # de modo que p delas (onde p < n) permaneçam juntas na roda de ciranda
        return factorial(p) * factorial(n - p)

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    # Teste
    n = 5
    print("Número de maneiras de organizar as crianças de modo que duas delas permaneçam juntas:", roda_ciranda_duas_juntas(n))
    p = 1
    print(f"Número de maneiras de organizar as crianças de modo que {p} delas permaneçam juntas:", roda_ciranda_p_juntas(n, p))



def questao61():
    print("Você escolheu a Questão 61.")
    # Código da questão 61

    print("De quantos modos n casais podem formar uma roda de ciranda de modo que cada homem permaneça ao lado de sua mulher? \n")

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)

    def modos_roda_ciranda(n):
        if n <= 1:
            return 1
        else:
            return fatorial(n - 1)

    n = int(input("Digite o número de casais: "))
    modos = modos_roda_ciranda(n)
    print("Número de modos:", modos)


def questao62():
    print("Você escolheu a Questão 62.")
    # Código da questão 62

    print("De quantos modos n casais podem formar uma roda de ciranda de modo que cada homem permaneça ao lado de sua mulher e que pessoas de mesmo sexo não fiquem juntas? \n")

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)

    def modos_roda_ciranda(n):
        if n <= 1:
            return 1
        else:
            return 2 * fatorial(n - 1)

    n = int(input("Digite o número de casais: "))
    modos = modos_roda_ciranda(n)
    print("Número de modos:", modos)




def questao63():
    print("Você escolheu a Questão 63.")
    # Código da questão 63


    print("São dados n pontos em um círculo. Quantos n-ágonos (não necessariamente convexos) existem com vértices nesses pontos? \n")

    def contar_zragonos(n):
        if n < 3:
            return 0
        else:
            fatorial = 1
            for i in range(1, n):
                fatorial *= i
            
            # Retorna (n - 1)! dividido por 2
            return fatorial // 2

    n = int(input("Digite o número de pontos no círculo: "))
    num_zragonos = contar_zragonos(n)
    print("Número de zr-ágonos:", num_zragonos)



def questao64():
    print("Você escolheu a Questão 64.")
    # Código da questão 64

    print("Uma pulseira deve ser cravejada com um rubi, uma esmeralda, um topázio, uma água-marinha, uma turmalina e uma ametista. De quantos modos isso pode ser feito supondo: \n")
    print("a) que a pulseira tem fecho e um relógio engastado no fecho; \n")
    print("b) que a pulseira tem fecho; \n")
    print("c) que a pulseira não tem fecho e o braço só pode entrar na pulseira em um sentido; \n")
    print("d) que a pulseira não tem fecho e o braço pode entrar na pulseira nos dois sentidos. \n")


    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)

    # a) Com fecho e relógio
    modos_a = fatorial(6)
    print("a) Número de modos com fecho e relógio:", modos_a)

    # b) Com fecho
    modos_b = fatorial(6) // 2
    print("b) Número de modos com fecho:", modos_b)

    # c) Sem fecho e braço em um sentido
    modos_c = fatorial(5)
    print("c) Número de modos sem fecho e braço em um sentido:", modos_c)

    # d) Sem fecho e braço em dois sentidos
    modos_d = fatorial(5) // 2
    print("d) Número de modos sem fecho e braço em dois sentidos:", modos_d)



def questao65():
    print("Você escolheu a Questão 65.")
    # Código da questão 65

    print("De quantos modos 5 mulheres e 6 homens podem formar uma roda de ciranda de modo que as mulheres permaneçam juntas? \n")


    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    def modos_roda_ciranda(mulheres, homens):
        if mulheres == 0 or homens == 0:
            return 1
        else:
            return fatorial(mulheres) * fatorial(homens)
        
    mulheres = 5
    homens = 6
    modos = modos_roda_ciranda(mulheres, homens)
    print("Número de modos:", modos)




def questao66():
    print("Você escolheu a Questão 66.")
    # Código da questão 66
    
    print("Quantos dados diferentes existem se a soma das faces opostas deve ser 7? \n")

    def contar_dados(soma_faces_opostas):
        return len(soma_faces_opostas)

    # Para um dado comum de seis faces
    soma_faces_opostas_seis_faces = [(1, 6), (2, 5), (3, 4)]
    num_dados_seis_faces = contar_dados(soma_faces_opostas_seis_faces)
    print("Número de dados diferentes para um dado de seis faces:", num_dados_seis_faces)


def questao67():
    print("Você escolheu a Questão 67.")
    # Código da questão 67

    print("A Figura 2.9 representa o mapa de uma cidade, na qual há 7 avenidas na direção norte-sul e 6 avenidas na direção leste-oeste. \n")
    print("Figura 2.9 - Você encontra na página 52 do pdf , questão 1. \n")
    print("a) Quantos são os trajetos de comprimento mínimo ligando o ponto A ao ponto B? \n")
    print("b) Quantos desses trajetos passam por C? \n")

    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0

    # Número de trajetos de comprimento mínimo de A para B
    num_trajetos_AB = combinacao(13, 6)

    # Número de trajetos de comprimento mínimo de A para B que passam por C
    num_trajetos_ABC = combinacao(7, 3) * combinacao(6, 4)

    print("a) Número de trajetos de A para B:", num_trajetos_AB)
    print("b) Número de trajetos de A para B que passam por C:", num_trajetos_ABC)


def questao68():
    print("Você escolheu a Questão 68.")
    # Código da questão 68

    print("Quantos números de 7 dígitos, maiores que 6000000, podem ser formados usando apenas os algarismos 1,3,6,6,6,8,8? \n")

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    def contar_numeros(digitos):
        numeros = set()
        for i in range(1, len(digitos) + 1):
            for j in itertools.permutations(digitos, i):
                num = int("".join(j))
                if num > 6000000:
                    numeros.add(num)
        return len(numeros)
    
    digitos = "136688"
    num_numeros = contar_numeros(digitos)
    print("Número de números de 7 dígitos maiores que 6000000:", num_numeros)


def questao69():
    print("Você escolheu a Questão 69.")
    # Código da questão 69

    print("Uma partícula, estando no ponto (x,y), pode mover-se para o ponto (x + 1, y) ou para o ponto (x, y + 1). Quantos são os caminhos que a partícula pode tomar para, partindo do ponto (0,0), chegar ao ponto (a, b), onde a > 0 e b > 0? \n")

    def contar_caminhos(a, b):
        return combinacao(a + b, a)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
    
    a = 3
    b = 4
    num_caminhos = contar_caminhos(a, b)
    print("Número de caminhos:", num_caminhos)



def questao70():
    print("Você escolheu a Questão 70.")
    # Código da questão 70

    print("Uma partícula, estando no ponto (x, y, z), pode mover-se para o ponto (x + 1, y, z) ou para o ponto (x, y + 1, z) ou para o ponto (x, y, z + 1). Quantos são os caminhos que a partícula pode tomar par, partindo do ponto (0, 0, 0), chegar ao ponto (a, b, c), onde a > 0, b > O e c > 0? \n")

    def contar_caminhos(a, b, c):
        return combinacao(a + b + c, a)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    a = 2
    b = 3
    c = 4
    num_caminhos = contar_caminhos(a, b, c)
    print("Número de caminhos:", num_caminhos)





def questao71():
    print("Você escolheu a Questão 71.")
    # Código da questão 71

    print("Quantos números de 5 algarismos podem ser formados usando apenas os algarismos 1,1,1,1,2 e 3? \n")

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    def contar_numeros(digitos):
        numeros = set()
        for i in range(1, len(digitos) + 1):
            for j in itertools.permutations(digitos, i):
                num = int("".join(j))
                numeros.add(num)
        return len(numeros)
    
    digitos = "11123"

    num_numeros = contar_numeros(digitos)
    print("Número de números de 5 algarismos:", num_numeros)




def questao72():
    print("Você escolheu a Questão 72.")
    # Código da questão 72

    print("Quantos são as soluções inteiras não negativos de x + y + z + w = 3?")

    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    n = 3
    k = 4
    num_solucoes = combinacao(n + k - 1, k - 1)
    print("Número de soluções inteiras não negativas:", num_solucoes)


def questao73():
    print("Você escolheu a Questão 73.")
    # Código da questão 73

    print("Quantos são as soluções inteiras não negativas de x + y + z + w < 6?")

    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
    
    n = 6
    k = 4

    num_solucoes = combinacao(n + k - 1, k - 1)
    print("Número de soluções inteiras não negativas:", num_solucoes)



def questao74():
    print("Você escolheu a Questão 74.")
    # Código da questão 74

    print("Quantas são as soluções inteiras positivas de x + y + z = 10? \n")

    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0

    n = 10
    k = 3

    num_solucoes = combinacao(n - 1, k - 1)
    print("Número de soluções inteiras positivas:", num_solucoes)




def questao75():
    print("Você escolheu a Questão 75.")
    # Código da questão 75

    print("Quantos são as soluções inteiras positivas de x + y + z < 10? \n")

    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    n = 10
    k = 3

    num_solucoes = combinacao(n - 1, k - 1)
    print("Número de soluções inteiras positivas:", num_solucoes)


def questao76():
    print("Você escolheu a Questão 76.")
    # Código da questão 76

    print("Quantas são as peças de um dominó comun? \n")

    def contar_pecas():
        pecas = set()
        for i in range(7):
            for j in range(i, 7):
                pecas.add((i, j))
        return len(pecas)
    
    num_pecas = contar_pecas()

    print("Número de peças de um dominó comum:", num_pecas)


def questao77():
    print("Você escolheu a Questão 77.")
    # Código da questão 77

    print("Im = {1, 2, ..., m} e In = {1, 2, ..., n}. Quantas são as funções f: Im -> In não decrescentes? \n")

    def contar_funcoes(m, n):
        return combinacao(m + n - 1, n - 1)

    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
    
    m = 3
    n = 4
    num_funcoes = contar_funcoes(m, n)
    print("Número de funções não decrescentes:", num_funcoes)

def questao78():
    print("Você escolheu a Questão 78.")
    # Código da questão 78

    print("De quantos modos podemos colocar em fila 7 letras A, 6 letras B e 5 letras C de modo que não haja duas letras B juntas? \n")

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    def contar_filas(letras_A, letras_B, letras_C):
        return fatorial(letras_A + letras_B + letras_C) // fatorial(letras_A) // fatorial(letras_B) // fatorial(letras_C)
    
    letras_A = 7
    letras_B = 6
    letras_C = 5
    num_filas = contar_filas(letras_A, letras_B, letras_C)
    print("Número de filas:", num_filas)


def questao79():
    print("Você escolheu a Questão 79.")
    # Código da questão 79

    print("A fábrica X produz 8 tipos de bombons que são vendidos em caixas de 30 bombons ( de um mesmo tipo ou sortido). Quantas caixas diferentes podem ser formadas? \n")    

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    def contar_caixas(bombons, caixas):
        return fatorial(bombons + caixas - 1) // fatorial(bombons) // fatorial(caixas - 1)
    
    bombons = 8
    caixas = 30
    num_caixas = contar_caixas(bombons, caixas)
    print("Número de caixas diferentes:", num_caixas)

def questao80():
    print("Você escolheu a Questão 80.")
    # Código da questão 80

    print("De quantos modos podem ser pintados 6 objetos iguais usando 3 cores diferentes? \n")

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    def contar_pinturas(objetos, cores):
        return fatorial(objetos + cores - 1) // fatorial(objetos) // fatorial(cores - 1)

    objetos = 6
    cores = 3
    num_pinturas = contar_pinturas(objetos, cores)
    print("Número de modos de pintura:", num_pinturas)


def questao81():
    print("Você escolheu a Questão 81.")
    # Código da questão 81

    print("Quantos números inteiros entre 1 e 100000 têm a soma dos algorismos igual a 6? \n")

    def contar_numeros(soma_algarismos):
        numeros = set()
        for i in range(1, 100001):
            soma = sum(int(d) for d in str(i))
            if soma == soma_algarismos:
                numeros.add(i)
        return len(numeros)
    
    soma_algarismos = 6

    num_numeros = contar_numeros(soma_algarismos)
    print("Número de números inteiros:", num_numeros)

def questao82():
    print("Você escolheu a Questão 82.")
    # Código da questão 82

    print("Quantas são as soluções inteiras não negativas de x1 + x2 + x3 + x4 + x5 + x6 = 20, nas quais exatamente 3 incógnitas são nulas? Em quantas pelo menos são nulas? \n")

    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
    
    n = 20
    k = 6

    # Exatamente 3 incógnitas nulas
    num_solucoes_exatamente_3_nulas = combinacao(k, 3) * combinacao(n + k - 1 - 3, k - 3)

    # Pelo menos 3 incógnitas nulas
    num_solucoes_pelo_menos_3_nulas = combinacao(k, 3) * combinacao(n + k - 1 - 3, k - 3) + combinacao(k, 4) * combinacao(n + k - 1 - 4, k - 4) + combinacao(k, 5) * combinacao(n + k - 1 - 5, k - 5) + combinacao(k, 6) * combinacao(n + k - 1 - 6, k - 6)

    print("Número de soluções inteiras não negativas com exatamente 3 incógnitas nulas:", num_solucoes_exatamente_3_nulas)
    print("Número de soluções inteiras não negativas com pelo menos 3 incógnitas nulas:", num_solucoes_pelo_menos_3_nulas)


def questao83():
    print("Você escolheu a Questão 83.")
    # Código da questão 83

    print("Os números inteiros compreendidos entre 100 000 e 999 999 são divididos em classes de modo que dois números diferentes estão na mesma classe se e só se eles têm os mesmos algarismos, diferindo apenas na ordem. Assim, por exemplo, 552 221 e 125 252 estão na mesma classe. Quantas classes são assim formadas? \n")

    def contar_classes():
        classes = set()
        for i in range(100000, 1000000):
            classe = "".join(sorted(str(i)))
            classes.add(classe)
        return len(classes)
    
    num_classes = contar_classes()

    print("Número de classes formadas:", num_classes)



def questao84():
    print("Você escolheu a Questão 84.")
    # Código da questão 84

    print("Quantas são as soluções inteiras não negativas de x + y + z + w = 20, nas quais x > y? \n")

    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    n = 20
    k = 4

    num_solucoes = combinacao(n + k - 1, k - 1) // 2
    print("Número de soluções inteiras não negativas:", num_solucoes)


def questao85():
    print("Você escolheu a Questão 85.")
    # Código da questão 85

    print("Quantos inteiros entre 1 e 100 000, inclusive, têm a propriedade: “cada dígito é menor ou igual ao seu sucessor”? \n")

    def contar_inteiros():
        inteiros = set()
        for i in range(1, 100001):
            if all(int(d) <= int(e) for d, e in zip(str(i), str(i)[1:])):
                inteiros.add(i)
        return len(inteiros)

    num_inteiros = contar_inteiros()

    print("Número de inteiros com a propriedade:", num_inteiros)


def questao86():
    print("Você escolheu a Questão 86.")
    # Código da questão 86

    print("Quantas permutações de 7 letras A e 7 letras B, nas quais não há 3 letras A adjacentes, existem? \n")

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    def contar_permutacoes(letras_A, letras_B):
        return fatorial(letras_A + letras_B) - 2 * fatorial(letras_A - 3) * fatorial(letras_B)
    
    letras_A = 7
    letras_B = 7
    num_permutacoes = contar_permutacoes(letras_A, letras_B)
    print("Número de permutações:", num_permutacoes)

def questao87():
    print("Você escolheu a Questão 87.")
    # Código da questão 87

    print("De quantos modos podemos escolher 3 números, não necessariamente distintos, no conjunto {1,2,..., 150} de modo que a soma dos números escolhidos seja divisível por 3? E se os números devessem ser distintos? \n")

    def contar_modos(numeros, soma, distintos=False):
        if distintos:
            return combinacao(numeros, 3)
        else:
            return combinacao(numeros + soma - 1, 3)
        
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
    
    numeros = 150
    soma = 3
    num_modos = contar_modos(numeros, soma)
    print("Número de modos com números não necessariamente distintos:", num_modos)


def questao88():
    print("Você escolheu a Questão 88.")
    # Código da questão 88

    print("De quantas maneiras é possivel colocar 6 anéis diferente em 4 dedos? \n")

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    def contar_maneiras(anéis, dedos):
        return fatorial(anéis + dedos - 1) // fatorial(anéis) // fatorial(dedos - 1)

    anéis = 6
    dedos = 4
    num_maneiras = contar_maneiras(anéis, dedos)
    print("Número de maneiras:", num_maneiras)


def questao89():
    print("Você escolheu a Questão 89.")
    # Código da questão 89

    print("Quantos inteiros entre 1 e 1000 inclusive: \n")
    print("a) são divisiveis por pelo menos três dos números 2, 3, 7 e 10? \n")
    print("b) não são divisiveis por nenhum dos números 2, 3, 7 e 10? \n")  
    print("c) são divisiveis por exatamente um dos números 2, 3, 7 e 10? \n")
    print("d) são divisiveis por pelo menos um dos números 2, 3, 7 e 10? \n")


    def contar_inteiros(divisores, n):
        inteiros = set()
        for i in range(1, n + 1):
            if any(i % d == 0 for d in divisores):
                inteiros.add(i)
        return len(inteiros)
    
    def contar_inteiros_nao_divisiveis(divisores, n):
        inteiros = set()
        for i in range(1, n + 1):
            if all(i % d != 0 for d in divisores):
                inteiros.add(i)
        return len(inteiros)
    
    def contar_inteiros_divisiveis_por_um(divisores, n):
        inteiros = set()
        for i in range(1, n + 1):
            if sum(i % d == 0 for d in divisores) == 1:
                inteiros.add(i)
        return len(inteiros)
    
    def contar_inteiros_divisiveis_por_pelo_menos_um(divisores, n):
        inteiros = set()
        for i in range(1, n + 1):
            if sum(i % d == 0 for d in divisores) >= 1:
                inteiros.add(i)
        return len(inteiros)
    
    divisores = [2, 3, 7, 10]
    n = 1000

    # a) Divisíveis por pelo menos três dos números 2, 3, 7 e 10
    num_inteiros_a = contar_inteiros(divisores, n)
    print("a) Número de inteiros divisíveis por pelo menos três dos números 2, 3, 7 e 10:", num_inteiros_a)

    # b) Não divisíveis por nenhum dos números 2, 3, 7 e 10
    num_inteiros_b = contar_inteiros_nao_divisiveis(divisores, n)
    print("b) Número de inteiros não divisíveis por nenhum dos números 2, 3, 7 e 10:", num_inteiros_b)

    # c) Divisíveis por exatamente um dos números 2, 3, 7 e 10
    num_inteiros_c = contar_inteiros_divisiveis_por_um(divisores, n)
    print("c) Número de inteiros divisíveis por exatamente um dos números 2, 3, 7 e 10:", num_inteiros_c)

    # d) Divisíveis por pelo menos um dos números 2, 3, 7 e 10
    num_inteiros_d = contar_inteiros_divisiveis_por_pelo_menos_um(divisores, n)
    print("d) Número de inteiros divisíveis por pelo menos um dos números 2, 3, 7 e 10:", num_inteiros_d)



def questao90():
    print("Você escolheu a Questão 90.")
    # Código da questão 90

    print("Quantos inteiros entre 1000 e 10000 inclusive não são divisíveis nem por 2, nem por 3 e nem por 5? \n")

    def contar_inteiros_nao_divisiveis(divisores, n, m):
        inteiros = set()
        for i in range(n, m + 1):
            if all(i % d != 0 for d in divisores):
                inteiros.add(i)
        return len(inteiros)
    
    divisores = [2, 3, 5]
    n = 1000
    m = 10000

    num_inteiros = contar_inteiros_nao_divisiveis(divisores, n, m)
    print("Número de inteiros não divisíveis por 2, 3 e 5:", num_inteiros)




def questao91():
    print("Você escolheu a Questão 91.")
    # Código da questão 91

    print("Lançam-se 3 dados. Em quantos dos 6^3 resultados possíveis a soma dos pontos é 12? \n")

    def contar_resultados(soma_pontos):
        resultados = set()
        for i in range(1, 7):
            for j in range(1, 7):
                for k in range(1, 7):
                    if i + j + k == soma_pontos:
                        resultados.add((i, j, k))
        return len(resultados)
    
    soma_pontos = 12

    num_resultados = contar_resultados(soma_pontos)
    print("Número de resultados com soma dos pontos igual a 12:", num_resultados)



def questao92():
    print("Você escolheu a Questão 92.")
    # Código da questão 92

    print("Quantas são as soluções inteiras não negativas de x + y + z = 12 nas quais pelo menos uma incógnita é maior que 7? \n")

    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
    
    n = 12
    k = 3

    # Pelo menos uma incógnita maior que 7
    num_solucoes = combinacao(n + k - 1, k - 1) - combinacao(n - 7 + k - 1, k - 1)

    print("Número de soluções inteiras não negativas:", num_solucoes)



def questao93():
    print("Você escolheu a Questão 93.")
    # Código da questão 93

    print("Se #A = n e #B = p (n >= p), quantas são as funções f : A —> B sobrejetoras? \n")

    def contar_funcoes(n, p):
        return sum((-1)**(p - k) * combinacao(p, k) * k**n for k in range(1, p + 1))
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    n = 3
    p = 2

    num_funcoes = contar_funcoes(n, p)
    print("Número de funções sobrejetoras:", num_funcoes)



def questao94():
    print("Você escolheu a Questão 94.")
    # Código da questão 94

    print("Determine o número de permutações de (1,2,3,4,5,6) nas quais nem o 4 ocupa o 4º lugar nem o 6 ocupa o 6º lugar. \n")

    def contar_permutacoes():
        permutacoes = set()
        for p in itertools.permutations(range(1, 7)):
            if p[3] != 4 and p[5] != 6:
                permutacoes.add(p)
        return len(permutacoes)
    
    num_permutacoes = contar_permutacoes()

    print("Número de permutações:", num_permutacoes)


def questao95():
    print("Você escolheu a Questão 95.")
    # Código da questão 95

    print("Quantos são os inteiros de n dígitos, que têm todos os dígitos pertencentes ao conjunto {1,2, 3}? Em quantos deles os inteiros 1, 2 e 3 figuram todos? \n")

    def contar_inteiros(digitos, n):
        inteiros = set()
        for i in range(1, 10**n):
            if all(int(d) in digitos for d in str(i)):
                inteiros.add(i)
        return len(inteiros)
    
    digitos = {1, 2, 3}
    n = 3

    num_inteiros = contar_inteiros(digitos, n)
    print("Número de inteiros com dígitos 1, 2 e 3:", num_inteiros)


def questao96():
    print("Você escolheu a Questão 96.")
    # Código da questão 96

    print("Determine o número de permutações das letras AABBCCDD nas quais não há letras iguais adjacentes. \n")

    def contar_permutacoes(letras):
        permutacoes = set()
        for p in itertools.permutations(letras):
            if all(p[i] != p[i + 1] for i in range(len(p) - 1)):
                permutacoes.add(p)
        return len(permutacoes)
    
    letras = "AABBCCDD"
    num_permutacoes = contar_permutacoes(letras)

    print("Número de permutações:", num_permutacoes)


def questao97():
    print("Você escolheu a Questão 97.")
    # Código da questão 97

    print("Quantos inteiros entre 1 e 1 000 000 não são nem quadrados perfeitos nem cubos perfeitos? \n")

    def contar_inteiros(n):
        inteiros = set()
        for i in range(1, n + 1):
            if not (i**0.5).is_integer() and not (i**(1/3)).is_integer():
                inteiros.add(i)
        return len(inteiros)
    
    n = 1000000

    num_inteiros = contar_inteiros(n)
    print("Número de inteiros não quadrados perfeitos nem cubos perfeitos:", num_inteiros)

def questao98():
    print("Você escolheu a Questão 98.")
    # Código da questão 98

    print("Oito crianças estão sentadas em tomo de um carrossel. De quantos modos elas podem trocar de lugar de modo que cada criança passe a ter uma criança diferente a sua direita? \n")

    def contar_modos(n):
        return fatorial(n) - fatorial(n - 1)
    
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    n = 8
    num_modos = contar_modos(n)
    print("Número de modos:", num_modos)
    

def questao99():
    print("Você escolheu a Questão 99.")
    # Código da questão 99

    print("5 pessoas devem se sentar em 15 cadeiras colocadas em tomo de uma mesa circular. De quantos modos isso pode ser feito se não deve haver ocupação simultânea de duas cadeiras adjacentes? \n")

    def contar_modos(pessoas, cadeiras):
        return fatorial(cadeiras) // fatorial(cadeiras - pessoas)
    
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    pessoas = 5
    cadeiras = 15
    num_modos = contar_modos(pessoas, cadeiras)
    print("Número de modos:", num_modos)

def questao100():
    print("Você escolheu a Questão 100.")
    # Código da questão 100

    print("Dado um decágono, quantos são os triângulos cujos vértices são vértices não consecutivos do decágono? \n")

    def contar_triangulos(n):
        return combinacao(n, 3)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    n = 10
    num_triangulos = contar_triangulos(n)
    print("Número de triângulos:", num_triangulos)


def questao101():
    print("Você escolheu a Questão 101.")
    # Código da questão 101

    print("De quantos modos é possível formar uma roda de ciranda com 7 meninas e 12 meninos sem que haja duas meninas em posições adjacentes? \n")

    def contar_modos(meninas, meninos):
        return fatorial(meninos) * combinacao(meninos + 1, meninas)
    
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
    
    meninas = 7
    meninos = 12
    num_modos = contar_modos(meninas, meninos)
    print("Número de modos:", num_modos)

def questao102():
    print("Você escolheu a Questão 102.")
    # Código da questão 102

    print("Quantos são os anagramas de araraquara que não possuem duas letras a consecutivas? \n")

    def contar_anagramas(palavra):
        anagramas = set()
        for p in itertools.permutations(palavra):
            if all(p[i] != "a" or p[i + 1] != "a" for i in range(len(p) - 1)):
                anagramas.add(p)
        return len(anagramas)
    
    palavra = "araraquara"

    num_anagramas = contar_anagramas(palavra)
    print("Número de anagramas:", num_anagramas)



def questao103():
    print("Você escolheu a Questão 103.")
    # Código da questão 103

    print("Em uma gaveta há 12 meias brancas e 12 meias pretas. Quantas meias devemos retirar ao acaso para termos certeza de obter um par de meias da mesma cor? \n")

    def contar_meias(meias):
        return meias + 1
    
    meias = 12
    num_meias = contar_meias(meias)
    print("Número de meias:", num_meias)
    


def questao104():
    print("Você escolheu a Questão 104.")
    # Código da questão 104

    print("63 127 candidatos compareceram a uma prova do vestibular (25 questões de múltipla-escolha com 5 alternativas por questão). Considere a afirmação: “Pelo menos dois candidatos responderam de modo idêntico a k primeiras questões da prova”. Qual é o maior valor de k para o qual podemos garantir que a afirmação acima é verdadeira? \n")

    def contar_candidatos(candidatos, questoes, alternativas):
        return candidatos // (alternativas**questoes) + 1
    
    candidatos = 127
    questoes = 25
    alternativas = 5

    num_candidatos = contar_candidatos(candidatos, questoes, alternativas)
    print("Número de candidatos:", num_candidatos)



def questao105():
    print("Você escolheu a Questão 105.")
    # Código da questão 105

    print("Refaça o problema anterior para a afirmação: “Pelo menos 4 candidatos responderam de modo idêntico as k primeiras questões da prova”. \n")

    def contar_candidatos(candidatos, questoes, alternativas):
        return candidatos // (alternativas**questoes) + 1
    
    candidatos = 127
    questoes = 25
    alternativas = 5

    num_candidatos = contar_candidatos(candidatos, questoes, alternativas)
    print("Número de candidatos:", num_candidatos)

def questao106():
    print("Você escolheu a Questão 106.")
    # Código da questão 106

    print("Qual é o número mínimo de pessoas que deve haver em um grupo para que possamos garantir que nele haja pelo menos 5 pessoas nascidas nomesmo mês? \n")

    def contar_pessoas(pessoas, meses):
        return pessoas // meses + 1
    
    pessoas = 60
    meses = 12

    num_pessoas = contar_pessoas(pessoas, meses)
    print("Número de pessoas:", num_pessoas)



def questao107():
    print("Você escolheu a Questão 107.")
    # Código da questão 107

    print("Usando a relação de Stifel, escreva as sete primeiras linhas do triângulo de Pascal. \n")

    def triangulo_pascal(n):
        triangulo = [[1]]
        for i in range(1, n):
            linha = [1]
            for j in range(1, i):
                linha.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
            linha.append(1)
            triangulo.append(linha)
        return triangulo
    
    n = 7
    triangulo = triangulo_pascal(n)
    for linha in triangulo:
        print(linha)
    



def questao108():
    print("Você escolheu a Questão 108.")
    # Código da questão 108

    print("Se A possui 512 subconjuntos, qual é o número de elementos de A? \n")

    def contar_elementos(subconjuntos):
        return 2**subconjuntos
    
    subconjuntos = 512
    num_elementos = contar_elementos(subconjuntos)
    print("Número de elementos de A:", num_elementos)


def questao109():
    print("Você escolheu a Questão 109.")
    # Código da questão 109

    print("Determine um conjunto que possua exatamente 48 subconjuntos. \n")

    def contar_subconjuntos(elementos):
        return 2**elementos
    
    def encontrar_conjunto(subconjuntos):
        elementos = 0
        while contar_subconjuntos(elementos) != subconjuntos:
            elementos += 1
        return elementos
    
    subconjuntos = 48
    conjunto = encontrar_conjunto(subconjuntos)
    print("Conjunto com 48 subconjuntos:", conjunto)


def questao110():
    print("Você escolheu a Questão 110.")
    # Código da questão 110

    print("Quantos coquetéis (misturas de duas ou mais bebidas) podem ser feitos a partir de 7 ingredientes distintos? \n")

    def contar_coqueteis(ingredientes):
        return 2**ingredientes - 1
    
    ingredientes = 7
    num_coqueteis = contar_coqueteis(ingredientes)
    print("Número de coquetéis:", num_coqueteis)

def questao111():
    print("Você escolheu a Questão 111.")
    # Código da questão 111

    print("Em uma sala há 7 lâmpadas. De quantos modos pode ser iluminada a sala? \n")

    def contar_modos(lâmpadas):
        return 2**lâmpadas
    
    lâmpadas = 7
    num_modos = contar_modos(lâmpadas)
    print("Número de modos:", num_modos)


def questao112():
    print("Você escolheu a Questão 112.")
    # Código da questão 112

    print("Calcule o valor da soma S = 50 * 51 + 51 * 52 + ... + 100 * 101")

    def calcular_soma(a, b):
        return sum(i * (i + 1) for i in range(a, b))
    
    a = 50
    b = 101

    soma = calcular_soma(a, b)
    print("Soma:", soma)


def questao113():
    print("Você escolheu a Questão 113.")
    # Código da questão 113

    print("Determine p para que C(p, 10) seja máximo. \n")

    def contar_permutacoes(n, k):
        return fatorial(n) // fatorial(n - k)
    
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    n = 10
    k = 10

    num_permutacoes = contar_permutacoes(n, k)
    print("Número de permutações:", num_permutacoes)

def questao114():
    print("Você escolheu a Questão 114.")
    # Código da questão 114

    print("Determine p para que C(p, 21) seja máximo. \n")

    def contar_permutacoes(n, k):
        return fatorial(n) // fatorial(n - k)
    
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    n = 21
    k = 21

    num_permutacoes = contar_permutacoes(n, k)
    print("Número de permutações:", num_permutacoes)

def questao115():
    print("Você escolheu a Questão 115.")
    # Código da questão 115

    print("Determine a soma dos coeficientes do desenvolvimento de (2x^2 - 3y)^1991 \n")

    def calcular_soma(coeficiente, expoente):
        return sum(combinacao(expoente, i) * coeficiente**(expoente - i) * (-1)**i for i in range(expoente + 1))
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    coeficiente = 2
    expoente = 1991

    soma = calcular_soma(coeficiente, expoente)
    print("Soma dos coeficientes:", soma)

def questao116():
    print("Você escolheu a Questão 116.")
    # Código da questão 116

    print("Determine o coeficiente de x^17 no desenvolvimento de (1 + x^5 + x^7)^20 \n")


    def calcular_coeficiente(coeficiente, expoente, termo):
        return combinacao(expoente, termo) * coeficiente**(expoente - termo)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    coeficiente = 1
    expoente = 20
    termo = 17

    coeficiente_x = calcular_coeficiente(coeficiente, expoente, termo)
    print("Coeficiente de x^17:", coeficiente_x)

def questao117():
    print("Você escolheu a Questão 117.")
    # Código da questão 117

    print("Determine a soma dos coeficientes do desenvolvimento de (x^3 - 3x + 1)^1822 \n ")

    def calcular_soma(coeficiente, expoente):
        return sum(combinacao(expoente, i) * coeficiente**(expoente - i) * (-3)**i for i in range(expoente + 1))
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    coeficiente = 1
    expoente = 1822

    soma = calcular_soma(coeficiente, expoente)
    print("Soma dos coeficientes:", soma)


def questao118():
    print("Você escolheu a Questão 118.")
    # Código da questão 118

    print("Quantos termos possui o desenvolvimento de (x1 + x2 + x3 + x4)^20 ? \n")

    def contar_termos(n, k):
        return combinacao(n + k - 1, k)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    n = 4
    k = 20

    num_termos = contar_termos(n, k)
    print("Número de termos:", num_termos)

def questao119():
    print("Você escolheu a Questão 119.")
    # Código da questão 119

    print("Uma caixa contém 20 peças em boas condições e 15 em más condições. Uma amostra de 10 peças é extraída. Calcular a probabilidade de que ao menos uma peça na amostra seja defeituosa. \n")

    def calcular_probabilidade(boas, más, amostra):
        return 1 - combinacao(boas, amostra) / combinacao(boas + más, amostra)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    boas = 20
    más = 15
    amostra = 10

    probabilidade = calcular_probabilidade(boas, más, amostra)
    print("Probabilidade de ao menos uma peça defeituosa:", probabilidade)



def questao120():
    print("Você escolheu a Questão 120.")
    # Código da questão 120

    print("Dez pessoas são separadas em dois grupos de 5 pessoas cada um. Qual é a probabilidade de que duas pessoas determinadas A e B façam parte do mesmo grupo? \n")

    def calcular_probabilidade(pessoas, grupo):
        return combinacao(grupo - 1, 1) * combinacao(pessoas - 2, grupo - 2) / combinacao(pessoas, grupo)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    pessoas = 10
    grupo = 5

    probabilidade = calcular_probabilidade(pessoas, grupo)
    print("Probabilidade de A e B no mesmo grupo:", probabilidade)


def questao121():
    print("Você escolheu a Questão 121.")
    # Código da questão 121

    print("Um número entre 1 e 200 é escolhido aleatoriamente. Calcular a probabilidade de que seja divisível por 5 ou por 7. \n")

    def calcular_probabilidade(n, divisores):
        return len([i for i in range(1, n + 1) if any(i % d == 0 for d in divisores)]) / n
    
    n = 200
    divisores = [5, 7]

    probabilidade = calcular_probabilidade(n, divisores)
    print("Probabilidade de ser divisível por 5 ou por 7:", probabilidade)



def questao122():
    print("Você escolheu a Questão 122.")
    # Código da questão 122

    print("Uma moeda foi cunhada de tal forma que é 4 vezes mais provável dar cara do que coroa. Calcular as probabilidades de cara e coroa. \n")

    def calcular_probabilidade(cara, coroa):
        return cara / (cara + coroa), coroa / (cara + coroa)
    
    cara = 4
    coroa = 1

    probabilidade_cara, probabilidade_coroa = calcular_probabilidade(cara, coroa)
    print("Probabilidade de cara:", probabilidade_cara)

def questao123():
    print("Você escolheu a Questão 123.")
    # Código da questão 123

    print("Aos números inteiros entre 1 e n são designadas probabilidades aos seus valores. Calcular P(i) para 1 <= i <= n")

    def calcular_probabilidade(n):
        return {i: 1 / n for i in range(1, n + 1)}
    
    n = 10

    probabilidade = calcular_probabilidade(n)
    for i, p in probabilidade.items():
        print(f"P({i}): {p}")

    

def questao124():
    print("Você escolheu a Questão 124.")
    # Código da questão 124

    print("Três dados são jogados simultaneamente. Calcular a probabilidade de obter 12 como soma dos resultados dos três dados. \n")

    def calcular_probabilidade(soma):
        resultados = set()
        for i in range(1, 7):
            for j in range(1, 7):
                for k in range(1, 7):
                    if i + j + k == soma:
                        resultados.add((i, j, k))
        return len(resultados) / 6**3
    
    soma = 12

    probabilidade = calcular_probabilidade(soma)
    print("Probabilidade de obter soma 12:", probabilidade)


def questao125():
    print("Você escolheu a Questão 125.")
    # Código da questão 125

    print("Dois dados são jogados simultaneamente. Calcular a probabilidade de obter 7 como soma dos resultados. \n")

    def calcular_probabilidade(soma):
        resultados = set()
        for i in range(1, 7):
            for j in range(1, 7):
                if i + j == soma:
                    resultados.add((i, j))
        return len(resultados) / 6**2
    
    soma = 7

    probabilidade = calcular_probabilidade(soma)
    print("Probabilidade de obter soma 7:", probabilidade)

def questao126():
    print("Você escolheu a Questão 126.")
    # Código da questão 126

    print("Escolhem-se ao acaso duas peças de um dominó. Qual é a probabilidade delas possuírem um número comum? \n")

    def calcular_probabilidade(peças):
        peças_comuns = set()
        for i in range(7):
            for j in range(i, 7):
                peças_comuns.add((i, j))
        return len(peças_comuns) / len(peças)
    
    peças = [(i, j) for i in range(7) for j in range(7)]
    probabilidade = calcular_probabilidade(peças)
    print("Probabilidade de peças com número comum:", probabilidade)



def questao127():
    print("Você escolheu a Questão 127.")
    # Código da questão 127

    print("Há 8 carros estacionados em 12 vagas em fila. \n")
    print("a) Qual é a probabilidade das vagas vazias serem consecutivas? \n")
    print("b) Qual é a probabilidade de não haver duas vagas vazias consecutivas? \n")

    def calcular_probabilidade_vagas_vazias(carros, vagas):
        return combinacao(vagas - carros, carros) / combinacao(vagas, carros)
    
    def calcular_probabilidade_vagas_ocupadas(carros, vagas):
        return 1 - combinacao(vagas - carros + 1, carros) / combinacao(vagas, carros)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    carros = 8
    vagas = 12

    probabilidade_vagas_vazias = calcular_probabilidade_vagas_vazias(carros, vagas)
    print("Probabilidade de vagas vazias consecutivas:", probabilidade_vagas_vazias)

    probabilidade_vagas_ocupadas = calcular_probabilidade_vagas_ocupadas(carros, vagas)
    print("Probabilidade de vagas ocupadas consecutivas:", probabilidade_vagas_ocupadas)


def questao128():
    print("Você escolheu a Questão 128.")
    # Código da questão 128

    print("Cinco homens e cinco mulheres sentam-se aleatoriamente em dez cadeiras em círculo. Calcule: \n")
    print("a) A probabilidade de os homens e as mulheres se sentarem em lugares alternados. \n")
    print("b) A probabilidade das mulheres se sentarem juntas. \n")

    def calcular_probabilidade_alternados(homens, mulheres, cadeiras):
        return 2 * combinacao(homens, homens) * combinacao(mulheres, mulheres) / combinacao(homens + mulheres, homens)
    
    def calcular_probabilidade_juntas(homens, mulheres, cadeiras):
        return combinacao(homens + mulheres - 1, mulheres) / combinacao(homens + mulheres, homens)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    homens = 5
    mulheres = 5

    probabilidade_alternados = calcular_probabilidade_alternados(homens, mulheres, homens + mulheres)
    print("Probabilidade de homens e mulheres alternados:", probabilidade_alternados)

    probabilidade_juntas = calcular_probabilidade_juntas(homens, mulheres, homens + mulheres)
    print("Probabilidade de mulheres juntas:", probabilidade_juntas)

def questao129():
    print("Você escolheu a Questão 129.")
    # Código da questão 129

    print("Em um grupo de 10 pessoas, quatro são sorteadas para ganhar um prêmio. Qual é a probabilidade de uma particular pessoa sorteada? \n")

    def calcular_probabilidade(pessoas, sorteadas):
        return 1 / combinacao(pessoas, sorteadas)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    pessoas = 10
    sorteadas = 4

    probabilidade = calcular_probabilidade(pessoas, sorteadas)
    print("Probabilidade de pessoa sorteada:", probabilidade)



def questao130():
    print("Você escolheu a Questão 130.")
    # Código da questão 130

    print("Doze pessoas são divididas em três grupos de 4. Qual é a probabilidade de duas determinadas pessoas ficarem no mesmo grupo? \n")

    def calcular_probabilidade(pessoas, grupo):
        return combinacao(pessoas - 2, grupo - 2) / combinacao(pessoas, grupo)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    pessoas = 12
    grupo = 4

    probabilidade = calcular_probabilidade(pessoas, grupo)
    print("Probabilidade de pessoas no mesmo grupo:", probabilidade)


def questao131():
    print("Você escolheu a Questão 131.")
    # Código da questão 131

    print("oão e Pedro lançam, cada um, um dado não tendencioso. Qual é a probabilidade do resultado de João ser maior ou igual ao resultado de Pedro? \n")

    def calcular_probabilidade(dados):
        return 1 / 2 + 1 / 6 * 1 / 6
    
    dados = 6

    probabilidade = calcular_probabilidade(dados)
    print("Probabilidade de João maior ou igual a Pedro:", probabilidade)

def questao132():
    print("Você escolheu a Questão 132.")
    # Código da questão 132

    print("Escolhe-se ao acaso um número entre 1 e 50. Se o número é primo, qual é a probabilidade de que seja ímpar? \n")

    def calcular_probabilidade(n):
        primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        ímpares = [i for i in range(1, n + 1) if i % 2 != 0]
        primos_ímpares = [i for i in primos if i in ímpares]
        return len(primos_ímpares) / len(primos)
    
    n = 50

    probabilidade = calcular_probabilidade(n)
    print("Probabilidade de primo ímpar:", probabilidade)



def questao133():
    print("Você escolheu a Questão 133.")
    # Código da questão 133

    print("Uma moeda é jogada 6 vezes. Sabendo-se que no primeiro lançamento deu coroa, calcular a probabilidade condicional de que o número de caras nos seis lançamentos supere o número de coroas. \n")

    def calcular_probabilidade(lançamentos):
        return 1 / 2**5
    
    lançamentos = 6

    probabilidade = calcular_probabilidade(lançamentos)
    print("Probabilidade condicional:", probabilidade)


def questao134():
    print("Você escolheu a Questão 134.")
    # Código da questão 134

    print("Uma moeda é jogada 4 vezes. Sabendo que o primeiro resultado foi cara, calcular a probabilidade condicional de obter pelo menos duas caras. \n")

    def calcular_probabilidade(lançamentos):
        return 1 / 2**3
    
    lançamentos = 4

    probabilidade = calcular_probabilidade(lançamentos)
    print("Probabilidade condicional:", probabilidade)


def questao135():
    print("Você escolheu a Questão 135.")
    # Código da questão 135

    print("Joguei um dado duas vezes. Calcule a probabilidade condicional de obter 3 na primeira jogada, sabendo que a soma dos resultados foi 7. \n")

    def calcular_probabilidade(lançamentos):
        return 1 / 6
    
    lançamentos = 2

    probabilidade = calcular_probabilidade(lançamentos)
    print("Probabilidade condicional:", probabilidade)

def questao136():
    print("Você escolheu a Questão 136.")
    # Código da questão 136

    print("Duas máquinas A e B produzem 3000 peças em um dia. A máquina A produz 100 peças, das quais 3% são defeituosas. A máquina B produzas restantes 2000, das quais 1% são defeituosas. Da produção total de um dia uma peça é escolhida ao acaso e, examinando-a, constata-se que é defeituosa. Qual é a probabilidade de que a peça tenha sido produzida pela máquina A? \n")

    def calcular_probabilidade(máquina, peças, defeituosas):
        return (peças[máquina] / sum(peças)) * defeituosas[máquina]
    
    máquina = 0

    peças = [100, 2000]
    defeituosas = [0.03, 0.01]

    probabilidade = calcular_probabilidade(máquina, peças, defeituosas)
    print("Probabilidade de peça defeituosa da máquina A:", probabilidade)


def questao137():
    print("Você escolheu a Questão 137.")
    # Código da questão 137

    print("Três umas I,II e III contêm respectivamente 1 bola branca e 2 pretas, 2 brancas e 1 preta e 3 brancas e 2 pretas. Uma uma é escolhida ao acaso e dela é retirada uma bola, que é branca. Qual é a probabilidade condicional de que a uma escolhida foi a I? \n")

    def calcular_probabilidade(umas, bolas, brancas):
        return (umas[0] / sum(umas)) * brancas[0]
    
    uma = 0

    umas = [1, 2, 3]
    bolas = [3, 3, 5]
    brancas = [1, 2, 3]

    probabilidade = calcular_probabilidade(umas, bolas, brancas)
    print("Probabilidade condicional de uma I:", probabilidade)




def questao138():
    print("Você escolheu a Questão 138.")
    # Código da questão 138

    print("Um estudante resolve um teste com questões do tipo verdadeiro—falso. Ele sabe dar a solução correta para 40% das questões. Quando ele responde uma questão cuja solução conhece, dá a resposta correta, e nos outros casos decide na cara ou coroa. Se uma questão foi respondida corretamente, qual é a probabilidade de que ele sabia a resposta? \n")

    def calcular_probabilidade(respostas, corretas, conhecidas):
        return (conhecidas / respostas) * corretas
    
    resposta = 1

    respostas = 1
    corretas = 1
    conhecidas = 0.4

    probabilidade = calcular_probabilidade(respostas, corretas, conhecidas)
    print("Probabilidade de resposta correta conhecida:", probabilidade)




def questao139():
    print("Você escolheu a Questão 139.")
    # Código da questão 139

    print("A probabilidade de um homem ser canhoto é 1/10. Qual é a probabilidade de, em um grupo de 10 homens, haver pelo menos um canhoto? \n")

    def calcular_probabilidade(homens, canhotos):
        return 1 - combinacao(homens - canhotos, 0) * (1 - canhotos)**homens
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    homens = 10
    canhotos = 1 / 10

    probabilidade = calcular_probabilidade(homens, canhotos)
    print("Probabilidade de pelo menos um canhoto:", probabilidade)



def questao140():
    print("Você escolheu a Questão 140.")
    # Código da questão 140

    print("Sacam-se, sucessivamente e sem reposição, duas cartas de um baralho comum (52 cartas). Calcule a probabilidade de a 1ª carta ser uma dama e a 2ª ser de copas. \n")

    def calcular_probabilidade(cartas, dama, copas):
        return (dama / cartas) * copas / (cartas - 1)
    
    carta = 1

    cartas = 52
    dama = 4
    copas = 13

    probabilidade = calcular_probabilidade(cartas, dama, copas)

    print("Probabilidade de 1ª dama e 2ª copas:", probabilidade)



def questao141():
    print("Você escolheu a Questão 141.")
    # Código da questão 141

    print("Um exame de laboratório tem eficiência de 95% para detectar uma doença quando essa doença existe de fato. Entretanto o teste aponta um resultado “falso positivo” para 1% das pessoas sadias testadas. Se 0,5% da população tem a doença, qual é a probabilidade de uma pessoa ter a doença dado que o seu exame foi positivo? \n")

    def calcular_probabilidade(população, doença, positivo):
        return (positivo / população) * doença / (positivo / população * doença + 0.01 * (1 - doença))
    
    população = 1
    doença = 0.005
    positivo = 0.95

    probabilidade = calcular_probabilidade(população, doença, positivo)
    print("Probabilidade de doença dado exame positivo:", probabilidade)


def questao142():
    print("Você escolheu a Questão 142.")
    # Código da questão 142

    print("Quantas pessoas você deve entrevistar para ter probabilidade igual ou superior a 0,5 de encontrar pelo menos um que aniversarie hoje? \n")

    def calcular_probabilidade(pessoas):
        return 1 - (364 / 365)**pessoas
    
    pessoas = 1

    probabilidade = calcular_probabilidade(pessoas)
    while probabilidade < 0.5:
        pessoas += 1
        probabilidade = calcular_probabilidade(pessoas)
    print("Número de pessoas para probabilidade 0.5:", pessoas)


def questao143():
    print("Você escolheu a Questão 143.")
    # Código da questão 143

    print("Uma uma contém 3 bolas vermelhas e 7 bolas brancas. A e B sacam altemadamente, sem reposição, bolas dessa uma até que uma bola vermelha seja retirada. A saca a Ia bola. Qual é a probabilidade de A sacar a bola vermelha? \n")

    def calcular_probabilidade(bolas, vermelhas, brancas):
        return vermelhas / bolas
    
    bola = 1

    bolas = 10
    vermelhas = 3
    brancas = 7

    probabilidade = calcular_probabilidade(bolas, vermelhas, brancas)
    print("Probabilidade de A sacar vermelha:", probabilidade)


def questao144():
    print("Você escolheu a Questão 144.")
    # Código da questão 144

    print("Quantas vezes, no mínimo, se deve lançar um dado não tendencioso para que a probabilidade de obter algum 6 seja superior a 0,9? \n")

    def calcular_probabilidade(lançamentos):
        return 1 - (5 / 6)**lançamentos
    
    lançamentos = 1

    probabilidade = calcular_probabilidade(lançamentos)
    while probabilidade < 0.9:
        lançamentos += 1
        probabilidade = calcular_probabilidade(lançamentos)

    print("Número de lançamentos para probabilidade 0.9:", lançamentos)

def questao145():
    print("Você escolheu a Questão 145.")
    # Código da questão 145

    print("Um júri de 3 pessoas tem dois jurados que decidem corretamente (cada um) com probabilidade p e um terceiro jurado que decide por cara ou coroa. As decisões são tomadas por maioria. Outro júri tem probabilidade p de tomar uma decisão correta. Qual dos júris tem maior probabilidade de acerto? \n")

    def calcular_probabilidade(p):
        return 3 * p**2 * (1 - p) + p**3
    
    p = 0.6

    probabilidade = calcular_probabilidade(p)
    print("Probabilidade do júri 1:", probabilidade)

    p = 0.6

    probabilidade = calcular_probabilidade(p)
    print("Probabilidade do júri 2:", probabilidade)

    



def questao146():
    print("Você escolheu a Questão 146.")
    # Código da questão 146

    print("Uma firma fabrica “chips” de computador. Em um lote de 1000 “chips”, uma amostra de 10 “chips” revelou 1 “chip” defeituoso. Supondo que no lote houvesse k “chips” defeituosos: \n")
    print("a) Calcule a probabilidade de em uma amostra de 20 chips haver exatamente um chip defeituoso. \n")
    print("b) Determine o valor de k. \n")

    def calcular_probabilidade(amostra, defeituosos):
        return combinacao(defeituosos, 1) * combinacao(1000 - defeituosos, 9) / combinacao(1000, 10)
    
    def calcular_defeituosos(amostra, defeituosos):
        return combinacao(defeituosos, 1) * combinacao(1000 - defeituosos, 9) / combinacao(1000, 10)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    amostra = 20
    defeituosos = 1

    probabilidade = calcular_probabilidade(amostra, defeituosos)
    print("Probabilidade de 1 defeituoso:", probabilidade)

    defeituosos = 1
    while calcular_defeituosos(amostra, defeituosos) < 0.05:
        defeituosos += 1
    print("Número de defeituosos:", defeituosos)



def questao147():
    print("Você escolheu a Questão 147.")
    # Código da questão 147

    print("Sacam-se, com reposição, 4 bolas de uma uma que contém 7 bolas brancas e 3 bolas pretas. Qual a probabilidade de serem sacadas 2 bolas de cada cor? Qual seria a resposta no caso sem reposição? \n")

    def calcular_probabilidade(bolas, brancas, pretas):
        return combinacao(brancas, 2) * combinacao(pretas, 2) / combinacao(bolas, 4)
    
    def calcular_probabilidade_sem_reposição(bolas, brancas, pretas):
        return (brancas / bolas) * ((brancas - 1) / (bolas - 1)) * (pretas / (bolas - 2)) * ((pretas - 1) / (bolas - 3))
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    bolas = 10
    brancas = 7
    pretas = 3

    probabilidade = calcular_probabilidade(bolas, brancas, pretas)
    print("Probabilidade com reposição:", probabilidade)

    probabilidade = calcular_probabilidade_sem_reposição(bolas, brancas, pretas)
    print("Probabilidade sem reposição:", probabilidade)



def questao148():
    print("Você escolheu a Questão 148.")
    # Código da questão 148

    print("Dois adversários A e B disputam uma série de 10 partidas. A probabilidade de A ganhar uma partida é 0,6 e não há empates. Qual é a probabilidade de A ganhar a série? \n")

    def calcular_probabilidade(partidas, vitórias):
        return combinacao(partidas, vitórias) * 0.6**vitórias * 0.4**(partidas - vitórias)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    partidas = 10
    vitórias = 6

    probabilidade = calcular_probabilidade(partidas, vitórias)
    print("Probabilidade de A ganhar a série:", probabilidade)



def questao149():
    print("Você escolheu a Questão 149.")
    # Código da questão 149

    print("Dois adversários A e B disputam uma série de partidas. O primeiro que obtiver 12 vitórias ganha a série. No momento o resultado é 6 x 4 a favor de A. Qual é a probabilidade de A ganhar a série sabendo que em cada partida as probabilidades de A e B vencerem são respectivamente 0,4 e 0,6? \n")

    def calcular_probabilidade(partidas, vitórias):
        return combinacao(partidas, vitórias) * 0.4**vitórias * 0.6**(partidas - vitórias)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    partidas = 12
    vitórias = 6

    probabilidade = calcular_probabilidade(partidas, vitórias)
    print("Probabilidade de A ganhar a série:", probabilidade)



def questao150():
    print("Você escolheu a Questão 150.")
    # Código da questão 150

    print("Suponha que uma característica (como a cor dos olhos, por exemplo) dependa de um par de genes. Representemos por A um gene dominante e por a um gene recessivo. Assim um indivíduo com genes A A é dominante puro, um com genes aa é um recessivo puro e um com genes Aa é um híbrido. Dominantes puros e híbridos são semelhantes em relação à característica. Filhos recebem um gene do pai e um da mãe. Suponha que pai e mãe sejam híbridos e tenham 4 filhos. \n")

    print("a) Qual é a probabilidade do primeiro filho ser um recessivo puro? \n")
    print("b) Qual é a probabilidade de exatamente um dos 4 filhos ser um recessivo puro? \n")

    def calcular_probabilidade(filhos, recessivos):
        return combinacao(filhos, recessivos) * 0.25**recessivos * 0.75**(filhos - recessivos)
    
    def combinacao(n, k):
        if 0 <= k <= n:
            num = 1
            den = 1
            for i in range(1, min(k, n - k) + 1):
                num *= n
                den *= i
                n -= 1
            return num // den
        else:
            return 0
        
    filhos = 4
    recessivos = 1

    probabilidade = calcular_probabilidade(filhos, recessivos)
    print("Probabilidade de 1 recessivo puro:", probabilidade)

    recessivos = 1

    probabilidade = calcular_probabilidade(filhos, recessivos)
    print("Probabilidade de 1 recessivo puro:", probabilidade)



def questao151():
    print("Você escolheu a Questão 151.")
    # Código da questão 151

    print("Lança-se repetidamente um par de dados não tendenciosos. Qual é a probabilidade de obtermos duas somas iguais a 7 antes de obtermos três somas iguais a 3? \n")

    def calcular_probabilidade(somas):
        return 1 - (5 / 36)**somas
    
    somas = 1

    probabilidade = calcular_probabilidade(somas)
    while probabilidade < 0.5:
        somas += 1
        probabilidade = calcular_probabilidade(somas)

    print("Número de somas para probabilidade 0.5:", somas)



def questao152():
    print("Você escolheu a Questão 152.")
    # Código da questão 152

    print("Uma moeda tem probabilidade 0,4 de dar cara. Lançando-a 12 vezes qual o mais possível valor do número de caras obtidas? \n")

    def calcular_probabilidade(lançamentos):
        return 0.4 * lançamentos
    
    lançamentos = 12

    probabilidade = calcular_probabilidade(lançamentos)
    print("Número de caras mais provável:", probabilidade)



def questao153():

    print("Daqui pra frente as questões serão do livro do barbetta. \n")

    print("Você escolheu a Questão 153.")
    # Código da questão 153

    Dados = [7, 8, 6, 5, 9, 4]

    # Cálculo da média
    Soma = 0
    for Loop in Dados:
        Soma += Loop
        
    Media = Soma / len(Dados)

    # Cálculo da variância
    SomaVariancia = 0
    for Loop in Dados:
        SomaVariancia += math.pow((Loop - Media), 2)

    print(f'A soma total foi de {Soma} resultando em uma média de {Media}')

    Variancia = (SomaVariancia / (len(Dados) - 1))
    print(f'A soma dos quadrados da variância foi de {SomaVariancia} resultando em uma variância de {Variancia}')

    # Desvio Padrão
    print(f'E o desvio padrão foi de {math.sqrt(Variancia):.2f}')

def questao154():
    print("Você escolheu a Questão 154.")
    # Código da questão 154

    # Valores reais de pressão sanguínea (mmHg)
    pressao_sanguinea = [118.6, 127.4, 138.4, 130.0, 113.7, 122.0, 108.3, 131.5, 133.2]
    
    # a. Mediana dos valores
    pressao_ordenada = sorted(pressao_sanguinea)
    n = len(pressao_ordenada)
    
    if n % 2 == 1:
        mediana = pressao_ordenada[n // 2]
    else:
        mediana = (pressao_ordenada[n // 2 - 1] + pressao_ordenada[n // 2]) / 2
    print(f"Mediana da pressão sanguínea: {mediana:.1f} mmHg")
    
    # b. Efeito de mudar o valor do segundo indivíduo
    pressao_sanguinea[1] = 127.6  # Mudança do segundo valor
    pressao_ordenada = sorted(pressao_sanguinea)
    if n % 2 == 1:
        nova_mediana = pressao_ordenada[n // 2]
    else:
        nova_mediana = (pressao_ordenada[n // 2 - 1] + pressao_ordenada[n // 2]) / 2
    print(f"Nova mediana após alteração: {nova_mediana:.1f} mmHg (mediana não alterada)")


def questao155():
    print("Você escolheu a Questão 155.")
    # Código da questão 155

    # Tempos de propagação (horas de voo/10^4)
    tempos = [0.736, 0.863, 0.865, 0.913, 0.915, 0.937, 0.983, 1.007, 1.011, 1.064, 
              1.109, 1.132, 1.140, 1.153, 1.253, 1.394]
    
    # a. Média amostral
    n = len(tempos)
    media_amostral = sum(tempos) / n
    print(f"Média amostral: {media_amostral:.3f}")
    
    # a. Mediana amostral
    tempos_ordenados = sorted(tempos)
    if n % 2 == 1:
        mediana = tempos_ordenados[n // 2]
    else:
        mediana = (tempos_ordenados[n // 2 - 1] + tempos_ordenados[n // 2]) / 2
    print(f"Mediana amostral: {mediana:.3f}")
    
    # Comparação média e mediana
    print(f"A média ({media_amostral:.3f}) é maior do que a mediana ({mediana:.3f}), indicando uma assimetria à direita.")
    
    # b. Até quanto a maior observação pode ser diminuída sem afetar a mediana
    maior_observacao = max(tempos)
    print(f"A maior observação ({maior_observacao:.3f}) pode ser diminuída até {tempos_ordenados[-2]:.3f} sem afetar a mediana.")


def questao156():
    print("Você escolheu a Questão 156.")
    # Código da questão 156

    # Consumo de oxigênio (mL/kg/min)
    oxigenio = [29.5, 49.3, 30.6, 28.2, 28.0, 26.3, 33.9, 29.4, 23.5, 31.6]
    
    # a. Amplitude amostral
    amplitude = max(oxigenio) - min(oxigenio)
    print(f"Amplitude amostral: {amplitude:.1f}")

    # b. Variância amostral
    n = len(oxigenio)
    media = sum(oxigenio) / n
    soma_quadrados = sum((x - media) ** 2 for x in oxigenio)
    variancia = soma_quadrados / (n - 1)
    print(f"Variância amostral: {variancia:.2f}")

    # c. Desvio padrão amostral
    desvio_padrao = variancia ** 0.5
    print(f"Desvio padrão amostral: {desvio_padrao:.2f}")
    
    # d. Método alternativo para variância
    soma_x_quadrado = sum(x ** 2 for x in oxigenio)
    soma_x = sum(oxigenio)
    variancia_alternativa = (soma_x_quadrado - (soma_x ** 2) / n) / (n - 1)
    print(f"Variância amostral (método alternativo): {variancia_alternativa:.2f}")



def questao157():
    print("Você escolheu a Questão 157.")
    # Código da questão 157

    # Módulo de Young (GPa)
    young = [116.4, 115.9, 114.6, 115.2, 115.8]

    # a. Média amostral
    media_amostral = sum(young) / len(young)
    print(f"Média amostral: {media_amostral:.2f} GPa")

    # b. Variância amostral
    soma_quadrados = sum((x - media_amostral) ** 2 for x in young)
    variancia = soma_quadrados / (len(young) - 1)
    print(f"Variância amostral: {variancia:.2f} GPa²")

    # c. Método alternativo para calcular variância
    soma_x_quadrado = sum(x ** 2 for x in young)
    soma_x = sum(young)
    variancia_alternativa = (soma_x_quadrado - (soma_x ** 2) / len(young)) / (len(young) - 1)
    print(f"Variância amostral (método alternativo): {variancia_alternativa:.2f} GPa²")

    # d. Comparação após subtração de 100
    young_subtracao = [x - 100 for x in young]
    media_subtracao = sum(young_subtracao) / len(young_subtracao)
    soma_quadrados_subtracao = sum((x - media_subtracao) ** 2 for x in young_subtracao)
    variancia_subtracao = soma_quadrados_subtracao / (len(young_subtracao) - 1)
    print(f"Variância após subtração de 100: {variancia_subtracao:.2f} GPa²")



def questao158():
    print("Você escolheu a Questão 158.")
    # Código da questão 158

    # Viscosidade estabilizada (cP)
    viscosidade = [2781, 2900, 3013, 2856, 2888]

    # a. Média e mediana
    media = sum(viscosidade) / len(viscosidade)
    viscosidade_ordenada = sorted(viscosidade)
    mediana = viscosidade_ordenada[len(viscosidade) // 2]
    print(f"Média amostral: {media:.1f} cP")
    print(f"Mediana amostral: {mediana:.1f} cP")


def questao159():
    print("Você escolheu a Questão 159.")
    # Código da questão 159

    # Resistência à ruptura (MPa)
    resistencia = [87, 93, 96, 98, 105, 114, 128, 131, 142, 168]

    # a. Mediana e média amostral
    resistencia_ordenada = sorted(resistencia)
    n = len(resistencia_ordenada)
    if n % 2 == 1:
        mediana = resistencia_ordenada[n // 2]
    else:
        mediana = (resistencia_ordenada[n // 2 - 1] + resistencia_ordenada[n // 2]) / 2
    media = sum(resistencia) / n
    print(f"Mediana amostral: {mediana} MPa")
    print(f"Média amostral: {media:.1f} MPa")

    # b. Desvio padrão amostral
    soma_quadrados = sum((x - media) ** 2 for x in resistencia)
    variancia = soma_quadrados / (n - 1)
    desvio_padrao = variancia ** 0.5
    print(f"Desvio padrão amostral: {desvio_padrao:.1f} MPa")



def questao160():
    print("Você escolheu a Questão 160.")
    # Código da questão 160

     # Tempo de oxidação-indução (min)
    oxidacao = [87, 103, 130, 160, 180, 195, 132, 145, 211, 105, 145, 153, 152, 138, 87, 99, 93, 119, 129]

    # a. Variância e desvio padrão
    n = len(oxidacao)
    media = sum(oxidacao) / n
    soma_quadrados = sum((x - media) ** 2 for x in oxidacao)
    variancia = soma_quadrados / (n - 1)
    desvio_padrao = variancia ** 0.5
    print(f"Variância amostral: {variancia:.2f} min²")
    print(f"Desvio padrão amostral: {desvio_padrao:.2f} min")

    # b. Variância e desvio padrão em horas
    variancia_horas = (desvio_padrao / 60) ** 2
    desvio_padrao_horas = desvio_padrao / 60
    print(f"Variância amostral em horas: {variancia_horas:.4f} horas²")
    print(f"Desvio padrão amostral em horas: {desvio_padrao_horas:.4f} horas")



def questao161():
    print("Você escolheu a Questão 161.")
    # Código da questão 161

    # Desvios fornecidos
    desvios = [0.3, 0.9, 1.0, 1.3]
    
    # a. Calcular o quinto desvio
    d5 = -(sum(desvios))
    print(f"Quinto desvio: {d5:.1f}")
    
    # b. Amostra que gera esses desvios
    amostra = [4.7, 5.3, 5.4, 5.7, 2.2]
    media_amostral = sum(amostra) / len(amostra)
    
    desvios_calculados = [x - media_amostral for x in amostra]
    print(f"Desvios calculados: {desvios_calculados}")
    print(f"Amostra: {amostra}")
    print(f"Média amostral: {media_amostral:.2f}")

def questao162():
    print("Você escolheu a Questão 162.")
    # Código da questão 162

    # a. Nível de confiança correspondente
    z_a_2_a = 2.81
    confianca_a = 99.5
    print(f"Valor crítico z: {z_a_2_a}, Nível de confiança: {confianca_a:.1f}%")

    # b. Nível de confiança para z = 1.44
    z_a_2_b = 1.44
    confianca_b = 85
    print(f"Valor crítico z: {z_a_2_b}, Nível de confiança: {confianca_b}%")

    # c. z para 99,7% de confiança
    confianca_c = 99.7
    z_a_2_c = 3.00
    print(f"Nível de confiança: {confianca_c}%, Valor crítico z: {z_a_2_c}")

    # d. z para 75% de confiança
    confianca_d = 75
    z_a_2_d = 1.15
    print(f"Nível de confiança: {confianca_d}%, Valor crítico z: {z_a_2_d}")

def questao163():
    print("Você escolheu a Questão 163.")
    # Código da questão 163

    # Intervalos fornecidos
    intervalo1 = (114.4, 115.6)
    intervalo2 = (114.1, 115.9)

    # a. Média amostral
    media_amostral = (intervalo1[0] + intervalo1[1]) / 2
    print(f"Média amostral: {media_amostral} Hz")

    # b. Identificar o nível de confiança
    print("O intervalo mais estreito é o (114.4, 115.6), que corresponde ao nível de confiança de 90%.")


def questao164():
    print("Você escolheu a Questão 164.")
    # Código da questão 164

    # Parâmetros
    x_barra = 498
    sigma = 5
    n = 40
    z_a_2 = 1.96  # 95% de confiança

    # a. Calcular intervalo de confiança
    erro_padrao = sigma / (n ** 0.5)
    margem_erro = z_a_2 * erro_padrao
    intervalo_conf = (x_barra - margem_erro, x_barra + margem_erro)
    print(f"Intervalo de confiança de 95%: {intervalo_conf}")

    # b. Intervalo com n=100
    n2 = 100
    erro_padrao_novo = sigma / (n2 ** 0.5)
    margem_erro_novo = z_a_2 * erro_padrao_novo
    intervalo_conf_novo = (x_barra - margem_erro_novo, x_barra + margem_erro_novo)
    print(f"Novo intervalo com n=100: {intervalo_conf_novo}")

def questao165():
    print("Você escolheu a Questão 165.")
    # Código da questão 165

     # a. Calcular IC de 95% para 20 espécimes
    x_barra = 4.85
    sigma = 0.75
    n = 20
    z_a_2 = 1.96  # 95% de confiança

    erro_padrao = sigma / (n ** 0.5)
    margem_erro = z_a_2 * erro_padrao
    intervalo_conf = (x_barra - margem_erro, x_barra + margem_erro)
    print(f"Intervalo de confiança de 95%: {intervalo_conf}")

    # b. IC de 98% para 16 espécimes
    x_barra2 = 4.56
    n2 = 16
    z_a_2_novo = 2.33  # 98% de confiança

    erro_padrao_novo = sigma / (n2 ** 0.5)
    margem_erro_novo = z_a_2_novo * erro_padrao_novo
    intervalo_conf_novo = (x_barra2 - margem_erro_novo, x_barra2 + margem_erro_novo)
    print(f"Intervalo de confiança de 98%: {intervalo_conf_novo}")

    # c. Tamanho da amostra para IC de 95% com amplitude 0,40
    amplitude = 0.40
    n_requerido = ((z_a_2 * sigma) / (amplitude / 2)) ** 2
    print(f"Tamanho da amostra necessário: {n_requerido:.0f}")

    # d. Tamanho da amostra para 99% de confiança com amplitude 0,2
    z_a_2_conf99 = 2.576  # 99% de confiança
    amplitude2 = 0.2
    n_requerido2 = ((z_a_2_conf99 * sigma) / (amplitude2 / 2)) ** 2
    print(f"Tamanho da amostra necessário para 99% de confiança: {n_requerido2:.0f}")



def questao166():
    print("Você escolheu a Questão 166.")
    # Código da questão 166

    # a. Intervalo de confiança de 90% para ponto de escoamento médio
    x_barra = 8439
    sigma = 100
    n = 25
    z_a_2 = 1.645  # 90% de confiança

    erro_padrao = sigma / (n ** 0.5)
    margem_erro = z_a_2 * erro_padrao
    intervalo_conf = (x_barra - margem_erro, x_barra + margem_erro)
    print(f"Intervalo de confiança de 90%: {intervalo_conf}")

    # b. Intervalo de confiança de 92%
    z_a_2_92 = 1.75  # 92% de confiança
    margem_erro_92 = z_a_2_92 * erro_padrao
    intervalo_conf_92 = (x_barra - margem_erro_92, x_barra + margem_erro_92)
    print(f"Intervalo de confiança de 92%: {intervalo_conf_92}")

def questao167():
    print("Você escolheu a Questão 167.")
    # Código da questão 167

    # a. Intervalo de confiança de 90% para ponto de escoamento médio
    x_barra = 8439
    sigma = 100
    n = 25
    z_90 = 1.645

    erro_padrao = sigma / (n ** 0.5)
    margem_erro = z_90 * erro_padrao
    intervalo_conf = (x_barra - margem_erro, x_barra + margem_erro)
    print(f"IC de 90%: {intervalo_conf}")

    # b. Intervalo de confiança de 92%
    z_92 = 1.75
    margem_erro_92 = z_92 * erro_padrao
    intervalo_conf_92 = (x_barra - margem_erro_92, x_barra + margem_erro_92)
    print(f"IC de 92%: {intervalo_conf_92}")



def questao168():
    print("Você escolheu a Questão 168.")
    # Código da questão 168

    # a. Intervalo de confiança de 99% para a duração média do eco do radar
    x_barra = 0.81
    s = 0.34
    n = 110
    z_99 = 2.576

    erro_padrao = s / (n ** 0.5)
    margem_erro = z_99 * erro_padrao
    intervalo_conf = (x_barra - margem_erro, x_barra + margem_erro)
    print(f"IC de 99%: {intervalo_conf}")



def questao169():
    print("Você escolheu a Questão 169.")
    # Código da questão 169

    # a. Intervalo de confiança de 95% para a densidade da camada colorida média real
    x_barra = 1.028
    s = 0.163
    n = 69
    z_95 = 1.96

    erro_padrao = s / (n ** 0.5)
    margem_erro = z_95 * erro_padrao
    intervalo_conf = (x_barra - margem_erro, x_barra + margem_erro)
    print(f"IC de 95%: {intervalo_conf}")

    # b. Tamanho da amostra necessário para amplitude de 0,05
    amplitude = 0.05
    n_requerido = ((z_95 * 0.16) / (amplitude / 2)) ** 2
    print(f"Tamanho da amostra necessário: {n_requerido:.0f}")



def questao170():
    print("Você escolheu a Questão 170.")
    # Código da questão 170

    # a. Intervalo de confiança de 95% para a resistência à fratura média real
    x_barra = 89.10
    s = 3.73
    n = 169
    z_95 = 1.96

    erro_padrao = s / (n ** 0.5)
    margem_erro = z_95 * erro_padrao
    intervalo_conf = (x_barra - margem_erro, x_barra + margem_erro)
    print(f"IC de 95%: {intervalo_conf}")

    # b. Tamanho da amostra necessário para amplitude de 0,5 MPa
    amplitude = 0.5
    n_requerido = ((z_95 * 4) / (amplitude / 2)) ** 2
    print(f"Tamanho da amostra necessário: {n_requerido:.0f}")

def questao171():
    print("Você escolheu a Questão 171.")
    # Código da questão 171

    # Dados
    n = 356
    aprovados = 201
    p_hat = aprovados / n
    z_95 = 1.96

    # Cálculo do intervalo de confiança
    erro_padrao = math.sqrt(p_hat * (1 - p_hat) / n)
    margem_erro = z_95 * erro_padrao
    intervalo_conf = (p_hat - margem_erro, p_hat + margem_erro)
    print(f"IC de 95%: {intervalo_conf}")

def questao172():
    print("Você escolheu a Questão 172.")
    # Código da questão 172

    # Dados
    n = 4722
    p_hat = 0.15
    z_99 = 2.576

    # Cálculo do intervalo de confiança
    erro_padrao = math.sqrt(p_hat * (1 - p_hat) / n)
    margem_erro = z_99 * erro_padrao
    intervalo_conf = (p_hat - margem_erro, p_hat + margem_erro)
    print(f"IC de 99%: {intervalo_conf}")

def questao173():
    print("Você escolheu a Questão 173.")
    # Código da questão 173

    # Dados
    n = 539
    armas = 133
    p_hat = armas / n
    z_95 = 1.645

    # Cálculo do limite inferior do intervalo de confiança
    erro_padrao = math.sqrt(p_hat * (1 - p_hat) / n)
    limite_inferior = p_hat - z_95 * erro_padrao
    print(f"Limite inferior IC de 95%: {limite_inferior}")

def questao174():
    print("Você escolheu a Questão 174.")
    # Código da questão 174

    # Dados
    n = 487
    p_hat = 0.072
    z_99 = 2.576

    # Cálculo do limite superior do intervalo de confiança
    erro_padrao = math.sqrt(p_hat * (1 - p_hat) / n)
    limite_superior = p_hat + z_99 * erro_padrao
    print(f"Limite superior IC de 99%: {limite_superior}")

def questao175():
    print("Você escolheu a Questão 175.")
    # Código da questão 175

    # Dados
    x_barra = 30.2
    s = 3.1
    n = 8
    t_95 = 2.364

    # Cálculo do intervalo de confiança
    erro_padrao = s / math.sqrt(n)
    margem_erro = t_95 * erro_padrao
    intervalo_conf = (x_barra - margem_erro, x_barra + margem_erro)
    print(f"IC de 95%: {intervalo_conf}")

def questao176():
    print("Você escolheu a Questão 176.")
    # Código da questão 176

    # Dados
    n = 9
    s = 2.81
    chi2_025 = 2.180
    chi2_975 = 17.534

    # Cálculo do intervalo de confiança para a variância
    var_min = (n - 1) * s**2 / chi2_975
    var_max = (n - 1) * s**2 / chi2_025
    intervalo_var = (var_min, var_max)
    print(f"IC de 95% para a variância: {intervalo_var}")

    # Cálculo do intervalo de confiança para o desvio padrão
    intervalo_sd = (math.sqrt(var_min), math.sqrt(var_max))
    print(f"IC de 95% para o desvio padrão: {intervalo_sd}")

def questao177():
    print("Você escolheu a Questão 177.")
    # Código da questão 177
    
    # Dados
    n = 22
    s = 4.97
    chi2_005 = 40.289
    chi2_995 = 8.897

    # Cálculo do intervalo de confiança para o desvio padrão
    sd_min = math.sqrt((n - 1) * s**2 / chi2_005)
    sd_max = math.sqrt((n - 1) * s**2 / chi2_995)
    intervalo_sd = (sd_min, sd_max)
    print(f"IC de 99% para o desvio padrão: {intervalo_sd}")

def questao178():
    print("Você escolheu a Questão 178.")
    # Código da questão 178

    # Dados
    n = 15
    s = 1.56
    chi2_025 = 26.119

    # Cálculo do limite superior do intervalo de confiança para o desvio padrão
    sd_max = math.sqrt((n - 1) * s**2 / chi2_025)
    print(f"Limite superior IC de 95% para o desvio padrão: {sd_max}")



def questao179():
    print("Você escolheu a Questão 179.")
    # Código da questão 179

    # Dados
    x_barra = 188.0  # média
    s = 7.2  # desvio padrão
    n = 9  # tamanho da amostra
    t_alpha_2 = 2.896  # valor t de Student para 98% e 8 graus de liberdade

    # Cálculo do intervalo de confiança para a média
    erro_padrao = s / math.sqrt(n)
    intervalo_min = x_barra - t_alpha_2 * erro_padrao
    intervalo_max = x_barra + t_alpha_2 * erro_padrao
    intervalo_ic = (intervalo_min, intervalo_max)
    print(f"IC de 98% para o índice cardíaco médio real: {intervalo_ic}")


def questao180():
    print("Você escolheu a Questão 180.")
    # Código da questão 180

    # Dados
    dados = [23.5, 31.5, 34.0, 46.7, 45.6, 32.5, 41.4, 37.2, 42.5, 46.9, 51.5, 36.4, 
             44.5, 35.7, 33.5, 39.3, 22.0, 51.2]
    n = len(dados)
    media = sum(dados) / n
    s = math.sqrt(sum((x - media)**2 for x in dados) / (n - 1))
    t_alpha_2 = 2.566  # valor t de Student para 98% e 17 graus de liberdade

    # Cálculo do intervalo de confiança para a média
    erro_padrao = s / math.sqrt(n)
    intervalo_min = media - t_alpha_2 * erro_padrao
    intervalo_max = media + t_alpha_2 * erro_padrao
    intervalo_ic = (intervalo_min, intervalo_max)
    print(f"IC de 98% para a saturação de gás residual: {intervalo_ic}")


def questao181():
    print("Você escolheu a Questão 181.")
    # Código da questão 181

    # Parte (a) - Proporção Amostral de Sucessos
    x = 7  # Sucessos
    n = 10  # Total de observações
    p_hat = x / n  # Proporção amostral
    print(f"(a) Proporção amostral de sucessos: {p_hat:.2f}")

    # Parte (b) - Cálculo de média amostral (substituindo S por 1 e F por 0)
    amostra_codificada = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1]
    media_amostral = sum(amostra_codificada) / len(amostra_codificada)
    print(f"(b) Média amostral: {media_amostral:.2f}")

    # Parte (c) - Inclusão de mais 15 carros
    n_novo = 25  # Novo total de observações
    p_desejado = 0.8  # Proporção desejada
    x_novo = p_desejado * n_novo  # Número total de sucessos desejado
    x_adicional = int(x_novo - x)  # Sucessos adicionais necessários
    print(f"(c) Sucessos adicionais necessários: {x_adicional}")

def questao182():
    print("Você escolheu a Questão 182.")
    # Código da questão 182

    # Dados fornecidos para a amostra
    x = [2.75, 2.62, 2.74, 3.85, 2.34, 2.74, 7.93, 3.41, 3.88, 4.33, 3.46, 4.52, 4.23, 3.65, 2.76, 3.15]

    # (a) Soma dos valores da amostra e dos quadrados dos valores
    soma_x = sum(x)
    soma_x2 = sum([i ** 2 for i in x])

    print(f"Soma dos valores da amostra (∑x_i): {soma_x:.2f}")
    print(f"Soma dos quadrados dos valores da amostra (∑x_i^2): {soma_x2:.4f}")

    # (b) Variância e desvio padrão amostral
    n = len(x)
    variancia = (soma_x2 - (soma_x ** 2) / n) / (n - 1)
    desvio_padrao = math.sqrt(variancia)

    print(f"Variância amostral (s²): {variancia:.4f}")
    print(f"Desvio padrão amostral (s): {desvio_padrao:.4f}")

def questao183():
    print("Você escolheu a Questão 183.")
    # Código da questão 183

    # Dados fornecidos
    dados = [48, 79, 100, 35, 92, 86, 57, 100, 17, 29]
    dados_ordenados = sorted(dados)

    # (a) Mediana amostral
    n = len(dados_ordenados)
    mediana = (dados_ordenados[n // 2 - 1] + dados_ordenados[n // 2]) / 2 if n % 2 == 0 else dados_ordenados[n // 2]

    print(f"Mediana amostral: {mediana}")

    # (b) Média amostral mínima (assumindo censura à direita como 100 horas)
    media_minima = sum(dados) / len(dados)

    print(f"Média amostral mínima: {media_minima:.2f}")

    # (c) Média aparada de 10% (remoção de 10% das observações extremas)
    dados_aparados = dados_ordenados[1:-1]  # Removendo o menor e o maior valor
    media_aparada = sum(dados_aparados) / len(dados_aparados)

    print(f"Média aparada de 10%: {media_aparada:.2f}")

def questao184():
    print("Você escolheu a Questão 184.")
    # Código da questão 184

    # Dados fornecidos
    x = [2.75, 2.62, 2.74, 3.85, 2.34, 2.74, 3.93, 4.21, 3.88, 4.33, 3.46, 4.52, 2.43, 3.65, 2.78, 3.56]

    # (a) Soma dos valores e dos quadrados
    soma_x = sum(x)
    soma_x2 = sum([i ** 2 for i in x])

    print(f"Soma dos valores da amostra (∑x_i): {soma_x:.2f}")
    print(f"Soma dos quadrados dos valores (∑x_i^2): {soma_x2:.4f}")

    # (b) Variância e desvio padrão amostral
    n = len(x)
    variancia = (soma_x2 - (soma_x ** 2) / n) / (n - 1)
    desvio_padrao = math.sqrt(variancia)

    print(f"Variância amostral (s²): {variancia:.4f}")
    print(f"Desvio padrão amostral (s): {desvio_padrao:.4f}")

def questao185():
    print("Você escolheu a Questão 185.")
    # Código da questão 185

    # Dados fornecidos
    uniformidade_125 = [2.6, 2.7, 3.0, 3.2, 3.8, 4.6]
    uniformidade_160 = [3.6, 4.2, 4.2, 4.6, 4.9, 5.0]
    uniformidade_200 = [2.9, 3.4, 3.5, 4.1, 4.6, 5.1]

    def calc_media_variancia_amplitude(dados):
        n = len(dados)
        media = sum(dados) / n
        variancia = sum((x - media) ** 2 for x in dados) / (n - 1)
        amplitude = max(dados) - min(dados)
        return media, variancia, amplitude

    # Valores descritivos para cada vazão
    media_125, variancia_125, amplitude_125 = calc_media_variancia_amplitude(uniformidade_125)
    media_160, variancia_160, amplitude_160 = calc_media_variancia_amplitude(uniformidade_160)
    media_200, variancia_200, amplitude_200 = calc_media_variancia_amplitude(uniformidade_200)

    print(f"Vazão 125 SCCM -> Média: {media_125:.2f}, Variância: {variancia_125:.2f}, Amplitude: {amplitude_125:.2f}")
    print(f"Vazão 160 SCCM -> Média: {media_160:.2f}, Variância: {variancia_160:.2f}, Amplitude: {amplitude_160:.2f}")
    print(f"Vazão 200 SCCM -> Média: {media_200:.2f}, Variância: {variancia_200:.2f}, Amplitude: {amplitude_200:.2f}")


def questao186():
    print("Você escolheu a Questão 186.")
    # Código da questão 186

    # Dados fornecidos
    x_bar = 76831  # Média amostral
    s = 180  # Desvio padrão amostral
    n = 4  # Número de espécimes

    # Calculando os valores das observações da metade da amostra
    # Para n = 4, as observações da metade da amostra são:
    # Observações: x1, x2, x3, x4 (ordenadas)
    # Onde: x2 = x_bar - s e x3 = x_bar + s para uma amostra normalizada

    x2 = x_bar - s
    x3 = x_bar + s

    print(f"Observações da metade da amostra:")
    print(f"Primeira observação (x2): {x2:.2f}")
    print(f"Segunda observação (x3): {x3:.2f}")

def questao187():
    print("Você escolheu a Questão 187.")
    # Código da questão 187

    # (a) Relações entre médias e variâncias
    print("Se y_i = a x_i + b, então:")
    print("1. Média: bar_y = a * bar_x + b")
    print("2. Variância: s_y^2 = a^2 * s_x^2")
    
    # (b) Conversão de Celsius para Fahrenheit
    media_c = 87.3
    desvio_padrao_c = 1.04

    media_f = (9/5) * media_c + 32
    desvio_padrao_f = (9/5) * desvio_padrao_c

    print(f"Média em Fahrenheit: {media_f:.2f}°F")
    print(f"Desvio padrão em Fahrenheit: {desvio_padrao_f:.3f}°F")

def questao188():
    print("Você escolheu a Questão 188.")
    # Código da questão 188

    n = 1000
    p = 0.95
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))

    print(f"Média esperada: {mu}")
    print(f"Desvio padrão: {sigma}")

    # Probabilidade usando a aproximação normal
    def normal_cdf(z):
        return (1.0 + math.erf(z / math.sqrt(2.0))) / 2.0

    def z_score(x, mu, sigma):
        return (x - mu) / sigma

    z1 = z_score(940, mu, sigma)
    z2 = z_score(960, mu, sigma)
    probabilidade = normal_cdf(z2) - normal_cdf(z1)

    print(f"Probabilidade de que o número de intervalos que capturam θ esteja entre 940 e 960: {probabilidade:.3f}")


def questao189():
    print("Você escolheu a Questão 189.")
    # Código da questão 189

    media = 0.81
    desvio_padrao = 0.34
    n = 110
    nivel_confianca = 0.99
    z_alpha2 = 2.576

    erro_padrao = desvio_padrao / math.sqrt(n)
    intervalo_inferior = media - z_alpha2 * erro_padrao
    intervalo_superior = media + z_alpha2 * erro_padrao

    print(f"Intervalo de Confiança de 99%: [{intervalo_inferior:.4f}, {intervalo_superior:.4f}]")
    print(f"Interpretação: Estamos 99% confiantes de que a duração média real do eco do radar está entre {intervalo_inferior:.4f} segundos e {intervalo_superior:.4f} segundos.")


def questao190():
    print("Você escolheu a Questão 190.")
    # Código da questão 190

    media = 1.028
    desvio_padrao = 0.163
    n = 69
    nivel_confianca = 0.95
    t_alpha2 = 2.000

    erro_padrao = desvio_padrao / math.sqrt(n)
    intervalo_inferior = media - t_alpha2 * erro_padrao
    intervalo_superior = media + t_alpha2 * erro_padrao

    print(f"Intervalo de Confiança de 95%: [{intervalo_inferior:.4f}, {intervalo_superior:.4f}]")
    print(f"Interpretação: Estamos 95% confiantes de que a densidade média real da camada colorida está entre {intervalo_inferior:.4f} e {intervalo_superior:.4f}.")

    # Cálculo do tamanho da amostra necessário
    amplitude_desejada = 0.05
    z_alpha2 = 1.96
    s = 0.16

    n_necessario = (z_alpha2 * s / (amplitude_desejada / 2)) ** 2
    print(f"Tamanho da amostra necessário: {math.ceil(n_necessario)}")


def questao191():
    print("Você escolheu a Questão 191.")
    # Código da questão 191

    media = 89.10
    desvio_padrao = 3.73
    n = 169
    nivel_confianca = 0.95
    z_alpha2 = 1.96

    erro_padrao = desvio_padrao / math.sqrt(n)
    intervalo_inferior = media - z_alpha2 * erro_padrao
    intervalo_superior = media + z_alpha2 * erro_padrao

    print(f"Intervalo de Confiança de 95%: [{intervalo_inferior:.2f}, {intervalo_superior:.2f}]")
    print(f"Interpretação: Estamos 95% confiantes de que a resistência à fratura média real está entre {intervalo_inferior:.2f} MPa e {intervalo_superior:.2f} MPa.")


def questao192():
    print("Você escolheu a Questão 192.")
    # Código da questão 192

    amostra = [7, 8, 6, 5, 9, 4]
    media = sum(amostra) / len(amostra)
    
    variancia = sum((x - media) ** 2 for x in amostra) / (len(amostra) - 1)
    desvio_padrao = math.sqrt(variancia)
    
    print(f"a) A média é: {media}")
    print(f"b) A variância é: {variancia}")
    print(f"c) O desvio padrão é: {desvio_padrao}")


def questao193():
    print("Você escolheu a Questão 193.")
    # Código da questão 193

    # Valores do exemplo 2.4 (supostos para o exemplo)
    n1, n2 = 10, 12  # Tamanhos das amostras dos grupos
    s1, s2 = 4.0, 5.0  # Variâncias dentro de cada grupo
    x1, x2 = 20, 25  # Médias de cada grupo
    x_barra = (n1 * x1 + n2 * x2) / (n1 + n2)  # Média geral
    k = 2  # Número de grupos
    
    # Calculando a variância agregada
    variancia_agregada = ((n1 - 1) * s1**2 + (n2 - 1) * s2**2 + n1 * (x1 - x_barra)**2 + n2 * (x2 - x_barra)**2) / (n1 + n2 - k)
    
    # Calculando os graus de liberdade
    graus_de_liberdade = n1 + n2 - k
    
    print(f"A variância agregada é: {variancia_agregada}")
    print(f"Os graus de liberdade associados são: {graus_de_liberdade}")

def questao194():
    print("Você escolheu a Questão 194.")
    # Código da questão 194

    amostra = [7, 8, 6, 10, 5, 9, 4, 12, 7, 8]
    media = sum(amostra) / len(amostra)
    
    variancia = sum((x - media) ** 2 for x in amostra) / (len(amostra) - 1)
    desvio_padrao = math.sqrt(variancia)
    
    print(f"a) A média é: {media}")
    print(f"b) O desvio padrão é: {desvio_padrao}")

def questao195():
    print("Você escolheu a Questão 195.")
    # Código da questão 195

    defeitos = [0, 1, 2, 3, 4]
    frequencias = [30, 25, 10, 5, 2]
    total_frequencias = sum(frequencias)
    
    media = sum(d * f for d, f in zip(defeitos, frequencias)) / total_frequencias
    
    variancia = sum((d - media) ** 2 * f for d, f in zip(defeitos, frequencias)) / total_frequencias
    desvio_padrao = math.sqrt(variancia)
    
    print(f"a) A média é: {media}")
    print(f"b) O desvio padrão é: {desvio_padrao}")

def questao196():
    print("Você escolheu a Questão 196.")
    # Código da questão 196

     # Exemplo genérico para calcular mediana e quartis
    dados = sorted([7, 8, 6, 10, 5, 9, 4, 12, 7, 8])
    
    def mediana(lst):
        n = len(lst)
        if n % 2 == 0:
            return (lst[n // 2 - 1] + lst[n // 2]) / 2
        else:
            return lst[n // 2]
    
    Q2 = mediana(dados)
    Q1 = mediana(dados[:len(dados)//2])
    Q3 = mediana(dados[len(dados)//2:])
    
    print(f"A mediana (Q2) é: {Q2}")
    print(f"O primeiro quartil (Q1) é: {Q1}")
    print(f"O terceiro quartil (Q3) é: {Q3}")

def questao197():
    print("Você escolheu a Questão 197.")
    # Código da questão 197

    p = 0.4
    q = 1 - p
    n = 3
    
    probabilidades = [comb(n, k) * (p ** k) * (q ** (n - k)) for k in range(n + 1)]
    
    print("Número de defeitos (k) | Probabilidade")
    for k, prob in enumerate(probabilidades):
        print(f"{k:<21} | {prob:.3f}")

def questao198():
    print("Você escolheu a Questão 198.")
    # Código da questão 198

    p_acumulada = [0.216, 0.432, 0.288, 0.064]
    F = [sum(p_acumulada[:i+1]) for i in range(len(p_acumulada))]
    
    print("Função de distribuição acumulada:")
    for k, f in enumerate(F):
        print(f"F({k}) = {f:.3f}")

def questao199():
    print("Você escolheu a Questão 199.")
    # Código da questão 199

    n = 3
    p = 0.4
    q = 1 - p
    
    E_X = n * p
    Var_X = n * p * q
    
    print(f"a) Valor esperado (E[X]) = {E_X}")
    print(f"b) Variância (Var[X]) = {Var_X}")

def questao200():
    print("Você escolheu a Questão 200.")
    # Código da questão 200

    media_liquido = 900
    dp_liquido = 10
    media_embalagem = 100
    dp_embalagem = 4
    
    media_bruto = media_liquido + media_embalagem
    dp_bruto = sqrt(dp_liquido ** 2 + dp_embalagem ** 2)
    
    print(f"Média do peso bruto = {media_bruto} g")
    print(f"Desvio padrão do peso bruto = {dp_bruto:.2f} g")
  

def questao_invalida():
    print("Questão inválida. Tente novamente.")

# Dicionário para mapear números de questões às funções
questoes = {
    #até a questão 200
    1: questao1,
    2: questao2,
    3: questao3,
    4 : questao4,
    5 : questao5,
    6 : questao6,
    7 : questao7,
    8 : questao8,
    9 : questao9,
    10 : questao10,
    11 : questao11,
    12 : questao12,
    13 : questao13,
    14 : questao14,
    15 : questao15,
    16 : questao16,
    17 : questao17,
    18 : questao18,
    19 : questao19,
    20 : questao20,
    21 : questao21,
    22 : questao22,
    23 : questao23,
    24 : questao24,
    25 : questao25,
    26 : questao26,
    27 : questao27,
    28 : questao28,
    29 : questao29,
    30 : questao30,
    31 : questao31,
    32 : questao32,
    33 : questao33,
    34 : questao34,
    35 : questao35,
    36 : questao36,
    37 : questao37,
    38 : questao38,
    39 : questao39,
    40 : questao40,
    41 : questao41,
    42 : questao42,
    43 : questao43,
    44 : questao44,
    45 : questao45,
    46 : questao46,
    47 : questao47,
    48 : questao48,
    49 : questao49,
    50 : questao50,
    51 : questao51,
    52 : questao52,
    53 : questao53,
    54 : questao54,
    55 : questao55,
    56 : questao56,
    57 : questao57,
    58 : questao58,
    59 : questao59,
    60 : questao60,
    61 : questao61,
    62 : questao62,
    63 : questao63,
    64 : questao64,
    65 : questao65,
    66 : questao66,
    67 : questao67,
    68 : questao68,
    69 : questao69,
    70 : questao70,
    71 : questao71,
    72 : questao72,
    73 : questao73,
    74 : questao74,
    75 : questao75,
    76 : questao76,
    77 : questao77,
    78 : questao78,
    79 : questao79,
    80 : questao80,
    81 : questao81,
    82 : questao82,
    83 : questao83,
    84 : questao84,
    85 : questao85,
    86 : questao86,
    87 : questao87,
    88 : questao88,
    89 : questao89,
    90 : questao90,
    91 : questao91,
    92 : questao92,
    93 : questao93,
    94 : questao94,
    95 : questao95,
    96 : questao96,
    97 : questao97,
    98 : questao98,
    99 : questao99,
    100 : questao100,
    101 : questao101,
    102 : questao102,
    103 : questao103,
    104 : questao104,
    105 : questao105,
    106 : questao106,
    107 : questao107,
    108 : questao108,
    109 : questao109,
    110 : questao110,
    111 : questao111,
    112 : questao112,
    113 : questao113,
    114 : questao114,
    115 : questao115,
    116 : questao116,
    117 : questao117,
    118 : questao118,
    119 : questao119,
    120 : questao120,
    121 : questao121,
    122 : questao122,
    123 : questao123,
    124 : questao124,
    125 : questao125,
    126 : questao126,
    127 : questao127,
    128 : questao128,
    129 : questao129,
    130 : questao130,
    131 : questao131,
    132 : questao132,
    133 : questao133,
    134 : questao134,
    135 : questao135,
    136 : questao136,
    137 : questao137,
    138 : questao138,
    139 : questao139,
    140 : questao140,
    141 : questao141,
    142 : questao142,
    143 : questao143,
    144 : questao144,
    145 : questao145,
    146 : questao146,
    147 : questao147,
    148 : questao148,
    149 : questao149,
    150 : questao150,
    151 : questao151,
    152 : questao152,
    153 : questao153,
    154 : questao154,
    155 : questao155,
    156 : questao156,
    157 : questao157,
    158 : questao158,
    159 : questao159,
    160 : questao160,
    161 : questao161,
    162 : questao162,
    163 : questao163,
    164 : questao164,
    165 : questao165,
    166 : questao166,
    167 : questao167,
    168 : questao168,
    169 : questao169,
    170 : questao170,
    171 : questao171,
    172 : questao172,
    173 : questao173,
    174 : questao174,
    175 : questao175,
    176 : questao176,
    177 : questao177,
    178 : questao178,
    179 : questao179,
    180 : questao180,
    181 : questao181,
    182 : questao182,
    183 : questao183,
    184 : questao184,
    185 : questao185,
    186 : questao186,
    187 : questao187,
    188 : questao188,
    189 : questao189,
    190 : questao190,
    191 : questao191,
    192 : questao192,
    193 : questao193,
    194 : questao194,
    195 : questao195,
    196 : questao196,
    197 : questao197,
    198 : questao198,
    199 : questao199,
    200 : questao200




}

print("Bem-vindo\n")

while True:
    print("\nEscolha qual questão deseja visualizar:\n")
    
    try:
        numero_questao = int(input("Digite o número da questão: "))
        # Obtém a função correspondente ou `questao_invalida` se o número não estiver no dicionário
        questoes.get(numero_questao, questao_invalida)()
    except ValueError:
        print("Por favor, insira um número válido.")
    
    # Pergunta se o usuário quer ver outra questão ou sair
    continuar = input("\nDeseja ver outra questão? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saindo do programa. Até a próxima!")
        break
