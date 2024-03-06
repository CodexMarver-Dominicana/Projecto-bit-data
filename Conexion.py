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
cursor.execute ("INSERT INTO Participante2 (cedula, nombre, apellido, Fecha_nacimiento, Telefono, celular, Dirrecion, EstadoCivil, Correo_Electronico, Sexo, Curso, Modulo1, Modulo2, Promedio) VALUES ('40213186407', 'Pablo', 'Peña', '19990524', '8098492353', '8298444956', 'Calle mano guayabo #15', 'Soltero', 'kevin.cano.cp@gmail.com', 'M', 'Manejo de big data', 89, 98, 100);")
conexion.commit()
print("El registro se ha insertado con exito")

