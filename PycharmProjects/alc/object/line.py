import alc.object.machine as myMachine


class Line:
    list_machine = []

    def __init__(self, id):
        """constructor"""
        self.id = id  # class instance (data) attribute

    def add_machine(self, machine):
        self.list_machine.append(machine)

    def is_machine_exists(self, machine_id):
        result = any(elem.id == machine_id for elem in self.list_machine)
        return result

    def find_machine(self, machine_id):
        for i in range(len(self.list_machine)):
            if self.list_machine[i].id == machine_id:
                result = self.list_machine[i]
                return result


# Create Class Instances
machine_1 = myMachine.Machine(1)
machine_2 = myMachine.Machine(2)
machine_3 = myMachine.Machine(3)

line_1 = Line(1)
line_1.add_machine(machine_1)
line_1.add_machine(machine_2)
line_1.add_machine(machine_3)
print('Line{}.CountMachine{}'.format(line_1.id, len(line_1.list_machine)))

my_machine = line_1.find_machine(1)
if my_machine is None:
    print('Not_found')
else:
    print('Found machine witch machine_id:{}'.format(my_machine.id))
