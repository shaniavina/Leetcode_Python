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

####sol 2
"""
        This is a good question but __poorly__ described.
        buf in the signature of read() is the destination buffer
        and _not_ the source. The buf in the description is the f@#$%king file
        on the disk.
        """
        buf4 = [""] * 4
        copied = 0
        remaining = n
        while remaining:
            r = read4(buf4)
            to_copy = min(r,remaining)
            buf[copied:copied+to_copy] = buf4[:to_copy]
            copied += to_copy
            remaining -= to_copy
            if r < 4:
                break
        
        return copied
