import numpy as np
from imageio import imread, imsave
import matplotlib.pyplot as plt

cat = imread("cat.jpg")
monkey = imread("test.jpg")

if __name__ == "__main__":
  
  # crop the image
  cropped_cat = cat[75:300, 75:300]
  cropped_monkey = monkey[40:200, 40:200]
  imsave(cropped_cat, "cropped_cat.jpg")
  imsave(cropped_monkey, "cropped_monkey.jpg")
  
  # make images brighter
  darker_cat = cat * [0.8,0.8,0.8]
  darker_monkey = monkey * [0.8,0.8,0.8]
  
  # make images darker
  brighter_cat = cat * [1.3,1.3,1.3]
  brighter_monkey = monkey * [1.3,1.3,1.3]
  
  plt.subplot(1,2,1)
  plt.imshow(monkey)
  plt.subplot(1,2,2)
  plt.imshow(np.uint8(np.clip(brighter_monkey, 0.0, 255.0)))
  plt.show()
  
  imsave(np.uint8(np.clip(brighter_monkey, 0.0, 255.0)), "brighter_monkey.jpg")
  
  plt.subplot(1,2,1)
  plt.imshow(cat)
  plt.subplot(1,2,2)
  plt.imshow(np.uint8(np.clip(brighter_cat, 0.0, 255.0)))
  plt.show()
  
  imsave(np.uint8(np.clip(brighter_cat, 0.0, 255.0)), "brighter_cat.jpg")
  
  plt.subplot(1,2,1)
  plt.imshow(cat)
  plt.subplot(1,2,2)
  plt.imshow(np.uint8(np.clip(darker_cat, 0.0, 255.0)))
  plt.show()
  
  imsave(np.uint8(np.clip(darker_cat, 0.0, 255.0)), "darker_cat.jpg")
  
  plt.subplot(1,2,1)
  plt.imshow(monkey)
  plt.subplot(1,2,2)
  plt.imshow(np.uint8(np.clip(darker_monkey, 0.0, 255.0)))
  plt.show()
  
  imsave(np.uint8(np.clip(darker_monkey, 0.0, 255.0)), "darker_monkey.jpg")
  
  input("exit: ")
