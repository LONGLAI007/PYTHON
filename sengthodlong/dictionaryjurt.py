

def eng(w):
    engh={'apple':'ໝາກໂປ່ມ',
           'orange':'ໝາກກ້ຽງ',
           'banana':'ໝາກກ້ວຍ',
           'coconut':'ໝາກພ້າວ',
           'jackfruit':'ໝາກມື້'}
    print(f'translate: {engh.get(w,"not found")}')

def lao(w):
    laos={'ໝາກໂປ່ມ':'apple',
           'ໝາກກ້ຽງ':'orange',
           'ໝາກກ້ວຍ':'banana',
           'ໝາກພ້າວ': 'coconut',
           'ໝາກມື້': 'jackfruit'}
    print(f'ແປເປັນອັງກິດ : {laos.get(w,"ບໍ່ພົບຄ່ານີ້")}')

print("Welcome to my dictionary")
ch=(input("ກົດ 1 ແປລາວເປັນອັງກິດ press 2 translate English to Lao:"))
if ch=='1':
    word = input('ສັບທີ່ຕ້ອງການແປ:')
    lao(word)
elif ch=='2':
    word = input('word to translate:')
    eng(word)
else:
    print('Error!!!')