from enum import Enum 
import os

from numpy import double 
os.system ("cls||clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO= "Feminino"

class Setor(Enum):
    FINACEIRO = "Financeiro"
    RECURSOS_HUMANOS= "Recursos Humanos"
    VENDAS= "Vendas"
    MARKETING="Marketing"

class funcionario:
    def __init__(self,id:int,nome:str,idade:int,salario: double,sexo:Sexo,setor:Setor) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.sexo = sexo
        self.setor= setor

    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSalario: {self.salario}"
                f"\nSexo: {self.sexo.value}"
                f"\nSetor: {self.setor.value}")
    
pessoa_1= funcionario(155,"Marta",10,1500,Sexo.FEMININO,Setor.RECURSOS_HUMANOS)
print(pessoa_1)