def isWon(result, rev=False):
    # print(result)
    result = result.split(":")
    if(int(result[0])==int(result[1])):
        return 2
    if(int(result[0])>int(result[1])):
        return 1 if not rev else 0
    else:
        return 0 if not rev else 1



def createFile(clubNumber, clubShrt, startYear, stopYear):
    f1 = open("spotkaniaf"+startYear+stopYear+"k"+clubNumber+".txt", "r", encoding="utf8")
    f1f = open("spotkaniafw"+startYear+stopYear+"k"+clubNumber+".txt", "w", encoding="utf8")
    for line in f1:    
        line = line.replace("\n","")
        row = line.split("\t")
        if(len(row)>1):
            print(row)
            if(row[2]==clubShrt):
                line = line + "\t" + str(isWon(row[4]))
            else:
                line = line + "\t" + str(isWon(row[4], True))
            line = line + "\n"
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