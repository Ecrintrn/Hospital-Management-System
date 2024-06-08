import sqlite3

class Doktor:
    def __init__(self):
        self.conn = sqlite3.connect('hastane.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doktor_name VARCHAR(150) NOT NULL,
            doctor_surname VARCHAR(150) NOT NULL,
            academic_rank VARCHAR(100) NOT NULL,
            specialization VARCHAR(150) NOT NULL,
            password VARCHAR(8) NOT NULL
            )
            ''')
        self.conn.commit()
        
    def add_doctor(self, doktor_name, doctor_surname, academic_rank, specialization, password):
        self.cursor.execute("INSERT INTO Doctors (doktor_name, doctor_surname, academic_rank, specialization, password) VALUES (?, ?, ?, ?, ?)",(doktor_name, doctor_surname, academic_rank, specialization, password))
        self.conn.commit()                    
        print(f"{doktor_name} {doctor_surname} başarılı bir şekilde eklendi.")
        
    def update_docotr(self, doktor_name, doctor_surname, academic_rank, specialization, password):
        self.cursor.execute("UPDATE Doctors SET doktor_name=?, doctor_surname=?, academic_rank=?, specialization=?, password=?",(self, doktor_name, doctor_surname, academic_rank, specialization, password))
                            
    def show_doctors(self):
        self.cursor.execute("SELECT * FROM Doctors")
        doctors = self.cursor.execute.fetchall()
        print("\n***** {Doctors.upper()} *****")
        for doctor in doctors:
            print(f"Doctor Name : {doctor[1]}, Doctor Surname : {doctor[2]}, Doctor's Academic Rank : {doctor[3]}, Doctor's specialization : {doctor[4]}")
            
    def ilac_yazma(self):
        pass
          