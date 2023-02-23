from pytube import YouTube

contador=0

while contador==0:
    link = input("Enter the link: ")
    yt = YouTube(link)

    print("Titulo: ",yt.title)
    print("Numero de visitas: ",yt.views)
    print("Longitud del video: ",yt.length,"segundos")
    print("Descripción: ",yt.description)
    print("Valoraciones: ",yt.rating)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
