import sys, getopt
import platform
import subprocess

from Volume import *


def get_windows_volumes():

    volumes = []
    directory = []
    # print "You're using Windows.\n"
    # print "Your available drives are: "
    # pipe = subprocess.Popen("C:\\windows\\system32\\cmd.exe /c \"wmic logicaldisk get caption, volumename\"",
    #                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #
    # while True:
    #     line = pipe.stdout.readline()
    #     if line:
    #          line = line.replace('\n', "")
    #          line = line.replace('\r', "")
    #          if line.strip(''):
    #             directory.append(line.split(" "))
    #     if not line:
    #         break
    directory = [['Caption', '', 'VolumeName', '', ''], ['C:', '', '', '', '', '', '', 'OS', '', '', '', '', '', '', '', '', '', ''], ['D:', '', '', '', '', '', '', 'Apps', '', '', '', '', '', '', '', ''], ['E:', '', '', '', '', '', '', 'Games', '', '', '', '', '', '', ''], ['F:', '', '', '', '', '', '', 'Data', '', '', '', '', '', '', '', ''], ['G:', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]
    for i in range(0,len(directory)):
        directory[i] = filter(bool,directory[i])
    directory = directory[1:]

    for row in directory:
        if len(row) == 1:
            volumes.append(Volume(row[0], ""))
        else:
            volumes.append(Volume(row[0], row[1]))

    return volumes
# TO DO


def get_linux_volumes():
    print "You're using Linux"
    directory = subprocess.check_output(["df"])
    for item in directory:
        print "TO DO"
        return directory


def get_volumes():
    file_system = platform.system().lower()
    Volume.set_file_system(file_system)
    volumes = []

    if file_system == "windows":
        volumes = get_windows_volumes()
    elif file_system == "linux":
        volumes = get_linux_volumes()

    print "Total Volumes: " + str(Volume.get_total_volume())

print "Name" + "{0:>15}".format("Volume Name")
print "____" + "{0:>12}".format("______ \n")
get_windows_volumes()



# def main(argv):
#     search_name = ''
#     volumes = get_volumes()
#
#     try:
#         opts, args = getopt.getopt(argv, "hd:", ["search_name"])
#     except getopt.GetoptError:
#         print 'driverscanner.py -d <drive name> \n driverscanner.py --drive <drive name>'
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt in ("-h", "--help"):
#             print 'driverscanner.py -d <drive name> \n driverscanner.py --drive <drive name>'
#             sys.exit()
#         elif opt in ("-d", "--drive"):
#             search_name = arg
#
#     print search_name
#
#
# if __name__ == "__main__":
#     main(sys.argv[1:])