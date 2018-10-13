def wrap(string, max_width):
    result = ""
    if len(string) <= max_width:
        return string
    else:
        for x in range(len(string)//4+1):
            result += string[x*max_width:x*max_width+max_width] + '\n'
    return(result)