def fill_completions(c_dict, fobj):
    for line in fobj:
        line_str = line.strip()
        line_sep = line_str.split()
        for word in line_sep:
            count = 0
            for letter in word:
                if (count,letter) in c_dict:
                    c_dict[(count,letter)].add(word)
                else:
                    c_dict[(count,letter)] = {word}
                count += 1
def find_completions(prefix, c_dict):
    number_of_pts = len(prefix)
    set1 = dictionary[0,prefix[0]]
    if number_of_pts == 1:
        words = dictionary[x,prefix[x]]
    else:
        count = 0
        for x in prefix:
            set1 = set1 & dictionary[count,x]
            count += 1
    return set1
file = open("fullWordFile.txt", "r")
dictionary = {}
fill_completions(dictionary, file)
print(dictionary)
print(find_completions("smo",dictionary))
file.close()
