import os
import collections
from pprint import pprint

# Download_Path = os.path.join(
#     os.path.expanduser('~'),
#     'Downloads'
# )

Download_Path = os.path.normpath('/home/harry/Desktop/Download_Files')

file_mappings = collections.defaultdict()

for filename in os.listdir(Download_Path):
    file_type = filename.split('.')[-1]
    file_mappings.setdefault(file_type, []).append(filename)

# pprint(file_mappings)

for folder_name, folder_items in file_mappings.items():
    folder_path = os.path.join(Download_Path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    for folder_item in folder_items:
        source = os.path.join(Download_Path, folder_item)
        destination = os.path.join(folder_path, folder_item)
        if source not in destination:
            os.rename(source, destination)
        # pprint(f'Moving {source} to {destination}')