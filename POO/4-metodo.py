class Movie:
  def __init__(self,name, year, includePlan, note, durationMinutes):
    self.name = name
    self.year = year
    self.includePlan = includePlan
    self.note = note
    self.durationMinutes = durationMinutes
    
  def __str__(self):
    return f"Movie: {self.name}"
  
  def technical_sheet(self):
    print("  Movies Information  ")
    print("----------------------")
    print(f"Movie: {self.name}")
    print(f"Year: {self.year}")
    print(f"Do Included Plan?: {self.includePlan}")
    print(f"Note: {self.note}")
    print(f"Duration: {self.durationMinutes} minutes")
    return "\n"

movie1 = Movie("Super Mario Bros", 2023, False, 5.0, 130)
movie2 = Movie("Avatar", 2023, False, 4.4, 220)
print(movie1.technical_sheet())
print(movie2.technical_sheet())