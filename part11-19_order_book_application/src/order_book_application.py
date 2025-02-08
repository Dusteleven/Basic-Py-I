# Write your solution here
# If you use the classes made in the previous exercise, copy them here
# Write your solution here:

class Task:
    id = 1

    def __init__(self, description: str, programmer:str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.id
        self.completed = False
        Task.id+=1

    def __str__(self):
        if self.is_finished():
            return(f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED")
        else:
            return(f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED")
        
    def is_finished(self):

        return self.completed
    
    def mark_finished(self):
        self.completed = True


class OrderBook:

    def __init__(self):
        self.orders = []
        
    def add_order(self):
        try:

            description = input("description: ").strip()

            if not description:
                raise ValueError ("erroneous input")
            
            p_and_w = input("programmer and workload estimate: ")

            if not p_and_w:
                raise ValueError ("erroneous input")


            plist = p_and_w.split(" ")
            if len(plist) !=2:
                raise ValueError("erroneous input")

            programmer = plist[0]
            if not programmer:
                raise ValueError ("erroneous input")
            if not isinstance(programmer, str):
                raise ValueError ("erroneous input")

            workload = plist [1]
            if not workload:
                raise ValueError ("erroneous input")
            if not workload.isdigit():
                raise ValueError ("erroneous input")
            
            order = Task(description, programmer, workload)
            self.orders.append(order)
            print("added!")
        except ValueError as e:
            print("erroneous input")

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        name_list = []

        for order in self.orders:
            name_list.append(order.programmer)
        f_list = list(set(name_list))
        for i in f_list:
            print (i)
        #return f_list

    def mark_finished(self):
        try:

            id = int(input("id: "))
            if not id:
                raise ValueError ("erroneous input")

            id_found = False
            for order in self.orders:
                if order.id == id:
                    id_found = True
                    order.mark_finished()
                    print("marked as finished")
            if not id_found:        
                raise ValueError("id not found")
        except ValueError as e:
            print("erroneous input")

    def finished_orders(self):
        fin_list = []
        for order in self.orders:
            if order.completed == True:
                fin_list.append(order)

        if not (fin_list):
            print("no finished tasks")
        else:
            for i in fin_list:
                print (i)



    def unfinished_orders(self):
        nfin_list = []
        for order in self.orders:
            if order.completed == False:
                nfin_list.append(order)
        if not (nfin_list):
            print("no unfinished tasks")
        else:
            for i in nfin_list:
                print (i)
                


    def status_of_programmer(self):
        try:
            programmer = input("programmer: ").strip()
            if not programmer:
                raise ValueError("erroneous input")
            
            num_fin = 0
            num_unfin = 0
            hours_fin = 0
            hours_unfin = 0
            programmer_found = False

            for order in self.orders:
                if order.programmer == programmer:
                    programmer_found = True
                    if order.is_finished():
                        num_fin += 1
                        hours_fin += int(order.workload)
                    else:
                        num_unfin +=1
                        hours_unfin += int(order.workload)

            if not programmer_found:
                raise ValueError("Programmer not found)")
            print(f"tasks: finished {num_fin} not finished {num_unfin}, hours: done {hours_fin} scheduled {hours_unfin}")
        except ValueError as e:
            print("erroneous input")
        
        


class Orderbook_Application:
    def __init__(self):
        self.__orderbook = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def exit(self):
        print("execution ended")

    def execute(self):
        self.help()
        while True:
            print("")
            try:
                u_input = input("command: ").strip()
                if not u_input.isdigit():
                    raise ValueError("erroneous input")

                u_input = int(u_input)
                
                if u_input == 0:
                    self.exit()
                    break
                elif u_input == 1:
                    self.__orderbook.add_order()
                elif u_input == 2:
                    self.__orderbook.finished_orders()
                elif u_input == 3:
                    self.__orderbook.unfinished_orders()
                elif u_input == 4:
                    self.__orderbook.mark_finished()
                elif u_input == 5:
                    self.__orderbook.programmers()
                elif u_input == 6:
                    self.__orderbook.status_of_programmer()
                else: 
                    print("erroneous input")
                    self.help()
            except ValueError as e:
                print(f"erroneous input")

    

application = Orderbook_Application()
application.execute()