import os
from mpris import *

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help', '-?'):
        print usage
        raise SystemExit(0)

    player_name = os.environ.get('MPRIS_REMOTE_PLAYER', '*')
    remote = MPRISRemote()

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

    
  #  print type(remote.verbose_status())
    s.write('\0')
    write(["","","",""])
    time.sleep(1)
    funny = []
#    funny.append('|')
#    funny.append('/')
#    funny.append('_')
#    funny.append('\\')

#    funny.append('*')
#    funny.append('**')
    ff =""
    for i in range(20):
        ff = ff+"*"
        funny.append(ff)
#    for i in range(20):
#        ff = ff[:i]
#        funny.append(ff)
    funny1 = funny
    funny2 = []
    for f in funny:
        funny2.append(f)

    funny2.reverse()
    funny = funny1 + funny2
    
    for i in funny:
        print i
    
    count = 0
    print funny
    s.timeout = 1
    s.flushInput()
    while(1):

        time.sleep(0.1)
        try:
            s.flushInput()
            encode = s.read()
            if(encode == '>'):
                remote.next()
            elif(encode == '<'):
                remote.prev()
                

            #s.readline()
            stat = remote.verbose_status()
            stat = stat.split('\n')

    #    l = remote.simple_status()
    #    write(l)
            artist = stat[1].split("artist:")[1][1:] 
            song = stat[2].split("title:")[1][1:]
            elap = stat[0].split(" ")[3]
            elap = "("+elap+")"
            #print song, len(song)
          #  print artist, len(artist)
          #  print elap, len(elap)
            if(count == len(funny)-1):
                count = 0
            else:
                count+=1
            other = funny[count]
          #  print other, count
            dump_list = [song,elap,artist,other]
            write(dump_list)

    #    print stat[0], '|   ', len(stat[0])
        #print stat[1], '|   ', len(stat[1])
        #print stat[2], '|   ', len(stat[2])
        #print stat[3], '|   ', len(stat[3])
        except:
            print "some kind of error"
            write(["nothing playing?","","",""])
    

    # try:
        
    #     output_generator = getattr(remote, method_name)(*args) or []
    #     for chunk in output_generator:
    #         sys.stdout.write(chunk.encode(encoding, 'replace'))

    # except BadUserInput, e:
    #     print >>sys.stderr, e
    #     raise SystemExit(1)
    # except NoTrackCurrentlySelected:
    #     print >>sys.stderr, "No track is currently selected."
    # except KeyboardInterrupt:
    #     raise SystemExit(2)



