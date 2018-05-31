import serial
import time


ser = serial.Serial('COM4', 9600)

time.sleep(3)


print('Enter 1 to Turn Arduino LED ON')
print('Enter 0 to Turn Arduino LED OFF')
print('Enter x to quit:')
ser_bytes = ser.readline()
ser.flushInput()
while True:
    print(ser_bytes)
    x = ser.readline()
    y=x.decode('utf-8')
    print(y)
    z=int(y)

    print(z)

    if(z==9):
        print("jipi")
        y = input()



        if y == '0':
            print("LED OFF")
            ser.write(bytes('0', 'UTF-8'))
            break
        if y == '1':
            print("LED ON")
            ser.write(bytes('1', 'UTF-8'))

            time.sleep(2)
            
            ser_bytes = ser.readline()
            ser.flushInput()
            print(ser_bytes)
            x = ser.readline()
            y=x.decode('utf-8')
            
            print(y)
            u=int (y)
            print(u)
            #time.sleep(2)
            while (u!=6):
                print("super")
                time.sleep(2)
            print("xyz")
            
            
            
    if (z==10):
        continue
    
    time.sleep(2)
    continue
    




time.sleep(2)
