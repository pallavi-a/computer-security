import os
def quest1():
    rawString = input("Enter the Cipher Text：")
    k = int(input("Enter the Shift："))
    changeString = rawString.lower()
    stringList = list(changeString)
    stringListDecryp = stringList
    i = 0
    while i < len(stringList):
        if ord(stringList[i]) >= 97+k:
            stringListDecryp[i] = chr(ord(stringList[i]) - k)
        else:
            stringListDecryp[i] = chr(ord(stringList[i]) + 26 - k)
        i = i+1
    print ("Answer is "+"".join(stringListDecryp))

def quest2():
    file = open('question2.txt') 
    text = file.read().replace('?',' ')
    charList = list(text)

    tempSet = set(charList)

    tempDict = {}
    for i in tempSet:
        tempDict[i] = charList.count(i)

    sortedDict = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
    frequencyList = []
    print("Letter", "Times", "Frequency")
    for i in sortedDict:
        print(i[0], "\t", i[1], "\t", i[1] / len(text))
        frequencyList.append(i[0]) 

    fp = open('quest2new.txt','w')
    table = {'A':'i','B':'j','C':'k','D':'d','E':'g','F':'l','G':'m','H':'n','I':'e','J':'o','K':'p','L':'z','M':'r','N':'c','O':'s','P':'t','Q':'u','R':'h','S':'a','T':'v','U':'b','V':'f','W':'w','X':'x','Y':'y','Z':'q'}
    for key,value in table.items():
        text =  text.replace(key,value)
    fp.write(text)
    fp.close()


def quest3():
    letterList='ABCDEFGHIJKLMNOPQRSTUVWXYZ'    
    
    keyList=[]
    key=input("Enter key:")
    for ch in key:
        keyList.append(ord(ch.upper())-65)

    plainText=""
    cipherText=input("Enter the Cipher Text:")
    i=0
    
    
    for ch in cipherText: 
        if 0==i%len(keyList):
            i=0
        if ch.isalpha():
            if ch.isupper():
                plainText+=letterList[(ord(ch)-65-keyList[i]) % 26]
                i+=1
            else:
                plainText+=letterList[(ord(ch)-97-keyList[i]) % 26].lower()
                i+=1
        else:
            plainText+=ch
    print("Plaintext:%s" % plainText)



if __name__ == "__main__":
    quest1()
    quest2()      
    quest3()