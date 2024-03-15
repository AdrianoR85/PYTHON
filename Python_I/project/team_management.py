import os
from time import sleep
def get_name(text):
  name = ''
  while name == '' or len(name) < 3 or name.isnumeric():
    name = input(text).title()
    
    if name == 'R': return None
    
  return name

def get_id(text):
  id = ''
  while not id.isdigit():
    id = input(text)
    if id.upper() == "R":
      return None
  return int(id)

def add_team(name, teams_list):
  if name == None: return
  teams_list.append({"Team": name, "Players": [], "TotalPlayers": 0})
  print(f"New team add: {name}\n")
  return teams_list

def remove_team(idx, teams_list):
  if idx == None: return
  
  team = teams_list.pop(idx)
  print(f"Team of {team['Team']} removed\n")
  return teams_list

def add_player(name, idx, teams_list):
  if name == None or idx == None: return
  
  if len(teams_list) == 0:
    print("No Time")
    return
  team = teams_list[idx]
  team['Players'].append(name)
  team['TotalPlayers'] += 1
  print(f"Player {name} add in the {team['Team']}\n")
  return teams_list

def remove_player(idx_team, idx_player, teams_list):
  team = teams_list[idx_team]
  name = team["Players"].pop(idx_player)
  team['TotalPlayers'] -= 1
  
  print(f"Player {name} removed\n")
  return teams_list

def show_teams(teams_list):
  header = f"{'ID':<5}{'TEAMS':<20}{'TOTAL PLAYERS':<15}"
  header_text("List All Teams")
  print(header)
  print("-" * len(header))
  
  if len(teams_list) == 0:
    print("No Teams")
    return
  
  for idx, team in enumerate(teams_list):
    team_row = f"{idx:<5}{team['Team']:<20}{team['TotalPlayers']:>7}"
    print(team_row)

def show_players(teams_list, idx):
  if len(teams_list) < idx:
    print(f"Team not found")
    return
  
  header = f"{'ID':<5}{'PLAYERS'}"
  team_name = teams_list[idx]['Team'].upper() 
  header_text(f"All Players of {team_name}")
  print(header)
  print("-" * len(header))
  
  if len(teams_list) == 0:
    print("No Teams")
    return
  
  players = teams_list[idx]['Players']

  for idx, player in enumerate(players): 
    team_row = f"{idx:<5}{player}"
    print(team_row)

def clean_window():
  os.system('cls' if os.name == 'nt' else 'clear')

def menu():
  menu_items = ["Show Teams",
                "Show Players",
                "Add New Team:",
                "Add New Player:",
                "Remove Team:",
                "Remove Player:",
                "Exit"]
  title="TEAM MANAGEMENT"
  subtitle="Choose one of the options below:"
  print("="*len(subtitle))
  print(title.center(len(subtitle)))
  print("="*len(subtitle))
  print(f"{subtitle}")
  print("-"*len(subtitle))
  for idx, item in enumerate(menu_items):
    print(f"[{idx+1}] {item} ")

def header_text(text1):
  print("="*40)
  print(f"{text1.center(40)}")
  print("="*40)

def main():
  teams_list = [ {"Team": "Santos", "Players": ['Julio', 'José', 'João'], "TotalPlayers": 3},
                {"Team": "Roma", "Players": ['Mario', '654', 'John'], "TotalPlayers": 3}]
  continue_command = True
  
  while continue_command:
    menu()
    option = input("Enter your option: ")
    
    # Show teams
    if (option == '1'):
      clean_window()
      show_teams(teams_list)
    # Show players
    elif (option == '2'):
      clean_window()
      show_teams(teams_list)
      id_team = get_id("\nWhich team do you want to see the players?\nEnter ID Team or [R] return: ")
      show_players(teams_list, id_team)
    # Add new team
    elif (option == '3'):
      clean_window()
      header_text("Add New Team")
      name = get_name("Enter the team name or [R] to return: ")
      add_team(name, teams_list)
    # Add new player
    elif (option == '4'):
      clean_window()
      show_teams(teams_list)
      print()
      header_text("Add New Player")
      id_team =  get_id("\nWhich Team do you add a new player?\n Enter ID Team or [R] to return: ")
      name = get_name("\nEnter the Player Name or [R] to return: ")
      add_player(name, id_team, teams_list)
    # Remove team
    elif (option == '5'):
      clean_window()
      show_teams(teams_list)
      header_text("Delete one Team")
      id_team = get_id("\nWhich team do you want to remove?\n Enter ID Team or [R] to return: ")
      remove_team(id_team, teams_list)
    # Remove player
    elif (option == '6'):
      clean_window()
      header_text("Delete one Player")
      show_teams(teams_list)
      id_team = get_id("\nWhich team do you want to remove the players?\nEnter ID Team or [R] to return: ")
      show_players(teams_list, id_team)
      id_player = get_id("\nWhich the player do you want to remove?\nEnter ID Player or [R] to return: ")
      remove_player(id_team, id_player, teams_list)
    # Exit
    elif (option == '7'):
      print("Finishing....")
      sleep(2)
      break
    # Invalid option
    else:
      print("Invalid option")

    resp = input("\nReturn to Menu or Exit[E]: ")
    if resp.upper() == "E":
      continue_command = False
    else:
      clean_window()
    
if __name__ == "__main__":
  main()