import matplotlib.pyplot as plt
from colorthief import ColorThief
siro_color = ColorThief("/Users/shubham/images/test_img.jpg")
# get the dominant color
dominant_color = siro_color.get_color(quality=1)
rgb=print(dominant_color)
plt.imshow([dominant_color])
plt.show()
