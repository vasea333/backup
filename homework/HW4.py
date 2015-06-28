def main():
   citynum = AskForNumberCities()
   citylist = AskForCityName(citynum)
   sentence = PrintFirstCitySentence(citylist)
   PrintAddOneCityNumSentence(sentence)

def AskForNumberCities():
   print "Pleas type number of city"
   citynum = raw_input()
   if citynum.isdigit() and (int(citynum) > 0):
       print "Number of city is "+citynum
       return int(citynum)
   else:
       print "Invalid Option, you needed to type a 1, 2 or 3...."
       return AskForNumberCities()

def AskForCityName(citynum):
    citylist = []
    while len(citylist) < int(citynum):
        print ("Please type city number " + str(len(citylist)+1))
        city = raw_input().upper()
        if city not in citylist and city.isalpha():
            citylist.append(city)
        else:
            print "Invalid Option"
    return citylist

def PrintFirstCitySentence(citylist):
  sentence = ""
  for i in range (0, len(citylist)):
      sentence = sentence +" and "+ citylist[i]+" "+str(i+1)
  print sentence[5:]
  return sentence

def PrintAddOneCityNumSentence(sentence):
   list1 = sentence.split()
   list1=[str(int(x)+1) if x.isdigit() else x for x in list1]
   print(' '.join(list1))[4:]

if __name__ == "__main__":
   main()