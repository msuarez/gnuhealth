def find_record(model, query):
    '''Find a record and return it, or None'''
    try:
        return model.search(query, limit=1)[0]
    except:
        return None

def dumb_url_generate(args):
    """Generate url route with arguments

    params:
        args should be list
    returs:
        string (e.g., /Patient/test-3)
    """
    return ''.join(['/{0}/'.format(args[0]), '-'.join(map(str, args[1:]))])
