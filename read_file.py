if __name__ == '__main__':
    f = open('add.py')
    is_doc_str = False
    for i, j in enumerate(f.readlines()):
        # print is_doc_str
        if is_doc_str:
            if "'''" not in j and '"""' not in j:
                continue
            else:
                is_doc_str = False
                continue

        if '"""' in j or "'''" in j:
            is_doc_str = True
            continue
        print  j