gameName = input("Enter the game name: ")

char = gameName[0].lower()
new_gameName =  gameName.replace(char, "$")
new_gameName = char + new_gameName[1:] 
print(new_gameName)

