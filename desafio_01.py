import os
import random
import numpy as np
from faker import Faker

fake = Faker('pt_BR')
os.system('cls')

class Tripulante:
    
    def __init__(self, nome, idade, id):
        self.nome = nome
        self.idade = idade
        self.id = id

    def __str__(self):
        return f'Tripulante: {self.id}\nNome: {self.nome}\nIdade: {self.idade}\n'

class Navio:
    
    def __init__(self, capacidade=50, tripulantes=None):
        self.capacidade = capacidade
        if tripulantes is None:
            self.tripulantes = np.empty(10000, dtype=object)
        else:
            self.tripulantes = tripulantes

    def get_passageiros_numero(self):
        
        total = 0
        
        for tripulante in self.tripulantes:
            
            if isinstance(tripulante, list):
                total += len(tripulante)
                
            elif tripulante is not None:
                total += 1
                
        return total

    def hash(self, x):
        a = len(x.nome)
        b = int(str(x.idade).replace('-', ''))
        hash_key = (a + b) % 10
        return int(hash_key)

    def embarcar(self, tripulante):
        
        check = self.get_passageiros_numero()
        
        if check == self.capacidade:
            
            return 0
        
        x = self.hash(tripulante)
        
        if self.tripulantes[x] is None:
            
            self.tripulantes[x] = tripulante
            return 1
        
        else:
            
            if type(self.tripulantes[x]) != list:
                holder = self.tripulantes[x]
                self.tripulantes[x] = []
                self.tripulantes[x].append(holder)
                return 1
            
            elif type(self.tripulantes[x]) == list:
                self.tripulantes[x].append(tripulante)
                return 1

    def get_passageiros(self):
        
        list_pass = []
        
        for tripulante in self.tripulantes:
            
            if isinstance(tripulante, list):
                
                for tri in tripulante:
                    list_pass.append(tri)
                    
            elif tripulante is not None:
                list_pass.append(tripulante)
                
        return list_pass

    def get_passageiro(self, x):
        
        hash_key = self.hash(x)
        
        if isinstance(self.tripulantes[hash_key], list):
            
            for tripulante in self.tripulantes[hash_key]:
                
                if tripulante.nome == x.nome and tripulante.idade == x.idade:
                    
                    return tripulante
                
            return f'Tripulante {x.nome} inexistente'
        
        elif self.tripulantes[hash_key] is not None:
            
            if self.tripulantes[hash_key].nome == x.nome and self.tripulantes[hash_key].idade == x.idade:
                
                return self.tripulantes[hash_key]
            
            return f'Tripulante {x.nome} inexistente'
        
        else:
            return f'Tripulante {x.nome} inexistente'

passageiros = []
navios = []

for x in range(250):
    
    passageiros.append(Tripulante(fake.name(), fake.date(), x))

count = 0

for pp in passageiros:
    
    if not navios:
        
        navios.append(Navio())
        
    if navios[count].embarcar(pp) == 0:
        
        if navios[count].get_passageiros_numero() == navios[count].capacidade:
            
            count = count + 1
            navios.append(Navio())
            navios[count].embarcar(pp)
            
        else:
            navios[count].embarcar(pp)

while True:
    
    print(f"""
    1 Checar lista de passageiros
    2 Procurar passageiro
    """)

    choise = input('>>> ')

    if choise == '1':
        
        for pp in passageiros:
            
            print(pp)
            
    elif choise == '2':
        
        count = 1
        
        while True:
            
            print("Digite o numero do passageiro")
            
            try:
                
                p_number = int(input('>>> '))
                p = passageiros[p_number]
                break
            
            except:
                
                print("ERRO!!!\nPor favor, Digite o numero do passageiro")
                continue
            
        count = 0
        
        for nav in navios:
            
            found = 0
            
            if isinstance(nav.get_passageiro(p), Tripulante):
                
                os.system('cls')
                print(f'Passageiro Encontrado!!!\nNavio: {count}\n{nav.get_passageiro(p)}')
                found = 1
                break
            
            else:
                
                count += 1
                
        if found == 1:
            continue
        else:
            print('Passageiro não encontrado')
            
    else:
        '<<< error >>>'
