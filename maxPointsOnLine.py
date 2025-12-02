#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
149. Max Points on a Line
Hard
Topics
premium lock iconCompanies

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

class Solution:
    def create_line(self, x, y) -> list[list[float], list[float]]:
        starting_point = x
        direction = []
        for i in range(len(x)):
            direction.append(y[i]-x[i])
        return [starting_point, direction]


    def is_point_on_line(self, p, starting_point, direction) -> bool:
        mu = set({})
        for i in range(len(p)):
            if direction[i] != 0:
                mu.add((p[i]-starting_point[i])/direction[i])
            elif p[i]-starting_point[i] == 0:
                continue
            else: return False
        if len(mu) > 1:
            return False
        return True

    def max_points(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2: return n
        max_points_on_line = 0
        for i in range(n-1):
            for j in range(i+1, n, 1):
                starting_point, direction = self.create_line(points[i], points[j])
                points_on_line = 0
                for k in range(n):
                    if k == i or k == j:
                        points_on_line += 1
                    else:
                        if self.is_point_on_line(points[k], starting_point, direction):
                            points_on_line += 1
                if points_on_line > max_points_on_line:
                    max_points_on_line = points_on_line
        return max_points_on_line

if __name__ == "__main__":
    points1 = [[1,1],[2,2],[3,3]]
    points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    sol = Solution()
    print(sol.max_points(points2))