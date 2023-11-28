from nltk.translate.bleu_score import sentence_bleu
reference = [
    'this is a dog'.split(),
]
candidate = 'it is a dog'.split()

print('Individual 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
