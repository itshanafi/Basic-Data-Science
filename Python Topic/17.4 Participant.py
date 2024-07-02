# In every class there will be many properties

class Participant:

    course = "Python Data Science"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        count = 1
        print(self.first_name, self.last_name, count)

    def getFullName(self):
        return self.first_name + " " + self.last_name
    
hanafi = Participant("Hanafi", "Akmal")
print(hanafi.getFullName())
print(Participant.course)