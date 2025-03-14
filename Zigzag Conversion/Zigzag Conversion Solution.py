class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """ 

        zigZagLength = numRows + max(numRows-2,0)
        
        #the length of a "zig" + the length of a "zag". for example, if numRows = 4, the pattern would look like this:
        #A    A      
        #A A  A A
        #AA   AA
        #A    A
        #the length of the zig part equals numRows and the zag part is two less

        #initializing a list of rows 
        row = [""]*numRows

        #iterating through the string
        for index, char in enumerate(s):

            #this is the position in the zigzag pattern described
            zigZagPosition = index % zigZagLength

            if zigZagPosition < numRows: # this character is in the zig part
                row[zigZagPosition] = row[zigZagPosition] + char
            else: #this character is in the zag part
                row[zigZagLength - zigZagPosition] = row[zigZagLength - zigZagPosition] + char
        
        #concatenating all the rows to form the final string
        answer = ""
        for r in row:
            answer = answer + r
        
        return answer


slt = Solution()


x = slt.convert("PAYPALISHIRING",2)
print(x)

x = slt.convert("PAYPALISHIRING",3)
print(x)

x = slt.convert("PAYPALISHIRING",4)
print(x)

x = slt.convert("PAYPALISNOTHIRIHGRIGHTNOW",5)
print(x)

x = slt.convert("PAYPALISNOTHIRIHGRIGHTNOW",6)
print(x)

x = slt.convert("A",1)
print(x)