from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.glob('**/*')
for path in file_paths:
  if path.is_file():
    parent_folder = (path.parts[-1])
    new_filename = f'{parent_folder}-{path.name}'
    print(new_filename)