import unittest
from ..app import create_app
from server.common import tryton
from trytond.transaction import Transaction
from trytond.pool import Pool

class MyTest(unittest.TestCase):

    def create_app(self):
        return create_app()

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def login(self, username, password):
        return self.client.post('/auth/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/auth/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'gnusolidario')
        assert 'signed in' in rv.data

        rv = self.logout()

        rv = self.login('adminx', 'default')
        assert 'sign in' in rv.data

    def test_endpoints_simple(self):
        resp = self.client.get('/Patient')
        assert 302 == resp.status_code
        rv = self.login('admin', 'gnusolidario')
        for ep in ['/Patient', '/DiagnosticReport', '/Observation',
                '/Procedure', '/Practitioner', '/Condition',
                '/FamilyHistory', '/Medication', '/MedicationStatement',
                '/Immunization', '/Organization']:
            resp = self.client.get(ep)
            assert 200 == resp.status_code
            assert 'feed' in resp.data
            assert 'Search results' in resp.data

            resp = self.client.post(ep, data=dict(test='atoeu'))
            assert 405 == resp.status_code

            resp = self.client.put(ep, data=dict(test='aoeu'))
            assert 405 == resp.status_code

            resp = self.client.delete(ep)
            assert 405 == resp.status_code

    def tearDown(self):
        # Remove login attempts
        database = self.app.config['TRYTON_DATABASE']
        with Transaction().start(database, 0, readonly=False) as t:
            logins=tryton.pool.get('res.user.login.attempt')
            l = logins.search([])
            logins.delete(l)
            t.cursor.commit()


if __name__=='__main__':
    unittest.main()
