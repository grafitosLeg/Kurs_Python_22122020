lap_times = (
  'Lewis Hamilton', 
  78.89, 
  79.89, 
  78.99, 
  80.89, 
  80.84  
)

print (lap_times[0])
################ 1 wersja
#print (lap_times[1: ]) SLICE od 1: do końca

#for x in lap_times[1: ]:
# print (x)

####### 2 wersja
#time_sum = 0
#for lap_time in lap_times [1: ]:
    #time_sum += lap_time
#print (time_sum/ (len(lap_times) -1))

time_sum = sum (lap_times [1: ])

print (time_sum/ (len(lap_times) -1))