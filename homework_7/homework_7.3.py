# 3. Создайте программу, имитирующую работу клиники. Создайте базовый
# класс Doctor с методом treat(). От него создайте три дочерних класса:
# Surgeon, Dentist и Therapist. В каждом дочернем классе
# переопределите метод treat(), чтобы каждый врач выводил сообщение
# о своём способе лечения.Создайте класс Patient, содержащий атрибуты treatment_plan — код
# плана лечения и doctor — назначенный пациенту врач. В классе
# Therapist реализуйте метод назначения врача пациенту. Если код плана
# лечения равен 1, пациенту назначается хирург; если код равен 2 —
# дантист; при любом другом значении — терапевт.
# После назначения врача необходимо сохранить соответствующий объект
# врача в current_patient.doctor и вызвать у него метод treat(). Создайте
# пациента, задайте ему план лечения и продемонстрируйте работу
# программы.

import random


class Doctor:
    doctor_type = None

    def treat(self):
        pass


class Surgeon(Doctor):
    doctor_type = "Хирург"

    def treat(self):
        print("Хирург проводит операцию для устранения проблемы")


class Dentist(Doctor):
    doctor_type = "Стоматолог"

    def treat(self):
        print("Дантист лечит зубы и проводит гигиену полости рта")


class Therapist(Doctor):
    doctor_type = "Терапевт"

    def treat(self):
        print("Терапевт назначает медикаментозное лечение и даёт рекомендации")

    def handle_patient(self, current_patient):

        if current_patient.treatment_plan is None:
            current_patient.treatment_plan = random.randint(0, 4)
            print(f"Терапевт назначил пациенту план лечения: {current_patient.treatment_plan}")

        if current_patient.treatment_plan == 1:
            current_patient.doctor = Surgeon()
            print(f"{self.doctor_type} направил пациента к хирургу")
        elif current_patient.treatment_plan == 2:
            current_patient.doctor = Dentist()
            print(f"{self.doctor_type} направил пациента к дантисту")
        else:
            current_patient.doctor = Therapist()
            print(f"{self.doctor_type} оставил пациента на лечении у себя")

        current_patient.doctor.treat()

        return True


class Patient:
    def __init__(self, treatment_plan=None, doctor=Therapist()):
        self.treatment_plan = treatment_plan
        self.doctor = doctor


# Демонстрация работы:
therapist = Therapist()
patient = Patient()

print("Пациент приходят к терапевту — он назначает план и направляет к специалисту:\n")
therapist.handle_patient(patient)
