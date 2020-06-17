class Solution(object):
    def decodeString(self, s):
        checkstr = self.checkint(s)
        if checkstr < 0:
            return s
    
        current = s[:checkstr] #current is string until it finds an int
        
        openBracket = s.find('[')
        closeBracket = self.findClosingBracket(s)
        num = int(s[checkstr:openBracket]) #convert numbers to int
        
        #multiplies num with the letters between the open/close brackets, 
        return current + (num * self.decodeString(s[openBracket + 1:closeBracket])) + self.decodeString(s[closeBracket + 1:])
        
    def findClosingBracket(self, s): #finds the final closing bracket
        stack = 0
        
        for i, char in enumerate(s):
            if char in ['[', ']']:
                if char == '[':
                    stack += 1
                elif char == ']':
                    stack -= 1
                if stack == 0:
                    return i
        return -1
    
    def checkint(self, s): #method to parse through string and make sure there are digits
        index = -1
        
        for i, char in enumerate(s):
            if '0' <= char <= '9':
                index = i
                break
        return index