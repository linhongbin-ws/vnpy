import sys

if (sys.version_info.major == 3 and sys.version_info.minor >=7):
    print("This script requires Python 3.6 or lower python 3 versions!")
    print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit('e')
sys.exit('p')