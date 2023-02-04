# -*- coding: utf-8 -*-
import re
import requests
import urllib.parse
import json

appid = '5AKP35-A839Q8YQEX'

def wolframWeather(godzina, data, miejscowosc):
    query = urllib.parse.quote_plus("weather " + "  " +data + "  " + godzina + "  " + miejscowosc)
    query_url = f"http://api.wolframalpha.com/v2/query?" \
                f"appid={appid}" \
                f"&input={query}" \
                f"&format=plaintext" \
                f"&output=json"

    r = requests.get(query_url).json()
    #print(r)    
    temperatura = "N/A"
    wilogtonsc = "N/A"
    wiatr = "N/A"
    opad = "0"
    mgla = "0"
    burza = "0"
    with open('queries/'+query+'.json', 'w') as outfile:
        json.dump(r, outfile)
    if('pods' in r["queryresult"].keys()):
        try:
            data = r["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
            data = data.split("\n")
            for val in data:
                if "temperature" in val:
                    m = re.search('(-?[0-9]{1,2})', val)
                    if m:
                        temperatura = m.group(1)
                        print(temperatura)
                elif "humidity" in val:
                    m = re.search('([0-9]{1,})', val)
                    if m:
                        wilogtonsc = m.group(1)
                        print(wilogtonsc)
                elif "wind" in val:
                    m = re.search('([0-9]{1,3})', val)
                    if m:
                        wiatr = m.group(1)
                        print(wiatr) 
            print(data)
        except: 
            pass

        try:
            data = r["queryresult"]["pods"][2]["subpods"][2]["plaintext"]

            print(data)
            data = data.split("|")
            for val in data:
                if "fog:" in val:
                    m = re.search('([0-9]{1,2}\.?[0-9]?)', val)
                    if m:
                        mgla = m.group(1)
                        print(mgla)
                elif "rain:" in val:
                    m = re.search('([0-9]{1,2}\.?[0-9]?)', val)
                    if m:
                        opad = m.group(1)
                        print(opad)
                elif "thunderstorm:" in val:
                    m = re.search('([0-9]{1,2}\.?[0-9]?)', val)
                    if m:
                        burza = m.group(1)
                        print(burza)
        except:
            pass
    return temperatura, wilogtonsc, wiatr, opad, mgla, burza

def removeAccents(input_text):
    strange='ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'
    ascii_replacements='UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'
    translator=str.maketrans(strange,ascii_replacements)
    return input_text.translate(translator)
    
def parse(row, startYear, stopYear):
    data = row[1].split(" ")[0]
    day = data.split(".")[0]
    month = data.split(".")[1]
    if(int(month)>=7):
        data = startYear + "." + month + "." + day
    else:
        data = stopYear + "." + month + "." + day
    godzina = row[1].split(" ")[1]
    gospodarz = row[3]
    gosc = row[5].replace("\n","")
    miejsowosc = miejsowosci[gospodarz] if gospodarz in miejsowosci.keys() else ""
    wynik = row[6]+":"+row[7]
    # temperatura = "N/A"
    # wilogtonsc = "N/A"
    # wiatr = "N/A"
    # opad = "0"
    # mgla = "0"
    # burza = "0"
    temperatura, wilogtonsc, wiatr, opad, mgla, burza = wolframWeather(godzina, data, removeAccents(miejsowosc.lower()))
    return data + "\t" + godzina + "\t" + gospodarz + "\t" + gosc + "\t" + wynik + "\t" + miejsowosc + "\t" + temperatura + "\t" + wilogtonsc + "\t" + wiatr + "\t" + opad + "\t" + mgla + "\t" + burza + "\n"

def extractClubFixtures(matchLine, outpufile, startYear, stopYear):
    if(matchLine):
        tekst = matchLine.string
        for key in kluby.keys():
            tekst = tekst.upper().replace(key.upper(), kluby[key])
        row = tekst.split("\t")
        print(row)
        tekst = parse(row, startYear, stopYear)
        print(tekst)
        outpufile.write(tekst)


kluby = {"Legia Warszawa":"LEG","Pogoń Szczecin":"POG","Śląsk Wrocław":"ŚLĄ","Warta Poznań":"WAR","Piast Gliwice":"PIA","Lechia Gdańsk":"LGD","Jagiellonia Białystok":"JAG","Lech Poznań":"LPO","Wisła Płock":"WPŁ","Wisła Kraków":"WIS","Cracovia":"CRA","Stal Mielec":"SMI","Arka Gdynia":"ARK","Górnik Zabrze":"GÓR","Korona Kielce":"KOR","ŁKS Łódź":"ŁKS","Raków Częstochowa":"RCZ","Zagłębie Lubin":"ZAG","BRUK-BET T.":"BBT","SANDECJA NOWY SĄCZ":"SAN","RUCH CHORZÓW":"RCH","GÓRNIK ŁĘCZNA":"GKŁ","PODBESKIDZIE B-B":"POD","GKS BEŁCHATÓW":"GKS","ZAWISZA BYDGOSZCZ":"ZAW"}
miejsowosci = {"LEG":"Warszawa","POG":"Szczecin","ŚLĄ":"Wrocław","WAR":"Poznań","PIA":"Gliwice","LGD":"Gdańsk","JAG":"Białystok","LPO":"Poznań","WPŁ":"Płock","WIS":"Kraków","CRA":"Kraków","SMI":"Mielec","ARK":"Gdynia","GÓR":"Zabrze","KOR":"Kielce","ŁKS":"Łódź","RCZ":"Bełchatów","ZAG":"Lubin","BBT":"Nieciecza","SAN":"Nowy Sącz","RCH":"Chorzów","GKŁ":"Lublin","POD":"Bielsko-Biała","GKS":"Bełchatów","ZAW":"Bydgoszcz"}

startYear = "2017"
stopYear = "2018"
f = open("spotkania"+startYear+stopYear+".txt", "r", encoding="utf8")
f1 = open("spotkania"+startYear+stopYear+"k1.txt", "w", encoding="utf8")
f2 = open("spotkania"+startYear+stopYear+"k2.txt", "w", encoding="utf8")
f3 = open("spotkania"+startYear+stopYear+"k3.txt", "w", encoding="utf8")
for x in f:    
    # x = re.search("(^.*Lech .*$)|(^.*Cracovia.*$)|(^.*Korona .*$)", x)
	#Tu wpisujemy interesujące nas kluby
    k1 = re.search("^.*Lech .*$", x)
    k2 = re.search("^.*Lechia .*$", x)
    k3 = re.search("^.*Cracovia.*$", x)
    extractClubFixtures(k1, f1, startYear, stopYear)
    extractClubFixtures(k2, f2, startYear, stopYear)
    extractClubFixtures(k3, f3, startYear, stopYear)
f1.close()
f2.close()
f3.close()
# (^.*Lech .*$)|(^.*Cracovia.*$)|(^.*Korona .*$)
