from ex003 import Trip

trip0 = Trip('New York')
trip1 = Trip('New Jersey')
trip2 = Trip('Houston')
trip3 = Trip('Dallas')
trip4 = Trip('San Francisco')

print('Hey, traveler. We have some offers for you!')
traveler = input('Enter your name: ').capitalize()
print(f'{traveler} we have this options that combine with you:')
print( 
      """
      [0] - New York
      [1] - New Jersey
      [2] - Houston
      [3] - Dallas
      [4] - San Francisco
      """
      )
choice = int(input('Select the destination of the trip: '))
list_trip = [trip0, trip1, trip2, trip3, trip4]

for option in list_trip:
  if choice >= 5:
    print(f'Sorry {traveler}, we do not have this option')
    break
  else:
    print(f'{traveler} your trip to {list_trip[choice].destiny} is booking')
    break