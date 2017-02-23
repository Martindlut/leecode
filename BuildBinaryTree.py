from collections import deque


def getinput():
    number = raw_input()
    return number


def buildtree():
    rawlist = getinput()
    nodes=rawlist.split(',')
    list = deque()
    for i in range(0, len(nodes)):
        list.append(int(nodes[i]))
    return list


def getleftchild(list, i):
    if len(list) > 2 * i + 1:
        return list[2*i+1]
    else:
        return None


def getrightchild(list, i):
    if len(list) > 2 * i +2:
        return list[2*i +2]
    else:
        return None


def traversetree(tree, i, list, sum, solutionlist):
    if tree is None or len(tree) <= i:
        return
    list.append(tree[i])

    if int(sum) == tree[i] and 2*i+1 >= len(tree) and 2*i +2 >= len(tree):
        record = ','.join([str(item) for item in list])
        solutionlist.append(record)
        list.pop()
        return

    traversetree(tree, 2*i + 1, list, sum - tree[i],solutionlist)
    traversetree(tree, 2*i + 2, list, sum - tree[i],solutionlist)

    list.pop()


def solution():
    total = int(getinput())
    tree = buildtree()
    solutionlist=[]
    traversetree(tree, 0, deque(), total, solutionlist)
    if len(solutionlist) > 0:
        for item in solutionlist:
            print(item)
    else:
        print('error')

if __name__ == '__main__':
    solution()