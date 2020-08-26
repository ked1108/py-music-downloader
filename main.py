import PySimpleGUI as sg
import download as d

sg.theme('DarkTeal')

layout =  [
    [sg.Text('Enter The Song Name:\t'), sg.InputText()],
    [sg.Text('Enter The Artist Name:\t'), sg.InputText()],
    [sg.Button('Download')]
]

window = sg.Window('Download', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Download':
        song = str(values[0])
        artist = str(values[1])

        d.getResults(song, artist)
        videoID = d.parseResults()
        d.download(videoID, song, artist)

window.close()
