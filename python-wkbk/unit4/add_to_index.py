def add_to_index(index, keyword, url):
    if (len(index == 0)):
        entry = index[0]
        entry[0] = keyword
        entry[1] = entry1.append[url]
    else:
        for entry in index:
            if (entry[0] == keyword):
                entry[1].append(url)
                return index

    t_index = []   
    add_to_index(t_index, 'udacity', 'udacity.com')
    print t_index
