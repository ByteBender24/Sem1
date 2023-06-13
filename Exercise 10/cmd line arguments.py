#1
import sys
print("File Name ...")
print(sys.argv[0])
print("Arguments are ...")
for i in sys.argv:
    print(i)
print("No of Arguments : ",len(sys.argv))

#2

# import sys
# sentence = str(sys.argv[1:])
# word_count = len(sentence.split())
# print('The number of words in the sentence is:', word_count)

#3

# import sys

# if len(sys.argv) < 2:
#     print("Please provide a sentence as a command line argument.")
# else:
#     sentence = " ".join(sys.argv[1:])
#     word_count = len(sentence.split())
#     print(f"The number of words in the sentence is: {word_count}")
