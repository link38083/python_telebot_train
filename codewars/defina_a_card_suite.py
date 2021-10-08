def define_suit(card):
    return {'C':'clubs', 'S':'spades', 'D':'diamonds', 'H':'hearts'}[card[-1]]

print(define_suit("4D"))