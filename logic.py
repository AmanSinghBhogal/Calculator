def calculate(inp):

    # Error to Print for Invalid Syntax
    syntax_Error = "Invalid Expression"
    available_operations = ['+','-','*','/','%','(',')']

    nums = []           # Holds all the Numbers
    operato = []        # Holds all the Operators

    temp = ''           # String to Hold the Number

    # Seperate the Operators from the numbers:
    bracket = 0
    for i,j in enumerate(inp):
        if j in available_operations:
            if j == ')' and bracket == 0:
                return syntax_Error
            elif j == '(':
                bracket += 1
            elif bracket != 0 and j == ')':
                bracket -= 1
            if temp != '':
                nums.append(float(temp))
            temp = ''
            operato.append(j)
        else:
            temp += j
    
    # if Last element is not an operator append it to the Number's list
    if temp != '':
        nums.append(float(temp))
    # if the Brackets are not satisfied
    if bracket != 0:
        return syntax_Error

    print(nums)
    print(operato)