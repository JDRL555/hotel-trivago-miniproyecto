import models as models
import re

class huesped():
    
    def insert(self, ced_hue, ape_hue, nom_hue, dir_hue, ciu_hue, email_hue, tel_hue):
        try:
            if not ced_hue or not ape_hue or not nom_hue or not dir_hue or not ciu_hue or not email_hue or not tel_hue:
                return "Faltan campos por llenar, por favor ingrese todos los datos que se le estan pidiendo."

            if not isinstance(ced_hue, int):
                return "La cedula no puede tener puntos decimales."
            
            if ced_hue < 100000 or ced_hue > 100000000:    
                return 'La cedula tiene que estar en el rango de 6 o 8 digitos.'

            validar_correo = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
            
            if not re.match(validar_correo, email_hue):
                return 'El correo electronico no es valido, intentelo nuevamente.'
            
            if not isinstance(tel_hue, int):
                return "El numero de telefono no puede tener letras, simbolos o signos."
            
            if tel_hue < 1000000000 or tel_hue > 10000000000:
                return "El numero de telefono no puede ser mayor ni menor a 11 digitos."


        except Exception as error:
            return error