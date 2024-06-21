class Movie:
  def __init__(self, name, year, includePlan, durationMinutes):
    self.name = name
    self.year = year
    self.includePlan = includePlan
    self.durationMinutes = durationMinutes
    self.reviews = 0
    self.totalReviewers = 0
    
  def review(self, note):
    self.reviews += note
    self.totalReviewers += 1
    # return self.reviews
  
  def __str__(self):
    return f"Movie: {self.name}"
  
  def technical_sheet(self):
    print("  Movies Information  ")
    print("----------------------")
    print(f"Movie: {self.name}")
    print(f"Year: {self.year}")
    print(f"Do Included Plan?: {self.includePlan}")
    print(f"Note: {(self.reviews / self.totalReviewers):.1f}")
    print(f"Duration: {self.durationMinutes} minutes")
    print(f"Total of Reviews: {self.totalReviewers}")
    return "\n"
  
movie1 = Movie("Super Mario Bros", 2023, False, 130)
# print(movie1.technical_sheet())

movie1.review(8)
movie1.review(7.5)
movie1.review(9.5)
print(movie1.technical_sheet())