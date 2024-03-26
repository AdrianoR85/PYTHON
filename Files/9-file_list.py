import glob, os, zipfile

# Current Directory
os.getcwd()

# List all .txt files
for file in glob.glob('data/*.txt'):
  print(file)
  
# List all .csv files
for file in glob.glob('data/*.csv'):
  print(file)
  
# unzip .txt files
with zipfile.ZipFile('names.zip', 'w') as zip:
  for file in glob.glob('data/*.txt'):
    zip.write(file)
