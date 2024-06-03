#def atwentycharacterfunc():
#    pass

def f() -> int:
    maxlen = 0
    # see https://docs.python.org/3/library/functions.html?highlight=globals#globals
    for k,v in globals().items():
        if str(v).startswith('<function'):
            curlen = len(k)
            if curlen >= maxlen:
                maxlen = curlen
    return maxlen

if __name__ == '__main__':
    print(f())
