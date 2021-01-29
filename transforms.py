# color jitter
def colorJitter(jitter_value):
  
  if not os.path.exists(col_path):
          os.mkdir(col_path)
          print("Directory " , col_path ,  " Created ")
  else:    
          print("Directory " , col_path ,  " already exists")

  rfiles = [f1 for f1 in os.listdir(train_path) if os.path.isfile(os.path.join(train_path, f1))]

  
  for i in range(len(rfiles)):
    
    img = cv2.imread(train_path + "/" + rfiles[i])
    
    h,w,c = img.shape 

    noise = np.random.randint(0,jitter_value,(h, w)) # design jitter/noise here
    jitter = np.zeros_like(img)
  
    jitter[:,:,2] = noise  

    noise_added = cv2.add(img, jitter)
      
    label_in_file = rfiles[i].find(".")
    cv2.imwrite(col_path + "/" + rfiles[i][0:label_in_file] +"cj.jpg", noise_added)

# random resized crop
def get_random_crop(in_path, crop_height, crop_width):

  if not os.path.exists(randcrop_path):
          os.mkdir(randcrop_path)
          print("Directory " , randcrop_path ,  " Created ")
  else:    
          print("Directory " , randcrop_path ,  " already exists")

  rfiles = [f1 for f1 in os.listdir(in_path) if os.path.isfile(os.path.join(in_path, f1))]

  for i in range(len(rfiles)):
    
    img = cv2.imread(in_path + "/" + rfiles[i])
    
    max_x = img.shape[1] - crop_width
    max_y = img.shape[0] - crop_height

    x = np.random.randint(0, max_x)
    y = np.random.randint(0, max_y)

    crop = img[y: y + crop_height, x: x + crop_width]
    cv2.imwrite(randcrop_path + "/" + rfiles[i], crop) #training data from randcrop path

# center crop
def center_crop(in_path, out_path, dim=(240, 240)):

  if not os.path.exists(out_path):
          os.mkdir(out_path)
          print("Directory " , out_path ,  " Created ")
  else:    
          print("Directory " , out_path ,  " already exists")

  rfiles = [f1 for f1 in os.listdir(in_path) if os.path.isfile(os.path.join(in_path, f1))]

  for i in range(len(rfiles)):
    
    img = cv2.imread(in_path + "/" + rfiles[i])

    width, height = img.shape[1], img.shape[0]
    
    #process crop width and height for max available dimension
    crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
    crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0]
    mid_x, mid_y = int(width/2), int(height/2)
    cw2, ch2 = int(crop_width/2), int(crop_height/2) 
    crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]

    cv2.imwrite(out_path + "/" + rfiles[i], crop_img) #validation in crop path, test in test_crop

# horizontal flip
def horizontalFlip(in_path):

  if not os.path.exists(flip_path):
          os.mkdir(flip_path)
          print("Directory " , flip_path ,  " Created ")
  else:    
          print("Directory " , flip_path ,  " already exists")

  rfiles = [f1 for f1 in os.listdir(in_path) if os.path.isfile(os.path.join(in_path, f1))]

  for i in range(len(rfiles)):
    
    img = cv2.imread(in_path + "/" + rfiles[i])
    
    if i%2 == 0:
      flippedimage= cv2.flip(img, 1)
    else:
      flippedimage = img

    label_in_file = rfiles[i].find(".")
    cv2.imwrite(flip_path + "/" + rfiles[i][0:label_in_file] +"flip.jpg", flippedimage)