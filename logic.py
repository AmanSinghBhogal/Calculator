def calculate(inp):
    syntax_Error = "Invalid Expression"
    try:
        result = eval(inp)
    except:
        return syntax_Error

    return result