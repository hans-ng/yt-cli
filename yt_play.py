from audio_search import audio_search
import os
import pafy
import vlc

def print_result(audios, page):
    os.system('cls')
    print("=========================================")
    for index in range(len(audios.ids)):
        no = index+1 + (page-1)*20
        print(no, audios.titles[index])
    print("=========================================")

def play_song(title, link):
    print('Playing:', title)
    audio = pafy.new(link)
    best_audio = audio.getbestaudio()
    playurl = best_audio.url

    # Instance = vlc.Instance()
    # player = Instance.media_player_new()
    # Media = Instance.media_new(playurl)
    # Media.get_mrl()
    # player.set_media(Media)
    # player.play()

    media = vlc.MediaPlayer(playurl)
    media.play()

    while True:
        control = input("Press !p to pause|play, !s to stop: ")

        if control == "!s":
            media.stop()
            break
        elif  control == "!p":
            state = media.get_state()
            if state == vlc.State.Playing:
                media.pause()
            elif state == vlc.State.Paused:
                media.play()
        else:
            continue

def yt_cli(entry):
    page = 1
    
    audios = audio_search(entry, offset=page, mode="list")
    while True:
        print_result(audios, page)

        choice = input("Press a number to play, !q to quit, !n for next results, and another entry to search: ")
        
        if choice == "!q":
            os.system('cls')
            break
        elif choice == "!n":
            page += 1
            audios = audio_search(entry, offset=page, mode="list")
            continue
        elif choice.isdigit():
            if (page-1)*20 <= int(choice) <= page*20:
                index = int(choice) - (page-1)*20 - 1
                play_song(audios.titles[index], audios.links[index])
        else:
            entry = choice
            audios = audio_search(entry, offset=page, mode="list")

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} search_entry')

    yt_cli(args[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)