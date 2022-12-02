import spacy
from spacy_sentiws import spaCySentiWS

nlp = spacy.load('de_core_news_sm')
nlp.add_pipe('sentiws', config={'sentiws_path': './'})
doc = nlp('Die Dummheit der Unterwerfung blüht in hübschen Farben.')

for token in doc:
    print(f" {token.text}, {token._.sentiws}, {token.pos_} ")