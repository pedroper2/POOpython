from abc import ABC, abstractmethod
import os 
os.system("clear || cls")
class Endereco:
    def __init__(self,logradouro:str,numero:int,complemento:str,cep:str,cidade:str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento= complemento
        self.cep = cep
        self.cidade=  cidade
    def __str__(self) -> str:
        return (f"\nLogra: {self.logradouro} \nnumero: {self.numero} \ncomple{self.complemento} \ncep:{self.cep} \nSalvador{self.cidade}")
class Funcionario(ABC):

    def __init__(self,nome:str,tell:str,email:str,endereco:Endereco) -> None:
        self.nome = nome
        self.tell = tell
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def calcular_salario (self)-> float:
        pass

   
    def __str__(self) -> str:
        return (f"\nNome: {self.nome} \nTell: {self.tell} \nemail {self.email} \nendereco {self.endereco} \nCnh{self.cnh}")
    
class Engenheiro (Funcionario):
    def __init__(self, nome: str, tell: str, email: str, endereco: Endereco,cnh:str) -> None:
        self.cnh = cnh
        super().__init__(nome, tell, email, endereco)

    def calcular_salario (self) -> float: 
        salario= 500
        return salario
    def __str__(self) -> str:
        super().__str__()
        f"\Crm: {self.cnh}"
        return 

    

class medico (Funcionario):
    def __init__(self, nome: str, tell: str, email: str, endereco:Endereco,crm:str) -> None:
        self.crm = crm
        super().__init__(nome, tell, email, endereco)
    def calcular_salario(self) -> float:
        salario= 2000
        return salario
    
    def __str__(self) -> str:
        return (f"\nNome: {self.nome} \nTell: {self.tell} \nemail {self.email} \nendereco {self.endereco} \nCnh{self.crm}")

Engenheiro01= Engenheiro ("Pedro","3325","pedrofkf",Endereco ("Rua A",57,"terrio","4555","salavdor"),"5554")
Medico01= medico ("fulano","888552","pedropereira@",Endereco ("avenida",57,"terrio","40471","Salvador"),'44527')
print(Engenheiro01)
print(f"salario: {Engenheiro01.calcular_salario()}")
print(Medico01)
print(f"salario: {Medico01.calcular_salario}")




