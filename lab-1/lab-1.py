import random

class Event:
    type: str
    payload: dict[str, any]

    def __init__(self, type: str, payload: dict[str, any]):
        self.type = type
        self.payload = payload


class Queue:
    queue: list[Event]

    def __init__(self):
        self.queue = [];

    def emit_event(self, event: Event):
        self.queue.append(event)

    def process_event(self, type: str):
        for index, event in enumerate(self.queue):
            if event.type == type:
                self.queue.pop(index)
                return event

        return None

    def is_empty(self):
        return len(self.queue) == 0

    def clear_queue(self):
        self.queue = []


class Student:
    queue: Queue
    first_name: str
    last_name: str
    day_birth: str
    address: str
    phone_number: str
    passport_number: str

    def __init__(self, queue: Queue, first_name: str, last_name: str, day_of_birth: str, address: str,
                 phone_number: str, passport_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.day_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number
        self.passport_number = passport_number
        self.queue = queue

    def ask_for_embassy_appointment(self, date: str):
        event = Event(Student, {'passport_number': self.passport_number, 'date': date})
        self.queue.emit_event(event)


class Embassy:
    queue: Queue
    name: str
    address: str
    phone_number: str
    email: str
    appointment_list: list[str]

    def __init__(self, queue: Queue, name: str, address: str, phone_number: str, email: str):
        self.appointment_list = []
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.queue = queue

    def handle_appointment_request(self):
        if self.queue.is_empty():
            return

        event = queue.process_event(Student)

        print(f'Received appointment request from {event.payload.get("passport_number")}')

        self.send_response_to_student(event.payload.get("passport_number"), event.payload.get("date"))

    def send_response_to_student(self, passport_number: str, date: str):
        is_confirmed = True

        if [appointment_date for appointment_date in self.appointment_list if appointment_date == date]:
            is_confirmed = False

        event = Event(Embassy, {'passport_number': passport_number, 'is_confirmed': is_confirmed})

        self.appointment_list.append(date)
        self.queue.emit_event(event)


queue = Queue()

student1 = Student(queue, "Piotr1", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323')
student2 = Student(queue, "Piotr2", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323')
student3 = Student(queue, "Piotr3", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323')

embassy1 = Embassy(queue, "The best Embassy", "Ankara", '5435345328', email='embassy@embassy.pl')

student1.ask_for_embassy_appointment('10.12.2024')

embassy1.handle_appointment_request()

student2.ask_for_embassy_appointment('10.12.2024')

embassy1.handle_appointment_request()

student3.ask_for_embassy_appointment('08.12.2024')

embassy1.handle_appointment_request()

print(queue.queue[0].payload)
print(queue.queue[1].payload)
print(queue.queue[2].payload)