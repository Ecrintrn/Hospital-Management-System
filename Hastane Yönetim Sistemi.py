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
                bithdate DATE NOT NULL,
                identity VARCHAR(11) NOT NULL,
                specialization VARCHAR(150) NOT NULL,
                doctor_name VARCHAR(150) NOT NULL,
                triage_color VARCHAR(200) NOT NULL
            )
        ''')
        self.conn.commit()

    def hasta_ekle(self, name, birthdate, identity, specialization, doctor_name, triage_color):
        self.cursor.execute(f"INSERT INTO {self.tablo_adi} (name, birthdate, identity, specialization, doctor_name, triage_color) VALUES (?, ?, ?, ?, ?, ?)", (name, birthdate, identity, specialization, doctor_name, triage_color))
        self.conn.commit()
        print(f"{name} eklendi.")

    def hasta_iptal(self, identity):
        self.cursor.execute(f"DELETE FROM {self.tablo_adi} WHERE identity=?", (identity,))
        self.conn.commit()
        print(f"{identity} kimlik numaralı hasta silindi.")

    def hasta_guncelle(self, name, birthdate, identity, specialization, doctor_name, triage_color):
        self.cursor.execute(f"UPDATE {self.tablo_adi} SET name=?, birthdate=?, identity=?, specialization=?, doctor_name=?, triage_color=? WHERE identity=?", (name, birthdate, identity, specialization, doctor_name, triage_color, identity))
        self.conn.commit()
        print(f"{identity} kimlik numaralı hasta güncellendi.")

    def hastalari_listele(self):
        self.cursor.execute("SELECT * FROM Hasta")
        hastalar = self.cursor.fetchall()
        print(f"\n***** {self.tablo_adi.upper()} *****")
        for hasta in hastalar:
            identity  = hasta[3][:3] + '*' * (len(hasta[3] - 3))
            print(f"Sıra No: {hasta[0]}, İsim: {hasta[1]}, Kimlik No: {identity},  Doktor Adı: {hasta[4]}, Triage Color: {hasta[5]}")

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
        print("\n***** Doctors.upper() *****")
        for doctor in doctors:
            print(f"Doctor Name : {doctor[1]}, Doctor Surname : {doctor[2]}, Doctor's Academic Rank : {doctor[3]}, Doctor's specialization : {doctor[4]}")
            
    def ilac_yazma(self):
        pass
            
class Hastane:
    def __init__(self):
        self.conn = sqlite3.connect('hastane.db')
        self.cursor = self.conn.cursor()
        self.hasta = Hasta()
        self.doktor = Doktor()
        passwords = ["12345678"]
        
    def kayıt_olustur(self):
        name = input("Hastanın Adı Soyadı:")
        birthdate = input("Hastanın doğum yılı:")
        identity = input("Kimlik No:")
        specialization = input("Gidilecek uzmanlık: ")
        doctor_name= input("Doktor Adı: ")
        triage_color = input("Hastanın acil durumu: ")
        count = self.cursor.execute('SELECT COUNT(*) FROM Doctors WHERE doktor_name=?', (doctor_name,))
        count = self.cursor.fetchone()[0]
        if count>0:
            self.hasta.hasta_ekle(name, birthdate, identity, specialization, doctor_name, triage_color)
        else:
            print("Böyle bir doktor bulunamamıştır.")
                            
    def doktor_ekle(self):
        doktor_name= input("Doktorun Adını Giriniz: ")
        doctor_surname = input("Doktorun Soyadını Giriniz: ")
        academic_rank = input("Doktorun akademik unvanı giriniz: ")                
        specialization = input("Doktorun uzmanlık alannını giriniz: ")
        password = input("Doktorun kullanacağı şifreyi giriniz: ")
        self.doktor.add_doctor(doktor_name, doctor_surname, academic_rank, specialization, password)
        self.passwords.append(password)
    
    def doktor_güncelle(self):
        doktor_name= input("Doktorun Adını Giriniz: ")
        doctor_surname = input("Doktorun Soyadını Giriniz: ")
        academic_rank = input("Doktorun akademik unvanı giriniz: ")                
        specialization = input("Doktorun uzmanlık alannını giriniz: ")
        password = input("Yeni şifreyi giriniz: ")  
        self.doktor.update_docotr(doktor_name, doctor_surname, academic_rank, specialization, password)
        
    def id_cevir(self, kimlik_numarası):
        self.cursor.execute('SELECT * FROM Hasta WHERE identity=?',(identity,))
        hasta = self.cursor.fetchall()
        if hasta:
            return True
        else:
            return False
        
hasta = Hasta()
doktor = Doktor()
hastane = Hastane()
while True:
    sifre = input("Şifrenizi giriniz :")
    if sifre == "12345678":
        print(20*"*","Hasta-Kayıt Sistemi",20*"*")
        print("""
    1. Yeni Hasta kabul
    2. Hasta Güncelleme
    3. Hasta Kayıt Silme""")
        islem = input("/nYapılacak işlemi girini<: ")
        if islem == "1":
            hastane.kayıt_olustur()
        elif islem == "2":
            hasta.hastalari_listele()
            kimlik_numarası = input("Güncellemek istenen hastanın kimlik numarasını giriniz: ")
            hasta = hastane.id_cevir(kimlik_numarası)
            if hasta == True:
                name = input("Hastanın Adı Soyadı:")
                birthdate = input("Hastanın doğum yılı:")
                identity = input("Kimlik No:")
                specialization = input("Gidilecek uzmanlık: ")
                doctor_name= input("Doktor Adı: ")
                triage_color = input("Hastanın acil durumu: ")
                hasta.hasta_guncelle(name, birthdate, identity, specialization, doctor_name, triage_color)
            else:
                print("Böyle bir kişi bulunamadı.")
        elif islem =="3":
            kimlik_numarası = input("İptal edilmek istenen hastanın kimlik numarasını giriniz: ")
            hasta = hastane.id_cevir(kimlik_numarası)
            if hasta == True:
                hasta.hasta_iptal(kimlik_numarası)
            else:
                print("Böyle bir hasta bulunmadı.")
        elif islem == "Q" or islem == "q" or islem == "0":
            continue
        else:
            print("Lütfen 1-3 arası bir tuş giriniz.")
    elif sifre== "87654321":
        print(20*"*","Doktor Sistemi", 20*"*")
        print("""
    1. Hasta Çağır
    2. Bilgilerimi Güncelle""")
        islem = input("/nYapılacak işlemi girini<: ")
