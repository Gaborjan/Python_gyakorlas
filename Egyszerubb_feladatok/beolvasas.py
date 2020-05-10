import sys, time
import platform
if platform.system() == "Windows":
    import msvcrt
else:
    from select import select

def input_with_timeout_sane(prompt, timeout, default):
    """Read an input from the user or timeout"""
    print(prompt)
    sys.stdout.flush()
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        s = sys.stdin.readline().replace('\n','')
    else:
        s = default
        print(s)
    return s
   
def input_with_timeout_windows(prompt, timeout, default): 
    start_time = time.time()
    print(prompt)
    sys.stdout.flush()
    input = ''
    read_f=msvcrt.getche
    input_check=msvcrt.kbhit
    if not sys.stdin.isatty( ):
        read_f=lambda:sys.stdin.read(1)
        input_check=lambda:True
    while True:
        if input_check():
            chr_or_str = read_f()
        try:
            if ord(chr_or_str) == 13: # enter_key
                break
            elif ord(chr_or_str) >= 32: #space_char
                input += chr_or_str
        except:
            input=chr_or_str
            break #read line,not char...        
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break
        if len(input) > 0:
            return input
        else:
            return default

def input_with_timeout(prompt, timeout, default=''):
    if platform.system() == "Windows":
        return input_with_timeout_windows(prompt, timeout, default)
    else:
        return input_with_timeout_sane(prompt, timeout, default)

print("\nAnswer is:"+input_with_timeout("test?",2,"no input entered"))