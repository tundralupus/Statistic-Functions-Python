def OpçõesMediana():
    print('''
                1. Voltar ao menu.
                2. Fazer outra operação.
                3. Fechar Programa.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        Mediana()
    elif Opção ==('3'):
        quit()
    else:
        print('Opção invalida')
        Menu()
        
def OpçõesVariancia():
    print('''
                1. Voltar ao menu.
                2. Fazer outra operação.
                3. Fechar Programa.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        Variancia()
    elif Opção ==('3'):
        quit()
    else:
        print('Opção invalida')
        Menu()
        
def OpçõesAmplitude():
    print('''
            1. Voltar ao menu.
            2. Fazer outra operação.
            3. Fechar Programa.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        Amplitude()
    elif Opção ==('3'):
        quit()
    else:
        print('Opção invalida')
        Menu()

def OpçõesMediaAritimetica():
    print('''
            1. Voltar ao menu.
            2. Fazer outra operação.
            3. Fechar Programa.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        MediaAritimetica()
    elif Opção ==('3'):
        quit()
    else:
        print('Opção invalida')
        Menu()
def OpçõesMediaPonderada():
    print('''
            1. Voltar ao menu.
            2. Fazer outra operação.
            3. Fechar Programa.''')
    Opção = input('Opção: ')
    if Opção == ('1'):
        Menu()
    elif Opção ==('2'):
        MediaPonderada()
    elif Opção ==('3'):
        quit()
    else:
        print('Opção invalida')
        Menu()
        
def MediaAritimetica():
    print('media aritimetica')
    list = []
    while True:
        try:        
            Elementos = int(input('Quantidade de numeros: '))
            if (Elementos <= 0):
                print('apenas numeros acima de 1')
                OpçõesMediaAritimetica()
            elif (Elementos >= 101):
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
            print('Entrada invalida')
            OpçõesMediaAritimetica()


def MediaPonderada():
    print('Media Ponderada')
    while True:
        try:  
            Quantidade = int(input('Quantidade de alunos? '))
            if Quantidade <= 0:
                print('opção invalida')
                Menu()            
            else:
                for i in range(Quantidade):
                    Ap1 = float(input('Ap1: '))
                    if Ap1 <= 0 or Ap1 >= 11:
                        print ('Numero invalido')
                        OpçõesMediaPonderada()
                    else:
                        Ap1 = Ap1 * 0.2
                        Ap2 = float(input('Ap2: '))
                        if (Ap2 <= 0) or (Ap2 >= 11):
                            print ('Numero invalido')
                            OpçõesMediaPonderada()
                        else:
                            Ap2 = Ap2 * 0.3
                            Ap3 = float(input('Ap3: '))
                            if (Ap3 <= 0) or (Ap3 >= 11):
                                print ('Numero invalido')
                                OpçõesMediaPonderada()
                            else:
                                Ap3 = Ap3 * 0.5
                                media = (Ap1 + Ap2 + Ap3)
                                print (media)
                OpçõesMediaPonderada()
        except ValueError:
            print('Entrada invalida')
            OpçõesMediaPonderada()
            
def Amplitude():
    print('Amplitude')
    lista = []
    while True:
        try:
            elementos = int(input('elementos: '))
            if elementos >= 11:
                print('Maximo 10')
                OpçõesAmplitude()
            else:
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
            print('Entrada invalida')
            OpçõesAmplitude()

def Mediana():
    print('Mediana')
    Mediana = []
    while True:
        try:   
            Elementos = int(input('Elementos: '))
            if Elementos >= 11:
                print('Maximo 10')
                OpçõesAmplitude()
            else:
                for i in range(Elementos):
                    Numeros = float(input('Numeros: '))
                    Mediana.append(Numeros)
                print (sorted(Mediana))
                import statistics
                print (statistics.median(Mediana))
                OpçõesMediana()
        except ValueError:
            print ('Entrada invalida')
            OpçõesMediana()

def Variancia():
    print('variancia')
    Variancia = []
    while True:
        try:
            Elementos = int(input('Elementos: '))
            if Elementos >= 11:
                print('Maximo 10')
                OpçõesVariancia()
            elif Elementos < 2:
                print('Minimo 2')
                OpçõesVariancia()
            else:
                for i in range (Elementos):
                    Numeros = float(input('Numeros: '))
                    Variancia.append(Numeros)
                import statistics
                print(statistics.variance(Variancia))
                OpçõesVariancia()
        except ValueError:
                print('Entrada invalida')
                OpçõesVariancia()
    
def Menu():
    print("""
    1. Calculos Estatisticos
    2. Historia da Universidade
    3. Quem Somos
    4. Sair
    Menu V0,4""")
    while True:
        try:
            Opção = input("Opção: ")    
            if Opção == ('1'):
                print("""
                1. Média Aritimetica
                2. Media Ponderada
                3. Mediana
                4. Amplitude
                5. Variancia
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
                    Variancia()
                elif Opção == ('6'):
                    Menu()
                else:
                    print('Opção invalida')
                    Menu()  
            elif Opção == ('2'):
                print('A Wyden Educacional faz parte do grupo Adtalem Global Education, com 85 anos de tradição, e que tem o objetivo de empoderar estudantes para que alcancem seus objetivos, encontrem o sucesso e façam contribuições inspiradoras para a comunidade global. Desde 2009, a Wyden Educacional vem construindo uma trajetória com foco no sucesso dos seus alunos e acredita na transformação do país por meio da promoção de uma educação com excelência acadêmica, programas para desenvolvimento dos estudantes, infraestrutura e benefícios internacionais. Ao todo, no Brasil, são mais de 52 mil alunos, em 12 instituições.')
                print('1. Voltar')
        
                Opção = input("Opção: ")
                if Opção == ('1'):
                    Menu()   
                else:
                    print('Opção invalida')
                    Menu()
            elif Opção == ('3'):
                print('''Dev's:
                Alan Carlos Gualberto da Silva
                Salomão Gouveia Santos
                Yuri Mateus Faria da Silva
                ''')
                print('1. Voltar')
                Opção = input("Opção: ")
                if Opção == ('1'):
                    Menu()            
                else:
                    print('Opção invalida')
                    Menu()
            if Opção == ('4'):
                quit()
        
        except ValueError:
            print('Opção invalida')
            Menu()   
                
Menu()

