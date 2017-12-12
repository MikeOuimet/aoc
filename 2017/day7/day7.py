
def get_parent(d, node):
    try:
        parent = d[node]
        return False, parent
    except:
        return True, node

def get_weight(d, node):
    data = d[node]
    weight = data[0]
    children = data[1]
    tmp = weight
    for child in children:
        tmp += get_weight(d, child)
    return tmp
        
def find_culprit(weights,children, parent):
    d = {}
    for i, weight in enumerate(weights):
        try:
            d[weight].append(children[i])
        except:
            d[weight] = [children[i]]
    
    for weight in weights:
        if len(d[weight])==1:
            return False, d[weight][0]
    return True, parent
        
        
            

f = open('input.txt', 'r')
rev_tree = {}
tree = {}
for line in f:
    split = line.split()
    parent = split[0]
    weight = int(split[1][1:-1])
    #print(split)
    if len(split)>3:
        temp = split[3:]
        #print(len(temp))
        children = []
        for child in temp:
            #print(child)
            if child[-1] == ',':
                children.append(child[:-1])
            else:
                children.append(child)
        #print(children)
        for child in children:
            rev_tree[child] = parent
    else:
        children = []
    tree[parent] = [weight, children]


parent = 'eugwuhl'
found_culprit = False
#print(tree[top])
#data = tree[top]
#children = data[1]
#weights = []
#for child in children:
#    weights.append(get_weight(tree, child))
#print(weights)
#found_culprit, culprit = find_culprit(weights, children, top)

while not found_culprit:
    data = tree[parent]
    children = data[1]
    weights = []
    for child in children:
        weights.append(get_weight(tree, child))
        found_culprit, culprit = find_culprit(weights, children, parent)
    print(weights)
    print(children)
    print(culprit)
    print('')
        
    parent = culprit

print(tree[culprit][0] - 8)



#child = 'thzvetu'
#done = False
#while not done:
#    done, child = get_parent(rev_tree, child)
#print(child)

