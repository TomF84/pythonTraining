from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Central Corridor", rv.data)
    
    rv = web.get('/game', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Central Corridor", rv.data)
    
    data = {'value': 'Laser Weapon Armory'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b"Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr", rv.data)
    
if __name__ == "__main__":
    app.run()