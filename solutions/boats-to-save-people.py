class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start=count = 0
        end = len(people)-1
        while start <= end:  
            if people[start]+people[end] > limit:
                end-=1
                count+=1
            elif people[start]+people[end] <= limit:
                count+=1
                start +=1
                end -=1   
        return count

           
        