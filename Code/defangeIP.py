class Solution:
    def defangIPaddr(self, address: str) -> str:
        self.address = address 
        a_Arr = address.split(".")
        
        output = ''
        for i in range(0,len(a_Arr)*2-1):
            if i%2 == 1:
                a_Arr.insert(i, "[.]")   
        
        for j in a_Arr:
            output += j
            
        return output


