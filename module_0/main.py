def game_core(predict):
    num_1 = 1
    num_2 = 100
    count = 1
    text_1 = 'Загаданное число ='
    text_2 = 'Использованое число попыток ='
    import random
    import numpy as np
    number=np.random.randint(num_1, num_2)
    while number != predict and count < num_2:
        predict = (num_1 + num_2)//2
        count +=1
        if predict < number:
            num_1 = (num_1 + num_2)//2
        elif predict > number:
            num_2 = (num_1 + num_2)//2
        else: 
            break
    print(text_1, predict)
    print(text_2, count)
    return(count)

def score_game(game_core):
    num_1 = 1
    num_2 = 100
    import numpy as np
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(num_1, num_2 + 1, size=(1000))
    for predict in random_array:
        count_ls.append(game_core(predict))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core)