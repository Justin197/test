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
    if (z==10):
        continue
    while y not in ['x']:
        y = input()

        if y == '0':
            print("LED OFF")
            ser.write(bytes('0', 'UTF-8'))
            break
        if y == '1':
            print("LED ON")
            ser.write(bytes('1', 'UTF-8'))
            break
    time.sleep(2)
    continue
    #if(z==2):
    #    print("noho")
    #break

#y = ''
#print(y)




time.sleep(2)

