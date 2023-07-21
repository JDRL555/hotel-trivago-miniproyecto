from models.ingreso import Ingreso
from datetime       import datetime

ingreso_modelo = Ingreso()

class ingreso():
    
    def insert(ced_hue, cod_hab, fec_ing, fec_sal, can_per):
        if not ced_hue or not cod_hab or not fec_ing or not fec_sal or not can_per:
            return {"error": True, "msg": "Faltan campos por llenar, por favor ingrese todos los datos que se le estan pidiendo."}            
        try:
            fec_ing = datetime.strptime(fec_ing, "%d-%m-%Y").date()
            fec_sal = datetime.strptime(fec_sal, "%d-%m-%Y").date()
        except ValueError:
            return {"error": True, "msg": "La fecha es inválida, debe estar e el formato dd-mm-aaaa, por ejemplo: 19-07-2023"}
    
        try:
            can_per = int(can_per)
        except ValueError:
            return {"error": True, "msg": "La cantidad de personas debe ser numerico."}
        
        result = ingreso_modelo.insert(ced_hue, cod_hab, fec_ing, fec_sal, can_per)
        print(result)
        return {"error": False, "msg": result}

    
    def select_all():
        todos_ing = ingreso_modelo.select_all()
        return {"error": True, "msg": todos_ing}
    
    def select_one(cod_ing):
        try:
          if not cod_ing:
              return {"error": True, "msg": "Faltan campos por llenar, por favor ingrese todos los datos que se le estan pidiendo."} 
          ing = ingreso_modelo.select_one(int(cod_ing))
          return {"error": False, "msg": ing}
        except ValueError:
          return {"error": False, "msg": "Codigo invalido"}

    def update(fec_ing, fec_sal, can_per, cod_ing):
        if not fec_ing or not fec_sal or not can_per or not cod_ing:
            return {"error": True, "msg": "Faltan campos por llenar, por favor ingrese todos los datos que se le estan pidiendo."}            

        try:
            fec_ing = datetime.strptime(fec_ing, "%d-%m-%Y").date()
            fec_sal = datetime.strptime(fec_sal, "%d-%m-%Y").date()
        except ValueError:
            return {"error": True, "msg": "La fecha es inválida, debe estar e el formato dd-mm-aaaa, por ejemplo: 19-07-2023"}
        
        try:
            can_per = int(can_per)
        except ValueError:
            return {"error": True, "msg": "La cantidad de personas debe ser numerico."}
    
        result = ingreso_modelo.update(fec_ing, fec_sal, can_per, cod_ing)
        return {"error": False, "msg": result}

    
    def delete(cod_ing):
        result = ingreso_modelo.delete(cod_ing)
        return {"error": False, "msg": result}