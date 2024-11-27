import unittest

class Student:
    communication_queue = []

    def __init__(self, communication_queue, first_name, last_name, day_of_birth, address, phone_number, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.day_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number
        self.passport_number = passport_number
        self.communication_queue = communication_queue

    def ask_for_embassy_appointment(self, date):
        event = {'name': 'embassy_appointment_request', 'payload': {'id': self.passport_number, 'date': date}}
        self.communication_queue.append(event)
        print('Event', event['name'], 'emitted!')


class Embassy:
    communication_queue = []

    def __init__(self, communication_queue, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.communication_queue = communication_queue

    def handle_appointment_request(self):
        current_request = self.communication_queue.pop(0).get('payload')
        print("Received request from student with Passport:", current_request['id'])

        event = {'name': 'appointment_confirmation', 'payload': {'id': current_request['id'], 'is_confirmed': True}}
        self.communication_queue.append(event)
        print('Event', event['name'], 'emitted!')


# UNIT TESTS

class ProgramDefaultBehaviour(unittest.TestCase):
    def test_Student_class(self):
        # Given:
        peter1 = Student([], "Piotr1", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323')

        # Then:
        self.assertEqual(peter1.first_name, "Piotr1", 'First Name should be Piotr1')
        self.assertEqual(peter1.last_name, "Brudny", 'Last Name should be Brudny')
        self.assertEqual(peter1.day_birth, "1.02.1984", 'Day of Birth should be 1.02.1984')
        self.assertEqual(peter1.address, "Ankara", 'Address should be Ankara')
        self.assertEqual(peter1.phone_number, "5435345345", 'Phone Number should be 5435345345')
        self.assertEqual(peter1.passport_number, "ED4234323", 'Passport Number should be ED4234323')

    def test_Student_class_emits_events(self):
        # Given:
        communication_queue = []
        peter1 = Student(communication_queue, "Piotr1", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323')
        date_for_appointment = '10.12.2024';
        student_event = {'name': 'embassy_appointment_request', 'payload': {'id': peter1.passport_number, 'date': date_for_appointment}}

        # When:
        peter1.ask_for_embassy_appointment(date_for_appointment)

        # Then:
        self.assertEqual(communication_queue[0], student_event, f'Emitted event should be {student_event}')

    def test_Embassy_class(self):
        # Given:
        polish_embassy = Embassy([],'Polish Embassy', 'Ankara, Harika 10', '343242344', 'polishembassy@gov.tr')

        # Then:
        self.assertEqual(polish_embassy.name, "Polish Embassy", 'Name should be Polish Embassy')
        self.assertEqual(polish_embassy.address, "Ankara, Harika 10", 'Address should be Ankara, Harika 10')
        self.assertEqual(polish_embassy.phone_number, "343242344", 'Phone Number should be 343242344')
        self.assertEqual(polish_embassy.email, "polishembassy@gov.tr", 'Email should be polishembassy@gov.tr')

    def test_Embassy_class_emits_and_handles_events(self):
        # Given:
        communication_queue = []
        peter1 = Student(communication_queue, "Piotr1", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323')
        date_for_appointment = '10.12.2024';
        polish_embassy = Embassy(communication_queue, 'Polish Embassy', 'Ankara, Harika 10', '343242344', 'polishembassy@gov.tr')
        embassy_event = {'name': 'appointment_confirmation', 'payload': {'id': peter1.passport_number, 'is_confirmed': True}}

        # When:
        peter1.ask_for_embassy_appointment(date_for_appointment)
        polish_embassy.handle_appointment_request()

        # Then:
        self.assertEqual(communication_queue[0], embassy_event, f'Emitted event should be {embassy_event}')

unittest.main()