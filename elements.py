# class file that automatically initializes object with elements 

class Elements:
    # info on elements from 
    # https://www.tabperiodic.com/en/
    # ONLY the following dictionary was generated with Gemini.

    __atmos = { # molar, name, series, electron config, electro-negativity, ion, state at 25C
        # Period 1
        "H" : [1.008,   "Hydrogen",    "Non-Metal",            "1s1",         2.2,  ["+1", "-1"], "g"],
        "He": [4.026,   "Helium",      "Noble Gas",            "1s2",         None, ["0"],        "g"],
        
        # Period 2
        "Li": [6.940,   "Lithium",     "Alkali Metal",         "1s2 2s1",     0.98, ["+1"],       "s"],
        "Be": [9.012,   "Beryllium",   "Alkaline Earth",         "1s2 2s2",     1.57, ["+2", "+1"], "s"],
        "B" : [10.810,  "Boron",       "Metalloid",            "1s2 2s2 2p1", 2.04, [],          "s"],
        "C" : [12.011,  "Carbon",      "Non-Metal",            "1s2 2s2 2p2", 2.55, ["+4", "-4"], "s"],
        "N" : [14.007,  "Nitrogen",    "Non-Metal",            "1s2 2s2 2p3", 3.04, ["-3", "+3", "+5"], "g"],
        "O" : [15.999,  "Oxygen",      "Non-Metal",            "1s2 2s2 2p4", 3.44, ["-2"],        "g"],
        "F" : [18.998,  "Fluorine",    "Halogen",              "1s2 2s2 2p5", 3.98, ["-1"],        "g"],
        "Ne": [20.180,  "Neon",        "Noble Gas",            "1s2 2s2 2p6", None, ["0"],        "g"],
        
        # Period 3
        "Na": [22.990,  "Sodium",      "Alkali Metal",         "[Ne] 3s1",    0.93, ["+1"],       "s"],
        "Mg": [24.305,  "Magnesium",   "Alkaline Earth",         "[Ne] 3s2",    1.31, ["+2"],       "s"],
        "Al": [26.982,  "Aluminum",    "Post-Transition Metal","[Ne] 3s2 3p1",1.61, ["+3"],       "s"],
        "Si": [28.085,  "Silicon",     "Metalloid",            "[Ne] 3s2 3p2",1.90, ["+4", "-4"], "s"],
        "P" : [30.974,  "Phosphorus",  "Non-Metal",            "[Ne] 3s2 3p3",2.19, ["-3", "+3", "+5"], "s"],
        "S" : [32.060,  "Sulfur",      "Non-Metal",            "[Ne] 3s2 3p4",2.58, ["-2", "+4", "+6"], "s"],
        "Cl": [35.450,  "Chlorine",    "Halogen",              "[Ne] 3s2 3p5",3.16, ["-1", "+1", "+3", "+5", "+7"], "g"],
        "Ar": [39.950,  "Argon",       "Noble Gas",            "[Ne] 3s2 3p6",None, ["0"],        "g"],
        
        # Period 4
        "K" : [39.098,  "Potassium",   "Alkali Metal",         "[Ar] 4s1",    0.82, ["+1"],       "s"],
        "Ca": [40.078,  "Calcium",     "Alkaline Earth",         "[Ar] 4s2",    1.00, ["+2"],       "s"],
        "Sc": [44.956,  "Scandium",    "Transition Metal",     "[Ar] 3d1 4s2",1.36, ["+3"],       "s"],
        "Ti": [47.867,  "Titanium",    "Transition Metal",     "[Ar] 3d2 4s2",1.54, ["+4", "+3"],  "s"],
        "V" : [50.942,  "Vanadium",    "Transition Metal",     "[Ar] 3d3 4s2",1.63, ["+5", "+4", "+3", "+2"], "s"],
        "Cr": [51.996,  "Chromium",    "Transition Metal",     "[Ar] 3d5 4s1",1.66, ["+3", "+6", "+2"], "s"],
        "Mn": [54.938,  "Manganese",   "Transition Metal",     "[Ar] 3d5 4s2",1.55, ["+2", "+7", "+4", "+6"], "s"],
        "Fe": [55.845,  "Iron",        "Transition Metal",     "[Ar] 3d6 4s2",1.83, ["+2", "+3"],  "s"],
        "Co": [58.933,  "Cobalt",      "Transition Metal",     "[Ar] 3d7 4s2",1.88, ["+2", "+3"],  "s"],
        "Ni": [58.693,  "Nickel",      "Transition Metal",     "[Ar] 3d8 4s2",1.91, ["+2", "+3"],  "s"],
        "Cu": [63.546,  "Copper",      "Transition Metal",     "[Ar] 3d10 4s1",1.90,["+2", "+1"],  "s"],
        "Zn": [65.380,  "Zinc",        "Transition Metal",     "[Ar] 3d10 4s2",1.65,["+2"],       "s"],
        "Ga": [69.723,  "Gallium",     "Post-Transition Metal","[Ar] 3d10 4s2 4p1", 1.81, ["+3"], "s"],
        "Ge": [72.630,  "Germanium",   "Metalloid",            "[Ar] 3d10 4s2 4p2", 2.01, ["+4", "+2"], "s"],
        "As": [74.922,  "Arsenic",     "Metalloid",            "[Ar] 3d10 4s2 4p3", 2.18, ["+3", "-3", "+5"], "s"],
        "Se": [78.971,  "Selenium",    "Non-Metal",            "[Ar] 3d10 4s2 4p4", 2.55, ["-2", "+4", "+6"], "s"],
        "Br": [79.904,  "Bromine",     "Halogen",              "[Ar] 3d10 4s2 4p5", 2.96, ["-1", "+5", "+1"], "l"],
        "Kr": [83.798,  "Krypton",     "Noble Gas",            "[Ar] 3d10 4s2 4p6", 3.00, ["0"],   "g"],
        
        # Period 5
        "Rb": [85.468,  "Rubidium",    "Alkali Metal",         "[Kr] 5s1",    0.82, ["+1"],       "s"],
        "Sr": [87.620,  "Strontium",   "Alkaline Earth",         "[Kr] 5s2",    0.95, ["+2"],       "s"],
        "Y" : [88.906,  "Yttrium",     "Transition Metal",     "[Kr] 4d1 5s2",1.22, ["+3"],       "s"],
        "Zr": [91.224,  "Zirconium",   "Transition Metal",     "[Kr] 4d2 5s2",1.33, ["+4"],       "s"],
        "Nb": [92.906,  "Niobium",     "Transition Metal",     "[Kr] 4d4 5s1",1.6,  ["+5", "+3"],  "s"],
        "Mo": [95.950,  "Molybdenum",  "Transition Metal",     "[Kr] 4d5 5s1",2.16, ["+6", "+4", "+3", "+5"], "s"],
        "Tc": [98.000,  "Technetium",  "Transition Metal",     "[Kr] 4d5 5s2",1.9,  ["+7", "+4"],  "s"],
        "Ru": [101.07,  "Ruthenium",   "Transition Metal",     "[Kr] 4d7 5s1",2.2,  ["+3", "+4", "+2", "+6", "+8"], "s"],
        "Rh": [102.91,  "Rhodium",     "Transition Metal",     "[Kr] 4d8 5s1",2.28, ["+3", "+2", "+4"], "s"],
        "Pd": [106.42,  "Palladium",   "Transition Metal",     "[Kr] 4d10",   2.20, ["+2", "+4"],  "s"],
        "Ag": [107.87,  "Silver",      "Transition Metal",     "[Kr] 4d10 5s1",1.93, ["+1"],      "s"],
        "Cd": [112.41,  "Cadmium",     "Transition Metal",     "[Kr] 4d10 5s2",1.69, ["+2"],      "s"],
        "In": [114.82,  "Indium",      "Post-Transition Metal","[Kr] 4d10 5s2 5p1", 1.78, ["+3"], "s"],
        "Sn": [118.71,  "Tin",         "Post-Transition Metal","[Kr] 4d10 5s2 5p2", 1.96, ["+4", "+2"], "s"],
        "Sb": [121.76,  "Antimony",    "Metalloid",            "[Kr] 4d10 5s2 5p3", 2.05, ["+3", "-3", "+5"], "s"],
        "Te": [127.60,  "Tellurium",   "Metalloid",            "[Kr] 4d10 5s2 5p4", 2.1,  ["-2", "+4", "+6"], "s"],
        "I" : [126.90,  "Iodine",      "Halogen",              "[Kr] 4d10 5s2 5p5", 2.66, ["-1", "+5", "+7"], "s"],
        "Xe": [131.29,  "Xenon",       "Noble Gas",            "[Kr] 4d10 5s2 5p6", 2.6,  ["0", "+4", "+6"], "g"],
        
        # Period 6
        "Cs": [132.91,  "Cesium",      "Alkali Metal",         "[Xe] 6s1",    0.79, ["+1"],       "s"],
        "Ba": [137.33,  "Barium",      "Alkaline Earth",         "[Xe] 6s2",    0.89, ["+2"],       "s"],
        "La": [138.91,  "Lanthanum",   "Lanthanide",           "[Xe] 5d1 6s2",1.1,  ["+3"],       "s"],
        "Ce": [140.12,  "Cerium",      "Lanthanide",           "[Xe] 4f1 5d1 6s2", 1.12, ["+3", "+4"], "s"],
        "Pr": [140.91,  "Praseodymium","Lanthanide",           "[Xe] 4f3 6s2",1.13, ["+3"],       "s"],
        "Nd": [144.24,  "Neodymium",   "Lanthanide",           "[Xe] 4f4 6s2",1.14, ["+3"],       "s"],
        "Pm": [145.00,  "Promethium",  "Lanthanide",           "[Xe] 4f5 6s2",1.13, ["+3"],       "s"],
        "Sm": [150.36,  "Samarium",    "Lanthanide",           "[Xe] 4f6 6s2",1.17, ["+3", "+2"],  "s"],
        "Eu": [151.96,  "Europium",    "Lanthanide",           "[Xe] 4f7 6s2",1.2,  ["+3", "+2"],  "s"],
        "Gd": [157.25,  "Gadolinium",  "Lanthanide",           "[Xe] 4f7 5d1 6s2", 1.2, ["+3"],  "s"],
        "Tb": [158.93,  "Terbium",     "Lanthanide",           "[Xe] 4f9 6s2",1.1,  ["+3", "+4"],  "s"],
        "Dy": [162.50,  "Dysprosium",  "Lanthanide",           "[Xe] 4f10 6s2",1.22, ["+3"],      "s"],
        "Ho": [164.93,  "Holmium",     "Lanthanide",           "[Xe] 4f11 6s2",1.23, ["+3"],      "s"],
        "Er": [167.26,  "Erbium",      "Lanthanide",           "[Xe] 4f12 6s2",1.24, ["+3"],      "s"],
        "Tm": [168.93,  "Thulium",     "Lanthanide",           "[Xe] 4f13 6s2",1.25, ["+3", "+2"],  "s"],
        "Yb": [173.05,  "Ytterbium",   "Lanthanide",           "[Xe] 4f14 6s2",1.1,  ["+3", "+2"],  "s"],
        "Lu": [174.97,  "Lutetium",    "Transition Metal",     "[Xe] 4f14 5d1 6s2", 1.27, ["+3"], "s"],
        "Hf": [178.49,  "Hafnium",     "Transition Metal",     "[Xe] 4f14 5d2 6s2", 1.3,  ["+4"],  "s"],
        "Ta": [180.95,  "Tantalum",    "Transition Metal",     "[Xe] 4f14 5d3 6s2", 1.5,  ["+5"],  "s"],
        "W" : [183.84,  "Tungsten",    "Transition Metal",     "[Xe] 4f14 5d4 6s2", 2.36, ["+6"],  "s"],
        "Re": [186.21,  "Rhenium",     "Transition Metal",     "[Xe] 4f14 5d5 6s2", 1.9,  ["+7", "+4", "+2"], "s"],
        "Os": [190.23,  "Osmium",      "Transition Metal",     "[Xe] 4f14 5d6 6s2", 2.2,  ["+4", "+3", "+2", "+6", "+8"], "s"],
        "Ir": [192.22,  "Iridium",     "Transition Metal",     "[Xe] 4f14 5d7 6s2", 2.2,  ["+4", "+3"],  "s"],
        "Pt": [195.08,  "Platinum",    "Transition Metal",     "[Xe] 4f14 5d9 6s1", 2.28, ["+2", "+4"],  "s"],
        "Au": [196.97,  "Gold",        "Transition Metal",     "[Xe] 4f14 5d10 6s1", 2.4, ["+3", "+1"],  "s"],
        "Hg": [200.59,  "Mercury",     "Transition Metal",     "[Xe] 4f14 5d10 6s2", 1.9, ["+2", "+1"],  "l"],
        "Tl": [204.38,  "Thallium",    "Post-Transition Metal","[Xe] 4f14 5d10 6s2 6p1", 1.62, ["+1", "+3"], "s"],
        "Pb": [207.20,  "Lead",        "Post-Transition Metal","[Xe] 4f14 5d10 6s2 6p2", 1.87, ["+2", "+4"], "s"],
        "Bi": [208.98,  "Bismuth",     "Post-Transition Metal","[Xe] 4f14 5d10 6s2 6p3", 2.02, ["+3", "+5"], "s"],
        "Po": [209.00,  "Polonium",    "Metalloid",            "[Xe] 4f14 5d10 6s2 6p4", 2.0, ["+4", "+2"], "s"],
        "At": [210.00,  "Astatine",    "Halogen",              "[Xe] 4f14 5d10 6s2 6p5", 2.2, ["-1", "+1", "+3", "+5"], "s"],
        "Rn": [222.00,  "Radon",       "Noble Gas",            "[Xe] 4f14 5d10 6s2 6p6", None, ["0"], "g"],
        
        # Period 7
        "Fr": [223.00,  "Francium",    "Alkali Metal",         "[Rn] 7s1",    0.7,  ["+1"],       "s"],
        "Ra": [226.00,  "Radium",      "Alkaline Earth",         "[Rn] 7s2",    0.9,  ["+2"],       "s"],
        "Ac": [227.00,  "Actinium",    "Actinide",             "[Rn] 6d1 7s2",1.1,  ["+3"],       "s"],
        "Th": [232.04,  "Thorium",     "Actinide",             "[Rn] 6d2 7s2",1.3,  ["+4"],       "s"],
        "Pa": [231.04,  "Protactinium","Actinide",             "[Rn] 5f2 6d1 7s2", 1.5, ["+5", "+4"], "s"],
        "U" : [238.03,  "Uranium",     "Actinide",             "[Rn] 5f3 6d1 7s2", 1.38, ["+6", "+4", "+5", "+3"], "s"],
        "Np": [237.00,  "Neptunium",   "Actinide",             "[Rn] 5f4 6d1 7s2", 1.36, ["+5", "+6", "+4"], "s"],
        "Pu": [244.00,  "Plutonium",   "Actinide",             "[Rn] 5f6 7s2",1.28, ["+4", "+6", "+3", "+5"], "s"],
        "Am": [243.00,  "Americium",   "Actinide",             "[Rn] 5f7 7s2",1.3,  ["+3", "+4", "+5", "+6"], "s"],
        "Cm": [247.00,  "Curium",      "Actinide",             "[Rn] 5f7 6d1 7s2", 1.3, ["+3"],      "s"],
        "Bk": [247.00,  "Berkelium",   "Actinide",             "[Rn] 5f9 7s2",1.3,  ["+3", "+4"],  "s"],
        "Cf": [251.00,  "Californium", "Actinide",             "[Rn] 5f10 7s2",1.3, ["+3"],      "s"],
        "Es": [252.00,  "Einsteinium", "Actinide",             "[Rn] 5f11 7s2",1.3, ["+3"],      "s"],
        "Fm": [257.00,  "Fermium",     "Actinide",             "[Rn] 5f12 7s2",1.3, ["+3"],      "s"],
        "Md": [258.00,  "Mendelevium", "Actinide",             "[Rn] 5f13 7s2",1.3, ["+3", "+2"],  "s"],
        "No": [259.00,  "Nobelium",    "Actinide",             "[Rn] 5f14 7s2",1.3, ["+3", "+2"],  "s"],
        "Lr": [266.00,  "Lawrencium",  "Transition Metal",     "[Rn] 5f14 7s2 7p1", 1.3, ["+3"], "s"],
        "Rf": [267.00,  "Rutherfordium","Transition Metal",    "[Rn] 5f14 6d2 7s2", None, ["+4"], "s"],
        "Db": [268.00,  "Dubnium",     "Transition Metal",     "[Rn] 5f14 6d3 7s2", None, ["+5"], "s"],
        "Sg": [269.00,  "Seaborgium",  "Transition Metal",     "[Rn] 5f14 6d4 7s2", None, ["+6"], "s"],
        "Bh": [270.00,  "Bohrium",     "Transition Metal",     "[Rn] 5f14 6d5 7s2", None, ["+7"], "s"],
        "Hs": [277.00,  "Hassium",     "Transition Metal",     "[Rn] 5f14 6d6 7s2", None, ["+8"], "s"],
        "Mt": [278.00,  "Meitnerium",  "Transition Metal",     "[Rn] 5f14 6d7 7s2", None, [],      "s"],
        "Ds": [281.00,  "Darmstadtium","Transition Metal",     "[Rn] 5f14 6d8 7s2", None, [],      "s"],
        "Rg": [282.00,  "Roentgenium", "Transition Metal",     "[Rn] 5f14 6d9 7s2", None, [],      "s"],
        "Cn": [285.00,  "Copernicium", "Transition Metal",     "[Rn] 5f14 6d10 7s2", None, ["+2"], "s"],
        "Nh": [286.00,  "Nihonium",    "Post-Transition Metal","[Rn] 5f14 6d10 7s2 7p1", None, [], "s"],
        "Fl": [289.00,  "Flerovium",   "Post-Transition Metal","[Rn] 5f14 6d10 7s2 7p2", None, [], "s"],
        "Mc": [289.00,  "Moscovium",   "Post-Transition Metal","[Rn] 5f14 6d10 7s2 7p3", None, [], "s"],
        "Lv": [293.00,  "Livermorium", "Post-Transition Metal","[Rn] 5f14 6d10 7s2 7p4", None, [], "s"],
        "Ts": [294.00,  "Tennessine",  "Halogen",              "[Rn] 5f14 6d10 7s2 7p5", None, [], "s"],
        "Og": [294.00,  "Oganesson",   "Noble Gas",            "[Rn] 5f14 6d10 7s2 7p6", None, [], "s"]
    }

    def __init__(self):
            self.__atomic = Elements.__atmos

            self.__MOL = {sym: row[0] for sym, row in self.__atomic.items()}
            self.__names = {sym: row[1] for sym, row in self.__atomic.items()}
            self.__name_sym = {row[1]: sym for sym, row in self.__atomic.items()}
            self.__series = {sym: row[2] for sym, row in self.__atomic.items()}
            self.__nobleConfig = {sym: row[3] for sym, row in self.__atomic.items()}
            self.__electroNegativity = {sym: row[4] for sym, row in self.__atomic.items()}
            self.__ionic = {sym: row[5] for sym, row in self.__atomic.items()}
            self.__stateAt25c = {sym: row[6] for sym, row in self.__atomic.items()}

            self.sym = self.__atomic.keys()


    # while i use variables that correspond to what the function is referencing,
    # i am pulling the "line" of elements rather than directly THAT specific property
    def getMOL(self, e):
        e = e.capitalize()
        return self.__MOL.get(e) 

    def getName(self, e):
        e = e.capitalize()
        return self.__names.get(e) 

    def getSeries(self, e):
        e = e.capitalize()
        return self.__series.get(e)

    def getNoble(self, e):
        e = e.capitalize()
        return self.__nobleConfig.get(e)

    def getElectroNegativity(self, e):
        e = e.capitalize()
        return self.__electroNegativity.get(e)

    def getIons(self, e):
        e = e.capitalize()
        return self.__ionic.get(e)

    def getState(self, e):
        e = e.capitalize()
        return self.__stateAt25c.get(e)

    def getSymbol(self, nm):
        self.__name_sym.get(nm)
        
