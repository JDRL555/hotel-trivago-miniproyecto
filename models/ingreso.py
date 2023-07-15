import mysql.connector
from mysql.connector import Error


class Ingreso():
    def conectar(self):
        conexion = mysql.connector.connect(host="localhost",user="root",passwd="",db="hospedaje",port=3307)
        return conexion

    def select_all(self):
        con = self.conectar()
        cursor = con.cursor()
        sql = "SELECT * FROM ingreso;"
        cursor.execute(sql)
        info = cursor.fetchall()
        cursor.close()
        return info

    def select_one(self, id):
        con = self.conectar()
        cursor = con.cursor()
        sql = f"SELECT * FROM ingreso WHERE cod_ing = {id}"
        cursor.execute(sql)
        info = cursor.fetchone()
        cursor.close()
        return info

    def insert(self,cedula,codigohabitacion,fechaingreso,fechasalida,cantidadpersonas):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"INSERT INTO ingreso (ced_hue, cod_hab,fec_ing,fec_sal,can_per) VALUES('{cedula}','{codigohabitacion}','{fechaingreso}','{fechasalida}','{cantidadpersonas}');)"
            cursor.execute(sql)
            result = cursor.rowcount #Número de filas afectadas
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e

    def update(self, fechaingreso, fechasalida, cantidadpersonas, id):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"UPDATE huesped SET fec_ing = {fechaingreso}, ape_ing = {fechasalida}, dir_ing = {cantidadpersonas} WHERE cod_ing = {id};"
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
            sql = f"DELETE FROM ingreso WHERE cod_ing = {id};"
            cursor.execute(sql)
            result = cursor.rowcount 
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e