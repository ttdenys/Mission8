#Code écrit par Roman Forest et Théo Denys
class Duree :
    def __init__(self,h,m,s):
        """
        @pre: h, m et s sont des entiers positifs (ou zéro)
            m et s sont < 60
        @post: Crée une nouvelle durée en heures, minutes et secondes.
        """
        self.h=h
        self.m=m
        self.s=s

    def to_secondes(self):
        """
        @pre:  -
        @post: Retourne le nombre total de secondes de cette instance de Duree (self).
        Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
        """
        return (float(self.h)*3600)+(float(self.m)*60+float(self.s))#We add hours and minutes to the seconds
    def delta(self,d) :
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne la différence en secondes entre cette durée (self)
            et la durée d passée en paramètre.
            Cette valeur renovoyée est positif si cette durée (self)
            est plus grand que la durée d, négatif sinon.
        Par exemple, si cette durée (self) est 8h 41m 25s (donc 31285 secondes)
        et la durée d est 0h 1m 25s, la valeur retournée est 31200.
        Inversement, si cette durée (self) est 0h 1m 25s et la durée
        d est 8h 41m 25s, alors la valeur retournée est -31200.
        """
        self.d=d
        difference = self.to_secondes()-self.d.to_secondes()
        return difference
    def apres(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne True si cette durée (self) est plus grand que la durée
            d passée en paramètre; retourne False sinon.
        """
        if self.delta(d)>0:
            return True
        else:
            return False
    def ajouter(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Ajoute une autre durée d à cette durée (self),
            corrigée de manière à ce que les minutes et les secondes soient
            dans l'intervalle [0..60[, en reportant au besoin les valeurs
            hors limites sur les unités supérieures
            (60 secondes = 1 minute, 60 minutes = 1 heure).
            Ne retourne pas une nouvelle durée mais modifié la durée self.
        """
        total_seconds = self.to_secondes() + d.to_secondes()
        self.h = int(total_seconds // 3600)
        remaining_seconds = total_seconds % 3600
        self.m = int(remaining_seconds // 60)
        self.s = int(remaining_seconds % 60)
        self.format_correction()


        return ("{:02}:{:02}:{:02}".format(self.h, self.m, self.s))
    def format_correction(self):
        """
        This is meant to convert a duration, contained in self, to a one that actually repsects the format.
        """
        conditions=[False, False, False, False, False]
        
        while all(conditions)==False:
            #Condition 1 and 3
            if isinstance(self.h , int)==False:
                self.m+=((float(self.h)-float(int(self.h)))*60) # The difference between lower round number and actual number, * by 6- to convert into minutes
                self.h=int(self.h) #this will remove any . digits
            if isinstance(self.m,int)==False:
                self.s=float(self.s)+((float(self.m)-float(int(self.m)))*60)
                self.m=int(self.m)
            if isinstance(self.s,int)==False:
                self.s=int(self.s)
            #Condition 2: check if it's below 60
            if self.s >= 60:
                self.m+=(int(self.s)//60)
                self.s-=(int(self.s)//60)*60
            if self.m >= 60:
                self.h+=(int(self.m)//60)
                self.m-=(int(self.m)//60)*60
            conditions=[isinstance(self.h , int), isinstance(self.m,int), isinstance(self.s,int), self.s<60, self.m<60] # Condition are True if format is correct

    
    def __str__(self):
        """
        @pre:  -
        @post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le string désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        self.format_correction()
        return ("{:02}:{:02}:{:02}".format(self.h, self.m, self.s))
#DUREE OK
test1=Duree(5,64,22)
print(test1)
test2=Duree(5,63,63)
print(test2)
test3=Duree(61,61,61)
#AJOUTER OK
test3.ajouter(Duree(2,0,0))
print(test3)


class Chanson :

    def __init__(self,t,a,d):
        """
        @pre:  t et a sont des string, d est une instance de la classe Duree
        @post: Crée une nouvelle chanson, caractérisée par un titre t,
                un auteur a et une durée d.
        """

        # "Let's Dance", "David Bowie", Duree(0, 4, 5)

        self.t = t
        self.a = a
        self.d = d


    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "TITRE - AUTEUR - DUREE".
            Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """

        return f"{self.t} - {self.a} - {self.d}"

class Album :
    def __init__(self, numero):
        """
        @pre:  numero est un entier identifiant de facon unique cet album
        @post: Crée un nouvel album, avec comme identifiant le numero,
            et avec une liste de chansons vide.
        """
        self.numero=numero
        self.album,self.bib=[],{} # Add a dictionnary with albums (bibilotheque)
        self.bib[self.numero]=self.album #Add album x
        self.duree_album=0


    def add(self,chanson):
        """
        @pre: une chanson au format TITRE CHANSON MINUTE DUREE
        @post: ajouter la chanson a l'abum 
        """
        self.chanson=chanson
        self.elems_chanson=self.chanson.split()
        print("elems chanson",self.elems_chanson)
        self.length=Duree(0,self.elems_chanson[2],self.elems_chanson[3])
        self.chanson_clean=self.elems_chanson[0]+" - "+self.elems_chanson[1]+" - " + str(self.length)
        print(self.chanson_clean)
        self.album.append(self.chanson_clean)
        self.duree_album+=Duree(0,float(self.elems_chanson[2]),float(self.elems_chanson[3])).to_secondes()
    def __str__(self):
        print("Album " , self.numero , "(" , len(self.album) , " chanson(s)" , "- " , self.duree_album , ")")
        for i in range(len(self.album)):
            print(i)
            for j in range(len((self.album[i].split("-")))): #Format for 0x not x needed + adding dashes betwwen elements
                l=self.album[i]
                print("t",l[j],l[j+1],l[j+2  ])
                j+=2
        return str(self.album)

if __name__ == "__main__":
    # Grâce à la ligne ci-dessus, le code ci-dessous ne sera exécuté que si on n'exécute ce fichier directement.
    # Ceci nous permet d'éviter que le code ci-dessous sera exécuté lorsqu'on fait un import de ce fichier,
    # par exemple dans notre fichier test.py
    pass
    # A COMPLETER PAR LES ETUDIANTS
    # (mettez ici votre code pour créer les albums à partir de la lecture du fichier 'music-db.txt')
    __name__

album1=Album(1)
album1.add('Avf Stromae 3 25')
album1.add("Éclairs Zaho_de_Zagazhan 3 61")
print(album1)