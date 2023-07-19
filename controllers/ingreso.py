import models as models
from datetime import datetime

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