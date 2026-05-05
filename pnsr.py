import platform
import os
import time
from linecache import cache
from os import name
from zoneinfo import reset_tzpath

from colorama import init, Fore, Back, Style
import subprocess
import json
import shutil

#variables
exist = False
UserQuit = False
UserChoice= 7
Linuxpath = ""
LinuxName = ""
whilestop= False
LinuxPartitions = [["","",False]]
LinuxPartitions.clear()
folders = ["Files", "Files/Photos", "Files/Videos", "Files/Documents",
           "Files/Compressed", "Files/Audio","Files/Programming","Files/Others"]
audio_formats = ('.mp3','.wav','.flac','.aac','.ogg','.m4a','.wma','.opus','.ac3','.dts','.alac','.aiff','.au','.mid','.midi','.ra','.ram','.ape','.mka','.tta','.wv','.mpc','.ofr','.spx','.tak')

video_formats = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm','.m4v', '.mpg', '.mpeg','.mts', '.m2ts','.3gp', '.3g2', '.ogv', '.divx','.vob', '.ts',  '.rm',  '.rmvb','.asf', '.f4v', '.f4p', '.f4a', '.f4b')

compress_formats = ('.zip', '.exe'     '.rar',      '.7z',       '.tar',      '.gz',       '.tgz',      '.bz2',      '.tbz2',     '.xz',       '.txz',      '.zst',      '.tar.zst',  '.lz',       '.lzma',     '.lzo',      '.gz',       '.bz',       '.Z',        '.zst',      '.ar',       '.cpio',     '.shar',     '.iso',      '.img',      '.dmg',      '.cab',      '.msi',      '.deb',      '.rpm',      '.pkg',      '.apk',      '.jar',      '.war',      '.ear',      '.egg',      '.whl',      '.snap',     '.appimage', '.flatpak','.squashfs')

programming_formats = ('.py','.pyw','.pyx','.ipynb','.js','.ts','.jsx','.tsx','.vue','.svelte','.c','.cpp','.cc','.cxx','.h','.hpp','.hxx','.cs','.csx','.java','.class','.jar','.go','.rs','.rb','.erb','.php','.php3','.php4','.php5','.phtml','.swift','.kt','.kts','.dart','.lua','.pl','.pm','.sh','.bash','.zsh','.fish','.ps1','.sql','.r','.rmd','.m','.scala','.sc','.hs','.lhs','.asm','.s','.json','.yaml','.yml','.toml','.ini','.cfg','.conf','.xml','.cmake','.mk','.gradle','.groovy','Dockerfile','.vb','.vbs','.f95','.f90','.f','.scm','.clj','.elm','.ex','.exs','.erl','.cr','.nim','.zig')

document_formats = ('.txt','.url', '.rtf', '.log', '.md', '.tex', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pub', '.one', '.odt', '.ods', '.odp', '.odg', '.odb', '.pdf', '.epub', '.mobi', '.azw', '.azw3', '.fb2', '.djvu', '.pages', '.numbers', '.key', '.csv', '.tsv', '.xps', '.wpd', '.abw')

photo_formats = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.ico', '.heic', '.heif', '.raw', '.cr2', '.nef', '.arw', '.dng', '.orf', '.rw2', '.psd', '.xcf', '.ai', '.eps', '.indd', '.jfif', '.pjpeg', '.pjp', '.avif', '.jxl')



#json load
try:
    with open('data.json', 'r') as t:
        LinuxPartitions = json.load(t)
except (FileNotFoundError, json.JSONDecodeError):
    with open('data.json', 'w') as f:
        json.dump(LinuxPartitions, f)



LinuxPartout=""
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        # For Linux/Mac - check if TERM exists
        if os.environ.get('TERM'):
            os.system('clear')
        else:
            # Fallback: just print newlines
            print('\n' * 100)

def menu ():
    clear_screen()
    print(Fore.GREEN+"------------------PARTITION SORTER------------------"+Fore.WHITE)
    print(Fore.GREEN+f"1:{Fore.WHITE} Show partitions\n{Fore.GREEN}2:{Fore.WHITE} Detect partitions\n{Fore.GREEN}3:{Fore.WHITE} Manual Partitioning\n{Fore.GREEN}4:{Fore.WHITE} Sort Files\n{Fore.GREEN}5:{Fore.WHITE} Settings\n{Fore.GREEN}6:{Fore.WHITE} Quit")
    return int(input("Your Choice: "))

def partitionsDetector():
    clear_screen()
    global exist
    exist = False
    if platform.system() == "Windows":
        pass # partition detecting
    else:
        print(Fore.GREEN + "------------------PARTITION DETECTOR------------------" + Fore.WHITE)
        print("detecting your partitions...")
        result = subprocess.run(['lsblk', '-l', '-o', 'NAME,MOUNTPOINT'], capture_output=True, text=True)
        lines = result.stdout.splitlines()[1:]

        for line in lines:
            if line.strip():
                parts = line.split()
                if len(parts) >= 2 and parts[1]:
                    exists = False
                    for testexist in LinuxPartitions:
                        if testexist[1] == parts[1]:
                            exists = True
                            break

                    if not exists:
                        LinuxPartitions.append([parts[0], parts[1],False])
        with open('data.json','w') as f:
            json.dump(LinuxPartitions,f,indent=2)


        time.sleep(2)
        return 7

def showpartitions():
    clear_screen()
    global LinuxPartout
    if platform.system() == "Windows":
        pass  # partition detecting
    else:
        clear_screen()
        print(Fore.GREEN + "------------------LIST OF PARTITIONS------------------" + Fore.WHITE)
        for name in LinuxPartitions:
            LinuxPartout = ""
            LinuxPartout = Fore.RED+"["+ name[0].upper()  +"] : "+Fore.WHITE+name[1]
            print(LinuxPartout)
        if int(input("enter 0 for exit: "))==0:
            return 7

def SortFiles():
    videoCounter=0
    audioCounter=0
    photoCounter=0
    documentCounter=0
    programmingCounter=0
    compressCounter=0
    otherCounter=0

    global Linuxpath
    clear_screen()
    SelectPartition = int(input("which one do you want\n1: Automatic\n2: Manual\n"))
    if SelectPartition == 1:
        global Linuxpath
        clear_screen()
        for Data in LinuxPartitions:
            if Data[2]==True:
                Linuxpath = Data[1]
                for folder in folders:
                    os.makedirs(os.path.join(Linuxpath, folder), exist_ok=True)
                # Check each file once (very fast)
                for item in os.listdir(Linuxpath):
                    item_path = os.path.join(Linuxpath, item)

                    # Skip if it's a directory (folder)
                    if os.path.isdir(item_path):
                        continue

                    if item.lower().endswith(photo_formats):
                        destination = Linuxpath + "/Files/Photos"
                        shutil.move(item_path, destination)
                        photoCounter += 1

                    elif item.lower().endswith(audio_formats):
                        destination = Linuxpath + "/Files/Audio"
                        shutil.move(item_path, destination)
                        audioCounter += 1

                    elif item.lower().endswith(video_formats):
                        destination = Linuxpath + "/Files/Videos"
                        shutil.move(item_path, destination)
                        videoCounter += 1

                    elif item.lower().endswith(document_formats):
                        destination = Linuxpath + "/Files/Documents"
                        shutil.move(item_path, destination)
                        documentCounter += 1

                    elif item.lower().endswith(programming_formats):
                        destination = Linuxpath + "/Files/Programming"
                        shutil.move(item_path, destination)
                        programmingCounter += 1

                    elif item.lower().endswith(compress_formats):
                        destination = Linuxpath + "/Files/Compressed"
                        shutil.move(item_path, destination)
                        compressCounter += 1

                    else:
                        destination = Linuxpath + "/Files/Others"
                        shutil.move(item_path, destination)
                        otherCounter += 1
            else:
                continue
        print(Fore.GREEN + "------------------STATUS------------------" + Fore.WHITE)
        print(
            f"video transferred: {Fore.GREEN + str(videoCounter) + Fore.WHITE}\naudio transferred: {Fore.GREEN + str(audioCounter) + Fore.WHITE}\nphoto transferred: {Fore.GREEN + str(photoCounter) + Fore.WHITE}\ndocument transferred: {Fore.GREEN + str(documentCounter) + Fore.WHITE}\ncompress transferred: {Fore.GREEN + str(compressCounter) + Fore.WHITE}\nprogramming file transferred: {Fore.GREEN + str(programmingCounter) + Fore.WHITE}\nother transferred: {Fore.GREEN + str(otherCounter) + Fore.WHITE}\ntotal transferred: {Fore.GREEN}{videoCounter + audioCounter + programmingCounter + photoCounter + compressCounter + documentCounter}{Fore.WHITE}")
        time.sleep(10)
    elif SelectPartition==2:
        global LinuxPartout
        if platform.system() == "Windows":
            pass  # partition detecting
        else:
            clear_screen()
            i =1
            for name in LinuxPartitions:
                LinuxPartout = ""
                LinuxPartout =f"{i}"+ Fore.RED + " [" + name[0].upper() + "] : " + Fore.WHITE + name[1]
                i +=1
                print(LinuxPartout)
        SelectPartition = int(input("enter the number of the partition: "))
        if SelectPartition <= len(LinuxPartitions):
            Data = LinuxPartitions[(SelectPartition-1)]
            Linuxpath = Data[1]
            try:
                for folder in folders:
                    os.makedirs(os.path.join(Linuxpath,folder),exist_ok=True)
                # Check each file once (very fast)
                for item in os.listdir(Linuxpath):
                    item_path = os.path.join(Linuxpath, item)

                    # Skip if it's a directory (folder)
                    if os.path.isdir(item_path):
                        continue

                    if item.lower().endswith(photo_formats):
                        destination = Linuxpath + "/Files/Photos"
                        shutil.move(item_path, destination)
                        photoCounter += 1

                    elif item.lower().endswith(audio_formats):
                        destination = Linuxpath + "/Files/Audio"
                        shutil.move(item_path, destination)
                        audioCounter += 1

                    elif item.lower().endswith(video_formats):
                        destination = Linuxpath + "/Files/Videos"
                        shutil.move(item_path, destination)
                        videoCounter += 1

                    elif item.lower().endswith(document_formats):
                        destination = Linuxpath + "/Files/Documents"
                        shutil.move(item_path, destination)
                        documentCounter += 1

                    elif item.lower().endswith(programming_formats):
                        destination = Linuxpath + "/Files/Programming"
                        shutil.move(item_path, destination)
                        programmingCounter += 1

                    elif item.lower().endswith(compress_formats):
                        destination = Linuxpath + "/Files/Compressed"
                        shutil.move(item_path, destination)
                        compressCounter += 1

                    else:
                        destination = Linuxpath + "/Files/Others"
                        shutil.move(item_path, destination)
                        otherCounter += 1

                # Move to Others
                clear_screen()
                print(Fore.GREEN + "------------------STATUS------------------" + Fore.WHITE)
                print(f"video transferred: {Fore.GREEN+str(videoCounter)+Fore.WHITE}\naudio transferred: {Fore.GREEN+str(audioCounter)+Fore.WHITE}\nphoto transferred: {Fore.GREEN+str(photoCounter)+Fore.WHITE}\ndocument transferred: {Fore.GREEN+str(documentCounter)+Fore.WHITE}\ncompress transferred: {Fore.GREEN+str(compressCounter)+Fore.WHITE}\nprogramming file transferred: {Fore.GREEN+str(programmingCounter)+Fore.WHITE}\nother transferred: {Fore.GREEN+str(otherCounter)+Fore.WHITE}\ntotal transferred: {Fore.GREEN}{videoCounter+audioCounter+programmingCounter+photoCounter+compressCounter+documentCounter}{Fore.WHITE}")
                time.sleep(5)

            except():
                print("Error for no reason, don't feel stupid buddy i don't know it too")

            time.sleep(3)
        else:
            clear_screen()
            print("enter a valid number")
            time.sleep(3)
            return 4


def manualpartitioning():
    global LinuxName,Linuxpath,exist
    clear_screen()
    if platform.system() == "Windows":
        pass  # partition detecting
    else:
        print(Fore.GREEN + "------------------MANUAL PARTITIONING------------------" + Fore.WHITE)
        os.system("lsblk")
        LinuxName = input("enter the name of the partition (it's just a label): ")
        Linuxpath = input("enter the path of the partition: ")
        if os.path.ismount(os.path.abspath(Linuxpath)) == True:
            for line in LinuxPartitions:
                if Linuxpath.strip() == line[1].strip():
                    exist = True
            if exist==True:
                clear_screen()
                print("partition already exist!")
                time.sleep(5)
                return 3
            else:
                clear_screen()
                LinuxPartitions.append([LinuxName, Linuxpath,False])
                with open('data.json', 'w') as f:
                    json.dump(LinuxPartitions, f, indent=2)
                print("partition added successfully")
                wantAnother = input("want to add another one? [y,n] ")
                if wantAnother == "y" or wantAnother == "yes":
                    return 3
                else:
                    return 7



        else :
            clear_screen()
            print("please enter a mounted path")
            time.sleep(3)
            return 3


def settingpartition():
    i = 1
    global LinuxPartout
    for check in LinuxPartitions:
        if check[2] == False:
            LinuxPartout = str(i) + Fore.RED + " [" + check[0].upper() + "] : " + Fore.WHITE + check[
                1] + Fore.RED + "   [" + str(check[2]) + "]" + Fore.WHITE
            print(LinuxPartout)
            i += 1
        else:
            LinuxPartout = str(i) + Fore.RED + " [" + check[0].upper() + "] : " + Fore.WHITE + check[
                1] + Fore.GREEN + "   [" + str(check[2]) + "]" + Fore.WHITE
            print(LinuxPartout)
            i += 1

    user_input = input("enter the number of the partition (0 for exit): ")
    return int(user_input)


def settings():
    clear_screen()
    global LinuxPartout, whilestop
    print(Fore.GREEN + "------------------SETTINGS------------------" + Fore.WHITE)
    settingsInput = int(input(
        f"{Fore.GREEN}1:{Fore.WHITE} add or remove auto sort partitions\n{Fore.GREEN}2:{Fore.WHITE} add a folder as a partition\n{Fore.GREEN}3:{Fore.WHITE} delete one partition from the app\n{Fore.GREEN}4:{Fore.WHITE} delete all the partitions from the app\nenter 0 for exit: "))

    if settingsInput == 1:
        clear_screen()
        while whilestop != True:
            clear_screen()
            partition_num = settingpartition()

            if partition_num <= 0:
                return 7

            selected = LinuxPartitions[partition_num - 1]

            if selected[2] == False:
                selected[2] = True  # Toggle to True
                print(f"Enabled auto-sort for {selected[0]}")
                LinuxPartitions[partition_num-1][2]=True

            else:
                selected[2] = False
                print(f"Disabled auto-sort for {selected[0]}")
                LinuxPartitions[partition_num-1][2]=False
            with open('data.json', 'w') as f:
                json.dump(LinuxPartitions, f, indent=2)

            time.sleep(2)
    if settingsInput==2:
        clear_screen()
        LinuxName = input("enter the name of the partition (it's just a label): ")
        Linuxpath = input("enter the path of the Folder (pls don't put / at the end, example: /home/$USER/Downloads): ")

        LinuxPartitions.append([LinuxName, Linuxpath,False])
        with open('data.json', 'w') as f:
            json.dump(LinuxPartitions, f, indent=2)
        print("Folder successfully added as a partition")
        wantAnother = input("want to add another one? [y,n] ")
        if wantAnother == "y" or wantAnother == "yes":
            return 5
        else:
            return 7
    if settingsInput==3:

        while whilestop!=True:
            clear_screen()
            partition_num = settingpartition()
            if partition_num==0:
                return 7
            else:
                LinuxPartitions.pop(partition_num - 1)
                with open('data.json','w') as f:
                    json.dump(LinuxPartitions,f,indent=2)
    if settingsInput==4:
        clear_screen()
        userchoice= input(Fore.RED+"are you sure you want to delete all of your partitions? [y/n]\n"+Fore.WHITE)
        if userchoice == "y" or userchoice=="yes":
            LinuxPartitions.clear()
            with open('data.json','w') as f:
                json.dump(LinuxPartitions,f,indent=2)
        else:
            return 7
    if settingsInput==0:
        return 7




while UserQuit != True:
    match (UserChoice):
        case 1:
            UserChoice = showpartitions()
        case 2:
            UserChoice = partitionsDetector()
        case 3:
            UserChoice = manualpartitioning()
        case 4:
            UserChoice = SortFiles()
        case 5:
            UserChoice = settings()
        case 6:
            clear_screen()
            print(Fore.GREEN+"Goodbye!")
            UserQuit = True
        case 7:
            UserChoice = menu()
        case _:
            UserChoice = menu()
