def getlongestfnlen() -> int:
    getlongestfnlen._maxlen
    maxlen = getlongestfnlen._maxlen

    curlen = 0
    # see https://docs.python.org/3/library/functions.html?highlight=globals#globals
    for k,v in globals().items():
        if str(v).startswith('<function'):
            curlen = len(k)
            if curlen >= maxlen:
                maxlen = curlen
    return maxlen

getlongestfnlen._maxlen = 0


if __name__ == '__main__':
    print(getlongestfnlen())
