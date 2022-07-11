class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.HEADER + "text" + bcolors.ENDC)
print(bcolors.OKBLUE + "text" + bcolors.ENDC)
print(bcolors.OKCYAN + "text" + bcolors.ENDC)
print(bcolors.OKBLUE + "text" + bcolors.ENDC)
print(bcolors.OKGREEN + "text" + bcolors.ENDC)
print(bcolors.WARNING + "text" + bcolors.ENDC)
print(bcolors.FAIL + "text" + bcolors.ENDC)
print(bcolors.ENDC + "text" + bcolors.ENDC)
print(bcolors.BOLD + "text" + bcolors.ENDC)
print(bcolors.UNDERLINE + "text" + bcolors.ENDC)
