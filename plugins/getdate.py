def getDate():
    import datetime
    month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
    }
    x = datetime.datetime.now()
    dateinfo={"day":x.day,"month":month[x.month],"year":x.year,"mon":x.month}
    return dateinfo
def getword():
    nested_hard_words = [
    ["aberration", "abstruse", "acrimonious", "anomalous", "apocryphal", "assiduous", "bellicose", "capricious",
     "cogent", "debilitate", "deleterious", "diaphanous", "effulgent", "ephemeral", "esoteric", "evanescent", 
     "fastidious", "fatuous", "inchoate", "ineffable", "intransigent", "laconic", "mendacious", "munificent", 
     "nefarious", "obfuscate", "obsequious", "parsimonious", "pernicious", "recalcitrant", "recondite"],


    ["sagacious", "sanguine", "sophistry", "sycophant", "taciturn", "tenebrous", "ubiquitous", "vainglorious", 
     "vituperate", "vociferous", "winsome", "zephyr", "xenophobic", "quixotic", "quintessential", "obdurate", 
     "parsimonious", "pusillanimous", "reverberate", "proclivity", "prestidigitation", "recondite", "ascetic", 
     "avaricious", "bumptious", "circuitous", "disparate", "enigmatic", "feckless", "hapless", "indefatigable"],


    ["inimical", "jejune", "lambent", "lugubrious", "malfeasance", "mellifluous", "obstreperous", "ostentatious", 
     "pugnacious", "quiescent", "rambunctious", "recalcitrant", "sanctimonious", "sardonic", "sesquipedalian", 
     "splenetic", "surreptitious", "temerity", "truculent", "ubiquitous", "vapid", "voracious", "whimsical", 
     "xenophobic", "yammer", "zealot", "antediluvian", "bloviate", "calumniate", "deleterious", "effervescent"],


    ["equanimity", "facetious", "grandiloquent", "heuristic", "idiosyncratic", "juxtapose", "kaleidoscopic", 
     "lachrymose", "maladroit", "neologism", "obstreperous", "pusillanimous", "querulous", "redolent", 
     "sacrilegious", "trifling", "unctuous", "vaudevillian", "wanderlust", "xenophile", "yen", "zephyr", 
     "alacrity", "boondoggle", "cantankerous", "deleterious", "enigmatic", "fortuitous", "gregarious", "hapless", 
     "indelible"],


    ["jingoistic", "kowtow", "lackadaisical", "maudlin", "nebulous", "obfuscate", "perfidious", "quandary", 
     "recalcitrant", "serendipity", "tantamount", "umbrage", "vexatious", "wanton", "xenial", "yonder", "zealous", 
     "amalgamate", "belligerent", "capricious", "dichotomy", "emollient", "fervid", "garrulous", "harangue", 
     "incongruous", "juxtaposition", "kudos", "laconic", "magnanimous", "nefarious"],

    ["obdurate", "perspicacious", "quintessence", "resplendent", "sagacious", "temerarious", "untenable", 
     "volition", "whimsy", "xenophobia", "yoke", "zeal", "apocryphal", "bucolic", "conflagration", "dissonant", 
     "effrontery", "fortuitous", "grandiose", "hapless", "inchoate", "jovial", "kaleidoscope", "limpid", 
     "munificent", "nonplussed", "oscillate", "perspicuity", "quagmire", "rectitude", "serpentine"],

   
    ["tacit", "umbrageous", "vapid", "winsome", "xeric", "yearn", "zephyr", "abstemious", "boorish", "convivial", 
     "decadent", "efficacious", "frivolous", "grievous", "hapless", "impudent", "juxtapose", "knell", "lucid", 
     "mawkish", "neologism", "obsequious", "parsimonious", "querulous", "refractory", "sinecure", "truculent", 
     "unfathomable", "vicarious", "wily", "xenophobic"],

 
    ["yokel", "zephyr", "ambiguous", "bombastic", "churlish", "deleterious", "egregious", "flippant", "gregarious", 
     "hubristic", "insipid", "jejune", "kudos", "loquacious", "misanthropic", "nonchalant", "obdurate", 
     "precarious", "quixotic", "rancorous", "solipsistic", "tantamount", "unctuous", "verbose", "willful", 
     "xeric", "yammer", "zeal", "abstruse", "bellicose", "capricious"],

    
    ["dilatory", "effulgent", "fatuous", "garrulous", "hubris", "iconoclast", "jejune", "kowtow", "luculent", 
     "mendicant", "nebulous", "obfuscate", "penurious", "quiescent", "reticent", "sophomoric", "terse", "unseemly", 
     "vagary", "whimsical", "xenophobic", "yore", "zenith", "notorious", "blandishment", "conciliatory",
     "diaphanous", "effervescent", "facetious", "gregarious", "histrionic"],


    ["idiosyncratic", "jejune", "kitsch", "lachrymose", "maudlin", "neologism", "obsequious", "puerile", 
     "quixotic", "resilient", "spurious", "taciturn", "unctuous", "verisimilitude", "winsome", "xenial", "yonder", 
     "zealous", "acrid", "boisterous", "cacophony", "deleterious", "ephemeral", "fortuitous", "garrulous", 
     "hermetic", "intransigent", "jovial", "knave", "lethargic", "misanthropic"],


    ["nonchalant", "obsequious", "perfidious", "quiescent", "recondite", "surreptitious", "taciturn", "umbrage", 
     "veracity", "whimsical", "xeric", "yen", "zealous", "acumen", "blandishment", "circumspect", "dissident", 
     "egregious", "fortitude", "gregarious", "haphazard", "inane", "jejune", "kudos", "laconic", "mendacious", 
     "nonplussed", "obstreperous", "placate", "quixotic", "recalcitrant"],

    ["sagacious", "tantamount", "ubiquitous", "vexatious", "whimsical", "xenophobia", "yammer", "zephyr", 
     "apocryphal", "bellicose", "cogent", "debilitate", "effusive", "fastidious", "grandiloquent", "hapless", 
     "inchoate", "juxtaposition", "kaleidoscopic", "lachrymose", "misanthropic", "nonchalant", "obsequious", 
     "puerile", "quixotic", "reverberate", "serendipity", "truculent", "urbane", "voracious", "winsome"]
    ]
    return nested_hard_words[getDate()["mon"]-1][getDate()["day"]-1]

print(getword())