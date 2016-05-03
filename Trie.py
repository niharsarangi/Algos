_end="_end_"
def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end
    return root
def inTrie(trie,word):
    current_dict=trie
    for letter in word:
        if letter in current_dict:
            current_dict=current_dict[letter]
        else:
            return False
    return _end in current_dict
    
def insert(trie,word):
    current_dict=trie
    for letter in word:
        current_dict=current_dict.setdefault(letter,{})
        current_dict[_end]=_end

def remove(trie,word):
    if not inTrie(trie,word):
        return
    current_dict=trie
    for letter in word:
        current_dict=current_dict[letter]
        if current_dict is None:
            break
    else:
        del current_dict[_end]
        
    
trie=make_trie(['foo', 'bar', 'baz', 'barz'])
insert(trie,'bart')
ch=inTrie(trie,'bart')
remove(trie,'bart')
ch=inTrie(trie,'bart')
