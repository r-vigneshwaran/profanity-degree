
words = ['Lorem', 'shit']  # these are predefined profanity words


def degree_of_profanity(file_path, word_list):
    overall = overall_line = 0
    with open(file_path, 'r') as f:
        for num, line in enumerate(f, start=1):
            for word in word_list:
                if word in line:
                    overall += line.strip().split().count(word)
                    overall_line += 1
                    if 0 <= line.strip().split().count(word) < 2:
                        print("line no", num, "low")
                    elif 2 <= line.strip().split().count(word) < 5:
                        print("line no", num, "medium")
                    elif 5 <= line.strip().split().count(word) < 7:
                        print("line no", num, "high")
                    elif line.strip().split().count(word) > 7:
                        print("line no", num, "very high")
    return [overall, overall_line]


# input document.txt
no_of_words, no_of_line = degree_of_profanity(input(), words)
print("Total no of profanity words in this file is", no_of_words, "and Totally", no_of_line, "no of line contains "
                                                                                             "profanity words")
