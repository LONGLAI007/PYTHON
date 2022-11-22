A={19,8,42,4,6,16,90,13,50,55,39,71,22,81,12,35,1,9,80}
B={81,12,35,1,9,80,13,50,55,39,71,22,77,32,76,44,14,17}
C={27,3,33,45,7,77,32,76,22,71,39,44,14,17,29,47}
D={29,44,14,17,39,55,50,13,69,66,313,31,92}

Grup=A|B|C|D
a_d=A&B&C&D

a_b=A&B
a_c=C&D
G_ab=a_b|a_c

only_a=A-B-C-D
only_b=B-A-C-D
only_c=C-A-B-D
only_d=D-A-B-C
G_only=only_a|only_b|only_c|only_d


print(f'number set A: {len(A)} = {A} \n number set B: {len(B)} = {B} \n number set C: {len(C)} = {C} \n number set D: {len(D)} = {D} \n');
print(f'ຕົວເລກທີ່ມີທັງມົດມີ={len(Grup)} ຄື:{Grup}')
print(f'ຕົວເລກທີ່ເປັນສະມາຊີກທຸກກຸ່ມມີ:{len(a_d)}ຄື={a_d}')
print(f'ຕົວເລກທີ່ເປັນສະມາຊີກພຽງກຸ່ມດຽວ:{len(G_only)}ຄື={G_only}')
print(f'ຕົວເລກທີ່ເປັນສະມາຊີກ2ກຸ່ມຂື້ນໄປ: {len(G_ab)} ຄື{G_ab}')


