#Este es uncomando muy importante...
# pip install mysql-connector-python

#Los valores  de user, pasword, host  y database de ser iguales a los que pusimos
#cuando estabamos instalado Mariadb en los anteriores videos. Importante!
import mysql.connector as mariadb

conexion = mariadb.connect (user="root",password="3025",
                            host="127.0.0.1",database="INFOTEP_BIGDATA3")

print(conexion)

if conexion:
    print("conexion con exito.")
    
cursor= conexion.cursor()
#cON ESTE COMANNADO SE Actualizar  un registo desde python
cursor.execute("Update participante2 Set Nombre='Pablo laureano 'WHERE id =6;")
conexion.commit()
print("El registro se ha insertado con exito")