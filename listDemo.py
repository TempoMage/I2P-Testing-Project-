import time
laps=[0,0,0,0]

def end():
        end = time.time()
        elapsed = end - start
        laps[0]+=1
        print "%s seconds" % (elapsed)
        print laps
        def lap():
            lapping = raw_input("lap? (l to lap)")
            if lapping == "l":
                end()
        starting = raw_input("start? (s to start)")
        if starting == "s":
            start = time.time()
            ending = raw_input("end? (e to end)")
            if ending == "e":
                end()
            lap()
end()