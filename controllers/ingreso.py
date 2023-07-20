from models.ingreso import Ingreso
from datetime import datetime

ingreso_modelo = Ingreso()

class ingreso():
    
    def insert(self, ced_hue, cod_hab, fec_sal, can_per):
        try:
            
            if not ced_hue or not cod_hab or not fec_sal or not can_per:
                return "Faltan campos por llenar, por favor ingrese todos los datos que se le estan pidiendo."
            
            if not isinstance(ced_hue, int):
                return "La cedula del huesped no puede tener puntos decimales."
            
            if not isinstance(can_per, int):
                return "La cantidad de personas no puede tener letras."

            fec_sal = datetime.datetime.strptime(fec_sal, "%d/%m/%Y").date()
        
        except ValueError:

            print("La fecha es inválida, debe estar e el formato dd/mm/aaaa, por ejemplo: 19/07/2023")
        
        else:
            print("¡La fecha es correcta!")

            result = ingreso_modelo.insert(ced_hue, cod_hab, fec_sal, can_per)
            return result
    
    def select_all(self):
        todos_ing = ingreso_modelo.select_all()
        return todos_ing
    
    def select_one(self, cod_ing):
        ing = ingreso_modelo.select_one(cod_ing)
        return ing
    
    def update(self, ced_hue, cod_hab, fec_sal, can_per):
        try:
            
            if not ced_hue or not cod_hab or not fec_sal or not can_per:
                return "Faltan campos por llenar, por favor ingrese todos los datos que se le estan pidiendo."
            
            if not isinstance(ced_hue, int):
                return "La cedula del huesped no puede tener puntos decimales."
            
            if not isinstance(can_per, int):
                return "La cantidad de personas no puede tener letras."

            fec_sal = datetime.datetime.strptime(fec_sal, "%d/%m/%Y").date()
        
        except ValueError:

            print("La fecha es inválida, debe estar e el formato dd/mm/aaaa, por ejemplo: 19/07/2023")
        
        else:
            print("¡La fecha es correcta!")

            result = ingreso_modelo.update(ced_hue, cod_hab, fec_sal, can_per)
            return result
    
    def delete(self, cod_ing):
        result = ingreso_modelo.delete(cod_ing)
        return result