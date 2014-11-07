from werkzeug.routing import BaseConverter, ValidationError

def get_address(string):
    '''Given string, retrieve full address, easily parsed'''
    import requests
    ENDPOINT_URL='https://open.mapquestapi.com/nominatim/v1/search'
    resp = requests.get(ENDPOINT_URL, params={'q':str(string),
                                            'format': 'json',
                                            'addressdetails': 1,
                                            'limit': 1})
    details = resp.json()
    if details:
        ad = details[0].get('address', {})
        try:
            ad['lat']=float(details[0].get('lat'))
        except:
            pass
        try:
            ad['lon']=float(details[0].get('lon'))
        except:
            pass
        try:
            ad['house_number']=int(ad['house_number'])
        except:
            pass

        return ad

class recordConverter(BaseConverter):
    '''Handle Model-ID-Field endpoint values'''
    def to_python(self, value):
        tmp = [None, None, None]
        for k,v in enumerate(value.split('-')):
            if k == 3: raise ValidationError()
            tmp[k]=v
        try:
            tmp[1]=int(tmp[1])
        except:
            raise ValidationError()
        return tmp

    def to_url(self, values):
        return '-'.join([BaseConverter.to_url(value) for value in values if value is not None])

