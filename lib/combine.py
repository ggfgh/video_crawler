import os
import sys
from output import output
from config import config

class Combine:
    def __init__(self,ts_count):
        self.ts_count = ts_count

    def write_bat(self):
        with open(config.bat_address,'r') as f:
            line_list = f.readlines()
            line_list[2] = "set end={}\n".format(self.ts_count)

        with open(config.bat_address,'w') as f:
            for line in line_list:
                f.writelines(line)
    
    def run(self):
        self.write_bat()
        # print("[+] Combine ts")
        print("\033[0;34m[%s INFO] Combine ts start \033[0m" %(output.nowtime()))
        os.system(config.bat_address)


if __name__ == '__main__':
    count = count.Count()
    combiner = Combine(103)
    combiner.run()
    


    