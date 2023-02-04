import string
import numpy as np
import math

n = input().strip()
n = int(n)
tytuly = []
tresci = []

tfTytulow = []
tfTresci = []

liczba_wystapien_w_dokumentach = []

sl={}


for i in range(0,n):
    tytuly.append(input().strip())
    tresci.append(input().strip())

m = input().strip()
m = int(m)
zapytania = []

tfArray = np.zeros((n, m))
idfArray = np.zeros(m)

for i in range(0,m):
    zapytania.append(input().strip())
    liczba_wystapien_w_dokumentach.append([0,0])

#indeks = dict()

for numer, tytul in enumerate(tytuly):
    tytuly_final = tytuly[numer].lower().replace(",","").replace("-","").replace(".","").split(" ")
    tresci_final = tresci[numer].lower().replace(",","").replace("-","").replace(".","").split(" ")

    liczba_wystapien_w_tytule = {}

    for term in tytuly_final:
        if len(term) == 0: continue
        lematyzacja = term
        if term in sl:
            lematyzacja = sl[term]
        liczba_wystapien_w_tytule[lematyzacja] = liczba_wystapien_w_tytule.get(lematyzacja, 0) +1

    liczba_wystapien_w_tresci = {}

    for term in tresci_final:
        if len(term) == 0: continue
        lematyzacja = term
        if term in sl:
            lematyzacja = sl[term]
        liczba_wystapien_w_tresci[lematyzacja] = liczba_wystapien_w_tresci.get(lematyzacja, 0) +1

    tf_temp = []
    #TF dla tytulu
    for zapytanie in zapytania:
        all_values = liczba_wystapien_w_tytule.values()
        max_value = max(all_values)
        if(liczba_wystapien_w_tytule.get(zapytanie)):
            zapytanie_value = liczba_wystapien_w_tytule.get(zapytanie)
        else:
            zapytanie_value = 0

        tf_temp.append(zapytanie_value/ max_value)

    tfTytulow.append(tf_temp)

    tf_temp = []
    for zapytanie in zapytania:
        all_values = liczba_wystapien_w_tresci.values()
        max_value = max(all_values)
        if(liczba_wystapien_w_tresci.get(zapytanie)):
            zapytanie_value = liczba_wystapien_w_tresci.get(zapytanie)
        else:
            zapytanie_value = 0

        tf_temp.append(zapytanie_value/ max_value)
    tfTresci.append(tf_temp)


    for numer, zapytanie in enumerate(zapytania):
        if(zapytanie in liczba_wystapien_w_tresci):
            liczba_wystapien_w_dokumentach[numer][1] += 1
        if(zapytanie in liczba_wystapien_w_tytule):
            liczba_wystapien_w_dokumentach[numer][0] += 1
        

idf = liczba_wystapien_w_dokumentach

for y in range(0,m):
    idf[0][y] = math.log( n*2 / idf[0][y], 10)
    idf[1][y] = math.log( n*2 / idf[1][y], 10)

for w in range(m):
    tfidf = []
    for uwu in range(n):
        tfidf.append(tfTytulow[uwu][w] * 2 *idf[0][w] + tfTresci[uwu][w] * idf[1][w])
    #print(tfidf)

    final_tfidf = []

    for i in range(len(tfidf)):
        if tfidf[i] != 0:
            final_tfidf.append([tfidf[i],i])

    final_tfidf.sort(reverse = True, key = lambda x:(x[0]))

    sort_index = []

    #print(final_tfidf)

    for x in final_tfidf:
        sort_index.append(x[1])
  
    #print(final_tfidf)
    print(sort_index)