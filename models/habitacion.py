import mysql.connector
from mysql.connector import Error


class Habitacion():
    def conectar(self):
        conexion = mysql.connector.connect(host="localhost",user="root",passwd="",db="hospedaje",port=3307)
        return conexion

    def select_all(self,id):
        con = self.conectar()
        cursor = con.cursor()
        sql = "SELECT * FROM habitacion;"
        cursor.execute(sql)
        info = cursor.fetchall()
        cursor.close()
        return info

    def select_one(self,id):
        con = self.conectar()
        cursor = con.cursor()
        sql = f"SELECT * FROM habitacion WHERE cod_hab = {id}"
        cursor.execute(sql)
        info = cursor.fetchone()
        cursor.close()
        return info

    def insert(self):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"INSERT INTO habitacion VALUES('')"
            cursor.execute(sql)
            result = cursor.rowcount #Número de filas afectadas
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e

    def update(self, tipohabitacion, capacidadhabitacion, preciohabitacion, statushabitacion, id):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"UPDATE habitacion SET tip_hab = {tipohabitacion}, cap_hab = {capacidadhabitacion}, pre_hab = {preciohabitacion},sta_hab = {statushabitacion} WHERE cod_hab = {id};"
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
            sql = f"DELETE FROM habitacion WHERE cod_hab = {id};"
            cursor.execute(sql)
            result = cursor.rowcount 
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e