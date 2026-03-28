from load_image import ft_load, display
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


image = ft_load("landscape.jpg")

image1 = ft_invert(image)
image2 = ft_red(image)
image3 = ft_green(image)
image4 = ft_blue(image)
image5 = ft_grey(image)

print(ft_invert.__doc__)
print(ft_red.__doc__)
print(ft_green.__doc__)
print(ft_blue.__doc__)
print(ft_grey.__doc__)

display(image, image1, image2, image3, image4, image5)
