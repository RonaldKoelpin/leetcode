#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
149. Max Points on a Line
Hard
Topics

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of
points that lie on the same straight line.


Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

    1 <= points.length <= 300
    points[i].length == 2
    -104 <= xi, yi <= 104
    All the points are unique.

"""
from math import gcd

def are_linearly_dependent(a, b, c):
    """Checks wether the 2D points A, B, C lie on one line by checking whether the directional vectors AB and AC are
    linearly dependent. Computes the determinant of the Matrix M = [AB AC] and checks whether det(M) == 0"""
    det = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    return det == 0

def max_points(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 2: return n
    max_points_on_line = 2
    for i in range(n-1):
        for j in range(i+1, n):
            points_on_line = 2
            for k in range(n):
                if k != i or k != j:
                    if are_linearly_dependent(points[i], points[j], points[k]):
                        points_on_line += 1
                if points_on_line > max_points_on_line:
                    max_points_on_line = points_on_line
    return max_points_on_line

def maxPoints(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 2: return n
    ans = 1
    for i in range(n):
        p1 = points[i]
        slopes = {}
        identical = 1 # every point is identical to itself
        for j in range(i+1, n):
            p2 = points[j]
            # getting slope dx/dy.
            # Don't divide to avoid floating point precision problems instead save tuple (dx, dy) to dict
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0 and dy == 0: # find identical points
                identical += 1
                continue
            # reduce slope
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            if dx < 0 or (dx == 0 and dy < 0): # normalize slope
                dx, dy = -dx, -dy
            slope = (dx, dy)
            if slope in slopes:
                slopes[slope] += 1
            else:
                slopes[slope] = 1
        max_num_points = identical
        if slopes:
            max_num_points = identical + max(slopes.values())
        ans = max(ans, max_num_points)
    return ans

def main():
    points1 = [[1, 1], [2, 2], [3, 3]]
    points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    points3 = [[0,0], [1,-1], [-1,1]]
    print(maxPoints(points1))
    print(maxPoints(points2))
    print(maxPoints(points3))

if __name__ == "__main__":
    main()