def calculate(inp):

    # Error to Print for Invalid Syntax
    syntax_Error = "Invalid Expression"
    available_operations = ['+','-','*','/','%','(',')']

    nums = []           # Holds all the Numbers
    operato = []        # Holds all the Operators

    temp = ''           # String to Hold the Number

    # Seperate the Operators from the numbers:
    bracket = False
    for i,j in enumerate(inp):
        if j in available_operations:
            if j == ')' and bracket == False:
                return syntax_Error
            elif bracket == False and j == '(':
                bracket = True
            elif bracket ==  True and j == ')':
                bracket = False
            if temp != '':
                nums.append(float(temp))
            temp = ''
            operato.append(j)
        else:
            temp += j
    if temp != '':
        nums.append(float(temp))
    if bracket == True:
        return syntax_Error

    print(nums)
    print(operato)