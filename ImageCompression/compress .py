import numpy as np
from  PIL import Image

def openImg(img_path):
  imOpen = Image.open(img_path)
  img = np.array(imOpen)
  ired = img[:,:,0]
  igreen = img[:,:,1]
  iblue = img[:,:,2]
  return [ired,igreen,iblue,imOpen]

def compressSingleChannel(channelDataMatrix, SingularValueLimit):
  uChannel, sChannel, vhChannel = np.linalg.svd(channelDataMatrix)
  aChannelCompressed = np.zeros((channelDataMatrix.shape[0], channelDataMatrix.shape[1]))
  k = SingularValueLimit

  leftSide = np.matmul(uChannel[:,0:k], np.diag(sChannel)[0:k,0:k])
  aChannelCompressedInner = np.matmul(leftSide,vhChannel[0:k,:])
  aChannelCompressed = aChannelCompressedInner.astype('uint8')
  return aChannelCompressed

def svd(path):
  aRed, aGreen, aBlue, originalImage = openImg(path)
  SingularValueLimit = 160

  aRedCompressed = compressSingleChannel(aRed,SingularValueLimit)
  aGreenCompressed = compressSingleChannel(aGreen,SingularValueLimit)
  aBlueCompressed = compressSingleChannel(aBlue,SingularValueLimit)

  imr = Image.fromarray(aRedCompressed,mode=None)
  img = Image.fromarray(aGreenCompressed,mode=None)
  imb = Image.fromarray(aBlueCompressed,mode=None)

  newImage = Image.merge("RGB", (imr,img,imb))

  return newImage