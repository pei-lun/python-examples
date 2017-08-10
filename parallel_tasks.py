from concurrent.futures import ProcessPoolExecutor
from random import choices
from time import sleep


def bot_sleeps(no: int, seconds):
    number = str(no).zfill(2)
    print(f'Bot No.{number}:', f'I\'m going to sleep for {seconds} seconds.')
    sleep(seconds)
    print(f'Bot No.{number}:', f'I wake up.')


def main():
    with ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(
            bot_sleeps,
            range(1, 16),
            choices(range(5, 11), k=15)
        )


if __name__ == '__main__':
    main()
