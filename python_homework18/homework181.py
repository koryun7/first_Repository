# Class Exercise:
# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule
class HospitalAccount:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.schedule = []

    def schedule_visit(self, date, time):
        appointment = f"Date: {date}, Time: {time}"
        self.schedule.append(appointment)
        print(f"Visit scheduled for {self.patient_name} on {date} at {time}.")

    def remove_schedule(self, date, time):
        appointment = f"Date: {date}, Time: {time}"
        if appointment in self.schedule:
            self.schedule.remove(appointment)
            print(f"Visit removed for {self.patient_name} on {date} at {time}.")
        else:
            print(f"No matching visit found for {self.patient_name} on {date} at {time}.")

    def view_schedule(self):
        if not self.schedule:
            print(f"{self.patient_name}'s schedule is empty.")
        else:
            print(f"{self.patient_name}'s Schedule:")
            for appointment in self.schedule:
                print(appointment)


# Example Usage:
patient_account = HospitalAccount("John Doe")

# Schedule visits
patient_account.schedule_visit("2024-01-05", "10:00 AM")
patient_account.schedule_visit("2024-01-07", "02:30 PM")
patient_account.schedule_visit("2024-01-10", "11:15 AM")

# View the schedule
patient_account.view_schedule()

# Remove a visit
patient_account.remove_schedule("2024-01-07", "02:30 PM")

# View the updated schedule
patient_account.view_schedule()
