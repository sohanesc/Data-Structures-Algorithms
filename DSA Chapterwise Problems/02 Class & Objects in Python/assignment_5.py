# Define a class Team with an instance object variable as a list of team member names. Provide methods to input member names and display member names.


class Team:
    def __init__(self):
        self.members = []

    def input_member(self, name):
        self.members.append(name)

    def display_members(self):
        print("Team members:", self.members)


t = Team()
t.input_member("Sohan")
t.input_member("Jane")
t.display_members()
