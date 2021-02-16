import glob
import compress

images = 'Data/Train/cardboard/'
# Create a list of all image names in the directory
img_c = glob.glob(images + '*.jpg')
images = 'Data/Train/glass/'
# Create a list of all image names in the directory
img_g = glob.glob(images + '*.jpg')
images = 'Data/Train/metal/'
# Create a list of all image names in the directory
img_m = glob.glob(images + '*.jpg')
images = 'Data/Train/paper/'
# Create a list of all image names in the directory
img_p = glob.glob(images + '*.jpg')
images = 'Data/Train/plastic/'
# Create a list of all image names in the directory
img_pl = glob.glob(images + '*.jpg')
images = 'Data/Train/trash/'
# Create a list of all image names in the directory
img_t = glob.glob(images + '*.jpg')

lists = [img_c, img_g, img_p, img_m, img_pl, img_t]
img = []
for j in range(6):
  for i in lists[i]:
    img.append(i)

directories = ['cardboard','glass','metal','paper','plastic','trash']
j = 0
for i in range(5):
  i = 0
  for images in lists[j]:
    compressed_img = compress.svd(images)
    compressed_img.save('compressed/data/'+directories[j]+'/'+str(i)+'.jpg')
    i+=1
  j+=1