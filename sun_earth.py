#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

############ Sonnenberechnung

#sonnendurchm = 100 # km
sonnendurchm = 1392700 #km
#erddurchmesser = 10 #km
erddurchmesser = 12742 #km
sonne_r = sonnendurchm/2.0
erd_r = erddurchmesser/2.0

kub_a = (4.0*erd_r)/(math.sqrt(2))

vec1_1 = [1,1,1]
vec1_2 = [1,1,0]
vec1_3 = [1,0,0]
vec1_4 = [0,1,1]
vec1_5 = [0,0,1]
vec1_6 = [1,0,1]

kub_vec = []
kub_count = 0

max_count = 100
min_count = max_count*(-1)
maximum = (max_count*2)*(2*max_count)*(2*max_count)

main_loop = 0

print_counter = 0
f = open("vektor.txt", "w")

for x in range(min_count, max_count, 1):
    for y in range(min_count, max_count, 1):
        for z in range(min_count, max_count, 1):
            main_loop+=1
            print_counter+=1
            if print_counter == 1000:
                print (str(main_loop)+"/"+str(maximum))
                print_counter=0
            
            kub1_1 = [x*vec1_1[0]*kub_a,y*vec1_1[1]*kub_a,z*vec1_1[2]*kub_a]
            #kub1_2 = [x*vec1_2[0]*kub_a,y*vec1_2[1]*kub_a,z*vec1_2[2]*kub_a]
            #kub1_3 = [x*vec1_3[0]*kub_a,y*vec1_3[1]*kub_a,z*vec1_3[2]*kub_a]
            #kub1_4 = [x*vec1_4[0]*kub_a,y*vec1_4[1]*kub_a,z*vec1_4[2]*kub_a]
            #kub1_5 = [x*vec1_5[0]*kub_a,y*vec1_5[1]*kub_a,z*vec1_5[2]*kub_a]
            #kub1_6 = [x*vec1_6[0]*kub_a,y*vec1_6[1]*kub_a,z*vec1_6[2]*kub_a]
        
            betrag_v1= math.sqrt(kub1_1[0]*kub1_1[0]+kub1_1[1]*kub1_1[1]+kub1_1[2]*kub1_1[2])
            #betrag_v2= math.sqrt(kub1_2[0]*kub1_2[0]+kub1_2[1]*kub1_2[1]+kub1_2[2]*kub1_2[2])
            #betrag_v3= math.sqrt(kub1_3[0]*kub1_3[0]+kub1_3[1]*kub1_3[1]+kub1_3[2]*kub1_3[2])
            #betrag_v4= math.sqrt(kub1_4[0]*kub1_4[0]+kub1_4[1]*kub1_4[1]+kub1_4[2]*kub1_4[2])
            #betrag_v5= math.sqrt(kub1_5[0]*kub1_5[0]+kub1_5[1]*kub1_5[1]+kub1_5[2]*kub1_5[2])
            #betrag_v6= math.sqrt(kub1_6[0]*kub1_6[0]+kub1_6[1]*kub1_6[1]+kub1_6[2]*kub1_6[2])
        
            if (betrag_v1 < sonne_r):
                f.write(str(kub1_1[0])+","+str(kub1_1[1])+","+str(kub1_1[2])+"\n")
                kub_count+=1

            #if (betrag_v2 < sonne_r):            
            #    f.write(str(kub1_2[0])+","+str(kub1_2[1])+","+str(kub1_2[2])+"\n")
            #    kub_count+=1

            #if (betrag_v3 < sonne_r):            
            #    f.write(str(kub1_3[0])+","+str(kub1_3[1])+","+str(kub1_3[2])+"\n")
            #    kub_count+=1

            #if (betrag_v4 < sonne_r):            
            #    f.write(str(kub1_4[0])+","+str(kub1_4[1])+","+str(kub1_4[2])+"\n")
            #    kub_count+=1

            #if (betrag_v5 < sonne_r):            
            #    f.write(str(kub1_5[0])+","+str(kub1_5[1])+","+str(kub1_5[2])+"\n")
            #    kub_count+=1

            #if (betrag_v6 < sonne_r):            
            #    f.write(str(kub1_6[0])+","+str(kub1_6[1])+","+str(kub1_6[2])+"\n")
            #    kub_count+=1

print(str(main_loop) + " Iterationen")
print("Erdradius: "+str(erd_r)+ " km")
print("Sonnenradius: "+str(sonne_r)+ " km")
print("Seitnlänge Kubus: "+str(kub_a)+" km")
print(kub_vec)
print("Anzahl Erden: "+str(kub_count))

f.close()

#f = open("vektor.txt", "r")
#kub_vec = []
#kub_count2 = 0
#f2 = open("vektor2.txt", "w")
#print_counter = 0
#main_loop=0
#while True:
#     line = f.readline()
#     main_loop+=1
#     print_counter+=1
#     if print_counter == 1000:
#         print (main_loop)
#         print_counter=0
#     if line in kub_vec:
#         continue
#     else:
#         kub_vec.append(line)
#         kub_count2+=1
#         f2.write(line)
#     if not line:
#         break
#     
# f.close()
# f2.close()
# #print(kub_vec)
# print("Anzahl Erden: "+str(kub_count2))
