class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        watering_can = capacity
        steps = 0
        for i,plant in enumerate(plants):
            if capacity >= plant:
                steps += 1
                capacity -= plant
            else:
                steps += i+(i+1) 
                capacity = watering_can-plant
        return steps
                
   