import sys
import os
from PIL from import Image


#grab first and second argument which is Pokedex/ & new/
images_folder = sys.argv[1]
output_folder = sys.argv[2]


#check if new\ exists, if not create it
if not os.path.exists(output_folder):
  os.makedirs(output_folder)


for filename in os.listdir(images_folder):
  img = Image.open(f'{images_folder}{filename}')
  clean_name = os.path.splitext(filename)
  #Below says save as png and .png file format
  img.save(f'{output_folder}{clean_name}.png', 'png')
  print('all done!')
#Loop through Pokedex
#Convert images to PNG
#Save to new folder
