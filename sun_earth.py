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

kubah_p = kub_a/2
kubah_m = (-1)*kub_a/2


# Kubus
vec1_1 = [kubah_m,kubah_m,kubah_m]
vec1_2 = [kubah_p,kubah_m,kubah_m]
vec1_3 = [kubah_p,kubah_m,kubah_p]
vec1_4 = [kubah_m,kubah_m,kubah_p]
vec1_5 = [kubah_m,kubah_p,kubah_m]
vec1_6 = [kubah_p,kubah_p,kubah_m]
vec1_7 = [kubah_p,kubah_p,kubah_p]
vec1_8 = [kubah_m,kubah_p,kubah_p]

kub_vec = []
kub_count = 0
kub_count_innen = 0
kub_count_rand = 0
kub_count_aussen = 0

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
            # Mittelpunkt Kubus
            kub1_1 = [x*kub_a,y*kub_a,z*kub_a]
                
            betrag_v1= math.sqrt(kub1_1[0]*kub1_1[0]+kub1_1[1]*kub1_1[1]+kub1_1[2]*kub1_1[2])
        
            # Sitzt der Kubis in der Nähe des Sonnenrandes
            if (betrag_v1 < (sonne_r+erddurchmesser)):
                # Vektor+
                kub1_1_erg = [kub1_1[0]+vec1_1[0],kub1_1[1]+vec1_1[1],kub1_1[2]+vec1_1[2]]
                kub1_2_erg = [kub1_1[0]+vec1_2[0],kub1_1[1]+vec1_2[1],kub1_1[2]+vec1_2[2]]
                kub1_3_erg = [kub1_1[0]+vec1_3[0],kub1_1[1]+vec1_3[1],kub1_1[2]+vec1_3[2]]
                kub1_4_erg = [kub1_1[0]+vec1_4[0],kub1_1[1]+vec1_4[1],kub1_1[2]+vec1_4[2]]
                kub1_5_erg = [kub1_1[0]+vec1_5[0],kub1_1[1]+vec1_5[1],kub1_1[2]+vec1_5[2]]
                kub1_6_erg = [kub1_1[0]+vec1_6[0],kub1_1[1]+vec1_6[1],kub1_1[2]+vec1_6[2]]
                kub1_7_erg = [kub1_1[0]+vec1_7[0],kub1_1[1]+vec1_7[1],kub1_1[2]+vec1_7[2]]
                kub1_8_erg = [kub1_1[0]+vec1_8[0],kub1_1[1]+vec1_8[1],kub1_1[2]+vec1_8[2]]

                betrag_kub_v1= math.sqrt(kub1_1_erg[0]*kub1_1_erg[0]+kub1_1_erg[1]*kub1_1_erg[1]+kub1_1_erg[2]*kub1_1_erg[2])
                betrag_kub_v2= math.sqrt(kub1_2_erg[0]*kub1_2_erg[0]+kub1_2_erg[1]*kub1_2_erg[1]+kub1_2_erg[2]*kub1_2_erg[2])
                betrag_kub_v3= math.sqrt(kub1_3_erg[0]*kub1_3_erg[0]+kub1_3_erg[1]*kub1_3_erg[1]+kub1_3_erg[2]*kub1_3_erg[2])
                betrag_kub_v4= math.sqrt(kub1_4_erg[0]*kub1_4_erg[0]+kub1_4_erg[1]*kub1_4_erg[1]+kub1_4_erg[2]*kub1_4_erg[2])
                betrag_kub_v5= math.sqrt(kub1_5_erg[0]*kub1_5_erg[0]+kub1_5_erg[1]*kub1_5_erg[1]+kub1_5_erg[2]*kub1_5_erg[2])
                betrag_kub_v6= math.sqrt(kub1_6_erg[0]*kub1_6_erg[0]+kub1_6_erg[1]*kub1_6_erg[1]+kub1_6_erg[2]*kub1_6_erg[2])
                betrag_kub_v7= math.sqrt(kub1_7_erg[0]*kub1_7_erg[0]+kub1_7_erg[1]*kub1_7_erg[1]+kub1_7_erg[2]*kub1_7_erg[2])
                betrag_kub_v8= math.sqrt(kub1_8_erg[0]*kub1_8_erg[0]+kub1_8_erg[1]*kub1_8_erg[1]+kub1_8_erg[2]*kub1_8_erg[2])
                
                tmp = 0
                vergleich = sonne_r-erd_r
                if (betrag_kub_v1 < (vergleich)):
                      tmp = tmp+1
                if (betrag_kub_v2 < (vergleich)):
                      tmp = tmp+1
                if (betrag_kub_v3 < (vergleich)):
                      tmp = tmp+1
                if (betrag_kub_v4 < (vergleich)):
                      tmp = tmp+1
                if (betrag_kub_v5 < (vergleich)):
                      tmp = tmp+1
                if (betrag_kub_v6 < (vergleich)):
                      tmp = tmp+1
                if (betrag_kub_v7 < (vergleich)):
                      tmp = tmp+1
                if (betrag_kub_v8 < (vergleich)):
                      tmp = tmp+1
                
                if ((tmp > 0) and (tmp < 8)):
                   kub_count_rand+=1    
                elif (tmp == 0):
                   kub_count_aussen+=1   
                elif (tmp == 8):
                   kub_count_innen+=1    
                
                f.write(str(kub1_1[0])+","+str(kub1_1[1])+","+str(kub1_1[2])+","+str(tmp)+"\n")
                kub_count+=1
        
        
                


print(str(main_loop) + " Iterationen")
print("Erdradius: "+str(erd_r)+ " km")
print("Sonnenradius: "+str(sonne_r)+ " km")
print("Seitenlänge Kubus: "+str(kub_a)+" km")
print(kub_vec)
print("Anzahl Kuben: "+str(kub_count))
print("Anzahl Kuben innen: "+str(kub_count_innen))
print("Anzahl Kuben rand: "+str(kub_count_rand))
print("Anzahl Kuben aussen: "+str(kub_count_aussen))

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
