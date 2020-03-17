num_1=1
num_2=100
count=0
text_1='Загаданное число ='
text_2='Использованое число попыток ='

import random
predict=random.randint(num_1, num_2 + 1)
while number != predict and count != num_2: #Запускаем цикл для подсчета количества попыток
    count +=1
    for count in range(num_1, num_2 + 1): #Запускаем подцикл для проверки на больше/меньше среднего и изменения границ диапазона
     number = (num_1 + num_2)//2
     if predict > number:
      num_1=(num_1 + num_2)//2
      count+=1        
     elif predict < number:
      num_2=(num_1 + num_2)//2
      count+=1
     else: break
    print(text_2, count)
else:
 print(text_1, predict)