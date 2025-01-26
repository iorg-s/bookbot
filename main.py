def main():
    path_to_book = "books/frankenstein.txt"
    frankenstein = get_book_text(path_to_book)
    number_of_words = word_count(frankenstein)
    number_of_characters = character_count(frankenstein)
    book_report(path_to_book, number_of_words,number_of_characters)


# Returns string from provided path
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def word_count(string):
    list_of_words = string.split()
    return len(list_of_words)


def character_count(string):
    result = {}
    for character in string.lower():
        if character not in result.keys():
            result[character] = 1
        else :
            result[character] += 1
    return result


# Converts a dictionary in format of {KEY:VALUE} to a list of dictionaries if format of [{"character" : KEY}, {"num" : VALUE}]
def dict_to_list(dict):
    result = []
    for each in dict:
        res = {}
        res["character"] = each
        res["num"] = dict[each]
        result.append(res)
    return result


# Provides a key on which to sort a list of dictionaries on (the same KEY should exist in each dictionary, in this case it's "num")
def sort_on(dict):
    return dict["num"]


# Sorts a list of dictionaries on value of key in reversed order 
def sorted_dictionary(list):
    return sorted(list, reverse=True, key=sort_on)


def book_report(book, num_words, num_char):
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document \n\n")
    list_of_dictionaries = sorted_dictionary(dict_to_list(num_char))
    for dict in list_of_dictionaries:
        if dict["character"].isalpha():
            print(f"The '{dict["character"]}' character was found {dict["num"]} times")
    print("--- End of report ---")




main()