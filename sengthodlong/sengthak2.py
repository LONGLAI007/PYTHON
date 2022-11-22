
#group A,B,C,D

A={19,8,42,4,6,16,90,13,50,55,39,71,22,81,12,35,1,9,80}
B={81,12,35,1,9,80,13,50,55,39,71,22,77,32,76,44,14,17}
C={27,3,33,45,7,77,32,76,22,71,39,44,14,17,29,47}
D={29,44,14,17,39,55,50,13,69,66,313,31,92}

groupall=A|B|C|D

groupad=A&B&C&D


only_a=A-B-C-D
only_b=B-A-C-D
only_c=C-A-B-D
only_d=D-A-B-C
G_only=only_a|only_b|only_c|only_d

a_b=A&B
b_c=B&C
a_d=C&D
G_ab=a_b|b_c|a_d

print(f' ກຸ່ມA ມີ:{len(A)}ຕົວ ຄື:{A}\n ກຸ່ມB ມີ:{len(B)}ຕົວ ຄື:{B}\n ກຸ່ມC ມີ:{len(C)}ຕົວ ຄື:{C}\n ກຸ່ມD ມີ:{len(D)}ຕົວ ຄື:{D}\n')
print(f'ຕົວເລກທັງໝົດມີ:{len(groupall)} ຄື:{groupall}')
print(f'ຕົວເລກທີ່ເປັນສະມາຊີກທຸກຕົວ:{len(groupad)} ຄື:{groupad}')
print(f'ຕົວເລກທີ່ເປັນສະມາຊີກພຽງກຸ່ມດຽວ:{len(G_only)} ຄື:{G_only}')
print(f'ຕົວເລກທີ່ເປັນສະມາຊີກຕັ້ງແຕ່2ກຸ່ມຂື້ນໄປມີ:{len(G_ab)} ຄື:{G_ab}')







