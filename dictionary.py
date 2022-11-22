def col(l):

    laocorlo={
        "ສີແດງ":"red",
        "ສີຟ້າ":"green",
        "ສີເຫຼືອງ":"yellow",
        "ສີມວງ":" purple",
        "ສີຂາວ":"white",
        "ສີດຳ":"black",
        "ສີສົມ":"orange",
        "ສີບົວ":"pink",
        "ສີເທົາ":"gray",
        "ສີຕັບໝູ":"brow",
        "ສີທະເລ":"cyan",
        "ສີທອງ":"glod",
    }
    print(f'ແປ :{laocorlo.get(l,"ບໍ່ພົບຄຳນີ້")}') #kro la nee t br sai tua brok commen nun ley
    print("welcome to funy dictionary")
def ll1(l):
    englo = {
        'red' : 'ສິແດງ',
           'green' : 'ສີຂຽວ',
           'blue' : 'ສີຟ້າ',
           'yellow':'ສີເຫຼືອງ',
           'purple':'ສີມ່ວງ',
           'black':'ສີດຳ',
           'white':'ສີຂາວ',
           'orange':'ສີສົ້ມ',
           'pink':'ສີບົວ',
           'gray':'ສີຂີ້ເຖົ່າ',
           'brow':'ສີຕັບໝູ',
           'cyan':'ສີທະເລ',
    }
    print(f'ແປ :{englo.get(l,"ບໍ່ພົບຄຳນີ້")}')
print("Welcom to funny dictionary.")
n = input("Enter number (1 & 2): ")
if n=='1':
     word = input("ຄຳສັບທີ່ຕ້ອງການແປ")
     col(word)
elif n=='2':
     word1 = input ("word to tanslat ")
     ll1(word1)
else:
      print('Error!! ')



  