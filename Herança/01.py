from abc import ABC,abstractmethod
import os
os.system ("clear||cls")

class Funcionario(ABC):
    def __init__(self,nome:str,idade:int,salario:float) -> None:
        self.nome= nome
        self.idade= idade
        self.salario= salario
    @abstractmethod
    def calcular_salario (self)-> float:
        pass
class Gerente (Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO= 1.2
        salario_Final= self.salario * BONIFICACAO
        return salario_Final
class Motoboy (Funcionario):
    def __init__(self, nome: str, idade: int, salario: float,cnh:str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    def calcular_salario(self) -> float:
        BONIFICACAO= 1.1
        salario_Final = self.salario * BONIFICACAO
        return salario_Final
 

Motoboy01= Motoboy("Reinan",25,1500.0,"454554")
Gerente1= Gerente("Arthu",22,1500.0)

print(f"Nome: {Gerente1.nome}")
print(f"Salario: {Gerente1.calcular_salario()}")
print(f"Nome: {Motoboy01.nome}")
print(f"Salario: {Motoboy01.calcular_salario()}")
        
        
        