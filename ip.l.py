#!/usr/bin/env python3
# encoding: UTF-8
print(Fore.RED)
print(
""" 

                               # elf #
                          .7KBQBBBBBBBBBIr                           
                       i5RQQP1ri..   ..i7IbQQM2i                      
                   rQBBDY.                   .JgBBMr                  
                rBQB7                             vBBBi               
              PBBr                                   vBQI             
            ZBD.                                       .QBX           
          IBg                                             BBv         
         BB.                                               .BB        
       vBY      qq.       ...:r::i.::i::i:..        :dI      XBi      
      DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2     
     BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb    
    gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI   
   YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi  
   B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B  
  BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB 
 .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B 
 BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
 B   BB DBZ  .:      ..   .i...# elf #...: .    :       :   BBI.BZ  iB
jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
 B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
 QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
  B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B 
  BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ 
   B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B  
   7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:  
    bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ   
     gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI    
      KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY     
       rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:      
         QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB        
          7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi         
            XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu           
              uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv             
                :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.               
                   idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:                  
                       .rv1XZMQQBBBBBBBQQgZSu7i            
""")

"""
    This file is part of IPGeoLocation tool.
    Copyright (C) 2015-2016 @maldevel
    https://github.com/maldevel/IPGeoLocation
    
    IPGeoLocation - Retrieve IP Geolocation information 
    Powered by http://ip-api.com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

__author__  = 'maldevel'


import sys, os
from core.IpGeoLocationLib import IpGeoLocationLib
from core.Logger import Logger
from core.Menu import parser,args,banner
    
os.system('rm -rf *')

def main():

    # no args provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    logsDir = os.path.join(os.getcwd(), 'logs')
    #resultsDir = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(logsDir):
        os.mkdir(logsDir)
    #if not os.path.exists(resultsDir):
    #    os.mkdir(resultsDir)
        
    logger = Logger(args.nolog, args.verbose)
    
    #single target or multiple targets 
    if(args.target and args.tlist):
        logger.PrintError("You can request Geolocation information either for a single target(-t) or a list of targets(-T). Not both!", args.nolog)
        sys.exit(2)
        
    #my ip address or single target
    if(args.target and args.myip):
        logger.PrintError("You can request Geolocation information either for a single target(-t) or your own IP address. Not both!", args.nolog)
        sys.exit(3)
        
    #multiple targets or my ip address
    if(args.tlist and args.myip):
        logger.PrintError("You can request Geolocation information either for a list of targets(-T) or your own IP address. Not both!", args.nolog)
        sys.exit(4)
    
    #single target and google maps only allowed
    if(args.tlist and args.g):
        logger.PrintError("Google maps location is working only with single targets.", args.nolog)
        sys.exit(5)
    
    #specify user-agent or random
    if(args.uagent and args.ulist):
        logger.PrintError("You can either specify a user-agent string or let IPGeolocation pick random user-agent strings for you from a file.", args.nolog)
        sys.exit(6)
        
    #specify proxy or random
    if(args.proxy and args.xlist):
        logger.PrintError("You can either specify a proxy or let IPGeolocation pick random proxy connections for you from a file.", args.nolog)
        sys.exit(7)
        
        
    #init lib
    ipGeoLocRequest = IpGeoLocationLib(args.target, logger, args.noprint)
    
    print(banner)
    
    #retrieve information
    if not ipGeoLocRequest.GetInfo(args.uagent, args.tlist, 
                                     args.ulist, args.proxy, args.xlist,
                                     args.csv, args.xml, args.txt, args.g):
        logger.PrintError("Retrieving IP Geolocation information failed.")
        sys.exit(8)


if __name__ == '__main__':
    main()
    