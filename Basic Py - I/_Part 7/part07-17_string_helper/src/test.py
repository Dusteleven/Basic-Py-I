import string_helper

if __name__ == "__main__":

    my_string = "Well hello there!"

    print(string_helper.change_case(my_string))

    p1, p2 = string_helper.split_in_half("abcdefg")

    print(p1)
    print(p2)

    m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)