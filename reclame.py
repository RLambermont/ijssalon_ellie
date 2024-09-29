from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    kortingsprijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingsprijs} euro."

def inkomsten_totaal(inkomsten): 
    totaal = sum(inkomsten)
    bedrag = totaal*0.09
    return f"Het toaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden"
 
def laag_en_hoog(mijn_lijst):
    return (min(mijn_lijst), max(mijn_lijst))

def gemiddelde(mijn_lijst):
    lengte = len(mijn_lijst)
    som = sum(mijn_lijst)
    bedrag = (som/lengte)
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

def meervoudig(invoer_lijst):
    return(laag_en_hoog(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])


