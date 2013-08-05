import os
from mpris import *

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help', '-?'):
        print usage
        raise SystemExit(0)

    player_name = os.environ.get('MPRIS_REMOTE_PLAYER', '*')
    remote = MPRISRemote()
    print remote
    try:
        remote.find_player(player_name)

    except RequestedPlayerNotRunning, e:
        print >>sys.stderr, 'Player "%s" is not running, but the following players were found:' % player_name
        for n in remote.players_running:
            print >>sys.stderr, "    %s" % n.replace("org.mpris.", "")
        print >>sys.stderr, 'If you meant to use one of those players, ' \
                            'set $MPRIS_REMOTE_PLAYER accordingly.'
        raise SystemExit(1)
    except NoPlayersRunning:
        print >>sys.stderr, "No MPRIS-compliant players found running."
        raise SystemExit(1)

    import locale
    encoding = sys.stdout.encoding or locale.getpreferredencoding() or 'ascii'

    if len(sys.argv) == 1:
        method_name = 'verbose_status'
        args = []
    else:
        method_name = sys.argv[1]
        args = sys.argv[2:]

    current_song_string = ""
    changed = False
    from pylcdsysinfo.pylcdsysinfo import BackgroundColours, TextColours, TextAlignment, TextLines, LCDSysInfo

    lcd = LCDSysInfo()
    lcd.set_brightness(255)
    lcd.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
    from time import sleep

    while(1):

        time.sleep(0.1)
        try:
            stat = remote.verbose_status()
            stat = stat.split('\n')

            artist = stat[1].split("artist:")[1][1:] 
            song = stat[2].split("title:")[1][1:]
            elap = stat[0].split(" ")[3]
            elap = "("+elap+")"
            
            song_string = artist + " - " + song
            if song_string != current_song_string:
                current_song_string = song_string
                print current_song_string
#            lcd.clear_lines(1, BackgroundColours.BLACK)
#            lcd.clear_lines(2, BackgroundColours.BLACK)
#            lcd.clear_lines(3, BackgroundColours.BLACK)
#            lcd.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
            lcd.display_text_on_line(1, artist, False, TextAlignment.LEFT, TextColours.WHITE)
            lcd.display_text_on_line(2, song, False, TextAlignment.LEFT, TextColours.WHITE)
            lcd.display_text_on_line(3, elap, False, TextAlignment.LEFT, TextColours.WHITE)
            
#            lcd.clear_lines(3, BackgroundColours.BLACK)
        except Exception as e:
            print e
            print "some kind of error"
            write(["nothing playing?","","",""])
    




