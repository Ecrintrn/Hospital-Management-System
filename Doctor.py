import sqlite3

class Doctor:
    def __init__(self):
        self.conn = sqlite3.connect('hospital.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        self.academic_rank = ["Research Assistant", "Assistant Professor", "Lecturer", "Doctor Lecturer", "Associate Professor", "Professor Doctor"]
        self.specialization = ["Ear Nose Throat (ENT)", "Internal Medicine", "Neurology", "Dermatology", "Emergency Service", "Infectious Diseases"]
        self.doctor_name = []
        
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
        self.doctor_name.append(doctor_name)
        print(f"{doctor_name} {doctor_surname} is successfully added to the system.")
        
    def update_doctor(self, doctor_name, doctor_surname, academic_rank, specialization, password):
        self.cursor.execute("UPDATE Doctors SET doctor_name=?, doctor_surname=?, academic_rank=?, specialization=?, password=?", (self, doctor_name, doctor_surname, academic_rank, specialization, password))
                            
    def show_doctors(self):
        self.cursor.execute("SELECT * FROM Doctors")
        doctors = self.cursor.fetchall()
        print("\n***** {Doctors.upper()} *****")
        for doctor in doctors:
            print(f"Doctor Name : {doctor[1]}, Doctor Surname : {doctor[2]}, Doctor's Academic Rank : {doctor[3]}, Doctor's specialization : {doctor[4]}")
    
    def preparing_prescription(self):
        pass
          