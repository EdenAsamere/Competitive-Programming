class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = {}
        for point in points:
            distance_from_origin = (point[0] ** 2 + point[1] ** 2) ** 0.5
            if distance_from_origin in closest:
                closest[distance_from_origin].append(tuple(point))
            else:
                closest[distance_from_origin] = [tuple(point)]
        
        sorted_closest = sorted(closest, key=lambda x: x)
        result = []
        for key in sorted_closest:
            result.extend(closest[key])
            
        return result[:k]
