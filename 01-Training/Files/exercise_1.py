def file_read_from_line(fname, nlines):
  from itertools import islice
  
  with open(f"data/{fname}.txt", 'r', encoding='utf-8') as f:
    for line in islice(f, nlines):
      print(line.rstrip())
      
fname = input('Enter the name of the file: ')
nline = int(input('Number of lines: '))

file_read_from_line(fname, nline)