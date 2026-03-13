class Adding:
    def __init__(self):
        self.a=0
        self.b=0
    def getting_input(self):
        a=int(input('enter a num'))
        b=int(input('enter a num'))
        self.a=a
        self.b=b
    def adding(self):
        return self.a+self.b
    
if __name__=='__main__':
    obj=Adding()
    obj.getting_input()
    print(obj.adding())
