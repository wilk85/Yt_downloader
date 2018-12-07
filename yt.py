from pytube import YouTube
import pytube
import os
import sys
import time

desktop = os.path.join(os.environ['HOMEPATH'], 'Desktop')

print()
print('Podaj link z wideo ktory chcesz pobrać : ', end=' ')
link = input()

def itag_check():
    ytobj = YouTube(link)
    ytstream = ytobj.streams.filter(file_extension='mp4').all() # wybieram tylko pliki .mp4
    lista1 = []
    print()
    print('Dostępne rozdzielczości dla wideo : ' +str(ytobj.title))

    for y in ytstream:
        if y.itag >= '18' and y.itag <= '22':
            lista1.append(y)
            print()
            print('     Numer : ' + str(ytstream.index(y)+1) + ', Tag filmu : ' + str(y.itag) + ', Rozdzielczość : ' + str(y.resolution) + '.')
            print() # tagi filmów o wartościach dwucyfrowych posiadają kodeki audio i wideo
               
    print('     Wybierz numer od 1 do ' + str(len(lista1)) + ' żeby pobrać odpowiednią rozdzielczość filmu : ', end='')
    num = int(input())
    print()
    
    def downl():
        if num-1 in range(0, len(lista1)): # zmieniam numer z 1 na 0, 2 na 1
            print('Pobieram film...')
            d_time = time.clock() 
            ytstream[num-1].download(desktop) # zmieniam numer z 1 na 0 , 2 na 1
            e_time = time.clock()
            print(' ::: Pobrano plik w : ' + '%.2f' % (e_time - d_time) + ' s')
        
    downl()
    
    print(' ::: Film pobrany został do lokalizacji : ' +str(desktop))
    sys.exit()
itag_check()    
