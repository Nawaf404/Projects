from random import choice
from turtle import color
from stegano import lsb
import datetime , os , platform , pyfiglet, socket
from termcolor import colored
print(f"""
------------------------------
Date [{colored(datetime.datetime.now().date(),'green')}] - Time [{colored(datetime.datetime.now().strftime('%X'),'blue')}]
.
Device name : {colored(socket.gethostname(),'red')}
IP Address (Local) : {colored(socket.gethostbyname(socket.gethostname()),'red')}
Path : {os.getcwd()}
{colored(' !!! This program is not responsible for any bad use !!!', 'red')}
------------------------
""")
print(pyfiglet.figlet_format("Crypt \nDecrypt"))
choice = str(input("\n1 - Hide Secret msg\n2 - Create Hide msg\n; "))

if choice == "1":
    suggest = []
    for checkingFiles in os.listdir():
        if checkingFiles.endswith(".png") or checkingFiles.endswith(".jpeg"):
            suggest.append(checkingFiles)
    ''.join(suggest)
    print(colored(f'Suggestion files : {suggest}','green'))
    image = input("Enter name of Image [ Be Accurate ]\n; ")
    # 1 - Step
    if image.endswith('.png') or image.endswith('.jpeg'):
        if os.path.isfile(image):
            print(colored("Working On it Sir, wait some seconds",'green'))
            # Start working ///

            message = str(input("Type Secret Msg\n: "))
            secret = lsb.hide(image, message)
            secret.save(f'SE_911-{image}')
            print('Image saved with name ', f'SE_911-{image}')

        else: 
            # if 1 step error
            print(colored('Are you Sure ? Seems name of image incorrect','red'))
    elif not  '.' in image[-3] or image[-4]:
        # Step 2 , if step 1 not work
        print("Sorry, that file doesn't have ext, maybe you missed up")
    else :
        print("Sorry Image doesn't carry correct ext \n", image[-3:])
elif choice == "2":
    print(colored('Enter name of image wants reveal : ','blue'))
    detect = input("; ")
    print(lsb.reveal(detect))
else :
    print("Maybe u missed the correct letter, try again !\nThis Program One way ON")