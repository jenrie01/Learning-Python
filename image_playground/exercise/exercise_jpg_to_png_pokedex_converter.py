import sys
import os
from PIL import Image

# grab first and second argument
sys.argv
from_folder = sys.argv[1]
to_folder = sys.argv[2]

# check if new/ exist, if not create it
path = './'
if to_folder in os.listdir(path):
    print(f'There\'s an existing {to_folder} folder')
else:
    os.mkdir(path+to_folder)

# loop through pokedex folder
for filename in os.listdir(path+from_folder):
    if filename.endswith('.jpg'):
        # convert images to png
        img = Image.open(f'{path}{from_folder}/{filename}')
        img.save(f'{path}{to_folder}/{filename[:-4]}.png', 'png')
        # save to the new folder
