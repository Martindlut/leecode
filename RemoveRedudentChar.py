
def removeduplicatechar():
    inputstr= raw_input()
    charlist = set()
    for char in inputstr:
        charlist.add(char)

    print(''.join(sorted([ item for item in charlist])))


if __name__ == '__main__':
    removeduplicatechar()