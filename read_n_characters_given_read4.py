def read(self, buf, n):
    i = 0
    while i < n: 
        buf4 = ['','','','']
        count = read4(buf4) # Read file into buf4.
        if not count: break # EOF
        count = min(count, n - i)
        buf[i:] = buf4[:count] # Copy from buf4 to buf.
        i += count
    return i
