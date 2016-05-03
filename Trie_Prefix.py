_end="_end_"
def insert(trie,word):
    current_dict=trie
    for letter in word:
        if letter in current_dict[0]:
            current_dict[0][letter][1]+=1
        current_dict=current_dict[0].setdefault(letter,[{},1])
        current_dict[0][_end]=_end

def prefix(A):
    trie=[dict(),1]
    for word in A:
        insert(trie,word)
    sol=[]
    for word in A:
        current_dict=trie
        pre=''
        for letter in word:
            if letter in current_dict[0]:
                current_dict=current_dict[0][letter]
                if current_dict[1]>1:
                    pre+=letter
                else:
                    pre+=letter
                    sol.append(pre)
                    break
    return sol

A=['zebra','dog','dove','duck']

print prefix(A)
