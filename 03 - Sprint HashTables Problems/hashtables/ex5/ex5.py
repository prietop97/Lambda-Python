def finder(files, queries):
    my_hash = {}
    result = []
    for query in queries:
        my_hash[query] = True
    
    for file_ in files:
        current = file_.replace('/', " ").split()
        if current[-1] in my_hash:
            result.append(file_)
        

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
