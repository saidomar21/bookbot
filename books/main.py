import string
def main():
    print("hello world")
    with open("/home/dsafg20/workspace/github.com/saidomar21/bookbot/frankenstein.txt") as f:
    # ...
        file_contents = f.read()
        word_with_punct = remove_punctuation(file_contents)
        word_count  =  count_letters(word_with_punct)
        report = report_values(word_count)
        num_count = get_word_count(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")

        print(f"{num_count} words found in the document")
        list_of_values =  [*word_count.items()]

        for item in report:
            print(f"The {item['char']} character was found {item["num"]} times ")



def sort_on(d):
    return d["num"]

def report_values(letters):

   sorted_list = []
   for val in letters:
       sorted_list.append({"char": val, "num" : letters[val]})
       sorted_list.sort(reverse=True, key=sort_on)
   return sorted_list

def get_word_count(words):
    count = words.split()

    return len(count)

def count_letters(words):
    final_count = {}
    for letter in words:
        lowered = letter.lower()
        if lowered in final_count:
            final_count[lowered] += 1
        else:
            final_count[lowered] = 1

    return final_count


def remove_punctuation(s):
    new_s = [i for i in s if i.isalnum() or i.isalpha() or i.isspace()]
    return ''.join(new_s)
main()