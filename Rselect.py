
a = [12, 12, 88, 12, 43, 111, 90, 98, 1111, 111, 99, 1111]

i = 0          # индекс
first_min = 0  # номер первого минимального элемента
last_min  = 0  # номер последнего минимального элемента
min = a[0]     # собственно минимальный элемент
first_max = 0  # номер первого максимального элемента
last_max  = 0  # номер последнего максимального элемента
max = a[0]     # собственно максимальный элемент

while (i < len(a)): 
    if (a[i] <= min): 
        if (a[i] < min): 
            first_min = i
        last_min = i
        min = a[i]
        
    if (a[i] >= max): 
        if (a[i] > max): 
            first_max = i
        last_max = i
        max = a[i]
        
    i += 1
    
print ("first_min = ", first_min)  
print ("last_min  = ", last_min)   
print ("min = ", min)              
print ("first_max = ", first_max)
print ("last_max  = ", last_max)
print ("max = ", max)           
