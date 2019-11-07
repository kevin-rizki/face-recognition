# Program memisahkan sample input 20% dari folder asal
# Nama file: generateinputdata.py
# Letakkan folder PINS dalam directory file ini
import os
from shutil import copyfile

# Mengenerate nama folder
for folderName in os.listdir("./PINS"):
    folderDir = os.path.join("./PINS",folderName)
    
    # Menghitung jumlah file dalam folder
    path, dirs, files = next(os.walk(folderDir))
    number_of_files = len(files)

    # Jumlah maksimal untuk data uji tiap folder dan counter jumlah test data yang sudah ter-copy
    tresshold = int(0.2 * float(number_of_files))
    number_test_data = 0

    # counter untuk membuat data uji random dengan modulo 2
    counter = 1
    
    for fileName in os.listdir(folderDir):
        # Directory file asal
        fileDir = os.path.join(folderDir, fileName)
        src = fileDir

        # Membuat directory untuk Referensi
        if (counter % 2 == 0) and (number_test_data < tresshold):
            newDir = os.path.join("TestData",folderName)
            number_test_data += 1
        else:    
            newDir = os.path.join("Reference",folderName)
    
        if not os.path.exists(newDir):
            os.makedirs(newDir)
        
        # Copy file ke directory baru dengan nama yang sama
        dst = os.path.join(newDir,fileName)
        copyfile(src,dst)        

        counter+=1
