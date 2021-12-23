# sWAP cASE
# Swap the letter cases of a given string.
#
# https://www.hackerrank.com/challenges/swap-case/problem
#

def swap_case(s):
    return s.swapcase()

# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
