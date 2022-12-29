from pathlib import Path
from datetime import datetime

root_dir = Path('files')

for path in root_dir.glob('**/*'):
  if path.is_file():
    create_date = datetime.fromtimestamp(path.stat().st_ctime)
    create_date_as_str = create_date.strftime("%Y-%m-%d_%H:%M:%S")
    new_filename = create_date_as_str + '_' + path.name
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)
    print(new_filename)