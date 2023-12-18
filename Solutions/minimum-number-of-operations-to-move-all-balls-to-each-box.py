class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        for i in range(len(boxes)):
            sumi = 0
            for j in range(len(boxes)):
                if(boxes[j] == '1'):
                    sumi += abs(j - i)
            answer.append(sumi)
        
        return answer
        
        