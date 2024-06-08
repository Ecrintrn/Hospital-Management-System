import sqlite3

class Hasta:
    def __init__ (self):
        self.conn = sqlite3.connect('hastane.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Hasta (
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

    def hasta_ekle(self, name, birthdate, identity, specialization, doctor_name, triage_color):
        self.cursor.execute("INSERT INTO Hasta (name, birthdate, identity, specialization, doctor_name, triage_color) VALUES (?, ?, ?, ?, ?, ?)", (name, birthdate, identity, specialization, doctor_name, triage_color))
        self.conn.commit()
        print(f"{name} eklendi.")

    def hasta_guncelle(self, name, birthdate, identity, specialization, doctor_name, triage_color):
        self.cursor.execute("UPDATE Hasta SET name=?, birthdate=?, identity=?, specialization=?, doctor_name=?, triage_color=? WHERE identity=?", (name, birthdate, identity, specialization, doctor_name, triage_color, identity))
        self.conn.commit()
        print(f"{identity} kimlik numaralı hasta güncellendi.")

    def hastalari_listele(self):
        self.cursor.execute("SELECT * FROM Hasta")
        hastalar = self.cursor.fetchall()
        print(f"\n***** {self.tablo_adi.upper()} *****")
        for hasta in hastalar:
            identity  = hasta[3][:3] + '*' * (len(hasta[3] - 3))
            print(f"Sıra No: {hasta[0]}, İsim: {hasta[1]}, Kimlik No: {identity},  Doktor Adı: {hasta[4]}, Triage Color: {hasta[5]}")

    def patient(self):
        self.cursor.execute('SELECT * FROM Hasta')
        patients = self.cursor.fetchall()
        return patients
    
    @staticmethod
    def is_there_patient(identity):
        conn = sqlite3.connect('hastane.db')
        cursor = conn.cursor()
        result = cursor.execute('SELECT EXISTS(SELECT * FROM Hasta WHERE identity=?)', (identity,))
        exists = result.fetchone()[0]
        conn.close()
        return exists

    @staticmethod
    def hasta_iptal(identity):
        conn = sqlite3.connect('hastane.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Hasta WHERE identity=?', (identity,))
        conn.commit()
        conn.close()
        print(f"Hasta {identity} iptal edildi.")