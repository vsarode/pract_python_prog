def get_version(line):
    # print line
    version = ''
    le = len(line)
    i = 0
    while i < le:
        if line[i] not in [' ', ',']:
            version += line[i]
        else:
            return version
        i += 1
    # for alpha in line:
    #     if alpha.isdigit():
    #         version += alpha
    #     else:
    #         return version
    return version


def find_tag(tag):
    lines = ['dsad dsadad dsadaa digvijay=123 dsad dsada',
             'dsad dsadad dsadaa vitthal=123 dsad dsada',
             'dsad dsadad dsadaa digvijay=345 dsad dsada']
    import re
    pattern = re.compile(tag)
    tags = []
    for line in lines:
        res = pattern.search(line)
        if res:
            start_index = line.find('=')
            version = get_version(line[start_index+1:])
            # print "ver->", version
            key_val = {}
            # tag, version = line.split('=')[0], line.split('=')[1]
            key_val[version] = tag
            tags.append(key_val)
    return tags


if __name__ == '__main__':
    tag = 'digvijay'
    print find_tag(tag)
    # print get_version('123 dsad dsada')
