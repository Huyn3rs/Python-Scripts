import re
from goody import irange

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the file pattern.txt


def pages (page_spec : str) -> [int]: #result in ascending order (no duplicates)
    page_list = []
    page_str = re.compile(r'^(?: )*([1-9][0-9]*)(?: )*(?:([\-:])(?: *)([1-9][0-9]*)(?: *))?$')
    pages = page_spec.split(',')
    for page in pages:
        p = page_str.match(page)
        assert p != None, 'Page Sequence does not match regular expression.'
        if p.group(2) == '-':
            assert int(p.group(1)) <= int(p.group(3)), 'pages: in page sequence {}-{}, {} > {}'.format(p.group(1), p.group(3), p.group(1), p.group(3))
            page_list.extend(list(irange(int(p.group(1)), int(p.group(3)))))
        elif p.group(2) == ':':
            page_list.extend(list(range(int(p.group(1)), int(p.group(1)) + int(p.group(3)))))
        else:
            page_list.append(int(p.group(1)))
    return sorted(set(page_list))


def expand_re(pat_dict:{str:str}):
    pattern = re.compile(r'#([^#]+)#')
    for pat in pat_dict:
        while pattern.search(pat_dict.get(pat)) != None:
            pat_dict[pat] = pattern.sub('(' + pat_dict.get(pattern.findall(pat_dict.get(pat))[0]) + ')', pat_dict.get(pat))
    
    



if __name__ == '__main__':
    print('Testing  examples of pages that returns lists')
#    pages('4-3')
    print("  pages('5,3,9'): ", pages('5,3,9'))
    print("  pages('3-5,10:2'): ", pages('3-5,10:2'))
    print("  pages('5  -8,10: 3,3'): ", pages('5  -8,10: 3,3'))
        
    print('\nTesting  examples of expand_re')
    pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary {'digit': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}
    
    pd = dict(integer       =r'[+-]?\d+',
              integer_range =r'#integer#(..#integer#)?',
              integer_list  =r'#integer_range#(?,#integer_range#)*',
              integer_set   =r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer'      : '[+-]?\\d+',
    #  'integer_range': '([+-]?\\d+)(..([+-]?\\d+))?',
    #  'integer_list' : '(([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*',   
    #  'integer_set'  : '{((([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'d': '(((correct)))',
    #  'c': '((correct))',
    #  'b': '(correct)',
    #  'a': 'correct',
    #  'g': '((((((correct))))))',
    #  'f': '(((((correct)))))',
    #  'e': '((((correct))))'
    # }

    print()
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
