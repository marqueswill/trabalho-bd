from Integracao.DBRestaurante import DBRestaurante
from Objetos.Restaurante import Restaurante
from Teste.TesteBase import TesteBase




class TesteRestaurante(TesteBase):
    def __init__(self):
        self.restaurante_db = DBRestaurante(teste=True)
    
    def test_insert(self):
        try:
            restaurantes = [
                Restaurante(
                    cnpjRestaurante="85920376000145",
                    endereco="Rua A, 123i",
                    razao="Restaurante Ain Ltda",
                    nome="Restaurante Ain",
                    telefone=11987654321,
                    cnpjMatriz=None, 
                    cpfGerente="78901234568" 
                ),
                Restaurante(
                    cnpjRestaurante="98765432000188",
                    endereco="Avenida B, 456",
                    razao="Restaurante B ME",
                    nome="Restaurante B",
                    telefone=11912345678,
                    cnpjMatriz="85920376000145", 
                    cpfGerente="89012345679" 
                ),
                Restaurante(
                    cnpjRestaurante="56789012000177",
                    endereco="Travessa C, 789",
                    razao="Restaurante C Comércio",
                    nome="Restaurante C",
                    telefone=11998765432,
                    cnpjMatriz="85920376000145", 
                    cpfGerente="90123456780" 
                )
            ]
            for f in restaurantes:
                self.restaurante_db.insert(f)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_get_by_id(self):
        try:
            restaurante = self.restaurante_db.get_by_id("85920376000145")

            if restaurante:
                return "Success"
            else:
                return "Failed - No restaurante found"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_get_all(self):
        try:
            self.restaurante_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_update(self):
        try:
            restaurante = self.restaurante_db.get_by_id("85920376000145")
            restaurante.endereco = "Avenida Central, 1000"  
            restaurante.razao = "Delícias da Serra Comércio de Alimentos Ltda"  
            restaurante.nome = "Delícias da Serra"  
            restaurante.telefone = 11999887766  

            self.restaurante_db.update(restaurante)

            return "Success"    

        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_delete(self):
        try:
            self.restaurante_db.delete("56789012000177")
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_delete_all(self):
        try:
            self.restaurante_db.delete_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"