

def palindromes (s):
    return s == s[::-1]
        


def main():
    

    while True:
        st = input("Please type in a palindrome: ")
        result = (palindromes(st))

        if result:
            print(f"{st} is a palindrome!")
            break
        elif not result:
            print("that wasn't a palindrome")

main()


# Note, that at this time the main program should not be written inside
#if __name__ == "__main__":

    #st = "Python"
    #result = palindromes(st)
    #print(result)