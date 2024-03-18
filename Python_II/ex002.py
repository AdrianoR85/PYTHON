# Criar uma função para agendar o desligamento do compurador em uma hora.
# Create a function to schedule to turn off the computer in one and hour.

import os

def turn_off_one_hour():
  os.system('shutdown /s /t 3600')

def turn_off_half_an_hour():
  os.system('shutdown /s /t 1800')

def cancel_shutdown():
  os.system('shutdown /a')
  
# turn_off_one_hour()
# turn_off_half_an_hour()
cancel_shutdown()


