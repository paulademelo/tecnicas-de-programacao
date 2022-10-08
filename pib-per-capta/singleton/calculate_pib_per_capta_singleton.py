import abc
from itertools import count
from json import load
from os import stat
from typing_extensions import Self
import pandas as pd
from abc import ABC, abstractclassmethod, abstractmethod

class Config:
    _base_file  = "data/base.xlsx"
    _region     = "UF_Regiao"

class AbstractCalculatePib(ABC):
    class AbstractCalculatePib(ABC):
        @abstractclassmethod
        def get_instance():
            raise RuntimeError('TODO: Método ainda não implementado')

        @abstractclassmethod
        def load_file(self):
            raise RuntimeError('TODO: Método ainda não implementado')
    
        @abstractclassmethod
        def load_uf_by_region(self):
            raise RuntimeError('TODO: Método ainda não implementado')

        @abstractclassmethod
        def print_all_content(self):
            raise RuntimeError('TODO: Método ainda não implementado')

        @abstractclassmethod
        def get_state_by_region(self):
            raise RuntimeError('TODO: Método ainda não implementado')

        @abstractclassmethod
        def get_region_by_state(self):
            raise RuntimeError('TODO: Método ainda não implementado')

        @abstractclassmethod
        def get_state_by_region_for(self):
            raise RuntimeError('TODO: Método ainda não implementado')    
  
class CalculatePibPerCaptaSingleton(AbstractCalculatePib):
    # Atributos da classe
    _instance       = None
    raw_data        = None
    current_content = None

    # Métodos
    # Construtor da classe
    def __init__(self):
       # Lançando uma exceção em tempo de execução para quando há mais de uma instãncia sendo criada
        raise RuntimeError('Singleton!!')

    @classmethod
    def instance__(cls):
        print("Test")
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            return cls._instance
        else:
            print("Instance has already been created")          
            return cls._instance
    
    @classmethod
    def load_file(self):
        print("Inicio do script de PIB x Percapta")
        self.raw_data = pd.ExcelFile(Config._base_file)
        return self.raw_data

    @classmethod
    def load_uf_by_region(self):
        self.current_content = pd.read_excel(self.raw_data, Config._region )
        return self.current_content

    @classmethod
    def print_all_content(self):
        print(self.current_content)

    '''
    Atividade 1)
    Retorna os estados dada uma região
    '''
    @classmethod
    def get_state_by_region(self, state):

        print("------- Atividade 1 -------")
        states = self.current_content[self.current_content['Regiao'] == state]
        print(+ states + " |" )

    '''
    Atividade 2)
    Retorna a região de acordo com o estado
    '''
    @classmethod
    def get_region_by_state(self, region):

        print("------- Atividade 2 -------")
        regions = self.current_content[self.current_content['Estado'] == region]
        print(+ regions + " |" )

    '''
    Atividade 4)
    Retorna o estado de acordo com a região usando for
    '''
    @classmethod
    def get_state_by_region_for(self, state):
        print("------- Atividade 4.1 usando For: -------")
        list = []
        for item in self.current_content[self.current_content['Regiao'] == state]:
            if state in item:
                list.append(item)
            return list

    ''' 
    Retorna o estado de acordo com a região usando iteração com pandas Dataframe
    '''
    @classmethod
    def get_state_by_region_data_frame(self, state):
       print("------- Atividade 4.2 usando Dataframe -------")
       for i in self.current_content:
        return pd.DataFrame(self.current_content, columns=['Estado', 'Regiao'])
       

    '''
    Atividade 5) Criar os seguintes métodos para sumarizar o resultado de Região e Estado:
    5.1
    Retorna o total de estados
    '''
    @classmethod
    def state_count(self):
        print("------- Atividade 5.1 Total de Estados -------")
        print(len(self.current_content))  

    '''
    Atividade 5)
    5.2
    Retorna o total de regiões
    '''
    @classmethod
    def region_count(self):
        print("------- Atividade 5.2 Total de Regiões -------")
        for i in self.current_content:
            if i in self.current_content[self.current_content['Regiao'] == i]:
                regions = i
        print(len(regions))
    
    ''' 5.3 
    Retorna a primeira região e estado em uma lista
    '''
    @classmethod
    def first_region_state(self):
        print("------- Atividade 5.3 primeira região e estado-------")
        first_region = pd.DataFrame(self.current_content, columns=['Estado', 'Regiao'])
        print(first_region.iloc[0,0]+ " -> " + first_region.iloc[0,1])
   
    ''' 5.4 
    Retorna a última região e estado em uma lista
    '''
    @classmethod
    def last_region_state(self):
        print("------- Atividade 5.3 última região e estado-------")
        last_region = pd.DataFrame(self.current_content, columns=['Estado', 'Regiao'])
        print(last_region.iloc[-1,0] + " -> " + last_region.iloc[-1,-1])
   
    '''
    Atividade 3)
    3.1 Qual a finalidade do Pacote Pandas do Python?
        R: O Pandas é uma biblioteca para manipulação dos dados

    3.2 Como o Pandas é organizado internamente em termos de estrutura de Dados em Python?
        R: Existem dois tipos de estruturas: pseires (unidimensional, o seja, representa um lista, e o DataFrame,
        que são abstrações de uma tabela.

    3.3 Qual a diferença entre um comando de iteração classico em Python e o uso de filtros customizados no Panda?
        R: A diferença está na rapidez, o filter consegue ser mais eficiente
    '''

                       



'''
rodar no terminal:  python3 script_pib_client.py
'''
