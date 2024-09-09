from abc import ABC, abstractmethod
import os

os.system("cls||clear")  # Limpa o terminal, específico para Windows

class VerificarSalarioError(Exception):
    pass

class Endereco:
    def __init__(self, logradouro: str, numero: int, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nCidade: {self.cidade}")

class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self._salario = None
        self.__set_salario(salario)  # Chama o método para definir o salário
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __set_salario(self, salario: float) -> None:
        try:
            self.__verifica_salario(salario)
            self._salario = salario  # Use o atributo protegido
        except VerificarSalarioError as error:
            print(f"Erro: {error}")

    def __verifica_salario(self, salario: float) -> None:
        if salario < 0:
            raise VerificarSalarioError("O salário não pode ser negativo.")

    def __str__(self) -> str:
        return (f"Nome: {self.nome}\n"
                f"Email: {self.email}\n"
                f"Salário: {self._salario}\n"
                f"Endereço: {self.endereco}")

class Motoboty(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco, cnh: str) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh

    def __str__(self) -> str:
        return super().__str__() + f"\nCNH: {self.cnh}"

    def salario_final(self) -> float:
        return self._salario

class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)

    def __str__(self) -> str:
        return super().__str__()

    def salario_final(self) -> float:
        return self._salario

# Exemplo de uso
motoboty01 = Motoboty("Pedro", "pedro@exemplo.com", 1500, Endereco("Avenida", 57, "Salvador"), "5856")
print(motoboty01)
