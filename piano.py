import serial
from pynput.keyboard import Key, Controller

ser = serial.Serial('COM4', baudrate = 9600, timeout=1)
keyboard = Controller()

while 1:
    arduinoData = str(ser.readline().decode('utf-8'))
    
    if(arduinoData == "Key - PRESSED.\r\n"):
        keyboard.press('1')

    if(arduinoData == "Key . PRESSED.\r\n"):
        keyboard.press('2')

    if(arduinoData == "Key , PRESSED.\r\n"):
        keyboard.press('3')

    if(arduinoData == "Key ) PRESSED.\r\n"):
        keyboard.press('4')

    if(arduinoData == "Key ] PRESSED.\r\n"):
        keyboard.press('5')

    if(arduinoData == "Key = PRESSED.\r\n"):
        keyboard.press('6')

    if(arduinoData == "Key $ PRESSED.\r\n"):
        keyboard.press('7')

    if(arduinoData == "Key & PRESSED.\r\n"):
        keyboard.press('8')

    if(arduinoData == "Key { PRESSED.\r\n"):
        keyboard.press('9')

    if(arduinoData == "Key [ PRESSED.\r\n"):
        keyboard.press('0')

    if(arduinoData == "Key ! PRESSED.\r\n"):
        keyboard.press('q')

    if(arduinoData == "Key # PRESSED.\r\n"):
        keyboard.press('w')

    if(arduinoData == "Key + PRESSED.\r\n"):
        keyboard.press('e')

    if(arduinoData == "Key 1 PRESSED.\r\n"):
        keyboard.press('r')

    if(arduinoData == "Key 8 PRESSED.\r\n"):
        keyboard.press('t')

    if(arduinoData == "Key a PRESSED.\r\n"):
        keyboard.press('y')

    if(arduinoData == "Key b PRESSED.\r\n"):
        keyboard.press('u')

    if(arduinoData == "Key | PRESSED.\r\n"):
        keyboard.press('ı')

    if(arduinoData == "Key f PRESSED.\r\n"):
        keyboard.press('o')

    if(arduinoData == "Key g PRESSED.\r\n"):
        keyboard.press('p')

    if(arduinoData == "Key h PRESSED.\r\n"):
        keyboard.press('a')

    if(arduinoData == "Key i PRESSED.\r\n"):
        keyboard.press('s')

    if(arduinoData == "Key j PRESSED.\r\n"):
        keyboard.press('d')

    if(arduinoData == "Key l PRESSED.\r\n"):
        keyboard.press('f')

    if(arduinoData == "Key m PRESSED.\r\n"):
        keyboard.press('g')

    if(arduinoData == "Key o PRESSED.\r\n"):
        keyboard.press('h')

    if(arduinoData == "Key 4 PRESSED.\r\n"):
        keyboard.press('j')

    if(arduinoData == "Key u PRESSED.\r\n"):
        keyboard.press('k')

    if(arduinoData == "Key v PRESSED.\r\n"):
        keyboard.press('l')

    if(arduinoData == "Key y PRESSED.\r\n"):
        keyboard.press('z')

    if(arduinoData == "Key p PRESSED.\r\n"):
        keyboard.press('x')

    if(arduinoData == "Key r PRESSED.\r\n"):
        keyboard.press('c')

    if(arduinoData == "Key @ PRESSED.\r\n"):
        keyboard.press('v')
        
    if(arduinoData == "Key - RELEASED.\r\n"):
        keyboard.release('1')

    if(arduinoData == "Key . RELEASED.\r\n"):
        keyboard.release('2')

    if(arduinoData == "Key , RELEASED.\r\n"):
        keyboard.release('3')

    if(arduinoData == "Key ) RELEASED.\r\n"):
        keyboard.release('4')

    if(arduinoData == "Key ] RELEASED.\r\n"):
        keyboard.release('5')

    if(arduinoData == "Key = RELEASED.\r\n"):
        keyboard.release('6')

    if(arduinoData == "Key $ RELEASED.\r\n"):
        keyboard.release('7')

    if(arduinoData == "Key & RELEASED.\r\n"):
        keyboard.release('8')

    if(arduinoData == "Key { RELEASED.\r\n"):
        keyboard.release('9')

    if(arduinoData == "Key [ RELEASED.\r\n"):
        keyboard.release('0')

    if(arduinoData == "Key ! RELEASED.\r\n"):
        keyboard.release('q')

    if(arduinoData == "Key # RELEASED.\r\n"):
        keyboard.release('w')

    if(arduinoData == "Key + RELEASED.\r\n"):
        keyboard.release('e')

    if(arduinoData == "Key 1 RELEASED.\r\n"):
        keyboard.release('r')

    if(arduinoData == "Key 8 RELEASED.\r\n"):
        keyboard.release('t')

    if(arduinoData == "Key a RELEASED.\r\n"):
        keyboard.release('y')

    if(arduinoData == "Key b RELEASED.\r\n"):
        keyboard.release('u')

    if(arduinoData == "Key | RELEASED.\r\n"):
        keyboard.release('ı')

    if(arduinoData == "Key f RELEASED.\r\n"):
        keyboard.release('o')

    if(arduinoData == "Key g RELEASED.\r\n"):
        keyboard.release('p')

    if(arduinoData == "Key h RELEASED.\r\n"):
        keyboard.release('a')

    if(arduinoData == "Key i RELEASED.\r\n"):
        keyboard.release('s')

    if(arduinoData == "Key j RELEASED.\r\n"):
        keyboard.release('d')

    if(arduinoData == "Key l RELEASED.\r\n"):
        keyboard.release('f')

    if(arduinoData == "Key m RELEASED.\r\n"):
        keyboard.release('g')

    if(arduinoData == "Key o RELEASED.\r\n"):
        keyboard.release('h')

    if(arduinoData == "Key 4 RELEASED.\r\n"):
        keyboard.release('j')

    if(arduinoData == "Key u RELEASED.\r\n"):
        keyboard.release('k')

    if(arduinoData == "Key v RELEASED.\r\n"):
        keyboard.release('l')

    if(arduinoData == "Key y RELEASED.\r\n"):
        keyboard.release('z')

    if(arduinoData == "Key p RELEASED.\r\n"):
        keyboard.release('x')

    if(arduinoData == "Key r RELEASED.\r\n"):
        keyboard.release('c')

    if(arduinoData == "Key @ RELEASED.\r\n"):
        keyboard.release('v')
        
        
    print(arduinoData)











    
