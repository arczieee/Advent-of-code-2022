from anytree import Node, RenderTree, search, find, find_by_attr
import numpy as np

with open('input.txt') as f:
    input_list = [line.rstrip() for line in f]

i = 1
currentDir ='/'
previousDir = ''

root = Node('/',ftype='folder',size=0)
currentNode = root
currentPath = root.path
currentPath = currentPath[0].name
temptemp=currentPath
print(currentPath)
parent = root

parentStack = []
parentStack.append(parent)

while i<len(input_list):
    tempStr = input_list[i]
    #print(tempStr)
    if tempStr == '$ cd ..':
        print(parentStack)
        tempName = previousDir
        previousDir = currentDir
        currentDir = tempName

        #searchPrnt = search.find(root,lambda node: node.name == currentDir)

        parent = parentStack.pop()
        parent = parentStack.pop()

        parentStack.append(parent)


    elif tempStr[0:4] == '$ cd':

        print(parentStack)
        previousDir = currentDir
        currentDir = tempStr[5:(len(tempStr))]
        nameSearch = currentDir
        currentPath = currentPath + '/' + currentDir

        childs = parent.children
        k = 0
        while k<len(childs):
            tempNodeParent = childs[k]
            if tempNodeParent.name == currentDir:
                parent = tempNodeParent
            k=k+1

        parentStack.append(parent)
        #parent = find(root,lambda node: node.name == nameSearch)

    if tempStr[0:4] == 'dir ':
        folderName = tempStr[4:(len(tempStr))]
        print('current folder = %s\t current path = %s'%(folderName,currentPath))
        #parent = find(root,lambda node: node.name == currentPath)
        temp_node = Node(folderName,parent,ftype='folder',size=0)

    if (ord(tempStr[0])>47)and(ord(tempStr[0])<58):
        x = tempStr.split(' ')
        print('current file = %s\t current path = %s'%(x[1],currentPath))
        #parent = find(root,lambda node: node.name == currentPath)
        temp_node = Node(x[1],parent,ftype='file',size=x[0])

    i=i+1

rootChildren = root.children

searchResult = search.findall(root,lambda node: node.ftype == 'file')

i = 0
while i<len(searchResult):
    cNode = searchResult[i]
    pNode = searchResult[i].parent
    pNode.size = int(pNode.size) + int(cNode.size)
    #print('%s in %s folder'%(cNode.name,pNode.name))
    print(cNode.path)
    
    i = i+1

searchResult = root.descendants

i = 0
maxDepth = 0

while i < len(searchResult):
    cNode = searchResult[i]
    if cNode.depth > maxDepth:
        maxDepth = cNode.depth
    i = i+1


searchResult = search.findall(root,lambda node: node.ftype == 'folder')
i = 0

while maxDepth > 0:

    while i < len(searchResult):
        cNode = searchResult[i]
        if int(cNode.depth) == int(maxDepth):
            pNode = cNode.parent
            pNode.size = pNode.size + cNode.size
        i = i+1

    i = 0
    maxDepth = maxDepth - 1
print('\n\n')

for pre, fill, node in RenderTree(root):
    print("%s%s"% (pre, node))

print('\n\n')

for pre, fill, node in RenderTree(root):
    index = len(node.path)-1
    tempN = node.path[index]
    tempPrint = tempN.name

    print("%s%s (%s) (size = %s) (path = %s)" % (pre, node.name,node.ftype,node.size,tempPrint))

searchResult = search.findall(root,lambda node: node.ftype == 'folder')
i = 0
size = 0
while i<len(searchResult):
    cNode = searchResult[i]
    if cNode.size < 100000:
        size = size+cNode.size
    i = i+1

print('\n')
print('Size to delete = %d'%size)
print('\n')
print('Total size = %d'%root.size)

freeSpace = 70000000 - root.size
print('\n')
print('Free space = %d'%freeSpace)

minSize = 70000000

i = 0

while i<len(searchResult):
    cNode = searchResult[i]
    if (freeSpace + cNode.size > 30000000):
        if (cNode.size<minSize):
            minSize = cNode.size
    i = i+1

print(minSize)