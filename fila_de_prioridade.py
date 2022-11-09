class FilaPrioridade:
    def __init__(self):
        self.__fila = [] #lista com os objetos professor
        self.__fila_tempo = [] # lista com os tempos de ifce de cada professor
                
    
    def push(self, professor):
        self.__fila_tempo.append(professor.tempo_de_ifce) #adiciona o tempo de ifce do professor a fila_tempo
        self.__fila_tempo.sort(reverse = True) #organiza fila_tempo do maior para o menor tempo
        for index in range(0, len(self.__fila_tempo)): 
            if professor.tempo_de_ifce == self.__fila_tempo[index]:
                self.__fila.insert(index, professor) #adiciona o professor a fila comparando o seu tmpo de ifce com o valor em fila_tempo
                

    def pop(self):
        self.__fila.pop(0) #remove o professor de maior prioridade, logo, o primeiro da lista

    def empty(self):
        if len(self.__fila) == 0: #verifica se a fila comtem elementos atraves da finção len()
            return True
        return False

    def lengh(self):
        return len(self.__fila) #calcula  a quantidade de professores na lista atravez da função len

    def __str__(self):
        if self.empty == True: #verifica se a lista esta vazia atraves do metodo interno empty
            return '[]' 
        ret = ', '.join(str(professor) for professor in self.__fila) #define a formatação da string caso existam elementos na lista
        return ret