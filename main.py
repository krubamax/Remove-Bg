import rembg
import numpy as np
from PIL import Image

input_image = Image.open('S__25550854.jpg')
input_image = np.array(input_image)

output_array = rembg.remove(input_image)
output_image = Image.fromarray(output_array)

output_image.save('image/output.png')
output_image.show()
#55555
