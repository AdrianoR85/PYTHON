class Client:
  def __init__(self, name, phone):
    self._name = name
    self._phone = phone
    
  @property
  def name(self):
    return self._name
  
  @name.setter  
  def name(self, name):
    self._name = name
    