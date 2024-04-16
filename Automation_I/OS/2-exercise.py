from pathlib import Path

# Creating 5 files
for i in range(5):
  with open(f'../data/Question{i}.txt', 'w') as f:
    f.write('')
    
# Get all paths    
paths = Path('../data')

index = 1
# Change the question file name
for path in paths.iterdir():
  file_name = path.stem[:-1] 
  if file_name  == "Question":
    new_filename = f'{index}-{file_name}{path.suffix}'
    new_path = path.with_name(new_filename)
    path.rename(new_path)
    index +=1
    