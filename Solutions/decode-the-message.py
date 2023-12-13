class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        joined_key = ''.join(key.split())
        hashmap = {" ":" "}
        result = ""
        j = 0
        alpha = range(ord('a'),ord('z')+1)
        for i in joined_key:
            if i not in hashmap:
                hashmap[i] = chr(alpha[j])
            else:
                continue
            j +=1    
        for mess in message:
            if mess in hashmap:
                result+=hashmap[mess]
        return result
       
            
            
        
        
        
        
        
    