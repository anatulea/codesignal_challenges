'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''
def reverseInParentheses(s):
    stack = []
    for x in s:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop() # pop the (
            for item in tmp:
                stack.append(item)
        else:
            stack.append(x)

    return "".join(stack)


def reverseInParentheses2(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


def reverseInParentheses3(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseInParentheses3(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s


def reverseInParentheses4(s):
    end = s.find(")")
    start = s.rfind("(",0,end)
    if end == -1:
        return s
    return reverseInParentheses4(s[:start] + s[start+1:end][::-1] + s[end+1:])
