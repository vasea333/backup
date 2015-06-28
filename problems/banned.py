text = "usa has banned letter"
alfabet = "abdehlnrstu"
for i in alfabet:
    print (text +": "+ i)
    text = "".join(text.replace(i,""))