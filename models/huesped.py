import mysql.connector
from mysql.connector import Error

class Huesped():
    def conectar(self):
        conexion = mysql.connector.connect(host="localhost",user="root",passwd="",db="hospedaje")
        return conexion

    def select_all(self):
        con = self.conectar()
        cursor = con.cursor()
        sql = "SELECT * FROM huesped;"
        cursor.execute(sql)
        info = cursor.fetchall()
        cursor.close()
        return info

    def select_one(self, id):
        con = self.conectar()
        cursor = con.cursor()
        sql = f"SELECT * FROM huesped WHERE ced_hue = {id}"
        cursor.execute(sql)
        info = cursor.fetchone()
        cursor.close()
        return info

    def insert(self, cedula, apellidos, nombres, direccion, ciudad, email,telefono):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"INSERT INTO huesped VALUES({cedula},'{apellidos}','{nombres}','{direccion}','{ciudad}' ,'{email}','{telefono}');"
            cursor.execute(sql)
            result = cursor.rowcount #Número de filas afectadas
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e

    def update(self, nombre, apellido, direccion, ciudad, email, telefono, id):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"UPDATE huesped SET ced_hue = {id}, nom_hue = '{nombre}', ape_hue = '{apellido}', dir_hue = '{direccion}', ciu_hue = '{ciudad}',email_hue = '{email}',tel_hue = '{telefono}' WHERE ced_hue = {id};"
            cursor.execute(sql)
            result = cursor.rowcount 
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e

    def delete(self, id):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"DELETE FROM huesped WHERE ced_hue = {id};"
            cursor.execute(sql)
            result = cursor.rowcount 
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e