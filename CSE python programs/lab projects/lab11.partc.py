
import string

def build_word_set( input_file ):
    """just adds all the words in the file into a set
input: the file name
output: the set of words in the file"""
    word_set = set()
    
    for line in input_file:

        # removes all formatting from the file
        word_lst = line.strip().split()

        # lowercases all the words and removes punctuation
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        
        for word in word_lst:
            
            if word != "":

                # as long as it not a space, addes the word into the set
                word_set.add( word )
                
    return word_set


def compare_files( file1, file2 ):
    """displays the intersection and the union of the two files
inputs: file1 and file2
outputs: None (executed for side effect)"""
    # Build two sets:
    #   all of the unique words in file1
    #   all of the unique words in file2
    set1 = build_word_set(file1)
    set2 = build_word_set(file2)

    # Display the total number of unique words between the
    # two files.  If a word appears in both files, it should
    # only be counted once.
    union = set1 | set2
    print(len(union))

    # Display the number of unique words which appear in both
    # files.  A word should only be counted if it is present in
    # both files.
    intersection = set1 & set2
    print(len(intersection))
  
     
######################################################################

f1 = open( "lab11.document1.txt" )
f2 = open( "lab11.document2.txt" )

compare_files( f1, f2 )

f1.close()
f2.close()

