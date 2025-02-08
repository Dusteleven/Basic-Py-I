


def anagrams (a,b):
    found = False

    if len(a)==len(b):
        found = True
        for c in a:
            if c not in b:
                found = False

        if found:
            for c in b:
                if c not in a:
                    found = False
        
    return found



if __name__ == "__main__":
    a = "tree"
    b = "three"
    result = anagrams(a,b)
    print(result)