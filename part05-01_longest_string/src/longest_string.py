# Write your solution here


def longest(SL):
  
    w = SL[0]

    for s in SL:

        if len(s) > len(w):
            w = s
    return w


if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    print(longest(strings))