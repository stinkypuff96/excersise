import imageio.v3 as iio

img = iio.imread('monke.jpg')
image_height, image_width, _ = img.shape
raster_size_x = 5
raster_size_y = 10
result = ''

image_width = image_width // raster_size_x * raster_size_x
image_height = image_height // raster_size_y * raster_size_y

for y in range(0, image_height, raster_size_y):
    for x in range(0, image_width, raster_size_x):
        avg_brightness = 0

        for rx in range(x, x + raster_size_x):
            for ry in range(y, y + raster_size_y):
                r, g, b = img[ry, rx]
                avg_brightness += int(r) + int(g) + int(b)

        avg_brightness /= raster_size_x * raster_size_y * 3

        if avg_brightness > 204:
            result += '\u2588'
        if avg_brightness > 153:
            result += '\u2593'
        if avg_brightness > 102:
            result += '\u2592'
        if avg_brightness > 51:
            result += '\u2591'
        else:
            result += ' '


    result += '\n'

with open('result.txt', 'w', encoding='utf8') as f:
    f.write(result)