if __name__ == '__main__':
    d = {'a': 1, 'b': 2}
    print(d.get('b', 'missing'))
    d['b'] = None
    print(d.get('b', 'missing'))
    del(d['b'])
    print(d.get('b', 'missing'))
