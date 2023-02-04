def getFreq(gosp, gosc):
    y = 0
    x = 0
    for index,row in enumerate(tab):
        if(gosp in row[0]):
            x = index
    for index,col in enumerate(tab[0]):
        if(gosc in col):
            y = index
    print(y,x,tab[x][y])
    return tab[x][y]


def createFile(clubNumber, clubShrt, startYear, stopYear):
    f1 = open("spotkania"+startYear+stopYear+"k"+clubNumber+".txt", "r", encoding="utf8")
    f1f = open("spotkaniaf"+startYear+stopYear+"k"+clubNumber+".txt", "w", encoding="utf8")
    for line in f1:    
        line = line.replace("\n","")
        row = line.split("\t")
        print(row)
        if(row[2]==clubShrt):
            line = line + "\t" + "1"
        else:
            line = line + "\t" + "0"
        line = line + "\t" + getFreq(row[2],row[3]) + "\n"
        f1f.write(line)
    f1.close()
    f1f.close()
    
startYear = "2017"
stopYear = "2018"

f = open("frekwencja"+startYear+stopYear+".txt", "r", encoding="utf8")
tab = []

for line in f:
    cols = line.split("\t")
    tab.append(cols)
#     print(line)
#     print(cols)
# print(tab)

createFile("1","LPO",startYear,stopYear)
createFile("2","LGD",startYear,stopYear)
createFile("3","CRA",startYear,stopYear)