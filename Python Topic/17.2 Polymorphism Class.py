# Polymorphism Class Inheritance

class Gender:
    def __init__(self, gender):
        self.gender = gender

    def doCarryObject(self):
        print("Carry Object")

class Male(Gender):
    def __init__(self, gender):
        super().__init__(gender)
    
    def doCarryObject(self):
        print("Carry heavy Object")

class Female(Gender):
    def __init__(self, gender):
        super().__init__(gender)

    def doCarryObject(self):
        print("Carry light object")
    
def getGender(name):
    if "Bin" in name or "bin" in name:
        return Male("Male")
    elif "A/L" in name or "a/l" in name:
        return Male("Male")
    elif "Binti" in name or "binti" in name:
        return Female("Female")
    elif "A/P" in name or "a/p" in name:
        return Female("Female")
    else:
        return Gender("Unknown")
    
def main():
    nama = str(input("Enter your name: "))
    gender = getGender(nama.capitalize())
    gender.doCarryObject()
    

if __name__ == '__main__':
    main()