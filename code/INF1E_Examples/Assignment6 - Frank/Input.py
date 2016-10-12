from sys import platform
# Source: http://code.activestate.com/recipes/134892/

def GetCh():
	try:
		return GetChWindows() if platform == "win32" else GetChUnix()
	except:
		return '\0'
		
def GetChWindows():
	import msvcrt
	return msvcrt.getch()
	
def GetChUnix():
	import sys, tty, termios
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	
	try:
		tt.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcgetattr(fd, termios.TCSADRAIN, old_settings)
	return ch