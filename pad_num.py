"""This helper function used the 'zfill()' built-in to pad out number string"""

def pad_num(num, *, pad=2):
    """returns a numerical string padded with zeros if digits < pad"""
    s_num = str(num)
    if len(s_num) < pad:
        f_num = s_num.zfill(pad)
        return f_num
    else:
        return s_num
