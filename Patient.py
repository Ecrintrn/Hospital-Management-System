import sqlite3

class Patient:
    def __init__(self):
        self.conn = sqlite3.connect('hospital.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        self.triage_color("White", "Red", "Yellow", "Black")
        
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
        self.cursor.execute("INSERT INTO Patients (name, birthdate, identity, specialization, doctor_name, triage_color) VALUES (?, ?, ?, ?, ?, ?)", (name, birthdate, identity, specialization, doctor_name, triage_color))
        self.conn.commit()
        print(f"{name} is added.")

    def update_patient(self, name, birthdate, identity, specialization, doctor_name, triage_color):
        self.cursor.execute("UPDATE Patients SET name=?, birthdate=?, identity=?, specialization=?, doctor_name=?, triage_color=? WHERE identity=?", (name, birthdate, identity, specialization, doctor_name, triage_color, identity))
        self.conn.commit()
        print(f"Patient with id no {identity} is updated.")

    def list_patients(self):
        self.cursor.execute("SELECT * FROM Patients")
        patients = self.cursor.fetchall()
        print(f"\n***** {self.table_name.upper()} *****")
        for patient in patients:
            identity = patient[3][:3] + '*' * (len(patient[3] - 3))
            print(f"No: {patient[0]}, Name: {patient[1]}, ID No: {identity},  Doctor Name: {patient[4]}, Triage Color: {patient[5]}")

    def patient(self):
        self.cursor.execute('SELECT * FROM Patients')
        patients = self.cursor.fetchall()
        return patients
    
    @staticmethod
    def is_there_patient(identity):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        result = cursor.execute('SELECT EXISTS(SELECT * FROM Patients WHERE identity=?)', (identity,))
        exists = result.fetchone()[0]
        conn.close()
        return exists

    @staticmethod
    def cancel_patient(identity):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Patients WHERE identity=?', (identity,))
        conn.commit()
        conn.close()
        print(f"Patient with {identity} id no is cancelled.")