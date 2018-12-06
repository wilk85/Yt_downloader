from pytube import YouTube
import pytube
import os
import sys

desktop = os.path.join(os.environ['HOMEPATH'], 'Desktop')

print()
print('Podaj link z wideo ktory chcesz pobrać : ', end=' ')
link = input()

def itag_check():
    ytobj = YouTube(link)
    ytstream = ytobj.streams.filter(file_extension='mp4').all() # wybieram tylko pliki .mp4
    lista1 = []
    
    print('Dostępne rozdzielczości dla wideo : ' +str(ytobj.title))

    for y in ytstream:
        if y.itag >= '18' and y.itag <= '22':
            lista1.append(y)
            print('     Numer : ' + str(ytstream.index(y)+1) + ', Tagi filmów : ' + str(y.itag) + ', Rozdzielczości : ' + str(y.resolution) + '.')
               
    print('   Wybierz numer od 1 do ' + str(len(lista1)) + ' żeby wybrać rozdzielczość filmu : ', end='')
    num = int(input())
    
    def downl():
        if num-1 in range(0, len(lista1)):
            print('Pobieram film...')
            ytstream[num-1].download(desktop)
        
    downl()

    print('Film pobrany został do lokalizacji : ' +str(desktop))
    sys.exit()
itag_check()    
