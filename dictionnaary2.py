    
def col(w):
    color={'red' : 'ສິແດງ',
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
           'cyan':'ສີທະເລ',}
    print(f'Translate : {color.get(w,"Not found")}')
def col2(w):
    colors  =  {'ສີແດງ': "red",
             'ສີຂຽວ' : "green",
             'ສີຟ້າ' : "blue",
             'ສີເຫຼືອງ' : "yellow",
             'ສີມ້ວງ' : "purple",
             'ສີດຳ' : "black",
             'ສີຂາວ' : "white",
             'ສີສົ້ມ' : "orange",
             'ສີບົວ' : "pink",
             'ສີຊົມພູ': "pink",
             'ສີຂີ້ເຖົ່າ' : "gray",
             'ສີຕັບໝູ' : "brow",
             'ສີທະເລ' : "cyan",}
    print(f'ແປ  : {colors.get(w,"ບໍ່ພົບຄຳວັບນີ້")}')
print("Welcom to funny dictionary.")
ch = input("ກົດ 1 ແປເປັນພາສາລາວ, press 2 for English to Lao : ")
if ch ==  '1':
    word = input(" ຄຳສັບທີ່ຕ້ອງການແປ: ")
    col2(word)
elif ch == "2":
    word = input('Word to translate : ')
    col(word)
else:
    print('Error!! ')
   


