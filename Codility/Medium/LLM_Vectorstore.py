import math

def calculate_distances_greater_than_two(pixels, b):
    distant_pixels = []

    for pixel in pixels:
        # 計算 歐基里德 距離
        #distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(pixel, b)))
        distance = math.dist(pixel, b)
        
        if distance > 5:
            distant_pixels.append(pixel)

    return distant_pixels, distance

pixels = [(1, 2), (5, 6), (7 , 8)]
b = (3,4)

print(calculate_distances_greater_than_two(pixels, b))


#import math
#
#def calculate_distances_greater_than_five(pixels, b):
#    distant_pixels = []
#
#    for pixel in pixels:
#        # 计算每个像素与 b 之间的欧几里得距离
#        distance = math.sqrt(sum((a - b_val) ** 2 for a, b_val in zip(pixel, b)))
#
#        if distance > 5:
#            distant_pixels.append(pixel)
#
#    return distant_pixels
#
## 示例像素列表和单个像素 b
#pixels = [(1, 2), (5, 6), (7, 8)]
#b = (3, 4)
#
#print(calculate_distances_greater_than_five(pixels, b))
