from playsound import playsound
import database as db
import os
import time
import socket

#os.system(./run.sh) #nanti di aktivin ketika di raspi
host = socket.gethostname()
ip_addr = socket.gethostbyname(host)
suara_masker = 'suara/masker.mp3'

while True:
    speaker = db.speaker()
    batas_orang = db.batas_orang()
    jumlah_orang = db.jumlah_orang()
    pelanggar_masker = db.pelanggar_masker()
    db.kirimIP(ip_addr)
    #status pada jumlah orang 
    if jumlah_orang >= int(batas_orang):
        print('melebihi batas')
    else:
        print('aman')

    print(pelanggar_masker)
    #peringatan pelanggar masker 
    if pelanggar_masker >= 1:
        print('terdapat pelanggar masker')
        if speaker == "true":
            playsound(suara_masker)
            time.sleep(2)
        else:
            pass
    else:
        print('tidak ada pelanggar masker')

    time.sleep(.7)
    
    #test
