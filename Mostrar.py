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
#Por ultimo ..Mostramos los datos de la tabla Participante desde python
cursor.execute("Select * from participante2;")
resultados=cursor.fetchall()

for row in resultados:
    print(row[0],row[1],row[2],row[3],row[4],row[5])
