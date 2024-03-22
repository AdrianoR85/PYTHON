class Contact:
  def __init__(self, name, phone_num, email):
    self.name = name
    self.phone_num = phone_num
    self.email = email
    
  def __str__(self):
    return f"{self.name :<10} {self.phone_num :<15} {self.email}"