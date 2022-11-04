
# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):           #-3 is 3rd last index
    if (len(s) > 3) and (s[-3:] == 'ing'):  #if length > 3 AND  last 3 characters (substring) is ing 
        s+='ly'
    elif (len(s) > 3):
        s+='ing'
    
    return s 



# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!


def not_bad(txt):
    
    n = txt.find('not')  # find returns the index of where the argument starts in a string
    b = txt.find('bad')
    #print ('not is at index {}, bad is at index {}'.format(n,b))

    if b > n:
        new_txt = txt[0:n] + 'good' + txt[(b+3):]
        return new_txt
    else:
        return txt


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    len_a = len(a)
    len_b = len(b)
    half_a = int (len_a/2) # implicit decleration of float to int. 5/2 = 2.5 ===> 2 
    half_b = int (len_b/2)
    
    if ((len_a % 2) == 0):
        a_front = a[0:half_a] # slicing only works on int arguments
        a_back = a[half_a:]
    else:
        a_front = a[0:half_a+1]
        a_back = a[half_a+1:]

    if ((len_b % 2) == 0):
        b_front = b[0:half_b]
        b_back = b[half_b:]
    else:
        b_front = b[0:half_b+1]
        b_back = b[half_b+1:]

    return (a_front + b_front + a_back + b_back)
	




def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')


  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')



if __name__ == '__main__':
  main()