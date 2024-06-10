import sqlite3

class Patient:
    def __init__(self):
        self.conn = sqlite3.connect('hospital.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birthdate DATE NOT NULL,
                identity VARCHAR(11) NOT NULL,
                specialization VARCHAR(150) NOT NULL,
                doctor_name VARCHAR(150) NOT NULL,
                triage_color VARCHAR(200) NOT NULL
            )
        ''')
        self.conn.commit()

    def add_patient(self, name, birthdate, identity, specialization, doctor_name, triage_color):
        self.cursor.execute(f"INSERT INTO {self.table_name} (name, birthdate, identity, specialization, doctor_name, triage_color) VALUES (?, ?, ?, ?, ?, ?)", (name, birthdate, identity, specialization, doctor_name, triage_color))
        self.conn.commit()
        print(f"{name} is added.")

    def cancel_patient(self, identity):
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE identity=?", (identity,))
        self.conn.commit()
        print(f"Patient with {identity} id no is cancelled.")

    def update_patient(self, name, birthdate, identity, specialization, doctor_name, triage_color):
        self.cursor.execute(f"UPDATE {self.table_name} SET name=?, birthdate=?, identity=?, specialization=?, doctor_name=?, triage_color=? WHERE identity=?", (name, birthdate, identity, specialization, doctor_name, triage_color, identity))
        self.conn.commit()
        print(f"Patient with {identity} id no is updated.")

    def list_patients(self):
        self.cursor.execute("SELECT * FROM Patients")
        patients = self.cursor.fetchall()
        print(f"\n***** {self.table_name.upper()} *****")
        for patient in patients:
            identity = patient[3][:3] + '*' * (len(patient[3] - 3))
            print(f"Sıra No: {patient[0]}, İsim: {patient[1]}, Kimlik No: {identity},  Doktor Adı: {patient[4]}, Triage Color: {patient[5]}")

class Doctor:
    def __init__(self):
        self.conn = sqlite3.connect('hospital.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_name VARCHAR(150) NOT NULL,
            doctor_surname VARCHAR(150) NOT NULL,
            academic_rank VARCHAR(100) NOT NULL,
            specialization VARCHAR(150) NOT NULL,
            password VARCHAR(8) NOT NULL
            )
            ''')
        self.conn.commit()
        
    def add_doctor(self, doctor_name, doctor_surname, academic_rank, specialization, password):
        self.cursor.execute("INSERT INTO Doctors (doctor_name, doctor_surname, academic_rank, specialization, password) VALUES (?, ?, ?, ?, ?)", (doctor_name, doctor_surname, academic_rank, specialization, password))
        self.conn.commit()                    
        print(f"{doctor_name} {doctor_surname} is updated successfully.")
        
    def update_doctor(self, doctor_name, doctor_surname, academic_rank, specialization, password):
        self.cursor.execute("UPDATE Doctors SET doctor_name=?, doctor_surname=?, academic_rank=?, specialization=?, password=?", (self, doctor_name, doctor_surname, academic_rank, specialization, password))
                            
    def show_doctors(self):
        self.cursor.execute("SELECT * FROM Doctors")
        doctors = self.cursor.fetchall()
        print("\n***** Doctors.upper() *****")
        for doctor in doctors:
            print(f"Doctor Name : {doctor[1]}, Doctor Surname : {doctor[2]}, Doctor's Academic Rank : {doctor[3]}, Doctor's specialization : {doctor[4]}")
            
    def preparing_prescription(self):
        pass


class Hospital:
    def __init__(self):
        self.conn = sqlite3.connect('hospital.db')
        self.cursor = self.conn.cursor()
        self.patient = Patient()
        self.doctor = Doctor()
        passwords = ["12345678"]
        
    def add_patient(self):
        name = input("Patient Name:")
        birthdate = input("Patient Birthdate:")
        identity = input("ID No:")
        specialization = input("Required specialization: ")
        doctor_name= input("Doctor Name: ")
        triage_color = input("Triage color of the patient: ")
        count = self.cursor.execute('SELECT COUNT(*) FROM Doctors WHERE doctor_name=?', (doctor_name,))
        count = self.cursor.fetchone()[0]
        if count > 0:
            self.patient.add_patient(name, birthdate, identity, specialization, doctor_name, triage_color)
        else:
            print("There is no such doctor in the database.")
                            
    def add_doctor(self):
        doctor_name= input("Doctor Name: ")
        doctor_surname = input("Doctor Surname: ")
        academic_rank = input("Doctor Academical Rank: ")
        specialization = input("Specialization of the doctor: ")
        password = input("Password of the doctor: ")
        self.doctor.add_doctor(doctor_name, doctor_surname, academic_rank, specialization, password)
        self.passwords.append(password)
    
    def update_doctor(self):
        doctor_name= input("Doctor Name: ")
        doctor_surname = input("Doctor Surname: ")
        academic_rank = input("Doctor Academical Rank: ")
        specialization = input("Specialization of the doctor: ")
        password = input("New Password of the doctor: ")
        self.doctor.update_doctor(doctor_name, doctor_surname, academic_rank, specialization, password)
        
    def get_id(self, identity):
        self.cursor.execute('SELECT * FROM Hasta WHERE identity=?',(identity,))
        patient = self.cursor.fetchall()
        if patient:
            return True
        else:
            return False
        

