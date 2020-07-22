from Logic.LogicClass import *


class MainClass(LogicClass):
    logic_class = LogicClass()

    def main_menu(self):
        print(self.logic_class.normal_adding(1, 1))
        print(self.logic_class.adding_two_for_result(1))
        print(self.logic_class.set_list_rand_ten_num())
        print(self.logic_class.set_variable(22))
        print(self.logic_class.get_variable())
        print(self.logic_class.name())


def main_menu():
    main_class = MainClass()
    main_class_1 = MainClass()

    print(main_class)
    print(main_class_1)
    main_class.main_menu()
    main_class_1.main_menu()


main_menu()
