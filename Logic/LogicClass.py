from random import randint


class LogicClass:
    NUMBER_TWO = 2
    list_with_random_num = []
    variable = None
    counter = 0
    name = None
    name_counter = 0

    @staticmethod
    def name_using_counter():
        LogicClass.name_counter += 1
        print(LogicClass.name_counter)

    @staticmethod
    def static():
        LogicClass.counter += 1
        return "Object number: " + str(LogicClass.counter)

    def __init__(self):
        print(LogicClass.static())

    def __del__(self):
        print("Remove LogicClass!!!")

    def normal_adding(self, number_1, number_2):
        return number_1 + number_2

    def adding_two_for_result(self, input_number):
        return input_number + self.NUMBER_TWO.__int__()

    def name(self):
        LogicClass.name_using_counter()
        self.name = "My name is: Kriss"
        print(self.name)

    def set_list_rand_ten_num(self):
        tmp_list = []
        for i in range(0, 11):
            tmp_list.append(randint(0, 100))
        self.list_with_random_num = tmp_list.copy()
        print(self.list_with_random_num)

    def set_variable(self, variable):
        self.variable = variable

    def get_variable(self):
        return self.variable
