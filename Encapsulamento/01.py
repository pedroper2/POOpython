import os 
os.system ("cls || clear") 
class saldoInsuficienteErro(Exception):
    pass
class valorNegativoErro(Exception):
    pass
class conta: 
    def __init__(self,agencia:int,conta: int) -> None:
        self.agencia= agencia
        self.conta = conta
        self._saldo= 0 #Atributo protegido 

    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self,valor):
        try:
            self.__verificar_sacar(valor)
            
        except saldoInsuficienteErro as error: 
            return f"Error: {error}"
        
        self._saldo -= valor
        return self._saldo
    
    def __verificar_sacar(self,valor): 
        if valor > self.saldo:
            raise saldoInsuficienteErro ("Saldo insuficiente")
        

    def deposita (self,valor):
        try:
            self.verificaDeposito(valor)
        except valorNegativoErro as erro:
            return f"erro: {erro}"
        
        self._saldo += valor
        return self._saldo
    
    def verificaDeposito(self,valor):
        if valor < 0:
            raise valorNegativoErro ("Não é possivel adiciona um valor menor que zero.") 

class ContaCorrente (conta):
    pass

class Contapoupanca(conta):
    pass 

conta_corrente01= ContaCorrente(222,333)
conta_poupanca01 = Contapoupanca(444,555)
print(conta_corrente01.saldo)
print(conta_corrente01.sacar (2000))
        
