import os
from pytube import YouTube
from halo import Halo

def video():
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    spinner.succeed("İndirme Tamamlandı")
    pass

def music():
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    downloaded_file = video.download()
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
    spinner.succeed("İndirme Tamamlandı")
    pass

print("Bu program ile bir youtube içeriğini video veya mp3 formatında indirebilirsiniz. Lütfen Seçim yapın: \n 1. Video (mp4) \n 2. Müzik (mp3)")
type = int(input("Seçiminiz: "))

if type == 1:
    url = str(input("İndirmek İstediğiniz YouTube URL'ini Girin: "))
    spinner = Halo(text='Downloading', spinner='dots')
    spinner.start()
    video()
elif type == 2:
    url = str(input("İndirmek İstediğiniz YouTube URL'ini Girin: "))
    spinner = Halo(text='Downloading', spinner='dots')
    spinner.start()
    music()
else:
    spinner = Halo(text='Downloading', spinner='dots')
    spinner.start()
    spinner.fail("Hatalı giriş! Lütfen 1 veya 2'yi seçin...")
    pass

