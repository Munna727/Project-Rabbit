import random
import requests
import re
def meaning_finder():
    rare_words = [
        "abecedarian", "adumbrate", "alexithymia", "amanuensis", "antediluvian", "apocryphal", "apsis",
        "ataraxia", "autocthonous", "bacchanalian", "bamboozle", "bathos", "bloviate", "cachinnate", "canorous", "caterwaul", "circumlocution", "circumspect", "cognoscente",
        "concatenation", "contumacious", "crepuscular", "cupidity",
        "deliquesce", "desideratum", "disequilibrium", "ebullient", "effulgent", "elucidate",
        "emollient", "ensorcelled", "equanimity", "ersatz", "etiolate", "farrago", "fatuous",
        "fecund", "foudroyant", "frisson", "gelid", "hobbledehoy", "impecunious", "incunabulum",
        "insouciant", "labile", "lagniappe", "lambent", "lachrymose", "legerdemain", "liminal",
        "logorrhea", "loquacious", "lubricious", "macaronic", "mellifluous", "mendacious",
        "misanthrope", "moribund", "nefarious", "nidificate", "numinous", "obfuscate", "obstreperous",
        "palimpsest", "pandiculation", "penumbra", "peregrinate", "perspicacity", "phantasmagoria",
        "plangent", "prestidigitation", "prognosticate", "propinquity", "pulchritude", "quixotic",
        "recondite", "redolent", "refulgent", "rodomontade", "sesquipedalian", "somnolent",
        "susurrus", "taciturn", "tatterdemalion", "threnody", "tintinnabulation", "truculent",
         "verisimilitude", "vicissitude", "vindicate", "vituperate", "woebegone",
        "xenophobia", "yare", "zephyr"
    ]
    random_rare_word = random.choice(rare_words)
    fulltest = ""
    word = random_rare_word
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        meaning = response.json()
        for i in meaning:
            for k, l in dict(i).items():
                if isinstance(l, list):
                    fulltest += str(k) + "\n"
                    for m in l:
                        if isinstance(m, dict):
                            for a, b in m.items():
                                fulltest += str(a) + str(b) + "\n"
                        else:
                            fulltest += str(m) + "\n"
                elif isinstance(l, dict):
                    fulltest += str(l) + "\n"
                    for x, y in l.items():
                        fulltest += str(x) + str(y) + "\n"
                else:
                    fulltest += str(k) + str(l) + "\n"
    else:
        fulltest = "No meaning found."
    match = re.search(r"'definition': '([^']*)'", fulltest)
    if match:
        definition = match.group(1)
    else:
        definition=None
    return  word, definition
