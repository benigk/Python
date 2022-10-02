from pydoc_data.topics import topics


name = {'n1': 'Gerlof von Bayes', 'n2': 'Arrietty Borrower', 'n3': 'Amélie Poulain', 'n4': 'Pi Thon-Rappel'}
print(name)

kindergarten = {
                'Gerlof von Bayes':{'birthday': '2016-12-31', 'soc.sec.no':'4567', 'topic':'syntax, historical linguistics, logic programming and spelling'},
                'Arrietty Borrower':{'birthday':'2017-07-17', 'soc.sec.no':'2345', 'topic': 'loan words'}, 
                'Amélie Poulain':{'birthday': '2015-03-03', 'soc.sec.no':'0123', 'topic': 'NLP for Parisian French, sand castle engineering'}, 
                'Pi Thon-Rappel':{'birthday':'2015-02-29', 'soc.sec.no':'8901', 'topic': 'programming language design'},
                }


##print(kindergarten['Gerlof']['birthday'])
#A4
for name in kindergarten:
    print(kindergarten[name]['topic'])

#A5
for name in kindergarten:
    if name.split()[-1].startswith('B'):
        print(kindergarten[name])

#B1
word_list = ['to','be',',','or','not','to','be',',','that','is','the','question',':']

bigram_dict = dict()

for index in range(len(word_list)-1):
    token1, token2 = word_list[index], word_list[index+1]
    if (token1, token2) in bigram_dict:
        bigram_dict[(token1, token2)] += 1
    else:
        bigram_dict[(token1, token2)] = 1

#B2
dict_downside = dict()

for bigram, count in bigram_dict.items():
    token1, token2 = bigram
    if token1 in dict_downside:
        if token2 in dict_downside[token1]:
            dict_downside[token1][token2] += 1
        else:
            dict_downside[token1][token2] = 1
    else:
        dict_downside[token1] = {token2: 1}

#B3
revert_bigram_dict = dict()

for token1 in dict_downside:
    for token2, count in dict_downside[token1].items():
        revert_bigram_dict[(token1, token2)] = count

#B4
trigram_sentence = ['can', 'you', 'can', 'a', 'can', 'as', 'a', 'canner', 'can', 'can', 'a', 'can','?']

trigram_dict = dict()

for index in range(len(trigram_sentence)-2):
    token1, token2, token3 = trigram_sentence[index], trigram_sentence[index+1], trigram_sentence[index+2]
    if (token1, token2, token3) in trigram_dict:
        trigram_dict[(token1, token2, token3)] += 1
    else:
        trigram_dict[(token1, token2, token3)] = 1

#B5
trigram_ratio_dict = dict()
new_bigram_dict = dict()


for index in range(len(trigram_sentence)-1):
    token1, token2 = trigram_sentence[index], trigram_sentence[index+1]
    if (token1, token2) in new_bigram_dict:
        new_bigram_dict[(token1, token2)] += 1
    else:
        new_bigram_dict[(token1, token2)] = 1

for (token1, token2, token3), count in trigram_dict.items():
    bigram_count = new_bigram_dict[(token1, token2)]
    trigram_ratio_dict[(token1, token2, token3)] = count / bigram_count