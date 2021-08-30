# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from alt_profanity_check import predict, predict_prob

def run_main():
    with open("document.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            if 0 < predict_prob([stripped_line])[0] < 0.25:
                print('Low')
            elif 0.25 < predict_prob([stripped_line])[0] < 0.5:
                print('medium')
            elif 0.5 < predict_prob([stripped_line])[0] < 0.75:
                print('high')
            else:
                print('very high')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
