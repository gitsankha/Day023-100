from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


#Initial number of cars shown on the screen
NO_OF_CARS_GENERATED = 6


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.speed_limit = STARTING_MOVE_DISTANCE
        self.create_cars()
        self.hideturtle()

    def create_cars(self):
        for i in range(NO_OF_CARS_GENERATED):
            car = Turtle()
            car.shape("square")
            car.setheading(180)
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.speed(random.randint(1,9))
            x  = random.randint(-300,300)
            y = random.randint(-300,300)
            car.goto(x,y)
            self.cars_list.append(car)


    def generate_new_car(self):
        y = random.randint(-300,300)
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid= 1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.penup()
        new_car.goto(300,y)
        self.cars_list.append(new_car)


    def move_cars(self):
        for i in range(len(self.cars_list)):
            self.cars_list[i].forward(self.speed_limit)


    def increase_car_speed(self):
        self.speed_limit += MOVE_INCREMENT
