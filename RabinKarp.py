def int_mod(a,b):
    return (a%b+b)%b

def naive_match(text1,text2):
    if len(text1) != len(text2):
        return False
        
    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            return False
    return True
        
def Rabin_Karp(text,pattern):
    n=len(text)
    m=len(pattern)
    
    B=541
    M=1511
    if n<m:
        return
    hp=0
    
    for i in range(m):
        hp=int_mod(hp*B+ord(pattern[i]),M)
    ht=0
    for i in range(m):
        ht=int_mod(ht*B+ord(text[i]),M)
    
    if ht==hp:
        print "Hash matched in the beginning"
        if naive_match(text[0:m],pattern):
            print "Strings matched too"
            return
        
    for i in range(m,n):
        E=(B**(m-1))%M
        ht=int_mod(ht-int_mod(ord(text[i-m])*E,M),M)
        ht=int_mod(ht*B,M)
        ht=int_mod(ht+ord(text[i]),M)
        
        if ht==hp:
            print "Hash matched at ",i-m+1
            if naive_match(text[i-m+1:i+1],pattern):
                print "Strings matched too."
                print "String is :", text[i-m+1:i+1]
                return
    print "Didn't match"
    
    
text="""To sure calm much most long me mean. Able rent long in do we. Uncommonly no it announcing melancholy an in. Mirth learn it he given. Secure shy favour length all twenty denote. He felicity no an at packages answered opinions juvenile. 

Oh he decisively impression attachment friendship so if everything. Whose her enjoy chief new young. Felicity if ye required likewise so doubtful. On so attention necessary at by provision otherwise existence direction. Unpleasing up announcing unpleasant themselves oh do on. Way advantage age led listening belonging supposing. 

Sudden looked elinor off gay estate nor silent. Son read such next see the rest two. Was use extent old entire sussex. Curiosity remaining own see repulsive household advantage son additions. Supposing exquisite daughters eagerness why repulsive for. Praise turned it lovers be warmly by. Little do it eldest former be if. 

Husbands ask repeated resolved but laughter debating. She end cordial visitor noisier fat subject general picture. Or if offering confined entrance no. Nay rapturous him see something residence. Highly talked do so vulgar. Her use behaved spirits and natural attempt say feeling. Exquisite mr incommode immediate he something ourselves it of. Law conduct yet chiefly beloved examine village proceed. 

Alteration literature to or an sympathize mr imprudence. Of is ferrars subject as enjoyed or tedious cottage. Procuring as in resembled by in agreeable. Next long no gave mr eyes. Admiration advantages no he celebrated so pianoforte unreserved. Not its herself forming charmed amiable. Him why feebly expect future now. 

Be at miss or each good play home they. It leave taste mr in it fancy. She son lose does fond bred gave lady get. Sir her company conduct expense bed any. Sister depend change off piqued one. Contented continued any happiness instantly objection yet her allowance. Use correct day new brought tedious. By come this been in. Kept easy or sons my it done. 

To shewing another demands to. Marianne property cheerful informed at striking at. Clothes parlors however by cottage on. In views it or meant drift to. Be concern parlors settled or do shyness address. Remainder northward performed out for moonlight. Yet late add name was rent park from rich. He always do do former he highly. 

In it except to so temper mutual tastes mother. Interested cultivated its continuing now yet are. Out interested acceptance our partiality affronting unpleasant why add. Esteem garden men yet shy course. Consulted up my tolerably sometimes perpetual oh. Expression acceptance imprudence particular had eat unsatiable. 

Man request adapted spirits set pressed. Up to denoting subjects sensible feelings it indulged directly. We dwelling elegance do shutters appetite yourself diverted. Our next drew much you with rank. Tore many held age hold rose than our. She literature sentiments any contrasted. Set aware joy sense young now tears china shy. 

Allow miles wound place the leave had. To sitting subject no improve studied limited. Ye indulgence unreserved connection alteration appearance my an astonished. Up as seen sent make he they of. Her raising and himself pasture believe females. Fancy she stuff after aware merit small his. Charmed esteems luckily age out. """
pattern= "place"

Rabin_Karp(text,pattern)
