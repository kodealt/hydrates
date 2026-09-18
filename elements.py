# class file that automatically initializes object with elements 

class Elements:
    #info on elements from 
    # https://www.tabperiodic.com/en/
    __atmos = { # molar, name, series, electron config, electro-negativity, ion, state at 25C, state at STP
        "H" : [001.008  ,"Hydrogen"    , "Non-Metal"    , "1s1"     , 2.2   , ["+1", "-1"], "g"],
        "He": [004.026  ,"Helium"      , "Noble Gas"    , "1s2"     , None  , ["0"] , "g"],
        "Li": [006.940  ,"Lithium"     , "Alkali Metal" , "1s2 2s1" , 0.98  , ["+1"], "s"],
        "Be": [009.012  ,"Beryllium"   , "Alkali Earth" , "1s2 2s2" , 1.57  , ["+2", "+1"], "s"],
        "B" : [010.810  ,"Boron"       , "Metalloid"    , "1s2 2s2 2p1", 2.04, []]



        }

    def __init__(self):
        self.__atomic = Elements.__atmos
    
    def getMOL(self, e) -> float:
        e = e.capitalize()
        return self.__atomic.get(e, 0.0)[0]

