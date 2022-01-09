def header(title):
    print("="*50);
    print("\t",title)
    print("="*50)

def hasil(output):
    print("");
    print(output)
    print("_"*50)

def ubahRamKeMbps(ramInGbps):
    return ramInGbps * 1024

def hitungPetaBit(blok, petabit):
    return blok / petabit
    
def Ramterpakai(os, kaprog1, kaprog2):
    return os + kaprog1 + kaprog2

def  RamTidakTerpakai(Ram,os,kaprog1,kaprog2):
    return Ram - os - kaprog1 - kaprog2
    
def akhir(terimakasih):
    print("="*50)
    print("\t\t\t",terimakasih)
    print("="*50)

def cuy(lama1,lama2,lama3):
    return [lama1,lama2,lama3]

def proses(lama1,lama2,lama3):
    if lama1>lama2 and lama2>lama3:
        if lama2>lama3:
            print(lama1, lama2, lama3)
        else:
            print(lama1, lama3, lama2)
    elif lama2>lama1 and lama2>lama3:
        if lama1>lama3:
            print(lama2, lama1, lama3)
        else:
            print(lama2, lama3, lama1)
    else:
        if lama1>lama2:
            print(lama3, lama1, lama2)
        else:
            print(lama3, lama2, lama1)