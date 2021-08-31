
words = ['Lorem', 'shit']  # these are predefined profanity words


def degree_of_profanity(file_path, word_list):
    overall = overall_line = 0
    results={}
    with open(file_path, 'r') as f:
        for num, line in enumerate(f, start=1):
            results[num] = 0
            for word in word_list:
                if word in line:
                    results[num] += line.strip().split().count(word)
        for item in results:
            overall += results[item]
            if results[item] > 0:
                overall_line += 1
            if 0 <= results[item] < 2:
                print("line no",item,"has LOW profanity words")
            elif 2 <= results[item] < 5:
                print("line no",item,"has MEDIUM profanity words")
            elif 5 <= results[item] < 7:
                print("line no",item,"has HIGH profanity words")
            elif results[item] >7 :
                print("line no",item,"has VERY HIGH profanity words")
    return [overall, overall_line]


# input document.txt
no_of_words, no_of_line = degree_of_profanity("document.txt", words)
print("Total no of profanity words in this file is", no_of_words, "and Totally", no_of_line, "no of line contains "
                                                                                             "profanity words")
