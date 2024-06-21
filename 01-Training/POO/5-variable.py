class Movie:
  platform = "Good Movies"
  def __init__(self, name, year, includePlan, durationMinutes):
    self.name = name
    self.year = year
    self.includePlan = includePlan
    self.durationMinutes = durationMinutes
    self.reviews = 0
    self.totalReviewers = 0
    self.average = 0.0
    
  def review(self, note):
    self.reviews += note
    self.totalReviewers += 1
    
    self.average = self.reviews / self.totalReviewers
    return self.average
  
  def __str__(self):
    return f"Movie: {self.name}"
  
  def technical_sheet(self):
    print("  Movies Information  ")
    print("----------------------")
    print(f"Platform: {Movie.platform}")
    print(f"Movie: {self.name}")
    print(f"Year: {self.year}")
    print(f"Do Included Plan?: {self.includePlan}")
    print(f"Note: {self.average:.1f}")
    print(f"Duration: {self.durationMinutes} minutes")
    print(f"Total of Reviews: {self.totalReviewers}")
    return "\n"
  
movie1 = Movie("Super Mario Bros", 2023, False, 130)
movie1.review(8)
movie1.review(7.5)
movie1.review(9.5)
print(movie1.technical_sheet())

Movie.platform = "Good Movies Pro"
movie2 = Movie("Avatar", 2023, False, 220)
movie2.review(7)
movie2.review(7.5)
movie2.review(6.5)
print(movie2.technical_sheet())
