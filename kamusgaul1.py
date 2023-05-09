meme_dict = {'CRINGE':'sesuatu yang alay atau menjijikan',
             'LOL':'ketawa sangat kencang',
             'OTW':'sedang mau kesana',
             'BTW':'omong-omong'
             }
             
word = input('ketik kata yang ingin dicari tau:')

if word in meme_dict.keys():
    #apa yang harus ditampilkan ketika kata nya ada di dalam kamus
    print(meme_dict[word])
else:
    #apa yang harus ditampilkan ketika kata nya tidak ada di dalam kamus
    print('kata yang dicari tidak tersedia')
