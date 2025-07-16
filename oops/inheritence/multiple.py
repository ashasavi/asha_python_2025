class mom:
    def cook(self):
        print("cooking....")

class dad:
    def sleep (self):
        print(" sleeping...")

class child(mom,dad):
    def study(self):
        print (" studying....")

d = dad()
m = mom()
c = child()

d.sleep()
m.cook()

c.study()
c.sleep()
c.cook()