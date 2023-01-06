#!python3

import os
import re

FOLDER_CONST = "emojisCut"

def tryint(s):
    """
    Return an int if possible, or `s` unchanged.
    """
    try:
        return int(s)
    except ValueError:
        return s

def alphanum_key(s):
    """
    Turn a string into a list of string and number chunks.

    >>> alphanum_key("z23a")
    ["z", 23, "a"]

    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def human_sort(l):
    """
    Sort a list in the way that humans expect.
    """
    l.sort(key=alphanum_key)
    return l

def getFilesFromDir():
    list_of_files = []
    path = f'C:\\Users\\ivanp\\IdeaProjects\\ENCOG-PrepoznavanjeSlika\\{FOLDER_CONST}\\.'
    # Get list of all files in a given directory sorted by name
    for (root, dir_name, file_name) in os.walk(path):
        list_of_files.append(file_name)

    # Iterate over sorted list of files and print the file paths 
    # one by one.
    return list_of_files[0] 

def walk_through_files(emoji_sorted_list, flag, f, file_extension='.png'):
    counter = 0
    emoji_counter = 0

    for emoji in emoji_sorted_list:
        if flag == 0 and not "merge" in emoji:
                if emoji_counter < 8:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:smiley_face\n")
                elif emoji_counter >= 8 and emoji_counter < 16:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:sad_face\n")
                elif emoji_counter >= 16 and emoji_counter < 24:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:neutral_face\n")
                elif emoji_counter >= 24 and emoji_counter < 32:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:heart_eyes_face\n")
                elif emoji_counter >= 32 and emoji_counter < 40:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:cool_face\n")
                elif emoji_counter >= 40 and emoji_counter < 48:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:wink_face\n")
                elif emoji_counter >= 48 and emoji_counter < 56:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:money_face\n")
                elif emoji_counter >= 56 and emoji_counter < 64:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:nerd_face\n")
                elif emoji_counter >= 64 and emoji_counter < 72:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:sleeping_face\n")
                elif emoji_counter >= 72 and emoji_counter < 80:
                    f.write(f"Input: image:./{FOLDER_CONST}/{emoji}, identity:clown_face\n")
                else:
                    break
                emoji_counter += 1

        elif flag == 1 and not "merge" in emoji:
                # counter += counter + 1
                f.write(f"Whatis: image:./{FOLDER_CONST}/{emoji}\n")

#                 f.write(f"Whatis: image:./{FOLDER_CONST}/emoji_99.jpg\n")
#                 f.write(f"Whatis: image:./{FOLDER_CONST}/emoji_98.jpg\n")
#                 f.write(f"Whatis: image:./{FOLDER_CONST}/emoji_97.jpg\n")
#                 f.write(f"Whatis: image:./{FOLDER_CONST}/emoji_96.jpg\n")
#                 f.write(f"Whatis: image:./{FOLDER_CONST}/emoji_95.jpg\n")
#                 f.write(f"Whatis: image:./{FOLDER_CONST}/emoji_94.jpg\n")
#                 break

width = 16
height = 16
img_type = "RGB"
hidden_1 = 100
hidden_2 = 0
mode = "gui"
minutes = 1

emoji_sorted_list = human_sort(getFilesFromDir())
# print(emoji_sorted_list)
f = open('command_emoji.txt', 'w')
f.write(f"CreateTraining: width:{width},height:{height},type:{img_type}\n")
walk_through_files(emoji_sorted_list, flag=0, f=f, file_extension=".jpg")
f.write(f"Network: hidden1:{hidden_1}, hidden2:{hidden_2}\nTrain: Mode:{mode}, Minutes:{minutes}, StrategyError:0.25,StrategyCycles:100\n")
walk_through_files(emoji_sorted_list, flag=1, f=f, file_extension=".jpg")
f.close()