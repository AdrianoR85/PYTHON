class Course:
  def __init__(self, name, trail):
    self.name = name
    self.trail = trail
    
  @staticmethod
  def courses_trail(trail):
    if trail == "Python Fundamentos":
      courses = ["Domindo o Python", "Módulos e Pip", "Orientação a Objetos"]
    elif trail == "Automação com Python":
      courses = ["Automação de Tarefas", "Web scraping", "Assistente Virtual em Python"]
    else:
      courses = ["A definir"]
    return courses    
  
print(Course.courses_trail("Python Fundamentos"))
print(Course.courses_trail("Automação com ddPython"))