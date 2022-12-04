from colorama import Fore,Back,Style
import sys,os
import socket as soc
import time as t
import pyfiglet as pyf
import phonenumbers as ph
from phonenumbers import timezone, geocoder, carrier


print('='*41)


text = pyf.figlet_format(Fore.CYAN+"FlashTool",font="slant")
print(text)

print('='*41)

print(Fore.CYAN+'$flash_toolkit')
print('''
\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Get Your IP
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m Get Websites IP
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m Phone Number Checker
''')
print('='*41)


while True:
     ch = int(input(Fore.BLUE+'$ Enter Your Choice > '))
     if ch == 1:
          host = soc.gethostname()
          ip_addr = soc.gethostbyname(host)
          print("$ Fetching..")
          t.sleep(2)
          print(Fore.BLUE+f'$ Your IP Address:',ip_addr)
          print(Fore.BLUE+f'$ Host Name:',host)
          print('\n')
     elif ch == 2:
          website = input(Fore.BLUE+'$ Enter Website Name:')
          full_url = Fore.BLUE+f"www.{website}.com"
          ip_add = soc.gethostbyname(full_url)
          print('$ Fetching..')
          t.sleep(2)
          print(Fore.BLUE+'$ IP Address:',ip_add)
          print('\n')

     elif ch == 3:
          phoneNumber = ph.parse(input(Fore.BLUE+"Target Number With Country Code:"))

          timeZone = timezone.time_zones_for_number(phoneNumber)

          Carrier = carrier.name_for_number(phoneNumber, 'en')

          Region = geocoder.description_for_valid_number(phoneNumber, 'en')

          print(Fore.BLUE+'Given Number Details')
          print(phoneNumber)
          print(Fore.RED+"TimeZone:  ",timeZone)
          print(Fore.RED+"Sim Carrier:  ",Carrier)
          print(Fore.RED+"Number In Region:  ",Region)

          
if "__name__" == "__main__":
     main(sys.argv[:1])



