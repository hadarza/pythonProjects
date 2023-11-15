import math

def findBottomLeft(points):
    bottom_most = points[0]

    for point in points:
        if point.y < bottom_most.y or (point.y == bottom_most.y and point.x < bottom_most.x):
            bottom_most = point

    return bottom_most
		

def sortCCW(points:list):
    bottom_left = findBottomLeft(points)
    points.sort(key = lambda point: math.atan2(point.y - bottom_left.y, point.x - bottom_left.x))

def isLeftTurn(p1,p2,p3):
	return (p2.x - p1.x) * (p3.y - p2.y) - (p2.y - p1.y) * (p3.x - p2.x) > 0

def grahamScan(points:list):
    sortCCW(points)

    # Initialize the convex hull with the leftmost point
    hull = [points[0]]

    for point in points:
        while len(hull) > 1 and isLeftTurn(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
        
    hull.append(points[0])

    return hull
