def game_core(number):
    num_1 = 1
    num_2 = 100
    count = 0
    text_1 = 'Загаданное число ='
    text_2 = 'Использованое число попыток ='
    import random
    import numpy as np
    predict=np.random.randint(num_1, num_2)
    while number != predict and count != num_2: #Запускаем цикл для подсчета количества попыток.
        count += 1
        for count in range(num_1, num_2): #Запускаем подцикл для проверки на больше/меньше среднего и изменения границ диапазона.
            number = (num_1 + num_2)//2
            if predict > number:
                num_1 = (num_1 + num_2)//2
                count += 1        
            elif predict < number:
                num_2 = (num_1 + num_2)//2
                count += 1
            else: 
             break
        print(text_2, count)
    else: 
        print(text_1, predict)
    return(count)

def score_game(game_core):
    num_1 = 1
    num_2 = 100
    import numpy as np
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(num_1, num_2 + 1, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core)