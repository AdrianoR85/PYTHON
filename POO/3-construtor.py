class Movie:
  def __init__(self,name, year, includePlan, note, durationMinutes):
    self.name = name
    self.year = year
    self.includePlan = includePlan
    self.note = note
    self.durationMinutes = durationMinutes
    
  def __str__(self):
    return f"Movie: {self.name}"
  
movie1 = Movie("Super Mario Bros", 2023, False, 5.0, 130)
movie2 = Movie("Avatar", 2023, False, 4.4, 220)
print(movie1.name)
print("\n"+movie2.name)
print(movie1)