# Write your solution here

import string
main_vars={} 
jump_list={}

def run(run_sequence):

    input_sequence=run_sequence

    for line in run_sequence:
        b = line.split(" ")
        a=b[0]
        if (a != "PRINT" and a != "MOV" and a != "ADD" and a != "SUB" and a != "MUL" and a != "JUMP" and a != "IF" and a != "END" ):
                loc(a,input_sequence)
    
    for line in run_sequence:
            run_list=[]
            run_list = line.split(" ")
            next(run_list, input_sequence)

def loop_run(new_sequence:list, input_sequence:list):
    

    if main_vars["A"] == 47:
        quit()

    for line in new_sequence:
        run_list=[]
        run_list = line.split(" ")
        next(run_list, input_sequence)            

def ctiip(val):
    try : 
        return int(val)
    except ValueError:
        return val

def if_jump(var, cond: str, val, loc: str, input_sequence: list):
    if isinstance(val, str):
        if eval(f"{main_vars[var]}{cond}{main_vars[val]}"):
            JUMP(loc, input_sequence)
    else:
        if eval(f"{main_vars[var]}{cond}{val}"):
            JUMP(loc, input_sequence)

def JUMP(loc: str, input_sequence: list):
    move_index = jump_list[loc]

    b=len(input_sequence)

    return_list=[]
    return_list=input_sequence[move_index+1:b] #### send cut list to loop run
    c=return_list
    loop_run(c, input_sequence)

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
    main_vars[var]-=value

def MUL(var: str, value: int):
    if isinstance(value, str):
        b = main_vars[value]
        main_vars[var]*=b
    else:
        main_vars[var]*=b

def loc(loc: str, runL: list):
    index=runL.index(loc)
    loc=loc.replace(":","")
    jump_list[loc] = index

def next(run_list, input_sequence):
    if run_list[0]== "PRINT":
        a=ctiip(run_list[1])
        if isinstance(a, str):
            print(main_vars[a])
        else:
            print(a)

    elif run_list[0]== "MOV":
        a=run_list[1]
        b=ctiip(run_list[2])
        MOV(a,b)

    elif run_list[0]== "ADD":
        a=run_list[1]
        b=ctiip(run_list[2])
        ADD(a,b)

    elif run_list[0]== "SUB":
        a=run_list[1]
        b=ctiip(run_list[2])
        SUB(a,b)

    elif run_list[0]== "JUMP":
        a=run_list[1]
        b=input_sequence
        c=JUMP(a,b)
        loop_run(c, input_sequence)

    elif run_list[0]=="MUL":
        a=run_list[1]
        b=ctiip(run_list[2])
        MUL(a,b)

    elif run_list[0]== "IF":
        a=ctiip(run_list[1])
        b=run_list[2]
        c=ctiip(run_list[3])
        d=run_list[5]

        (if_jump(a,b,c,d, input_sequence), input_sequence)

    elif run_list[0]== "END":
        quit()
            


if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)