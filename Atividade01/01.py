class Livro:
    #construtor
    def __init__(self,Titulo:str,Autor:str,NumeroDePaginas:int,preco:int)->None:
        self.Titulo = Titulo
        self.Autor = Autor
        self.NumeroDePaginas = NumeroDePaginas
        self.preco = preco

    def exibir_dados(self) -> str:
        return f"\nNome: {self.Titulo} \nAutor: {self.Autor} \nNumero de pag: {self.NumeroDePaginas} \nValor: {self.preco}";

    
primeiro_livro = Livro ("Pai pobre, pai rico", "Robert Kiosaki",325,45) 
segundo_livro = Livro ("O poder do hábito", "Charles",561,205) 

print(primeiro_livro.exibir_dados())
print(segundo_livro.exibir_dados())