class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Initialize column number
        colNum = 0
        
        # Initialize power of 26 exponent
        j = 0

        # Iterate through the characters in columnTitle in reverse order
        for i in range(len(columnTitle), 0, -1):
            # Calculate the contribution of the current character to the column number
            colNum += (ord(columnTitle[i-1]) - 64) * 26**j
            
            # Increment the power of 26 exponent
            j += 1

        # Return the calculated column number
        return colNum