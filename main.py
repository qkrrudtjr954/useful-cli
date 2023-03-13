import datetime

import click
import pyautogui


@click.group("main")
def main():
    pass


@main.command("display-point")
def display_point():
    pyautogui.displayMousePosition()


@main.command("auto-click")
@click.argument("x")
@click.argument("y")
@click.option("--sleep", "-s")
@click.option("--times", "-c")
def auth_click(x, y, sleep=60, times=None):
    if int(sleep) < 5:
        print("sleep parameter must bigger than 5 seconds.")

    time_checking = times is not None

    if time_checking and int(times) <= 0:
        print("times parameter must bigger than 0.")

    print("Press Ctrl-c to quit.")

    count = 0

    try:
        while True:
            pyautogui.sleep(int(sleep))
            pyautogui.click(int(x), int(y))
            count += 1
            now = datetime.datetime.now().strftime("%Y년 %m월 %d일, %H시 %M분 %S초")
            print(f"[{now}] {count} clicked", end="\r")

            if time_checking and count >= int(times):
                raise KeyboardInterrupt

    except KeyboardInterrupt:
        print("\nbye bye ~")


if __name__ == '__main__':
    main()
