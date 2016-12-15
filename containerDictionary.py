books = {'DS': 'PseudoCode Approach' , 'CA': 'CLRS Book'};

if 'DS' in books:
    books['C++'] = 'E Balgurusawamy';
else:
    print('Fine');
print(books);
print(books.get('COA'));
print(books.get('COA' , 'N/A'));