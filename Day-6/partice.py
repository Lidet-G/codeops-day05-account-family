from abc import ABC, abstractmethod
class Report:
    def create(self):
        print("Creating report...")

class ReportSaver:
    def save(self):
        print("Report saved.")

class EmailSender:
    def send(self):
        print("Email sent.")

report = Report()
report.create()

save = ReportSaver()
save.save()

email = EmailSender()
email.send()

print("\n====================")



class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        print("Area of Circle")


class Square(Shape):

    def area(self):
        print("Area of Square")


class Triangle(Shape):

    def area(self):
        print("Area of Triangle")


shapes = [Circle(), Square(), Triangle()]

for shape in shapes:
    shape.area()


print("\n====================")



class AppSettings:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"

        return cls._instance


a = AppSettings()
b = AppSettings()

print(a.currency)
print(a is b)

print("\n====================")

class Circle:
    pass


class Square:
    pass


class Triangle:
    pass


class ShapeFactory:

    @staticmethod
    def create(kind):

        if kind == "circle":
            return Circle()

        elif kind == "square":
            return Square()

        elif kind == "triangle":
            return Triangle()

        else:
            raise ValueError("Invalid Shape")


shape = ShapeFactory.create("circle")
print(type(shape).__name__)


print("\n====================")


class NewsAgency:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, news):

        for sub in self.subscribers:
            sub.update(news)


class TV:

    def update(self, news):
        print("TV:", news)


class Radio:

    def update(self, news):
        print("Radio:", news)


agency = NewsAgency()

agency.subscribe(TV())
agency.subscribe(Radio())

agency.notify("Python 3.15 Released!")