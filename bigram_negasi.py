import re
kata_negasi = ["tidak", "bukan"]
kata_dicari = "saya tidak marah dan tidak makan bukan juga tidak pergi"
def biGram(kata_negasi, kata_dicari):
    if type(kata_negasi) != list:
        kata_negasi = [kata_negasi]  
    n_index = []
    
    for i in kata_negasi:
        index_replace = [(m.end(0)) for m in re.finditer(i,kata_dicari)]
        n_index += index_replace
    for rep in n_index:
        huruf = [x for x in kata_dicari]
        huruf[rep] = "_"
        kata_dicari = "".join(huruf)
    return kata_dicari

biGram(kata_negasi, kata_dicari)
