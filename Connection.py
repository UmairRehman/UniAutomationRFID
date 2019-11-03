
#!/usr/bin/env python
import os
import RPi.GPIO as GPIO
import mysql.connector as cn

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
GPIO.setwarnings(False)

try:
    print("Please scan a card...")
    id, text = reader.read()
except:
    pass
finally:
    GPIO.cleanup()

#clear console
os.system("clear")

#connecting to database
connection = cn.connect(host='192.168.18.58', password='admin', user='umair',database='fyp')

#getting cursor
cursor = connection.cursor()

#executing select query
#cursor.execute("select * from vehicle where student_id= " + str(id) + ";")
cursor.execute("INSERT INTO vehicle(vehicle_no,Category,student_id) values ('AET-665', 'Bike', 12313123)")
#finalizing changes
connection.commit()

"""
#getting result
result = cursor.fetchall()

#getting status message after executing a query
#print(cursor._rowcount)

#printing result
for i in result:
    print ("ID is: " + i[2])
    print ("Car type is: " + i[1])
    print ("Car number is: " + i[0])


"""