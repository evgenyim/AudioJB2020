from os import listdir

from pydub import AudioSegment


def show_help():
    print('Commands:\n'
          'help\n'
          '     show help\n'
          'show\n'
          '     shows resources\n'
          'merge <output file> <file1> <file2> ...\n'
          '     merge files and place result to <output file>\n'
          'cut <file> [<start>;<finish>] [<start>;<finish>] ...\n'
          '     split file to intervals, which would be saved automatically\n'
          'reverse <file> <output file>\n'
          '     reverse <file>\n')


def merge_audio(files):
    sound = AudioSegment.from_file(files[0])
    for i in range(1, len(files)):
        sound = sound + AudioSegment.from_file(files[i])
    return sound


def reverse_audio(filepath):
    sound = AudioSegment.from_file(filepath)
    return sound.reverse()


def cut_audio(filepath, intervals):
    sound = AudioSegment.from_file(filepath)
    ret = []
    for i in intervals:
        a = i[1:-1].split(';')
        start = float(a[0]) * 1000
        finish = float(a[1]) * 1000
        ret.append(sound[start:finish])
    return ret


def save_audio(audio, filename):
    audio.export(filename, format='mp3')


def main():
    res = 'resources/'
    while True:
        cmd = input().split()
        if len(cmd) < 1:
            print('Use help option')
        if cmd[0] == 'help':
            show_help()
        elif cmd[0] == 'merge':
            if len(cmd) < 4:
                print('Wrong arguments, use help option')
            sound = merge_audio(list(map(lambda x: res + x, cmd[2:])))
            save_audio(sound, res + cmd[1])
        elif cmd[0] == 'reverse':
            if len(cmd) < 3:
                print('Wrong arguments, use help option')
            sound = reverse_audio(res + cmd[1])
            save_audio(sound, res + cmd[2])
        elif cmd[0] == 'cut':
            if len(cmd) < 3:
                print('Wrong arguments, use help option')
            intervals = cmd[2:]
            sounds = cut_audio(res + cmd[1], intervals)
            filename = cmd[1].split('.')[0]
            for i in range(len(intervals)):
                save_audio(sounds[i], res + filename + 'interval_{}.mp3'.format(i))
        elif cmd[0] == 'exit':
            return
        elif cmd[0] == 'show':
            onlyfiles = [f for f in listdir(res)]
            print(onlyfiles)
        else:
            print('Use help option')


if __name__ == '__main__':
    main()

