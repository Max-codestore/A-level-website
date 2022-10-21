import csv,random,base64
from cryptography.fernet import Fernet


def read_text_file(file,end="\n"):  # requires file to be imputed when the fuction is called and defines end as new line charater
    data = []  # creats the list data
    f = open(file, "r")  # opens the file specified when the fuction is called
    for line in f.readlines():  # for as many lines as the file has read them
        data.append(
            line.strip(end))  # reads each line until it finds a new line charater and adds the content to the list data
    f.close()  # closes the file after all lines have been read
    return data  # returns the list data to the rest of the code



def read_text_file_muti_collum(file, end="\n"):
    dataTwo = []
    f = open(file, 'r')
    for line in f.readlines():
        line = line.split()
        record = []
        for item in line:
            record.append(item.strip(end))
        dataTwo.append(record)
    f.close()
    return dataTwo



def read_text_file_2D(text_file):
    data = []
    file = open(text_file, 'r')
    for line in file.readlines():
        line = line.split()
        record = []
        for item in line:
            record.append(item.strip("\n"))
        data.append(record)
    file.close()
    return data


def read_csv_file(csv_file):
    l = []
    file = open(csv_file)
    r = csv.reader(file)
    num = 0
    for i in r:
        l.append(i)
        num = num + 1
    file.close()
    return l


def write_file_list(file, list):
    f = open(file, 'w')
    f.writelines(str(list))
    f.close()
b = 0


def write_text_file(text, file, end=""):
    for i in range(len(text)):
        text[i] = text[i] + end

    f = open(file, 'w')
    f.writelines(text)
    f.close()





def append_file_list(file, list):
    f = open(file, 'a')
    f.writelines(list)
    f.close()



def help():
    print(
        "to read a text file use text_file_manger.read_text_file(put the name of the file you want to read here) to "
        "read a muti collum file use read_text_file_2D(put the name of the file you want to read here)to read a csv "
        "file use text_file_manger.read_csv_file(enter file name here) and to write a file  use "
        "text_file_manger.write_file_list('what you want to call the file.txt'['enter text you want to enter here',"
        "'enter text you want here'] and to append a text file text_file_manger.append_file_list('what you want to "
        "call the file.txt'['enter text you want to enter here','enter text you want here'] ")


text = [['Bart', 'Simpson', 12, 17, 18],
        ['Nelson', 'Muntz', 15, 16, 19],
        ['Ralf', 'Wiggum', 23, 10, 10]]


def write_text_file_2d(data, file, end=""):
    f = open(file, 'w')
    for line in data:
        for item in line:
            item = str(item) + " "
            f.write(item)
        f.write(end)
    f.close()


text = [['Bart', 'Simpson', 12, 17, 18],
        ['Nelson', 'Muntz', 15, 16, 19],
        ['Ralf', 'Wiggum', 23, 10, 10]]



def append_text(text, file):
    f = open(file, "a")
    print(f.write(text))
    f.close()


def append_text_file_2d(data, file, end=""):
    f = open(file, 'a')
    for line in data:
        for item in line:
            item = str(item) + " "
            f.write(item)
        f.write(end)
    f.close()




def copy_file(copy, paste):
    fi = open(copy, 'r')
    fo = open(paste, 'w')
    for line in fi.readlines():
        fo.write(line)
    fi.close()
    fo.close()

