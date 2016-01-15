from StringIO import StringIO
from operator import attrgetter
from .datastore import find_record
from server.common import safe_attrgetter
from. health_mixin import ExportXMLMixin
import server.fhir as supermod
import sys

try:
    from flask import current_app, url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False

class Organization_Map:

    root_search = []
    resource_search_params={ '_id': 'token',
                            '_language': None,
                            'active': None,
                            'identifier': 'token',
                            'name': 'string',
                            'partof': None,
                            'phonetic': None,
                            'type': None}
    model_mapping = {
            'gnuhealth.institution':
                {
                    'name': 'name.name',
                    'identifier': 'code',
                    'type': 'institution_type',
                    'address': 'name.addresses',
                    'contacts': 'name.contact_mechanisms'
                    }
                }
    search_mapping={
            '_id': ['id'],
            'identifier': ['code'],
            'name': ['name.name']}
            #'type': ['institution_type']
            #}

class health_Organization(supermod.Organization, Organization_Map, ExportXMLMixin):
    """This subclass provides the glue between the schema generated bindings
    and GNU Health models. The Organization resource is robust, including
    healthcare providers, insurance companies, departments, etc. Currently,
    only GNU Health instutitions (gnuhealth.institution model) are supported.
    In the future, it is unclear whether there will be a need for other types 
    of organizations, but possibly units in the institution.
    """

    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_Organization, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_organization(rec)

    def set_gnu_organization(self, organization):
        """Set the organization

        Keyword arguments:
        organization - organization (Health class)
        """

        self.organization = organization
        self.model_type = self.organization.__name__

        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        self.map_ = self.model_mapping[self.model_type]

        self.__import_from_gnu_organization()
        self.__set_feed_info()

    def __import_from_gnu_organization(self):
        if self.organization:
            self.set_name(safe_attrgetter(self.organization,
                self.map_['name']))
            self.set_identifier(safe_attrgetter(self.organization,
                self.map_['identifier']))

            # Need selection text, not value
            t = self.map_['type']
            v = safe_attrgetter(self.organization, t)
            d = dict(self.organization.fields_get(t)[t]['selection'])
            self.set_type(d.get(v))

            self.set_address(safe_attrgetter(self.organization,
                self.map_['address'], default=[]))
            self.set_telecom(safe_attrgetter(self.organization,
                self.map_['contacts']))
            self.set_active(True)

    def __set_feed_info(self):
        """Set the feed-relevant data"""
        if self.organization:
            if RUN_FLASK:
                uri = url_for('org_record', log_id=self.organization.id,
                        _external=True)
            else:
                uri = dumb_url_generate(['Organization', self.organization.id])
            self.feed={'id': uri,
                'published': self.organization.create_date,
                'updated': self.organization.write_date or \
                        self.organization.create_date,
                'title': self.organization.name.rec_name
                        }

    def set_type(self, type_):
        """Extend superclass

        Set the institution's type

        Keyword arguments:
        type_ - type description
        """

        # TODO Use FHIR codes
        g=supermod.CodeableConcept()
        coding = supermod.Coding(
                system=supermod.uri(value='http://hl7.org/fhir/organization-type'),
                code=supermod.code(value='prov'),
                display=supermod.string(value='Healthcare Provider'))
        if type_:
            g.text = supermod.string(value=str(type_))
        g.coding = [coding]
        super(health_Organization, self).set_type(g)

    def set_identifier(self, identifier):
        """Extend superclass

        Set the institution's identifier

        Keyword arguments:
        identifier - institution code
        """

        if identifier is not None:
            ident = supermod.Identifier(
                        use=supermod.IdentifierUse(value='official'),
                        label=supermod.string(value='Institution code'),
                        value=supermod.string(value=str(identifier)))
            super(health_Organization, self).set_identifier([ident])

    def set_address(self, addresses):
        """Extend superclass

        Set the institution's address

        Keyword arguments:
        addresses - address models (party.address)
        """

        ads=[]
        for address in addresses:
            ad=supermod.Address()
            ad.set_use(supermod.string(value='work'))
            line=[]
            street, zip_, city, state, country = safe_attrgetter(
                                    address,
                                    'street',
                                    'zip',
                                    'city',
                                    'subdivision.name',
                                    'country.name')

            # Deal with number in field maybe never
            #if number:
                #line.append(str(number))
            if street:
                line.append(street)
            if line:
                ad.add_line(supermod.string(value=' '.join(line)))

            if city:
                ad.set_city(supermod.string(value=city))

            if state:
                ad.set_state(supermod.string(value=state))

            if zip_:
                ad.set_zip(supermod.string(value=zip_))

            if country:
                ad.set_country(supermod.string(value=country))

            ads.append(ad)

        super(health_Organization, self).set_address(ads)

    def set_telecom(self, contacts):
        """Extends superclass for convenience

        Set telecom information

        Keyword arguments:
        contacts -- contacts info (Party model)
        """

        telecom = []
        for contact in contacts:
            c=supermod.Contact()
            c.value = supermod.string(value=contact.value)
            if contact.type == 'phone':
                system='phone'
                use='work'
            else:
                use = system = contact.type
            c.system=supermod.ContactSystem(value=system)
            c.use=supermod.ContactUse(value=use)
            telecom.append(c)

        if telecom:
            super(health_Organization, self).set_telecom(telecom)

    def set_name(self, name):
        """Extend superclass

        Set the Organization's name

        Keyword arguments:
        name - organization name
        """

        if name:
            super(health_Organization, self).set_name(supermod.string(value=str(name)))

    def set_active(self, active=True):
        """Extend superclass

        Set the active status

        Keyword arguments:
        active - active status (boolean)
        """

        if active in [True, 'true']:
            d = supermod.boolean(value='true')
        else:
            d = supermod.boolean(value='false')
        super(health_Organization, self).set_active(d)

supermod.Organization.subclass = health_Organization
