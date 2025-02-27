import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Время вышло! 🎉")

if __name__ == "__main__":
    try:
        duration = int(input("Введите время в секундах: "))
        countdown_timer(duration)
    except ValueError:
        print("Пожалуйста, введите число!")