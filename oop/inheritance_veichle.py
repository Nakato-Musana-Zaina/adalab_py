class Veichle:
    def __init__(self, make, color):
        self.make =make
        self.color = color

    def accerelate(self):
        print("Acelerate start")

    def hoot(self):
        print("honk honk")


class Bus(Veichle):
    def __init__(self, make, color,passesngers):
        super() .__init__ (make, color)
        self.padssenger =passesngers

    def start_bording(self):
        print("the bus is boarding")

class Lorry(Veichle):
    def __init__(self, make, color, max_load):
        super().__init__(make, color)
        self.max_laod = max_load

    def unload(self):
        print("unloading")



        

