from abc import ABC, abstractmethod
import os 

os.system ("cls||clear")

    
class VerificarSalarioError(Exception):
    pass

class Endereco:
    def __init__(self,logradouro:str,numero:int,cidade:str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade= cidade
    def __str__(self) -> str:
        return f"\nlogradouro:{self.logradouro} \nnumero: {self.numero} \ncidade{self.cidade}"

class funcionario(ABC):
    def __init__(self,nome:str,email:str,salario:float,endereco:Endereco) -> None:
        self.nome = nome
        self.email = email
        self.__salario = None
        self.__set_salario (salario)
        self.endereco = endereco

    @abstractmethod
    def salario_Final(self) -> float:
        pass

    def __set_salario(self, salario: float) -> None:
        try:
            self.__verifica_salario(salario)
            self.__salario = salario
        except VerificarSalarioError as error:
            print(f"Erro: {error}")

    def __verifica_salario(self,salario:float)->None:
        if salario < 0 :
            raise VerificarSalarioError ("O salario não pode ser 0")


    def __str__(self) -> str:
        return (f"Nome: {self.nome}\n"
                f"Email: {self.email}\n"
                f"Salário: {self._salario}\n"
                f"Endereço: {self.endereco}")
    
    
class Motoboty(funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco,cnh:str) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh= cnh

    def __str__(self) -> str:
        return (super().__str__() +
        f"Cnh: {self.cnh}")
    
    def salario_Final(self) -> float:
        return self._salario

class Gerente (funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
    def __str__(self) -> str:
        return super().__str__()
    
    def salario_Final() -> float:
        pass

motoboty01 = Motoboty ("Pedro", "PEdro@ham",1500, endereco= Endereco ("Avenida",57,"Salvador"))   
print (motoboty01)
   
        
        
        
        