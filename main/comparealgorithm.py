# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np

"""##### 쏘카 데이터베이스"""

socar = pd.read_csv('static/csv/socar.csv')
socar = socar.set_index('car_type')

"""##### 쏘카 주행료 데이터 베이스"""

dr = pd.read_csv('static/csv/driving_fee.csv')
dr = dr.set_index('car_type')

"""##### 그린카 데이터베이스"""

green = pd.read_csv('static/csv/green.csv')
green = green.set_index('car_type')

"""##### 그린카 쿠폰 계산 함수"""

def green_coupon_computer(rental_time,start_time,car):
    
    if rental_day != '토' and rental_day != '일' and 18<=start_time<=24 and rental_time>=16:
        rental_cost.append(int(6900 + (rental_time - 16)*int(green['rental_gap'][car])*(green['discount_basic'][car])))
        coupon_var_green.append('적용된 쿠폰은 \'퇴근부터 출근까지 6,900원 할인\'')
    elif rental_day != '토' and rental_day != '일' and 10<= rental_time <=24:
        rental_cost.append(23000)
        coupon_var_green.append('적용된 쿠폰은 \'10시간 이상 대여시 하루 종일 23,000원 할인\'')
    elif rental_day != '토' and rental_day != '일' and rental_time>=34 :
        rental_cost.append(59000)
        coupon_var_green.append('적용된 쿠폰은 \'1박2일 59,000원 할인\'')
    elif rental_day != '토' and rental_day != '일' and rental_time>=58 :
        rental_cost.append(79000)
        coupon_var_green.append('적용된 쿠폰은 \'2박 3일 79,000원 할인\'')
    elif rental_day != '토' and rental_day != '일' and rental_time>=82:
        rental_cost.append(99000)
        coupon_var_green.append('적용된 쿠폰은 \'3박 4일 99,000원 할인\'')
            
    else:
        coupon_var_green.append('적용할 수 있는 쿠폰 없음')
        rental_cost.append(int(green['rental_fee'][car]*float(green['discount_basic'][car]) + (rental_time - 1)*int(green['rental_gap'][car])))

"""#### 그린카 가격 측정 함수"""

def green_option():
    global green_cost_small
    global ensure_1,ensure_1_cost,total_cost,total_cost_dic,semi_medium_car_driving_cost,semi_medium_car_rental_cost,d_cost,r_cost
    global medium_car_driving_cost,medium_car_rental_cost, suv_car_rental_cost, suv_car_driving_cost,minute,start_time,finish_time,rental_day,rental_time
    global green_cost,coupon_green,semi_medium_car_list,rental_cost
    global coupon_var_green
    rental_cost=[]
    coupon_var_green=[]
    coupon_green=[]
    geen_cost=0
    green_cost_small=0
    ensure_1={}
    ensure_1_cost=[]
    total_cost=[]
    total_cost_dic={}  
    semi_medium_car_driving_cost={}
    semi_medium_car_rental_cost={}
    medium_car_driving_cost={}
    medium_car_rental_cost={}
    suv_car_driving_cost={}
    suv_car_rental_cost={}
    d_cost=[]
    r_cost=[]
    
 
    
    if car_type[0:2]=='경형':   
        small_car_list = ['morning']

        driving_cost = driving_km* int(green['driving_fee'][small_car_list[0]])
        for car in small_car_list:
            green_coupon_computer(rental_time,start_time,car) 
            tmp = min(rental_cost)
            index = rental_cost.index(tmp)
            coupon_var=coupon_var_green[index]
            small_car_rental_cost[car]=tmp
            coupon_green.append(coupon_var)
            
            
        if ensure_type == 1: 

            ensure_charge = int(green['ensure_70_basic'][small_car_list[0]])+(rental_time - 1)*(int(green['ensure_70'][small_car_list[0]]))
            print(type(green_cost_small), type(rental_cost), type(ensure_charge), type(driving_cost))
            print(rental_cost)
            green_cost_small = green_cost_small + sum(rental_cost) + ensure_charge + driving_cost

            
        elif ensure_type == 2:

            ensure_charge = int(green['ensure_30_basic'][small_car_list[0]])+(rental_time - 1)*(int(green['ensure_30'][small_car_list[0]]))
            print(type(green_cost_small), type(rental_cost), type(ensure_charge), type(driving_cost))

            green_cost_small = green_cost_small + sum(rental_cost) + ensure_charge + driving_cost

        elif ensure_type == 3:
                
            ensure_charge = int(green['ensure_5_basic'][small_car_list[0]])+(rental_time - 1)*(int(green['ensure_5'][small_car_list[0]]))
            print(type(green_cost_small), type(rental_cost), type(ensure_charge), type(driving_cost))

            green_cost_small = green_cost_small + sum(rental_cost) + ensure_charge + driving_cost
        
        green_cost = int(green_cost_small)   
        
            
    if car_type[0:3]=='준중형':    
        semi_medium_car_list = ['Ionic', 'k3', 'All_New_Avante']
               
        for i in range(len(semi_medium_car_list)):
            driving_cost = driving_km* int(green['driving_fee'][semi_medium_car_list[i]])
            d_cost.append(driving_cost) 
            semi_medium_car_driving_cost[semi_medium_car_list[i]]=d_cost[i] 
        
        for car in semi_medium_car_list:  
            green_coupon_computer(rental_time,start_time,car) 
            tmp = min(rental_cost)
            index = rental_cost.index(tmp)
            coupon_var=coupon_var_green[index]
            semi_medium_car_rental_cost[car]=tmp
            coupon_green.append(coupon_var)

        if ensure_type == 1: 
            for i in range(len(semi_medium_car_list)):
            
                ensure_charge = int(green['ensure_70_basic'][semi_medium_car_list[i]])+(rental_time - 1)*(int(green['ensure_70'][semi_medium_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[semi_medium_car_list[i]]=ensure_1_cost[i]
          
                green_cost_semi = semi_medium_car_rental_cost[semi_medium_car_list[i]] + ensure_1[semi_medium_car_list[i]] + semi_medium_car_driving_cost[semi_medium_car_list[i]]
                total_cost.append(green_cost_semi)
                total_cost_dic[semi_medium_car_list[i]]=total_cost[i]

        if ensure_type == 2: 
            for i in range(len(semi_medium_car_list)):
            
            
                ensure_charge = int(green['ensure_30_basic'][semi_medium_car_list[i]])+(rental_time - 1)*(int(green['ensure_30'][semi_medium_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[semi_medium_car_list[i]]=ensure_1_cost[i]

                green_cost_semi = semi_medium_car_rental_cost[semi_medium_car_list[i]] + ensure_1[semi_medium_car_list[i]] + semi_medium_car_driving_cost[semi_medium_car_list[i]]
                total_cost.append(green_cost_semi)
                total_cost_dic[semi_medium_car_list[i]]=total_cost[i]

        if ensure_type == 3: 
            for i in range(len(semi_medium_car_list)):
           
            
                ensure_charge = int(green['ensure_5_basic'][semi_medium_car_list[i]])+(rental_time - 1)*(int(green['ensure_5'][semi_medium_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[semi_medium_car_list[i]]=ensure_1_cost[i]
        

                green_cost_semi = semi_medium_car_rental_cost[semi_medium_car_list[i]] + ensure_1[semi_medium_car_list[i]] + semi_medium_car_driving_cost[semi_medium_car_list[i]]
                total_cost.append(green_cost_semi)
                total_cost_dic[semi_medium_car_list[i]]=total_cost[i]

        green_cost = total_cost_dic 
            
    if car_type[0:2]=='중형':    
        medium_car_list = ['k5_Hybrid', 'k5', 'sonata']
             
        for i in range(len(medium_car_list)):
            driving_cost = driving_km* int(green['driving_fee'][medium_car_list[i]])
            d_cost.append(driving_cost)
            medium_car_driving_cost[medium_car_list[i]]=d_cost[i]
        
        for car in medium_car_list: 
            green_coupon_computer(rental_time,start_time,car) 
            tmp = min(rental_cost)
            index = rental_cost.index(tmp)
            coupon_var=coupon_var_green[index]
            medium_car_rental_cost[car]=tmp
            coupon_green.append(coupon_var)
        if ensure_type == 1: 
            for i in range(len(medium_car_list)):
       
            
                ensure_charge = int(green['ensure_70_basic'][medium_car_list[i]])+(rental_time - 1)*(int(green['ensure_70'][medium_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[medium_car_list[i]]=ensure_1_cost[i]
        
            
        
                green_cost_mid = medium_car_rental_cost[medium_car_list[i]] + ensure_1[medium_car_list[i]] + medium_car_driving_cost[medium_car_list[i]]
                total_cost.append(green_cost_mid)
                total_cost_dic[medium_car_list[i]]=total_cost[i]
            
            
            

        if ensure_type == 2: 
            for i in range(len(medium_car_list)):
          
            
                ensure_charge = int(green['ensure_30_basic'][medium_car_list[i]])+(rental_time - 1)*(int(green['ensure_30'][medium_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[medium_car_list[i]]=ensure_1_cost[i]
        
            
            
                green_cost_mid = medium_car_rental_cost[medium_car_list[i]] + ensure_1[medium_car_list[i]] + medium_car_driving_cost[medium_car_list[i]]
                total_cost.append(green_cost_mid)
                total_cost_dic[medium_car_list[i]]=total_cost[i]
            
            
         
        
   
        if ensure_type == 3: 
            for i in range(len(medium_car_list)):
            
            
                ensure_charge = int(green['ensure_5_basic'][medium_car_list[i]])+(rental_time - 1)*(int(green['ensure_5'][medium_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[medium_car_list[i]]=ensure_1_cost[i]
        
            
            
                green_cost_mid = medium_car_rental_cost[medium_car_list[i]] + ensure_1[medium_car_list[i]] + medium_car_driving_cost[medium_car_list[i]]
                total_cost.append(green_cost_mid)
                total_cost_dic[medium_car_list[i]]=total_cost[i]
            
            
           
        
        green_cost = total_cost_dic
        
    if car_type[0:3]=='suv':   
        suv_car_list = ['Seltos', 'trailblazer', 'XM3']
              
        for i in range(len(suv_car_list)):
            driving_cost = driving_km* int(green['driving_fee'][suv_car_list[i]])
            d_cost.append(driving_cost) 
            suv_car_driving_cost[suv_car_list[i]]=d_cost[i] 
        
        for car in suv_car_list:
            green_coupon_computer(rental_time,start_time,car) 
            tmp = min(rental_cost)
            index = rental_cost.index(tmp)
            coupon_var=coupon_var_green[index]
            suv_car_rental_cost[car]=tmp
            coupon_green.append(coupon_var)
        if ensure_type == 1: 
            for i in range(len(suv_car_list)):
            
            
                ensure_charge = int(green['ensure_70_basic'][suv_car_list[i]])+(rental_time - 1)*(int(green['ensure_70'][suv_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[suv_car_list[i]]=ensure_1_cost[i]
        
            
            
                green_cost_suv = suv_car_rental_cost[suv_car_list[i]] + ensure_1[suv_car_list[i]] + suv_car_driving_cost[suv_car_list[i]]
                total_cost.append(green_cost_suv)
                total_cost_dic[suv_car_list[i]]=total_cost[i]
            
            
          
        
        
        if ensure_type == 2: 
            for i in range(len(suv_car_list)):
            
            
                ensure_charge = int(green['ensure_30_basic'][suv_car_list[i]])+(rental_time - 1)*(int(green['ensure_30'][suv_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[suv_car_list[i]]=ensure_1_cost[i]
        
            
            
                green_cost_suv = suv_car_rental_cost[suv_car_list[i]] + ensure_1[suv_car_list[i]] + suv_car_driving_cost[suv_car_list[i]]
                total_cost.append(green_cost_suv)
                total_cost_dic[suv_car_list[i]]=total_cost[i]
      
        if ensure_type == 3: 
            for i in range(len(suv_car_list)):
            
            
                ensure_charge = int(green['ensure_5_basic'][suv_car_list[i]])+(rental_time - 1)*(int(green['ensure_5'][suv_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[suv_car_list[i]]=ensure_1_cost[i]
        
            
            
                green_cost_suv = suv_car_rental_cost[suv_car_list[i]] + ensure_1[suv_car_list[i]] + suv_car_driving_cost[suv_car_list[i]]
                total_cost.append(green_cost_suv)
                total_cost_dic[suv_car_list[i]]=total_cost[i]
            
            
            
        green_cost = total_cost_dic

"""#### 쏘카 쿠폰계산 함수"""

def socar_coupon_computer(rental_time,start_time,car):
    global rental_cost,coupon_var_socar
    
    if rental_day != '토' and rental_day != '일' and start_time >=17 and finish_time<=35 and 6<=rental_time<=16:
            coupon_var_socar.append('적용된 쿠폰은 \'16시간 9,900원 부터\'')
            rental_cost.append(9900)
                
    if rental_day != '토' and rental_day != '일' and start_time >=17 and finish_time<=35  and rental_time>16:
            coupon_var_socar.append('적용된 쿠폰은 \'16시간 9,900원 부터\'')
            rental_cost.append(9900 + (rental_time-16)*int(socar['rental_gap'][car]))

                
    if rental_day !='토' and start_time>=19 and car_type[0:3] !='suv'and 4<=rental_time<=24:
            coupon_var_socar.append('적용된 쿠폰은 \'내륙하루종일 29,000원\'')
            rental_cost.append(29000)
                
                    
    if  rental_day !='토' and start_time>=19 and car_type[0:3] !='suv'and rental_time>24:
            coupon_var_socar.append('적용된 쿠폰은 \'내륙하루종일 29,000원\'')
            rental_cost.append(29000 + (rental_time-24)*(rental_time-16)*int(socar['rental_gap'][car]))
                    

                    
    if car_type[0:2]=='경형'and 30<=rental_time <=48:
            rental_cost.append(60000)
            coupon_var_socar.append('적용된 쿠폰은 \'경형 1박 2일 60,000원\'')
            
    if car_type[0:2]=='경형' and rental_time>48:
            coupon_var_socar.append('적용된 쿠폰은 \'경형 1박 2일 60,000원\'')
            rental_cost.append(60000 +(rental_time-48)*int(socar['rental_gap'][car]))

                    
                    
    if 30<=rental_time<=90:
            coupon_var_socar.append('적용된 쿠폰은 \'2박 3일 114,000원\'')
            rental_cost.append(114000)
    if rental_time>90:
            coupon_var_socar.append('적용된 쿠폰은 \'2박 3일 114,000원\'')
            rental_cost.append( 114000 +(rental_time-90)*int(socar['rental_gap'][car]))
    if car_type[0:3] !='suv' and 30<=rental_time <=48:
            coupon_var_socar.append('적용된 쿠폰은 \'1박 2일 84,000원\'')
            rental_cost.append(84000)
            
    if car_type[0:3] !='suv' and rental_time>48:
            coupon_var_socar.append('적용된 쿠폰은 \'1박 2일 84,000원\'')
            rental_cost.append(84000 +(rental_time-48)*int(socar['rental_gap'][car]))

    else:
        coupon_var_socar.append('적용할 수 있는 쿠폰 없음')
        rental_cost.append(int(int(socar['rental_fee'][car] + (rental_time - 1)*int(socar['rental_gap'][car]))))

"""#### 쏘카 차종 별 주행료 계산 함수"""

def driving_cost_computer(driving_km,car) :
    
    driving_fee = 0

    if driving_km <= 30 :
        driving_fee = dr['30km'][car] * driving_km
    elif 30 < driving_km <= 100 :
        driving_fee = (dr['30km'][car] * 30) + (dr['100km'][car] * (driving_km-30))
    elif driving_km > 100 :
        driving_fee = (dr['30km'][car] * 30) + (dr['100km'][car] * 70) + (dr['up100km'][car] * (driving_km-100))

    return driving_fee

"""#### 쏘카 가격측정 함수"""

def socar_option():
    global socar_cost_small,socar_cost
    global ensure_1,ensure_1_cost,total_cost,total_cost_dic,semi_medium_car_driving_cost,semi_medium_car_rental_cost,d_cost,r_cost,small_car_list
    global suv_car_rental_cost,suv_car_driving_cost,small_car_driving_cost,small_car_rental_cost,minute,rental_day,car_type,rental_cost,rental_time
    global coupon_var_socar,rental_cost,coupon_socar,coupon_var
    coupon_socar=[]
    rental_cost=[]
    coupon_var_socar=[]
    socar_cost=0
    socar_cost_small=0
    ensure_1={}
    ensure_1_cost=[]
    total_cost=[]
    total_cost_dic={}  
    small_car_driving_cost={}
    small_car_rental_cost={}
    semi_medium_car_driving_cost={}
    semi_medium_car_rental_cost={}
    suv_car_driving_cost={}
    suv_car_rental_cost={}
    d_cost=[]
    r_cost=[]
    
    suv_car_list = ['Seltos', 'Sportage_thevold']
    semi_medium_car_list = ['The_new_avante', 'All_new_avante', 'The_new_K3']
    small_car_list = ['Morning_urban']

    if car_type[0:2]=='중형':
        socar_cost = '쏘카 중형 차량 없음'

    if car_type[0:2]=='경형':    

        for car in small_car_list:
            driving_cost = driving_cost_computer(driving_km,car)
            small_car_driving_cost[car]=driving_cost
            socar_coupon_computer(rental_time,start_time,car) 
            tmp = min(rental_cost)
            index = rental_cost.index(tmp)
            coupon_var=coupon_var_socar[index]
            small_car_rental_cost[car]=tmp
            coupon_socar.append(coupon_var)
            
      
            
        if ensure_type == 1: 
            for i in range(len(small_car_list)):
         
            
                ensure_charge = int(socar['ensure_70_basic'][small_car_list[i]])+(rental_time - 1)*(int(socar['ensure_70'][small_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[small_car_list[i]]=ensure_1_cost[i]
        
            
            
                socar_cost_small = small_car_rental_cost[small_car_list[i]] + ensure_1[small_car_list[i]] + small_car_driving_cost[small_car_list[i]]
                total_cost.append(socar_cost_small)
                total_cost_dic[small_car_list[i]]=total_cost[i]
            
            
            
    
        if ensure_type == 2: 
            for i in range(len(small_car_list)):
            
            
                ensure_charge = int(socar['ensure_30_basic'][small_car_list[i]])+(rental_time - 1)*(int(socar['ensure_30'][small_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[small_car_list[i]]=ensure_1_cost[i]
        
            
            
                socar_cost_small = small_car_rental_cost[small_car_list[i]] + ensure_1[small_car_list[i]] + small_car_driving_cost[small_car_list[i]]
                total_cost.append(socar_cost_small)
                total_cost_dic[small_car_list[i]]=total_cost[i]
    
        if ensure_type == 3: 
            for i in range(len(small_car_list)):
            
            
                ensure_charge = int(socar['ensure_5_basic'][small_car_list[i]])+(rental_time - 1)*(int(socar['ensure_5'][small_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[small_car_list[i]]=ensure_1_cost[i]
        
            
            
                socar_cost_small = small_car_rental_cost[small_car_list[i]] + ensure_1[small_car_list[i]] + small_car_driving_cost[small_car_list[i]]
                total_cost.append(socar_cost_small)
                total_cost_dic[small_car_list[i]]=total_cost[i]
            
           
            
        socar_cost= total_cost_dic
    
    
    if car_type[0:3]=='준중형':    
        
                
        for car in semi_medium_car_list:
            driving_cost = driving_cost_computer(driving_km,car)
            semi_medium_car_driving_cost[car]=driving_cost
            socar_coupon_computer(rental_time,start_time,car) 
            tmp = min(rental_cost)
            index = rental_cost.index(tmp)
            coupon_var=coupon_var_socar[index]
            semi_medium_car_rental_cost[car]=tmp
            coupon_socar.append(coupon_var)
            
        if ensure_type == 1: 
            for i in range(len(semi_medium_car_list)):
           
            
                ensure_charge = int(socar['ensure_70_basic'][semi_medium_car_list[i]])+(rental_time - 1)*(int(socar['ensure_70'][semi_medium_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[semi_medium_car_list[i]]=ensure_1_cost[i]
        
            
          
                socar_cost_semi = semi_medium_car_rental_cost[semi_medium_car_list[i]] + ensure_1[semi_medium_car_list[i]] + semi_medium_car_driving_cost[semi_medium_car_list[i]]
                total_cost.append(socar_cost_semi)
                total_cost_dic[semi_medium_car_list[i]]=total_cost[i]
            
            
            
            
        if ensure_type == 2: 
            for i in range(len(semi_medium_car_list)):
            
            
                ensure_charge = int(socar['ensure_30_basic'][semi_medium_car_list[i]])+(rental_time - 1)*(int(socar['ensure_30'][semi_medium_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[semi_medium_car_list[i]]=ensure_1_cost[i]
        
            
           
                socar_cost_semi = semi_medium_car_rental_cost[semi_medium_car_list[i]] + ensure_1[semi_medium_car_list[i]] + semi_medium_car_driving_cost[semi_medium_car_list[i]]
                total_cost.append(socar_cost_semi)
                total_cost_dic[semi_medium_car_list[i]]=total_cost[i]
            
            
            
            
            
        if ensure_type == 3: 
            for i in range(len(semi_medium_car_list)):
            
            
                ensure_charge = int(socar['ensure_5_basic'][semi_medium_car_list[i]])+(rental_time - 1)*(int(socar['ensure_5'][semi_medium_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[semi_medium_car_list[i]]=ensure_1_cost[i]
        
            
           
                socar_cost_semi = semi_medium_car_rental_cost[semi_medium_car_list[i]] + ensure_1[semi_medium_car_list[i]] + semi_medium_car_driving_cost[semi_medium_car_list[i]]
                total_cost.append(socar_cost_semi)
                total_cost_dic[semi_medium_car_list[i]]=total_cost[i]
            
            
            
        socar_cost= total_cost_dic

    if car_type[0:3]=='suv':    
        
               
        for car in suv_car_list:
            driving_cost = driving_cost_computer(driving_km,car)
            suv_car_driving_cost[car]=driving_cost
            socar_coupon_computer(rental_time,start_time,car) 
            tmp = min(rental_cost)
            index = rental_cost.index(tmp)
            coupon_var=coupon_var_socar[index]
            suv_car_rental_cost[car]=tmp
            coupon_socar.append(coupon_var)
            

        if ensure_type == 1: 
            for i in range(len(suv_car_list)):

                ensure_charge = int(socar['ensure_70_basic'][suv_car_list[i]])+(rental_time - 1)*(int(socar['ensure_70'][suv_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[suv_car_list[i]]=ensure_1_cost[i]

                socar_cost_suv = suv_car_rental_cost[suv_car_list[i]] + ensure_1[suv_car_list[i]] + suv_car_driving_cost[suv_car_list[i]]
                total_cost.append(socar_cost_suv)
                total_cost_dic[suv_car_list[i]]=total_cost[i]

        if ensure_type == 2: 
            for i in range(len(suv_car_list)):
            
            
                ensure_charge = int(socar['ensure_30_basic'][suv_car_list[i]])+(rental_time - 1)*(int(socar['ensure_30'][suv_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[suv_car_list[i]]=ensure_1_cost[i]
        
            
            
                socar_cost_suv = suv_car_rental_cost[suv_car_list[i]] + ensure_1[suv_car_list[i]] + suv_car_driving_cost[suv_car_list[i]]
                total_cost.append(socar_cost_suv)
                total_cost_dic[suv_car_list[i]]=total_cost[i]
            
             
           
            
            
        if ensure_type == 3: 
            for i in range(len(suv_car_list)):

                ensure_charge = int(socar['ensure_5_basic'][suv_car_list[i]])+(rental_time - 1)*(int(socar['ensure_5'][suv_car_list[i]]))
                ensure_1_cost.append(ensure_charge)
                ensure_1[suv_car_list[i]]=ensure_1_cost[i]

                socar_cost_suv = suv_car_rental_cost[suv_car_list[i]] + ensure_1[suv_car_list[i]] + suv_car_driving_cost[suv_car_list[i]]
                total_cost.append(socar_cost_suv)
                total_cost_dic[suv_car_list[i]]=total_cost[i]
            
            
           
        socar_cost= total_cost_dic

"""## 가격측정모델"""

def compare_model(a_1, b_1, car_type_1, ensure_type_1, driving_km_1, rental_1):
    global driving_km,rental_time,car_type,ensure_type,rental_day,socar_df,green_df
    global coupon_var_socar,coupon_var_green,socar_cost_list,green_cost_list,start_time,finish_time
    green_car_list=[]
    green_cost_list=[]
    socar_car_list=[]
    socar_cost_list=[]
    a = a_1
    b = b_1

    a = a.replace(':',".")
    b = b.replace(':',".")

    if int(a[3:])>=0:
        minute=int(a[3:])/60
        start_time = int(a[:2])+minute

    if int(b[3:])>=0:
        minute=int(b[3:])/60
        finish_time = int(b[:2])+minute


    rental_time = finish_time-start_time

    car_type = car_type_1
        #input('차 종(글자입력)\n1.경형\n2.준중형\n3.중형\n4.suv\n')
    ensure_type = ensure_type_1
    #nt(input('보험 단계[숫자만 기입]\n1단계 : 최대 70만원 부담\n2단계 : 최대 30만원 부담\n3단계 : 최대 5만원 부담\n'))
    driving_km = driving_km_1
        #int(input('예상 주행거리(km 제외):'))
    rental_day = rental_1
        #input('대여시작 요일\n(예: 월):')

    socar_option()
    green_option()
    
    if car_type=='경형':
        total_pay = [green_cost]
        green_dic = {'car':['morning'], 'totalpay':total_pay,'coupon': coupon_green }
        green_df = pd.DataFrame(green_dic)

        for cost in socar_cost.values():
            socar_cost_list.append(cost)
                
        for car in socar_cost.keys():
            socar_car_list.append(car)
            
        socar_df_dic = {'car':socar_car_list,'totalpay':socar_cost_list,'coupon': coupon_socar }
        #socar_df = pd.DataFrame(socar_df_dic)
        #green_df.index.names=['Green']
        #socar_df.index.names=['Socar']

        return [green_dic, socar_df_dic]
        #display(socar_df)
        #display(green_df)
        
    elif car_type == '중형':
        #print('\n!쏘카는 대여할 수 있는 중형 차량 없음!')
        for cost in green_cost.values():
            green_cost_list.append(cost)
        
        for car in green_cost.keys():
            green_car_list.append(car)
            
        green_df_dic = {'car': green_car_list,'totalpay': green_cost_list,'coupon': coupon_green}
        #green_df = pd.DataFrame(green_df_dic)
        #green_df.index.names=['Green']
        #green_df.index=green_df.index+1
        
        return [green_df_dic, {}]
        #display(green_df)
        
    else:
        for cost in green_cost.values():
            green_cost_list.append(cost)
        
        for car in green_cost.keys():
            green_car_list.append(car)
            
        green_df_dic = {'car': green_car_list, 'totalpay': green_cost_list, 'coupon': coupon_green}
        #green_df = pd.DataFrame(green_df_dic)
        
        for cost in socar_cost.values():
            socar_cost_list.append(cost)
        
        for car in socar_cost.keys():
            socar_car_list.append(car)
        socar_df_dic = {'car': socar_car_list, 'totalpay': socar_cost_list, 'coupon': coupon_socar }

        #socar_df = pd.DataFrame(socar_df_dic)
        #green_df.index.names = ['Green']
        #socar_df.index.names = ['Socar']
        #socar_df.index=socar_df.index+1
        #green_df.index=green_df.index+1

        #display(socar_df)
        #display(green_df)
        returnValue = [green_df_dic, socar_df_dic]

        return returnValue
