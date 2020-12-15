'''
One summer Felicia was visiting her granny's summer house. There were several old and withered vines growing in the garden, that no longer produced grapes. Felicia found it sad, and decided to decorate the vines with wooden grapes she carved out herself. She also watered them with cola, since cola makes everything better.

When winter came, Felicia left, but the vines were still there, better than ever before. Each year they grew higher and wider, and the pairs of neighboring vines entangled together, forming a single vine. The wooden grapes were also doing just fine: they remained firmly attached to the vines.

Now that n years has passed, Felicia is going to visit her granny again, and she is curious about how the vines are doing. Given the number of grapes she hang on the vines, return the number of grapes on each vine after n years, assuming that each year the (2 * i - 1)th and the (2 * i)th vines (1-based) merged into a single vine (for each integer i in range [1, <number_of_vines> / 2]).

Example

For vines = [1, 2, 3, 4, 5] and n = 2, the output should be
mergingVines(vines, n) = [10, 5].

After the first year vines two pairs of vines entangled: vines 1 and 2 and vines 3 and 4 (1-based). The last vine didn't have anything to entangle with. The vines could thus be represented as [3, 7, 5].
After the second year, another pair of vines entangled. The first and the second vines entangled, forming a single vine. It's possible to represent the vines as [10, 5], which is the answer.
'''
import functools
def mergingVines(vines, n):
    def nTimes(n):
       return lambda x: functools.reduce(lambda f, g: lambda x: f(g(x)), [x] * n, lambda x: x)

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)

'''
    Decorators (ex: @nTimes(n)) are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.

    In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
'''


'''
    def mergingVines(vines, n):
    def nTimes(n):
        def func_decor(func):
            def func_wrapper(vines):
                for _ in range(n):
                    vines = func(vines)
                return vines
            return func_wrapper
        return func_decor
            

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)
'''