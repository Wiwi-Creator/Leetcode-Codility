import math
import csv

def calculate_center(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def get_answer(data):
    centers = []
    distant_rectangles = []

    # 计算所有矩形的中心点
    for row in data:
        x1, y1, x2, y2 = map(float, row)
        center = calculate_center(x1, y1, x2, y2)
        centers.append(center)

    # 比较所有矩形中心点之间的距离
    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            distance = math.dist(centers[i], centers[j])
            if distance > 20:
                distant_rectangles.append((data[i], data[j]))

    return distant_rectangles

filename = "/Users/wiwi_kuo/GitHub/rectangles.csv"
output_data = []
with open(filename, 'r') as data:
    csv_reader = csv.reader(data)
    next(csv_reader)  # 跳过标题行
    for line in csv_reader:
        output_data.append(line)

distant_rects = get_answer(output_data)
print(distant_rects)
 