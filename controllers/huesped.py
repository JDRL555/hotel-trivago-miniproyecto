from models.huesped import Huesped
import re

huesped_modelo = Huesped()

class huesped():
	def insert(ced_hue, ape_hue, nom_hue, dir_hue, ciu_hue, email_hue, tel_hue):
		if not ced_hue or not ape_hue or not nom_hue or not dir_hue or not ciu_hue or not email_hue or not tel_hue:
			return {"error": True, "msg": "Faltan campos por llenar, por favor ingrese todos los datos que se le estan pidiendo."}
		try: 
			ced_hue = int(ced_hue)
		except ValueError:
			return {"error": True, "msg": "La cedula no puede tener puntos decimales."}

		if ced_hue < 100000 or ced_hue > 100000000:    
			return {"error": True, "msg": "'La cedula tiene que estar en el rango de 6 o 8 digitos.'"}

		validar_correo = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
		
		if not re.match(validar_correo, email_hue):
			return {"error": True, "msg": "'El correo electronico no es valido, intentelo nuevamente.'"}

		try: 
			tel_hue = int(tel_hue)
		except ValueError:
			return {"error": True, "msg": "El numero de telefono no puede tener letras, simbolos o signos."}
		
		if tel_hue < 1000000000 or tel_hue > 10000000000:
			return {"error": True, "msg": "El numero de telefono no puede ser mayor ni menor a 11 digitos."}
		
		result = huesped_modelo.insert(ced_hue, ape_hue, nom_hue, dir_hue, ciu_hue, email_hue, str(tel_hue))

		return {"error": False, "msg": result}
		
	def select_all():
		todos_hue = huesped_modelo.select_all()
		return {"error": False, "msg": todos_hue}
	
	def select_one(ced_hue):
		try:
			hue = huesped_modelo.select_one(int(ced_hue))
			return {"error": False, "msg": hue}
		except ValueError:
			return {"error": True, "msg": "Cedula invalida"}
	
	def update(ced_hue, ape_hue, nom_hue, dir_hue, ciu_hue, email_hue, tel_hue):
		if not ced_hue or not ape_hue or not nom_hue or not dir_hue or not ciu_hue or not email_hue or not tel_hue:
			return {"error": True, "msg": "Faltan campos por llenar, por favor ingrese todos los datos que se le estan pidiendo."}
		
		try: 
			ced_hue = int(ced_hue)
		except ValueError:
			return {"error": True, "msg": "La cedula no puede tener puntos decimales."}

		if ced_hue < 100000 or ced_hue > 100000000:    
			return {"error": True, "msg": "'La cedula tiene que estar en el rango de 6 o 8 digitos.'"}

		validar_correo = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
		
		if not re.match(validar_correo, email_hue):
			return {"error": True, "msg": "'El correo electronico no es valido, intentelo nuevamente.'"}

		try: 
			tel_hue = int(tel_hue)
		except ValueError:
			return {"error": True, "msg": "El numero de telefono no puede tener letras, simbolos o signos."}
		
		if tel_hue < 1000000000 or tel_hue > 10000000000:
			return {"error": True, "msg": "El numero de telefono no puede ser mayor ni menor a 11 digitos."}
		
		result = huesped_modelo.update(nom_hue, ape_hue, dir_hue, ciu_hue, email_hue, str(tel_hue), ced_hue)
		return {"error": False, "msg": result}
		
	def delete(ced_hue):
		try:
			print(ced_hue)
			result = huesped_modelo.delete(int(ced_hue))
			return {"error": False, "msg": result}
		except ValueError:
			return {"error": True, "msg": "Cedula invalida"}