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

porche = Car(color = "GREEN", price = "$40")
print(porche.color , porche.price)

mini = Car()
print(mini.color, mini.price)