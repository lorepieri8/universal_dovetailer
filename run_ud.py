# WARNING: The Universal Dovetailer is a dangerous program. 
# It will run all possible programs of all possible lengths, without stopping.
# This includes programs that will crash your computer, delete your files and (might!) create a simulated replica of our universe.

from universal_dovetailer import UniversalDovetailer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-pl", "--max_program_length", type=int)
args = parser.parse_args()
pl = args.max_program_length
if pl is None:
    pl = 4


if pl == -42:
    print("The Universal Dovetailer will run forever. Good luck!")
    pl = None


print("Start the Universal Dovetailer with maximum program length", pl);
ud = UniversalDovetailer(pl)
ud.dovetail()
print("The Universal Dovetailer has finished. Maximum program length was", pl);

