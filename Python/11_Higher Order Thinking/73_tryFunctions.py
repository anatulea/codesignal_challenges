'''
You've been working on a numerical analysis when something went horribly wrong: your solution returned completely unexpected results. It looks like you apply a wrong function at some point of calculation. This part of the program was implemented by your colleague who didn't follow the PEP standards, so it's extremely difficult to comprehend.

To understand what function is applied to x instead of the one that should have been applied, you decided to go ahead and compare the result with results of all the functions you could come up with. Given the variable x and a list of functions, return a list of values f(x) for each x in functions.

Example

For x = 1 and
functions = ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"],
the output should be
tryFunctions(x, functions) = [0.84147, 0.5403, 2, 1].
'''
def tryFunctions(x, functions):
    return [eval(f)(x) for f in functions]
    # return  [fun(x) for fun in map(eval,functions)]
    
    '''eval(expression, globals=None, locals=None)
            -expression - the string parsed and evaluated as a Python expression
            -globals (optional) - a dictionary
            -locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.
        -The eval() method parses the expression passed to this method and runs python expression (code) within the program
    '''