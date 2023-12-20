import math 
import csv

def get_answer(data: list):
    data[0]
    for i in len(data): 
        middle_x = (data[i][i]+data[i][i])/2
        middle_y = (data[i][i]+data[i][i])/2
        middle = [middle_x, middle_y]
    #    #middle_bx = (b[0]+b[1])/2
    #    #middle_by = (b[2]+b[3])/2
    #    middle_a= [middle_ax, middle_ay]
    #    middle_b= [middle_bx, middle_by]
        distance2 = math.dist(middle_a, middle_b)
    return 1
    #if distance2 < 20 :
    #    c.pop(a)
    #return distance2
    
filename = "/Users/wiwi_kuo/Downloads/rectangles.csv"
output_data = []
with open(filename,'r') as data:
    for line in csv.reader(data):
        output_data.append(line)

print(get_answer(output_data))