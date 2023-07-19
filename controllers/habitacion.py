import models as models

class habitacion():

    def insert(self, cod_hab, num_hab, tip_hab, cap_hab, pre_hab, sta_hab):

        if not cod_hab or not num_hab or not tip_hab or not cap_hab or not pre_hab or not sta_hab:
            return "Faltan campos por llenar, por favor ingrese todos los datos que se le estan pidiendo."
        
        if len(cod_hab) > 4:
            return "El codigo debe ser menor o igual a 4 caracteres."
        
        if len(num_hab) > 4:
            return "El numero debe ser menor o igual a 4 caracteres."
        
        if len(tip_hab) > 1 and not ("N" in tip_hab or "E" in tip_hab or "S" in tip_hab):
            return 'Debe poner solo una letra y debe ser alguna de estas tres opciones ("N" normal, "E" ejecutiva, "S" suite).'

        if len(cap_hab) > 1 and not ("I" in cap_hab or "M" in cap_hab or "D" in cap_hab or "T" in cap_hab):
            return 'Debe poner solo una letra y debe ser alguna de estas tres opciones ("I" individual, "M" matrimonial, "D" doble, "T" triple).'

        if type(pre_hab) != float:
            return "El precio debe ser un decimal."
        
        if len(sta_hab) > 1 and not ("D" in sta_hab or "O" in sta_hab):
            return 'Debe poner una letra y debe ser alguna de estas 2 ("D" desocupada, "O" ocupada).'