from abc import ABC, abstractmethod

class Control(ABC):
  @abstractmethod
  def turnOn(self):
    ...
  @abstractmethod
  def turnOff(self):
    ...

class TVControl(Control):
  def turnOn(self):
    print("TV is turning on")
  
  def turnOff(self):
    print("TV is turning off")

c = TVControl()
c.turnOn()
c.turnOff()


  