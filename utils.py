import sys
import threading
try:
    import thread
except ImportError:
    import _thread as thread


# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    # https://stackoverflow.com/questions/64502127/int-to-bytes-length-calculation
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def quit_function(fn_name):
    print('{0} took too long'.format(fn_name), file=sys.stderr)
    sys.stderr.flush() 
    thread.interrupt_main() # raises KeyboardInterrupt

# https://stackoverflow.com/a/31667005/7106915
def exit_after(s):
    '''
    exit process if function takes longer than s seconds
    '''
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer
