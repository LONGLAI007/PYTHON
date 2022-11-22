
#ຂໍ້ຄວາມອັນທີ່1  print(f'translate: {engh.get(w,"not found")}')
def eng(w):
    engh={ 'apple':'ໝາກແອບເປີນ',
           'banana':'ໝາກກ້ວຍ',
           'orange':'ໝາກກ້ຽງ',
           'coconut':'ໝາກພ້າວ',
           'jackfruit':'ໝາກມື້',
           'vokado':'ໝາກໂວກາໂດ'}
    print(f'translate: {engh.get(w,"not found")}')

def lao(w):
    laos={' ໝາກແອບເປີນ':'apple',
           'ໝາກກ້ຽງ':'orange',
           'ໝາກກ້ວຍ':'banana',
           'ໝາກພ້າວ': 'coconut',
           'ໝາກມື້': 'jackfruit'}
    print(f'ແປເປັນອັງກິດ : {laos.get(w,"ບໍ່ພົບຄ່ານີ້")}')

print("Welcome to my dictionary")
ch=(input(" ກົດ 1 ແປລາວເປັນອັງກິດ \n press 2 translate English to Lao:\n"))
if ch=='1':
    word = input('ສັບທີ່ຕ້ອງການແປ:')
    lao(word)
elif ch=='2':
    word = input('word to translate:')``
    eng(word)
else:
    print('Error!!!')
    

