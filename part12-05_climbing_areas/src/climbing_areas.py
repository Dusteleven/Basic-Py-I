class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        # last route
        return routes_in_order[-1]

    def __str__(self):
        hardest_route = self.hardest_route()
        return f"{self.name} {self.routes()} routes, hardest {hardest_route.grade}"





def sort_by_most_difficult(routes:list):

    def order_dif(r:ClimbingArea):
        grade_str= r.hardest_route().grade
        return (grade_to_num(grade_str))
    
    return sorted(routes, key=order_dif, reverse=True)


def grade_to_num(grade:str):

    grade_scale = {
            "5+": 1, "5": 2, "5A": 3, "5A+": 4, "5B": 5, "5B+": 6,
            "6A": 7, "6A+": 8, "6B": 9, "6B+": 10, "6C": 11, "6C+": 12,
            "7A": 13, "7A+": 14, "7B": 15, "7B+": 16, "7C": 17, "7C+": 18,
            "8A": 19, "8A+": 20, "8B": 21, "8B+": 22, "8C": 23, "8C+": 24
    }

    return grade_scale.get(grade,0)






def sort_by_number_of_routes(routes:list):

    def num_routes(r:ClimbingArea):
        return r.routes()
    
    return sorted(routes, key=num_routes)




if __name__ == "__main__":
    ca1 = ClimbingArea("Olhava")
    ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
    ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
    ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))

    ca2 = ClimbingArea("Nummi")
    ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))

    ca3 = ClimbingArea("Nalkkila slab")
    ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
    ca3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
    ca3.add_route(ClimbingRoute("Piggy not likey", 12 , "6B+"))
    ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))

    areas = [ca1, ca2, ca3]
    for area in sort_by_most_difficult(areas):
        print(area)