from collections import Counter
import csv
import hashlib

def password1():
    f = open("password1.txt","r")
    lines = f.readlines()
    list1 =[]
    list2 = []
    list3 = []
    dictionary ={}
    for line1 in lines:
        a = line1.split(',')[4]
        list1.append(a)
    for line1 in lines:
        a = line1.split(',')[3]
        list2.append(a)
    for line1 in lines:
        line1 = line1.strip('\n')
        a = line1.split(',')[-1]
        list3.append(a)
    list3 = list(map(int,list3))
    d = zip(list2,list3)
    dictionary = dict(d)
    mostFailed = max(dictionary,key = lambda x:dictionary[x])
    print("There are ",len(list1)," entries")
    print("The most commonly used password is",Counter(list1).most_common(1))
    print('Most failed login attempts:',mostFailed)

def password2():
    f = open("wordList.txt","r")
    lines = f.readlines()
    fs = open("password2.txt","r")
    line = fs.readlines()
    list1 = []
    list3 = []
    for line1 in lines:
        line1 = line1.strip('\n')
        list1.append(line1)
    list2 = []  
    for line1 in line:
        a = line1.split(',')[4]
        list3.append(a)
    print(list3)

    for i in range(len(list1)):
        for j in range(len(list1)):
            list2.append(list1[i] + list1[j])
    for i in list2:
        hl = hashlib.md5()
        hl.update(i.encode(encoding = "utf-8"))
        x = hl.hexdigest()
        if x in list3:
            print(x,i)
        else:
            continue 


if __name__ == "__main__":
    password1()
    password2()