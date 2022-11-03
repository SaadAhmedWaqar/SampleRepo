
# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works..


def match_ends(words):
    print (words)
    c = 0
    for w in words:
        if (len(w) >= 2) and (w[0] == w[-1]):
            c+=1       
    return (c)


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.


def front_x(orignal):
    words = orignal
    sorted_list = []

    #print ('NEW WORD LIST',orignal)
    for w in orignal:
        #print ('w is',w)
        if w[0] == 'x':
            #print ('word starting with x',w)
            sorted_list.append(w)
            #print('sorted list with x is',sorted_list)
            #words.remove(w)
            #print('after removal of x',words)
    for x in sorted_list:
        words.remove(x)


        #if x[0] == 'x':
         #   words.remove(x)
          #  print('after removal of x',words)

    words.sort()
    #print('sorted without x',words)
    sorted_list.sort()
    #print('X sorted ', sorted_list)
    output = sorted_list + words

    return output




# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    tuples.sort(key = last_elem)
    return tuples

def last_elem(list):
	return list[-1]

#print (srt.sort( key = last_elem))



def main():
  print ('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print ('front_x')
  test(front_x(['xaa', 'ccc', 'axx', 'xzz', 'bbb']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),  ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

  print ('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


def test(got, expected):
    if got == expected:
        prefix = (' OK ')
    else:
        prefix = ('  X ')
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



if __name__ == '__main__':
  main()

