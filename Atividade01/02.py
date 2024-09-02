
class Endereco:
    def __init__(self,logradouro:str,numero:int) -> None:
        self.logradouro= logradouro
        self.numero= numero
    #def _exibir_endereco(self) -> str:
        #return f"\nLogradouro: {self.logradouro} \nNumero:{self.numero}"
    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNumero:{self.numero}"
class Aluno:    
    #construtor
    def __init__(self,nome:str,idade:int,endereco: Endereco) -> None:
        #Atributo
        self.nome = nome
        self.idade= idade
        self.endereco = endereco
    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nidade: {self.idade} \nEndereco: {self.endereco}"
    #def _exibir_dados (self) -> str:
     #   return f"\nNome: {self.nome} \nIdade: {self.idade} \nEndereco: {self.endereco()}"

#Instaciando Classe.

aluno1 = Aluno ("Maria",8,Endereco("Rua A",22))

print(aluno1)