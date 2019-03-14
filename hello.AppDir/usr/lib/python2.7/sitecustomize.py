import sys,os
prefix = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(sys.path[0]))))
sys.path = [ prefix+s for s in sys.path if not s.startswith(prefix) ]
