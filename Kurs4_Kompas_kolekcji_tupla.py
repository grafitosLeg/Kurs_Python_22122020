lap_times = (
  'Lewis Hamilton', 
  78.89, 
  79.89, 
  78.99, 
  80.89, 
  80.84  
)

print (lap_times [0])
#1st wersja SLICE + pętla
#print (lap_times [1:])

#for x in lap_times:
 #   print (x)


#2nd wersja z pętlą i licznikiem
#time_sum = 0

#for lap_time in lap_times [1: ]:
#   print (lap_time)
#   time_sum += lap_time
#print (time_sum / (len (lap_times) -1))

#3rd wersja 

time_sum = sum (lap_times [1:])
print (time_sum / (len(lap_times) -1))