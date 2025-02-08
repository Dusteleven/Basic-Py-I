# WRITE YOUR SOLUTION HERE:

class ListHelper:


    @classmethod
    def greatest_frequency(cls, my_list: list):
        highc = 0
        num=""
        for i in my_list:
            if my_list.count(i)>highc:
                highc = my_list.count(i)
                num = i
        
        return num


    @classmethod
    def doubles(cls, my_list: list):
        doubles =[]
        c=0
        for i in my_list:
            if my_list.count(i)>=2 and i not in doubles:
                c +=1
                doubles.append(i)
        
        return c