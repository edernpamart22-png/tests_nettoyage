from nettoyage import supprimer_valeurs_negatives

def test_supprime_negatifs():
    assert supprimer_valeurs_negatives([3, -1, 5, -2]) == [3, 5]
