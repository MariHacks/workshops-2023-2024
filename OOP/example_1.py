# implementation of "Club" class

class Club:
    club_count = 0  # total number of instances (class attribute)

    class Student:  # we can create a class inside a class
        def __init__(self, name, id):
            self.name = name
            self.id = id

    # constructor method, implicitly called when an instance of the class is created
    def __init__(self, name, description="", members=[], budget=0):
        self.name = name
        self.description = description
        self.members = members
        self.__budget = budget  # private attribute
        Club.club_count += 1  # increase the number of clubs when a new instance is created

    def __repr__(self):  # implicitly called when a string representation of the instance is required
        s = f"Club name: {self.name} \nDescription: {self.description}"
        return s

    def __del__(self):  # destructor
        print(f"{self.name} is deleted.")
        Club.club_count -= 1

    def __len__(self):  # we can define the size of the class to be the number of members
        return len(self.members)

    def print_memberList(self):  # member list consists of instances of "Student" class
        print(f"{self.name} member list:")
        print("{:10s} {:5s}".format("Name", "ID"))
        for member in self.members:
            print("{:10s} {:5d}".format(member.name, member.id))

    def get_budget(self):
        return self.__budget

    def add_budget(self, amount):
        self.__budget += amount

    def add_member(self, member_name, member_id):
        new_member = Club.Student(member_name, member_id)
        self.members.append(new_member)


# inheritance example

class ScienceClub(Club):

    def create_workshop(self, workshop_name):
        print(f"Welcome to {self.name}'s {workshop_name} workshop!")


if __name__ == "__main__":

    programming_club = ScienceClub("Programming Club",
                                   "A club for coding enthusiasts!",
                                   budget=100)

    # as a science club, programming_club object inherits properties from Club class
    print(programming_club)
    programming_club.add_member("Sarina", 111111)
    programming_club.add_member("Carolyn", 222222)
    programming_club.print_memberList()
    print(f"current number of members: {len(programming_club)}")
    programming_club.add_budget(50)
    print(f"our current budget is ${programming_club.get_budget()}")
    programming_club.create_workshop("OOP")
