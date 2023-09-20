#pip install mypy
#pip install flake8
uma_string:str = "valor"
um_inteiro:int = 123456
um_float:float = 1.23
um_boolean:bool = True
um_set:set = {1,2,3}
uma_lista:list = []
uma_tuple:tuple = 1,2,3
um_dicionario:dict = {}

#uma_string = 1 #o python roda normal mas o linter vai dizer que a variavel ja tinha sido definido

def soma(x:int,y:int,z:float) -> float: # -> significa retorna o ripo especifico
    return x + y

lista_inteiro:list[int] = [1,2,3,4]
lista_str:list[str] = ['1','2','3','4']
lista_tuplas:list[tuple] = [(1,"a"),(2,'c')]
lista_lists_int:list[list[int]] = [[1],[1,2,3]]

um_dict: dict[str,int]={
    "a":0,
    "b":1,
    "c":3
}
um_dict_list:dict[str,list[int]] = {
    "a":[1,2],
    "b":[1,2,3],
    "c":[3,2,3]
}

um_set:set[int] = {1,2,3}

ListaInteiro = list[int] #type alias
DictListaInteiros = dict[str,ListaInteiro] #type alias
um_dict_list:DictListaInteiros = { #usando o alias do alias
    "a":[1,2],
    "b":[1,2,3],
    "c":[3,2,3]
}

string_e_inteiros: str | int = 1 #union
string_e_inteiros = 1 #union
string_e_inteiros = "a" #union
lista:list[str | int] = [1,2,3,4,'a'] #union

def somar(x:int,y:float | None = None) -> float: #se não vier valor no y ele vai ser none, senão tem que vir float
    if isinstance(y,float | int):
        return x + y
    return x + x

#USANDO CALLABLES
from collections.abc import Callable

SomaInteiros = Callable[[int,int],int] #recebe dois inteiros e retorna um inteiro

def executa_callable(func: SomaInteiros, a:int, b:int) -> int:
    return func(a,b)

def soma(a:int,b:int) -> int:
    return a+b

def soma_dois(a:float,b:str) -> dict[str,float]:
    return a+b

executa_callable(soma, 1,2) #o func vai receber a funcao e retornar os tipos especificados

#USANDO TYPEVARS
from typing import TypeVar

T = TypeVar('T')

def get_item(list:list[T],index:int) -> T: #especifica um generico e retorna um generico
    return list[index]

list_int = get_item([1,2,3,4],2)
list_str = get_item(['a','b','v','a'],1)

#classes tipos
from typing import Any

class Person:
    def __init__(self,firstname,lastname) :
        self.firstname = firstname  #self esta meio que criando e inicializando essas variaveis
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname}{self.lastname}"
    
def say_my_name(person:Person,person_any:Any) -> str:
    person.lastname
    return person.full_name

def say_my_person(person:Person,person_any:Any) -> list[Person]:
    return [person,person_any]

print(say_my_name(Person("Heisen","Berg"),"")) #iniciando classe e passando os nomes

