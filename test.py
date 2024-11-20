#TEST THEO

# D'abord on doit importer les classe à tester
from mission8 import Duree, Chanson, Album

# CREATION DE QUELQUES OBJETS DE LA CLASSE Duree A TESTER
d0 = Duree(0,0,0)
d1 = Duree(10,20,59)
d2 = Duree( 8,41,25)
d3=Duree( 9, 49,65)
d4=Duree (61,61,61)

# FONCTION POUT TESTER LA METHODE __str__ DE LA CLASSE Duree
def test_Duree_str() :
    assert d1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert d2.__str__() == "08:41:25", "Test 2 Duree __str__"

# FONCTION POUR TESTER LA METHODE toSecondes DE LA CLASSE Duree
def test_Duree_to_secondes() :
    assert d1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert d2.to_secondes() == 31285, "Test 2 Duree toSecondes"
    assert d3.to_secondes() == 35405, "Test 3 Duree toSecondes (sec >60)"
    assert d4.to_secondes()== 223321, "Test 4 Duree toSecondes (h,m,s >60)"

# FONCTION POUR TESTER LA METHODE delta DE LA CLASSE Duree
def test_Duree_delta():
    assert d0.delta(0)==0, "Test 1 Duree_delta :how do you handle null time & d "
    assert d1.delta(0)==37259, "Test 2 Duree_delta :how do you handle null d "
    assert d2.delta(Duree(8,41,25))==0, "Test 3 Duree_delta :how do you handle d=self ? "

# FONCTION POUR TESTER  LA METHODE apres DE LA CLASSE Duree
def test_Duree_apres():
    assert d1.apres(d2),     "Test 1 Duree apres"
    assert not d0.apres(d1), "Test 2 Duree apres"
    assert not d0.apres(d0), "Test 3 Duree_apres : how do you handle d0.apres(d0)?"
    assert d4.apres(d0), "Test 4 Duree apres"
    
# FONCTION POUR TESTER LA METHODE ajouter DE LA CLASSE Duree
def test_Duree_ajouter():
    assert d0.ajouter(0) ==0, "test 1 Duree_ajouter"
    #To continue

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Duree_str()
test_Duree_to_secondes()
test_Duree_delta()
test_Duree_apres()
test_Duree_ajouter()

################################
# Tests pour la classe Chanson #
################################

# CREATION DE QUELQUES OBJETS DE LA CLASSE Chanson A TESTER
c = Chanson("Let's Dance", "David Bowie", Duree(0,4,5))

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Chanson
def test_Chanson_str(chanson) :
    # A COMPLETER
    pass

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Chanson_str(c)

##############################
# Tests pour la classe Album #
##############################

# CREATION D'UN OBJET DE LA CLASSE Album A TESTER


# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Album

# FONCTION POUR TESTER LA METHODE add DE LA CLASSE Album

# APPEL DES DIFFERENTES FONCTIONS TEST


#####################################
# Test du comportement du programme #
#####################################

# QUELQUES TESTS ICI POUR TESTER QUE LES 3 CLASSES COLLABORENT CORRECTEMENT
# ET PEUVENT ETRE UTILISE POUR CREER DES ALBUMS DE CHANSONS SELON LES CONSIGNES
# DE LA MISSION
# à fournir


#TEST ROMAN 

d0 = Duree(0, 0, 0)
d1 = Duree(10, 20, 59)
d2 = Duree(8, 41, 25)
c = Chanson("Let's Dance", "David Bowie", Duree(0, 4, 5))
album = Album("Album 1")
chanson1 = Chanson("Let's Dance", "David Bowie", Duree(0, 4, 5))
chanson2 = Chanson("Space Oddity", "David Bowie", Duree(0, 5, 15))


def test_Duree_str():

    assert d1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert d2.__str__() == "08:41:25", "Test 2 Duree __str__"


def test_Duree_to_secondes():
    assert d1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert d2.to_secondes() == 31285, "Test 2 Duree toSecondes"


def test_Duree_delta():

    delta = d1.delta(d2)  
    assert delta.__str__() == "01:39:34", "Test delta Duree"


def test_Duree_apres():
    assert d1.apres(d2), "Test 1 Duree apres"
    assert not d0.apres(d1), "Test 2 Duree apres"


def test_Duree_ajouter():
    d3 = d1.ajouter(d2)
    assert d3.__str__() == "19:02:24", "Test ajouter Duree"


def test_Chanson_str():
    assert c.__str__() == "Let's Dance - David Bowie (Durée: 04:05)", "Test 1 Chanson __str__"


def test_Album_str():
    album.add(chanson1)
    album.add(chanson2)
    assert album.__str__() == "Album 1\nChansons:\nLet's Dance - David Bowie (Durée: 04:05)\nSpace Oddity - David Bowie (Durée: 05:15)\n", "Test 1 Album __str__"


def test_Album_add():
    album.add(Chanson("Heroes", "David Bowie", Duree(0, 6, 30)))
    assert len(album.chansons) == 3, "Test 1 Album add"


def run_tests():
    test_Duree_str()
    test_Duree_to_secondes()
    test_Duree_delta()
    test_Duree_apres()
    test_Duree_ajouter()
    test_Chanson_str()
    test_Album_str()
    test_Album_add()

    print("Tous les tests ont réussi!")

