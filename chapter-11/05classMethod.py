class Employee:
    a = 1
    @classmethod  # class metod use to access class attribute
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = Employee()
e.a = 45


e.show()