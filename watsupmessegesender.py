from pyautogui import typewrite,press
from time import sleep
from os import system
from msvcrt import getch
msg=input("enter meassege you want to send : ")
try:
    repeat=int(input('how many times the messege will send : '))
except ValueError:
    print('please enter a valid repetation')
else:
    print('please mait-',end='')
    for i in range(20):
        print('🛬',end='')
        sleep(0.1)
    print('🛫')
    print('press any key to continue......')
    getch()
    print('put the cursor to where messege type in 10 seconds.')
    sleep(10)
    print('time over')
    sleep(2)
    for i in  range(repeat):
        typewrite(msg)
        press('enter')
finally:
    print('''thanks for using my litil software 
if there is any issue'😓 you can contact me.
thank you.''')
getch()