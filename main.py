def plus (*args):
    result = 0;
    for number in args:
        result += number
    print(result)
    return result
# *args, **args 
plus(1, 2, 1,1,1,1,1,1,3,4,2345,35,2)

