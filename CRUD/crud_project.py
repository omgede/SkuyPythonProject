import sqlalchemy as db
import pandas as pd
from sqlalchemy import Table, Column, Integer, String, MetaData

meta = MetaData()
engine = db.create_engine("sqlite:///thefile.db")
connection = engine.connect()
metadata = db.MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('firstname', String), 
   Column('lastname', String), 
   Column('age', Integer), 
   Column('height', Integer)
)
meta.create_all(engine)

partisipan = db.Table('students', metadata, autoload = True, autoload_with = engine)


def crud(lakukan, get_result):
    if(lakukan == 1): #CREATE
        namaD = input("Masukan Nama Depan: ")
        namaB = input("Masukan Nama Belakang: ")
        age = input("Masukan umur: ")
        height = input("Masukan tinggi (cm)")

        valuest_list = [
            {
                "firstname": namaD,
                "lastname": namaB,
                "age": age,
                "height": height
            }
        ]
        tambah = db.insert(partisipan)
        connection.execute(tambah, valuest_list)

        query = db.select([partisipan])
        result = connection.execute(query)
        get_result = result.fetchall()

        return get_result

    elif(lakukan == 2): #READ
        print(get_result)
        pilihID = int(input("Input ID: "))

        query = db.select([partisipan]).where(partisipan.columns.id == pilihID)
        result = connection.execute(query)
        get_result = result.fetchall()
        print(get_result)


    elif(lakukan == 3): #UPDATE
        print(get_result)
        pilihNama = input("Pilih nama yang ingin diupdate: ")
        print("Pilih field yang ingin diupdate:")
        print("1. Nama Depan")
        print("2. Nama Belakang")
        print("3. Age")
        print("4. Tinggi")
        pilihField = int(input("Pilih: "))
        if(pilihField == 1):
            valueBaru = input("Input perubahan: ")
            values = {
                "firstname": valueBaru
            }
        elif(pilihField == 2):
            valueBaru = input("Input perubahan: ")
            values = {
                "lastname": valueBaru
            }
        elif(pilihField == 3):
            valueBaru = int(input("Input perubahan: "))
            values = {
                "age": valueBaru
            }
        elif(pilihField == 4):
            valueBaru = int(input("Input perubahan: "))
            values = {
                "height": valueBaru
            }
        

        # query = db.update(partisipan).values(fieldnya = valueBaru).where(partisipan.columns.firstname == pilihNama)
        query = db.update(partisipan).values(**values).where(partisipan.columns.firstname == pilihNama)
        hasil = connection.execute(query)

        
        print("Berhasil mengupdate")
        query = db.select([partisipan])
        hasil = connection.execute(query)
        get_result = hasil.fetchall()
        print(get_result)


    elif(lakukan == 4): #DELETE
        print(get_result)
        print("Pilih id yang mau dihapus: ")
        aid = int(input())
        
        apus = db.delete(partisipan).where(partisipan.columns.id == aid)
        hasil = connection.execute(apus)

        query = db.select([partisipan])
        hasil = connection.execute(query)
        get_result = hasil.fetchall()

        return get_result

  
    elif(lakukan == 0):

        query = db.select([partisipan])
        result = connection.execute(query)
        get_result = result.fetchall()

        return get_result


#-----------------------------------------------------------------------------
while(True):
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    pilih = int(input("Pilih: "))

    hasil = crud(0, None)
    df = pd.DataFrame(hasil, columns=['id', 'firstname', 'lastname', 'age', 'height'])
    df.set_index('id', inplace = True)



    if(pilih == 1):
        hasil = crud(1, None)
    elif(pilih == 2):
        hasil = crud(2, hasil)
        print(df)
    elif(pilih == 3):
        hasil = crud(3, hasil)
        print(df)
    elif(pilih == 4):
        hasil = crud(4, hasil)
        print(df)    
    elif(pilih == 5):
        break
    else:
        continue
