
#kan set dictionary
A={21,4,11,5,6,13,20,16}
B={2,3,17,22,20,13,5,6,}
C={9,8,14,18,17,3}
D={1,10,16,15,20,22,17,18}


# lom ao tung mod t U nai group A,B,C,D start
all=A|B|C|D

#print("all nuber:",len(all),all)
#print("Set A:",len(A),A);

# lom ao tung mod t U nai group A,B,C,D end 

#lom sa thc number t U nai set A&B start
a_b=A&B
#print("there are number in A&B",len(a_b),a_b);

#lom sa thc number t U nai set A&B end


#print tung mod nai tag dw start
print(f' all number :{len(all)} number is:{all} \n number A&B:{len(a_b)} number is:{a_b} \n set A:{len(A)} number is:{A}')
#print tung mod nai tag dw end 

#tae la set me to dai t br U nai group num mu start
G_A=A-B-C-D
G_B=B-A-C-D
G_C=C-A-B-D
G_D=D-A-B-C
print(f' set A only:{len(G_A)} number is:{G_A} \n set B only:{len(G_B)} number is:{G_B} \n set C only:{len(G_C)} number is:{G_C} \n set D only:{len(G_D)} number is:{G_D}')



#tae la set me to dai t br U nai group num mu end

