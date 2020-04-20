import torch
import numpy as np
import os
import json
import matplotlib.pyplot as plt
from PIL import Image

def copy_other_files(): 
  load_path ='drive/My Drive/CityScapeEval/gtFine/val/frankfurt'
  direction_path ='drive/My Drive/CityScapeEvalTest/gtFine/val/frankfurt'
  img_ids = []
  suffix = '_leftImg8bit.png'
    
  # all the files in all the subdirectories
  for city_name, _, files in os.walk(load_path):
    print('lenght of files {len(files)}')
    for file in files:
      if file.endswith(suffix):  # read all the images in the folder with the desired suffix
        img_ids.append(os.path.join(city_name, file))

  imgs = img_ids
  print(f'In [copy]: read {len(imgs)} from: "{load_path}"')
  print(f'In [copy]: will save imgs to: "{direction_path  }"')

  for i in range(len(imgs)):
    if i > 0 and i % 50 == 0:
      print(f'In [Copy]: done for the {i}th image')

    img_full_name = imgs[i].split('/')[-1]
    city = img_full_name.split('_')[0]
    image = Image.open(imgs[i])
    image = np.array(image)
    resized = scipy.misc.imresize(image, (h, w))
    scipy.misc.imsave(f'{direction_path}/{img_full_name}', resized)

  print('In [Copy]: All done')