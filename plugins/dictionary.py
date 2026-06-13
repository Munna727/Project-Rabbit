import requests
import re
from bs4 import BeautifulSoup
def define(word):
    fulltest = ""
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
        definition = None
    return definition

def synonym(word):
    paryay=""
    response=requests.get(f"https://www.thesaurus.com/browse/{word}")
    soup=BeautifulSoup(response.content,"html.parser")
    try:
      synonyms=soup.find("ul",class_="szYvJSVZyfoDF0zoOQi1")
      syn=synonyms.findAll("li")
    except:
        synonyms=soup.findAll("a",class_="Bf5RRqL5MiAp4gB8wAZa")
        syn=list(synonyms)

    emp=[]
    if len(syn)>3:
      for i in range(3):
         emp.append(syn[i].text)
    else:
        for i in syn:
            emp.append(i.text)
    return emp
''' if len(syn)>3:
        for k in range(3):
            paryay+=syn[k].text+","
        paryay=paryay[:-1]
        paryay+="."
        paryay=paryay.title()
        return paryay
    else:
        for i in syn:
            paryay+=i.text+","
        paryay=paryay[:-1]
        paryay+="."
        paryay=paryay.title()
        return paryay'''
def antonym(word):
    response=requests.get(f"https://www.antonym.com/antonyms/{word}")
    soup=BeautifulSoup(response.content,"html.parser")
    antonyms=soup.findAll("li",class_="chip")
    vyatirekh=list(antonyms)
    opposite=[]
    if len(vyatirekh)>3:
        for i in range(3):
            opposite.append(vyatirekh[i].text)
    else:
        for i in vyatirekh:
            opposite.append(i.text)
    return opposite
def example_sentence(word):
    response=requests.get(f"https://www.thesaurus.com/browse/{word}#example-sentences")
    soup=BeautifulSoup(response.content,"html.parser")
    parsed_sentence=soup.find("div",class_="dkA1ih27tI9o0MHLDxKt")
    sentence=parsed_sentence.text
    return sentence


    # if len(antonyms)>3:
    #     for i in range(3):
    #         vyatirekh+=antonyms[i].text+","
    #     vyatirekh=vyatirekh[:-1]
    #     vyatirekh+="."
    #     vyatirekh=vyatirekh.title()
    #     return vyatirekh
    # else:
    #     for i in antonyms:
    #         vyatirekh+=i.text+","
    #     vyatirekh=vyatirekh[:-1]
    #     vyatirekh+="."
    #     vyatirekh=vyatirekh.title()
    #     return vyatirekh
def pronunciation(word):
    from gtts import gTTS
    myobj = gTTS(text=word ,lang="en", slow=False)
    myobj.save("static/audios/demo.mp3")



