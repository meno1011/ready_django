class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4
    
#print(dir(Car))
#dir()은 모든 property를 보여준다

    def __init__(self, *args, **kwargs):
        print(kwargs)
        #kwargs의 구조는 dictionary이다 key , value로 get을 이용해서 값을 가져올수 있다.
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color","black")
        self.price = kwargs.get("price","$20")
    
    #method를 보여주기 class 안에 tab으로 구분해서 들어가있으면 method가 된다.
    def __str__(self):
        return f"Car with {self.wheels} wheels"

    def take_off(self):
        return "taking off"

class Convertible(Car):

    def __init__(self, **kwargs):
        #super는 부모클래스의 method를 호출할때 쓰는 함수이다.
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"

porche = Convertible(color = "GREEN", price = "$40")
print(porche.color)