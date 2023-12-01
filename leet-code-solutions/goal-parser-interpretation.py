class Solution:
    def interpret(self, command: str) -> str:
        pre = ""
        for i in range(len(command)):
            if command[i] == "G":
                pre+=command[i]
            elif command[i] == "(" and command[i+1] == ")":
                pre+="o"
            elif command[i] =="(" and command[i+1] =="a":
                pre +='al'
        return pre
            
        