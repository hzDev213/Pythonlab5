try:  # испорльзуем try т.к нужно обработать исключение #* с помощью try Python проверяет код на наличие исключений.
    with open("Score.txt", "r") as file:  # * открываем файл с именем Score.txt в режиме чтения
        lines = file.readlines()  # * загружаем все строик в список

        scores = [
            int(line.strip()) for line in lines # * Метод strip()удаляет все начальные и конечные пробелы.
        ]  

        if scores:
            max_score = max(scores)
            print(f"Hieghest score: {max_score}")
        else:
            print("File is empty.")
except FileNotFoundError:
    print("File not found.")
