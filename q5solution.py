from functools import reduce # for code_metric; map and filter do not need to be imported


def is_sorted(s):
    if s == []:
        return True
    elif min(s) == s[0]:
        return is_sorted(s[1:])
    else:
        return False

def merge (l1,l2):
    if l1 == [] and l2 == []:
        return []
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    
    final_l = []
    if l1[0] <= l2[0]:
        final_l.append(l1[0])
        final_l.extend(merge(l1[1:], l2))   
        
    elif l1[0] >= l2[0]: 
        final_l.append(l2[0])
        final_l.extend(merge(l1, l2[1:]))
    
    return final_l

def sort(l):
    if len(l) <= 1:
        return l
    
    l1 = l[:len(l)//2]
    l2 = l[len(l)//2:]
    
    if len(l1) == 1 and len(l2) == 1:
        return merge(l1, l2)
    
    n_l1 = sort(l1)
    n_l2 = sort(l2)
    
    return merge(n_l1, n_l2)


def compare(a,b):
    if a == '' and b == '':
        return '='
    elif a == '':
        return '<'
    elif b == '':
        return '>'
    
    elif a[0] > b[0]:
        return '>'
    elif a[0] < b[0]:
        return '<'
    
    elif a[0] == b[0]: 
        return compare(a[1:], b[1:]) 

def code_metric(file):
    filter_result = filter(lambda x: x != '\n', open(file).readlines())
    map_result = map(lambda x: (1, len(x.rstrip('\n'))), list(filter_result))
    return reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), map_result)
        




if __name__=="__main__":
    import predicate,random,driver
    from goody import irange
    
    print('\nTesting is_sorted')
    print(is_sorted([]))
    print(is_sorted([1,2,3,4,5,6,7]))
    print(is_sorted([1,2,3,7,4,5,6]))
    print(is_sorted([1,2,3,4,5,6,5]))
    print(is_sorted([7,6,5,4,3,2,1]))
    
    print('\nTesting merge')
    print(merge([],[]))
    print(merge([],[1,2,3]))
    print(merge([1,2,3],[]))
    print(merge([1,2,3,4],[5,6,7,8]))
    print(merge([5,6,7,8],[1,2,3,4]))
    print(merge([1,3,5,7],[2,4,6,8]))
    print(merge([2,4,6,8],[1,3,5,7]))
    print(merge([1,2,5,7,10],[1,2,6,10,12]))


    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = list(range(20))  # List of values 0-19
    for i in range(10):  # Sort 10 times
        random.shuffle(l)
        print(sort(l), sep='-->')
    
    
    print('\nTesting compare')
    print(compare('',''))
    print(compare('','abc'))
    print(compare('abc',''))
    print(compare('abc','abc'))
    print(compare('bc','abc'))
    print(compare('abc','bc'))
    print(compare('aaaxc','aaabc'))
    print(compare('aaabc','aaaxc'))
   
    
    print('\nTesting code_metric')
    print(code_metric('cmtest.py'))
    print(code_metric('collatz.py'))
    print(code_metric('q5solution.py'))  # A function analyzing the file it is in
