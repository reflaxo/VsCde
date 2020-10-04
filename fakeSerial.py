import serial
import time

#giving rights before workingn on serial port
#sudo chmod o+rw /dev/tty0 
#cat /dev/tty0

ser = 0

#initialize serial connection 
def init_serial():
    COMNUM = 9 #set you COM port # here
    global ser #must be declared in each fxn used
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = '/dev/tty0' 
    ser.close()
    #you must specify a timeout (in seconds) so that the
    # serial port doesn't hang
    ser.timeout = 1
    ser.open() #open the serial port

    # print port open or closed
    if ser.isOpen():
        print('Open:' + ser.portstr)
#setup
#init serial
init_serial()

#read in gps log file
f = open("output.nmea","r")
data = f.read()
#split into lines
splittext= data.split('\n')
#print('text' + data.split('\n')[3])
#convert to bytes for input to serial formatting
bdata = bytes(splittext[3], 'utf8')


#main
while True:
    #prints what is sent in on the serial port
    ser.write(bdata) #write to the serial port
    time.sleep(5) 
    #line = ser.readline() #reads in bytes followed by a newline 
    #print('You sent: ' + str(line.decode('utf8'))) #print to the console
    #break #jump out of loop 

