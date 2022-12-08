""" Testing package pypi packaging with a simple project
"""

import wikipedia

def ask_wikipedia_api(question, wiki_lang):
    """
    End half of ask_wikipedia, it calls the helper function get_info_wikipedia
    question: the string input to wiki api
    wiki_lang: the language for wikipedia to search in, e.g. "sv"
    """
    summary, image = get_info_wikipedia(question, wiki_lang)
    return summary, image
    
    
def get_info_wikipedia(term, wiki_lang):
    """
    term: A string as input into a wikipedia search
    """
    wikipedia.set_lang(wiki_lang)
    summary = wikipedia.summary(term, sentences=2)
    try:
        page = wikipedia.page(term)
        image = page.images[0] 
        print("[INFO]: wiki image: " + image)# pylint: disable=superfluous-parens
        return summary, image

    except IndexError as error:
        print(error)# pylint: disable=superfluous-parens

    return (summary, 
    "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")