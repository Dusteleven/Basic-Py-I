# Write your solution here

def no_vowels(st):

    st=st.replace('a',"")
    st=st.replace('e',"")
    st=st.replace('i',"")
    st=st.replace('o',"")
    st=st.replace('u',"")
    return st

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))