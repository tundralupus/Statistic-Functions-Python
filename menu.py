def OpçõesMediana():
    print('''
                1. Voltar ao menu.
                2. Fazer outra operação.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        Mediana()
    else:
        print('opção invalida')
        Menu()
        
def OpçõesVariação():
    print('''
                1. Voltar ao menu.
                2. Fazer outra operação.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        Variação()
    else:
        print('opção invalida')
        Menu()
        
def OpçõesAmplitude():
    print('''
            1. Voltar ao menu.
            2. Fazer outra operação.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        Amplitude()
    else:
        print('opção invalida')
        Menu()

def OpçõesMediaAritimetica():
    print('''
            1. Voltar ao menu.
            2. Fazer outra operação.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        MediaAritimetica()
    else:
        print('opção invalida')
        Menu()
def OpçõesMediaPonderada():
    print('''
            1. Voltar ao menu.
            2. Fazer outra operação.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        MediaPonderada()
    else:
        print('opção invalida')
        Menu()
        
def MediaAritimetica():
    print('media aritimetica')
    list = []
    while True:
        try:        
            Elementos = int(input('Quantidade de numeros: '))
            if Elementos != (int):
                if (Elementos <= 1):
                    print('apenas numeros acima de 1')
                    OpçõesMediaAritimetica()
                elif (Elementos >= 100):
                    print('apenas numeros abaixo de 100')
                    OpçõesMediaAritimetica()
                else: 
                    for i in range(Elementos):
                        Numeros = float(input('Numero:  '))
                        list.append(float(Numeros))
                        Media = sum(list) / Elementos
                print('Media = ',Media)
                OpçõesMediaAritimetica()
        except ValueError:
            print('Apenas numeros')
            OpçõesMediaAritimetica()


def MediaPonderada():
    print('Media Ponderada')
    while True:
        try:  
            Quantidade = int(input('Quantidade? '))
            for i in range(Quantidade):
                if Quantidade <= 0:
                    print('opção invalida')
                    Menu()
                else:
                    Ap1 = float(input('Ap1: '))
                    if Ap1 <= 0 or Ap1 >= 10:
                        print ('Numero invalido')
                        OpçõesMediaPonderada()
                    else:
                        Ap1 = Ap1 * 0.2
                        Ap2 = float(input('Ap2: '))
                    if (Ap2 <= 0) or (Ap2 >= 10):
                        print ('Numero invalido')
                        OpçõesMediaPonderada()
                    else:
                        Ap2 = Ap2 * 0.3
                        Ap3 = float(input('Ap3: '))
                        if (Ap3 <= 0) or (Ap3 >= 10):
                            print ('Numero invalido')
                            OpçõesMediaPonderada()
                        else:
                            Ap3 = Ap3 * 0.5
                            media = (Ap1 + Ap2 + Ap3)
                            print (media)
                            OpçõesMediaPonderada()
        except ValueError:
            print('Apenas numeros')
            OpçõesMediaPonderada()
            
def Amplitude():
    print('Amplitude')
    lista = []
    while True:
        try:
            elementos = int(input('elementos: '))
            for i in range(elementos):
                numeros = (input('numero: '))
                lista.append(numeros)
                lista.sort(key=int) 
            print(lista)
            minimo = int(lista[0])
            lista.reverse()
            maximo = int(lista[0])
            amplitude = (maximo-minimo)
            print('Valor máximo:', maximo)
            print('Valor mínimo:', minimo)
            print('Amplitude Total:', amplitude)
            OpçõesAmplitude()
        except ValueError:
            print('Apenas numeros')

def Mediana():
    print('Mediana')
    OpçõesMediana()

def Variação():
    print('variação')
    OpçõesVariação()
    
def Menu():
    print("""
    1. Calculos Estatisticos
    2. Historia da Universidade
    3. Quem Somos
    4. Sair
    Menu V0,4""")
    
    Opção = input("Opção: ")    
    if Opção == ('1'):
        print("""
        1. Média Aritimetica
        2. Media Ponderada
        3. Mediana
        4. Amplitude
        5. Variação
        6. Voltar""")
        
        Opção = input("Opção: ")
        if Opção == ('1'):
            MediaAritimetica()            
        elif Opção == ('2'):
            MediaPonderada()            
        elif Opção == ('3'):
            Mediana()           
        elif Opção == ('4'):
            Amplitude()            
        elif Opção == ('5'):
            Variação()
        elif Opção == ('6'):
            Menu()
        else:
            print('opção invalida')
            Menu()  
    elif Opção == ('2'):
        print('A Wyden Educacional faz parte do grupo Adtalem Global Education, com 85 anos de tradição, e que tem o objetivo de empoderar estudantes para que alcancem seus objetivos, encontrem o sucesso e façam contribuições inspiradoras para a comunidade global. Desde 2009, a Wyden Educacional vem construindo uma trajetória com foco no sucesso dos seus alunos e acredita na transformação do país por meio da promoção de uma educação com excelência acadêmica, programas para desenvolvimento dos estudantes, infraestrutura e benefícios internacionais. Ao todo, no Brasil, são mais de 52 mil alunos, em 12 instituições.')
        print('1. Voltar')
        
        Opção = input("Opção: ")
        if Opção == ('1'):
            Menu()   
        else:
            print('opção invalida')
            Menu()
    elif Opção == ('3'):
        print('''Dev's:
        blablabla''')
        print('1. Voltar')
        Opção = input("Opção: ")
        if Opção == ('1'):
            Menu()            
        else:
            print('opção invalida')
            Menu()
    elif Opção == ('4'):
        print('Off')
        
    else:
            print('opção invalida')
            Menu()   
                
Menu()

