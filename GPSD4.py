import gps 


gps._\_init__()
gps.stream()
gps.data()
gps.waiting()
gps.unpack
gps.close()

session = gps(**opts)
    session.stream(WATCH_ENABLE|WATCH_NEWSTYLE)
    for report in session:
        print report