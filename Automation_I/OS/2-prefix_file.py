from pathlib import Path

root_dir = Path('../data')
file_paths = root_dir.iterdir()

for path in file_paths:
  # print(file.stem)
  # print(file.suffix)
  new_filename = f'new-{path.stem}{path.suffix}'
  new_filepath = path.with_name(new_filename)
  path.rename(new_filepath)