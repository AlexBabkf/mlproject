from mlproject.distance import haversine

def test_haversine():
    assert round(haversine(48.865, 2.380, 48.235, 2.393)) == 70