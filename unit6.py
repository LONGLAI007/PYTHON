from itertools import count


yougth={"somchai","viboun","vanhna","NIundon","vilai vanny","mali","chitthanome",
"vongchan","sengthong","sengchan","souchai","sonxay","somkhit","thongkhan"}
union={"bounmee","thongsa","sysun","sengvanh","mali","sengchan","sengthong",
"chitthanome","vongchan","souchai","sonxay","somkhit","thongkhan"}
women={"Alouny","vanthong","channy","somsy","sysun","sengvanh","mali","sengchan","sengthong",
"chitthanome","vongchan","NIundon","vilai vanny"}

a=yougth|union|women #ຈຳນວນທັງໝົດຄົນ3ກຸ່ມ
print("ຈຳນວນຄົນທັງໝົດ",len(a),a )
print("*********************************************************")
print("ຈຳນວນໄວໝຸມທັງໝົດ",len(yougth),yougth)#ຊາວໝຸມທັງມົດ
print("*********************************************************")
print("ຈຳນວນກຳມະບານທັງໝົດ",len(union),union)#ກຳມະບານທັງມົດ
print("*********************************************************")
print("ຈຳນວນແມ່ຍິງທັງໝົດ",len(women),women)#ແມ່ຍີງທັງມົດ
print("*********************************************************")

b=yougth&union #ຈຳນວນຄົນທີ່ເປັນໄວໝຸມ ແລະ ກຳມະບານ
print("ໄວໝຸມແລະກຳມະບານ",len(b),b)
print("*********************************************************")

c=yougth&women #ຈຳນວນຄົນທີ່ເປັນໄວໝຸມ ແລະ ແມ່ຍີງ
print("ໄວໝຸມແລະແມ່ຍີງ",len(c),c)
print("*********************************************************")

d=women&union # ແມ່ຍີງແລະ ກຳມະບານ
print("ແມ່ຍີງແລະ ກຳມະບານ",len(d),d)
print("*********************************************************")

e=yougth&union&women  #ຄົນທີ່ເປັນທັງ ແມ່ຍີງ ຊາວໝຸມ ກຳມະບານ
print("ຄົນທີ່ເປັນທັງ ແມ່ຍີງ ຊາວໝຸມ ກຳມະບານ",len(e),e)

print("*********************************************************")

f=yougth-union-women #ຄົນທີ່ເປັນຊາວໝຸມຢ່າງດຽວ
print("ຄົນທີ່ເປັນຊາວໝຸມຢ່າງດຽວ",len(f),f)

print("*********************************************************")
g=union-women-yougth #ຄົນທີ່ເປັນ ກຳມະບານຢ່າງດຽວ
print("ຄົນທີ່ເປັນ ກຳມະບານຢ່າງດຽວ",len(g),g)
print("*********************************************************")
h=women-yougth-union #ຄົນທີ່ເປັນ ແມ່ຍີງຢ່າງດຽວ
print("ຄົນທີ່ເປັນ ແມ່ຍີງຢ່າງດຽວ",len(h),h)
print("*********************************************************")
i=f|g|h #ຄົນທີ່ເປັນຊາວໝຸມ,ແມ່ຍີງ,ກຳມະບານ ຢ່າງດຽວມີ
print("ຄົນທີ່ເປັນຊາວໝຸມ,ແມ່ຍີງ,ກຳມະບານ ຢ່າງດຽວມີ",len(i),i)








