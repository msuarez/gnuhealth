def find_record(model, query):
    '''Find a record and return it, or None'''
    try:
        return model.search(query, limit=1)[0]
    except:
        return None

