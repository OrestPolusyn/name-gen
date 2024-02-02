import requests

NAMELIX_URL = 'https://namelix.com/app/load2.php'

def get_names(keywords, styles='brandable', lengths='short', **kwargs):
    """
    Get the generated names from namelix.com.

    Options for styles: multiword, brandable, language, wordmix, spelling, dictionary, rhyme, person
    Options for lengths: short, medium, long
    """
    data = kwargs.copy()

    # Pass in keywords into data dictionary
    data['keywords'] = ' '.join(keywords) if isinstance(keywords, list) else keywords
    
    # Pass in chosen style into data dictionary
    data['styles[]'] = styles
    
    # Pass in chosen length into data dictionary
    data['lengths[]'] = lengths

    # Post request to namelix.com
    resp = requests.post(NAMELIX_URL, data=data)

    # For item in resp, yield from generator
    # for item in resp.json():
    #     yield item.get('title')
    ret = []
    for item in resp.json():
        ret.append(item.get('title'))

    return ret