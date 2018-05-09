from collections import defaultdict

def between(low : int, high : int) -> bool:
    if low > high:
        raise AssertionError
    def inside (number : int) -> bool:
        return low <= number <= high
    return inside


def both(p1 : callable, p2: callable):
    def predicates(number : int) -> bool:
        return p1(number) and p2(number)
    return predicates


def sort_descendants(d : {str:[int]}) -> [str]: 
    return sorted(sorted(d), key = lambda x: sum(d.get(x)))
        
def sort_generations(d : {str:[int]}) -> [(str,[int])]:
    return sorted(d.items(), key = lambda x: (-len(x[1]), -sum(x[1]), x[0]))


def big_family(d : {str:[int]}) -> {str}:
    return {name for name in d if sum(d[name]) > 10}
    
def big_word_map(words : str) -> {str:{str}}:
    big_words = defaultdict(set)
    for word in words.split():
        if len(word) > 3:
            big_words[word] = set(word)
    return big_words


def near1(s : str, dist : int) -> {str:{str}}:
    words = dict()
    for number in range(len(s)):
        if s[number] not in words.keys():
            words[s[number]] = set()
        for num in range(-dist, dist + 1):
            if 0 <= number + num < len(s):
                words[s[number]].add(s[number + num])
    return words

def near2(s : str, dist : int) -> {str:{str}}:
    words = defaultdict(set)
    for number in range(len(s)):
        for num in range(-dist, dist + 1):
            if 0 <= number + num < len(s):
                words[s[number]].add(s[number + num])
    return words

def alt_dictionary (d:{(str,str):int}) -> {str:{str:int}} :
    alt = defaultdict(dict)
    for caller, called in d.keys():
        alt[caller][called] = d[(caller,called)]
    return alt
        
    

if __name__ == '__main__':
    from goody import irange
    from predicate import is_prime

    # Feel free to test other cases as well
    
    print('Testing between: teenager')
    teenager = between(13,19) 
    print( [(a,teenager(a)) for a in irange(12,20)] )
    
    print('\nTesting between: middle_ager')
    middle_ager = between(30,50) 
    print( [(a,middle_ager(a)) for a in irange(29,51)] )
        
    print('\nTesting both: prime and between 50 and 60 inclusive')
    check = both(is_prime, lambda x : 50 <= x <= 60) 
    print([(i,check(i)) for i in irange(48,62)])
        
    print('\nTesting both: lower-case and consonant')
    check = both(lambda x : 'a' <= x <= 'z', lambda x : x not in 'aeiou') 
    print([(c,check(c)) for c in "Mr. Smith Goes to Washington"])
        

    print('\nTesting sort_descendants: ')
    family = dict(David=[6,4,8],Muriel=[3,5],Barbara=[5,3],Chester=[6,6,6],Ingrid=[4,4,4,2,4])
    print(sort_descendants(family))

    print('\nTesting sort_descendants: ')
    family = dict(Allen=[6,4,8],Dody=[3,5],Emile=[5,3],Harold=[6,6,6],Louis=[4,4,4,2,4])
    print(sort_descendants(family))
       
    print('\nTesting sort_generations:')
    family = dict(David=[6,5,8],Muriel=[3,5],Barbara=[5,3],Chester=[6,6,6],Ingrid=[4,4,4,2,4])
    print(sort_generations(family))
    
    print('\nTesting sort_generations:')
    family = dict(Allen=[12],Dody=[15],Emile=[8],Harold=[6,6,6],Louis=[4,4,4,2,4],Robert=[6,12])
    print(sort_generations(family))
    
    
    print('\nTesting big_family:')
    family = dict(David=[6,5,8],Muriel=[3,5],Barbara=[5,3],Chester=[6,6,6],Ingrid=[4,4,4,2,4])
    print(big_family(family))

    print('\nTesting big_family:')
    family = dict(Allen=[12],Dody=[15],Emile=[8],Harold=[6,6,6],Louis=[4,4,4,2,4],Robert=[6,12])
    print(big_family(family))

    print('\nTesting big_word_map:')
    print(sorted(big_word_map('To be or not to be that is the question').items()))

    print('\nTesting big_word_map:')
    print(sorted(big_word_map('When in the course of human events').items()))

    
    print('\nTesting near1: radar 1-3')
    print(sorted(near1('radar',1).items()))
    print(sorted(near1('radar',2).items()))
    print(sorted(near1('radar',3).items()))
    
    print('\nTesting near1: whiplash 1-7')
    print(sorted(near1('whiplash',1).items()))
    print(sorted(near1('whiplash',2).items()))
    print(sorted(near1('whiplash',3).items()))
    print(sorted(near1('whiplash',4).items()))
    print(sorted(near1('whiplash',5).items()))
    print(sorted(near1('whiplash',6).items()))
    print(sorted(near1('whiplash',7).items()))
    
    print('\nTesting near2: radar 1-3')
    print(sorted(near2('radar',1).items()))
    print(sorted(near2('radar',2).items()))
    print(sorted(near2('radar',3).items()))
    
    print('\nTesting near2: whiplash 1-7')
    print(sorted(near2('whiplash',1).items()))
    print(sorted(near2('whiplash',2).items()))
    print(sorted(near2('whiplash',3).items()))
    print(sorted(near2('whiplash',4).items()))
    print(sorted(near2('whiplash',5).items()))
    print(sorted(near2('whiplash',6).items()))
    print(sorted(near2('whiplash',7).items()))
    
    print('\nTesting ald_dictionary:')
    calls = {('a','b'):3, ('b','c'): 2, ('a','c'): 5} 
    print(sorted(alt_dictionary(calls).items()))

    print('\nTesting ald_dictionary:')
    calls = {('a','b'):3, ('b','c'): 2, ('a','c'): 5, ('a','d'):2, ('d','a'):3, ('c','d'):4, ('d','b'):5} 
    print(sorted(alt_dictionary(calls).items()))


    
    print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()