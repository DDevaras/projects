import sys
import os
from PIL from import Image


images_folder = sys.argv[1]
new_folder = sys.argv[2]


#check if new/ exists, if not create it
if not os.path.exists(new_folder):
  os.makedirs(new_folder)


for filename in os.listdir(images_folder):
  img = Image.open(f'{images_folder}{filename}')
  clean_name = os.path.splitext(filename)
  #Below says save as png and .png file format
  img.save(f'{new_folder}{clean_name}.png', 'png')
  print('all done!')
#Loop through
#Convert images to PNG
#Saves to a new folder
