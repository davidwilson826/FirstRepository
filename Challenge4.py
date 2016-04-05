rectangle1 = '-2 1 4 3'#input("Enter rectangle1: ")
rectangle2 = '-5 -1 5 2'#input("Enter rectangle2: ")

rectangle1 = [int(x) for x in rectangle1.split()]
rectangle2 = [int(x) for x in rectangle2.split()]

print(rectangle1, rectangle2)

def points(rectangle):
    rectpoints = [(rectangle[0], rectangle[1]) for x in list(range(0,4))]
    rectpoints[1][0] += rectangle[2]
    rectpoints[2][1] += rectangle[3]
    rectpoints[3][0] += rectangle[2]
    rectpoints[3][1] += rectangle[3]
    
points(rectangle1)
rect1points = rectpoints
points(rectangle2)
rect2points = rectpoints

print(rect1points, rect2points)

result = "No collision"

