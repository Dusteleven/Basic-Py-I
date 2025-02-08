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
        
    def add_order(self, description: str, programmer:str, workload: int):
        order = Task(description, programmer, workload)
        self.orders.append(order)

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        name_list = []

        for order in self.orders:
            name_list.append(order.programmer)
        f_list = list(set(name_list))
        return f_list

    def mark_finished(self, id: int):
        id_found = False
        for order in self.orders:
            if order.id == id:
                id_found = True
                order.mark_finished()
        if not id_found:        
            raise ValueError("id not found")

    def finished_orders(self):
        fin_list = []
        for order in self.orders:
            if order.completed == True:
                fin_list.append(order)
        return fin_list



    def unfinished_orders(self):
        nfin_list = []
        for order in self.orders:
            if order.completed == False:
                nfin_list.append(order)
        return nfin_list


    def status_of_programmer(self, programmer: str):
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
                    hours_fin += order.workload
                else:
                    num_unfin +=1
                    hours_unfin += order.workload

        if not programmer_found:
            raise ValueError("Programmer not found)")
        return (num_fin, num_unfin, hours_fin, hours_unfin)


    # number finished
    # number unfin
    # est time finished
    # est time unfin
        

if __name__ == "__main__":
    t = OrderBook()
    t.add_order("program web store", "Andy", 10)
    t.unfinished_orders()