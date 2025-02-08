# Write your solution here


#main_vars={} 
#jump_list={}


#################initialize jump list within function and main_vars all to zero
###################################################################################
#if jump list empty
import string


def set_jump_list(input_sequence):
    jump_list={}
    for line in input_sequence:
        b = line.split(" ")
        a=b[0]
        if (a != "PRINT" and a != "MOV" and a != "ADD" and a != "SUB" and a != "MUL" and a != "JUMP" and a != "IF" and a != "END" ):
                jump_list[a.replace(":","")]=loc(a,input_sequence)
    return jump_list

def set_main_vars():
 
    m_vars={}
    alph_list = list(string.ascii_uppercase)
    for char in alph_list:
        m_vars[char]=0
    return m_vars



def run(run_sequence):
    index=0
    input_sequence=run_sequence
    global jump_list
    jump_list={}
    global main_vars
    main_vars = {}
    print_list=[]

    if not jump_list:
         jump_list = set_jump_list(input_sequence)
    if not main_vars:
         main_vars = set_main_vars()

    
    while index < len(input_sequence):
        line = input_sequence[index]
        run_list = line.split(" ")
        index = next(run_list, input_sequence, index,main_vars, print_list)
    return print_list

def next(run_list, input_sequence, index, main_vars, print_list):
    if run_list[0]== "PRINT":
        a=ctiip(run_list[1])
        if isinstance(a, str):
            print_list.append(main_vars[a])
        else:
            print_list.append(a)
        return (index+1)

    elif run_list[0]== "MOV":
        a=run_list[1]
        b=ctiip(run_list[2])
        MOV(a,b)
        return (index+1)

    elif run_list[0]== "ADD":
        a=run_list[1]
        b=ctiip(run_list[2])
        ADD(a,b)
        return (index+1)

    elif run_list[0]== "SUB":
        a=run_list[1]
        b=ctiip(run_list[2])
        SUB(a,b)
        return (index+1)

    elif run_list[0]== "JUMP":
        a=run_list[1]
        return JUMP(a, input_sequence)

    elif run_list[0]=="MUL":
        a=run_list[1]
        b=ctiip(run_list[2])
        MUL(a,b)
        return (index+1)

    elif run_list[0]== "IF":
        a=ctiip(run_list[1])
        b=run_list[2]
        c=ctiip(run_list[3])
        d=run_list[5]
        return if_jump(a,b,c,d, input_sequence, index)
        #(if_jump(a,b,c,d, input_sequence), input_sequence)
    
    elif run_list[0]== "END":
        index = len(input_sequence)
        return index
    
    elif isinstance(run_list[0], str):
        return index+1

def ctiip(val):
    try : 
        return int(val)
    except ValueError:
        return val

def if_jump(var, cond: str, val, loc: str, input_sequence: list, index: int):
    if isinstance(val, str):
        if eval(f"{main_vars[var]}{cond}{main_vars[val]}"):
            return JUMP(loc, input_sequence)
    
    elif eval(f"{main_vars[var]}{cond}{val}"):
        return JUMP(loc, input_sequence)
    
    return index+1

def JUMP(loc: str, input_sequence: list):
    move_index = jump_list[loc]
    return(move_index)

def PRINT(value: int):
    print(f"{value}")
    if value == 5:
        quit()

def MOV(var: str, value):    
    if isinstance(value, int):
        main_vars[var]=value
    else:
        main_vars[var]=main_vars[value]

def ADD(var: str, value: int):
    
    if isinstance(value, str):
        main_vars[var]+= main_vars[value]
    else:
        main_vars[var]+=value

def SUB(var: str, value: int):
    if isinstance(value, int):
        main_vars[var]-=value
    else:
        main_vars[var]-=main_vars[value]

def MUL(var: str, value: int):
    if isinstance(value, str):
        b = main_vars[value]
        main_vars[var]*=b
    else:
        main_vars[var]*=value

def loc(loc: str, runL: list):
    j_list={}
    index=runL.index(loc)
    loc=loc.replace(":","")
    j_list[loc] = index
    return index


            


if __name__ == "__main__":
    a=['MOV A 1', 'MOV B 1', 'start:', 'MUL A 2', 'ADD B 1', 'IF B != 101 JUMP start', 'PRINT A']
    result = run(a)
    print(result)