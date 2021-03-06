# import stuff
from os import listdir, rename, remove

# get show name and season
show = input("Input name of the show\n")
sea = input("\nInput the season number in double digits (01, 02, etc)\n")
ext = input("\nWhat is the file extension? (mp4, mkv, etc)\n")
info = input("\nWant extra info? (Y/N): ")[0].lower()

# get extra info if necessary
if info == "y":
    info = input("What info would you like every episode to have displayed at the end?\n")
    ex = True
else:
    ex = False

#episode counter
ep = 1

# iterate through all files in the current directory
for x in listdir():

    # find the files that end with the desired extension
    if x.endswith(ext):

        # format episode number
        if ep < 10:
            eps = f"0{ep}"
        else:
            eps = f"{ep}"
        
        # rename based on extra info
        if ex:
            rename(x, f"{show} - s{sea}e{eps} - {info}.{ext}")
        else:
            rename(x, f"{show} - s{sea}e{eps}.{ext}")
        
        #increment episode number
        ep += 1