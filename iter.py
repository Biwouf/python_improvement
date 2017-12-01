#! /usr/bin/env python3
# coding: utf-8

import re
import logging as lg 

#Conf
lg.basicConfig(level=lg.DEBUG) 

big_data = """Le sénateur, dont il a été parlé plus haut, était un homme entendu qui 
    avait fait son chemin avec une rectitude inattentive à toutes ces rencontres qui font 
    obstacle et qu'on nomme conscience, foi jurée, justice, devoir; il avait marché droit à 
    son but et sans broncher une seule fois dans la ligne de son avancement et de son intérêt. 
    C'était un ancien procureur, attendri par le succès, pas méchant homme du tout, rendant 
    tous les petits services qu'il pouvait à ses fils, à ses gendres, à ses parents, même à 
    des amis; ayant sagement pris de la vie les bons côtés, les bonnes occasions, les bonnes 
    aubaines. Le reste lui semblait assez bête. Il était spirituel, et juste assez lettré 
    pour se croire un disciple d'Epicure en n'étant peut-être qu'un produit de Pigault-Lebrun.
    [...]
    (Les Misérables, Victor Hugo)
    """

def is_part_of_a_word(letter):
    """Return 1 if it's a letter. Else > 0"""
    return len(re.findall('[\wéàôêè]', letter))

def get_words(text):
    """Identify each word in a string"""
    print('Je commence à lire le texte')

    word = ''

    for ch in big_data:
        if is_part_of_a_word(ch):
            word += ch
        elif is_part_of_a_word(ch) == 0 and word != '':
            yield word
            word = ''
        else:
            continue

def find_long_words(words):
    """Identify longs words. More than or 6 characters"""
    return (x for x in words if len(x) >= 6)

def find_words_with_a(words):
    """Identify longs words which contain at least the 'a' character"""
    return (x for x in words if 'a' in x)

def main():
    """Main program"""
    #Création d'un générateur qui va comprendre tous les mots du texte
    words = get_words(big_data)
    #Création d'un nouveau générateur qui va comprendre les mots de plus ou de 6 caractères
    words = find_long_words(words)
    #Création d'un nouveau générateur qui va comprendre les mots de plus ou de 6 caractères qui contiennent un a
    words = find_words_with_a(words)
    print("Words n'est encore un générateur :")
    print('Inventaire des mots de 6 lettes ou plus qui contiennent un a :')
    print ([w for w in words])

	
if __name__ == '__main__':
	main()