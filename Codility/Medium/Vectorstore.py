import math

def calculate_distances_greater_than_two(pixels):
    distant_pixels = []

    for i in range(len(pixels)):
        for j in range(i + 1, len(pixels)):
            # 計算 歐基里德 距離
            distance1 = math.dist(pixels[i], pixels[j])
            distance2 = math.sqrt(sum((a - b_value) ** 2 for a, b_value in zip(pixels[i], pixels[j])))
            if distance1 > 5:
                distant_pixels.append((pixels[i], pixels[j]))
    return distant_pixels, distance1, distance2

#pixels = [(1, 2, 3, 4), (5, 6, 7, 8), (255,22,44,44)]
pixels = [(1, 2),(5,6)]

print(calculate_distances_greater_than_two(pixels))
