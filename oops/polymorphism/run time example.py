class mom:
    def cook(self):
        print("Indian")

class daughter(mom):
    def cook(self):
        print("chinese")

a = mom()
b = daughter()

a.cook()
b.cook()

