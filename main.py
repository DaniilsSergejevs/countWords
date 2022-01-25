teksts = input("Ievadi tekstu: ")
def countWords(teksts):
  summa = 0
  sar1 = teksts.split()
  for word in sar1:
    if len(word)>1:
      summa += 1
    print(summa)
  return summa
countWords(teksts)