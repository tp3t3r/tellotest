class TelloMock():
    def __init__(self, host, retry_count, udp_port):
        pass
    def connect(self):
        print("%s.%s" %(self.__class__.__name__, __name__))
    def setspeed(self, speed):
        print("speed: %d" % speed)
    def streamon(self):
        print("%s.%s" %(self.__class__.__name__, __name__))   
    def streamoff(self):
        print("%s.%s" %(self.__class__.__name__, __name__))
    def takeoff(self):
        print("%s.%s" %(self.__class__.__name__, __name__))
    def land(self):
        print("%s.%s" %(self.__class__.__name__, __name__))
    def get_frame_read(self):
        print("%s.%s" %(self.__class__.__name__, __name__))
    def send_rc_control(self, lr, fb, ud, yaw):
        print("%s.%s" %(self.__class__.__name__, __name__))
        print(" args:", locals())

