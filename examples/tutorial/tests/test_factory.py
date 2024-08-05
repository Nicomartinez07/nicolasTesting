from flaskr import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    response = client.get("/hello")
    #HAY Q HACER DECODE PARA USAR CARACTERES Q NO ESTAN PERMITIDOS
    
    #decode() bytes --> string
    #encode() string --> bytes

    #b'hola mundo' hace que se convierta en bytes aunque se muestre en texto
    assert response.data.decode() == "¡Hola Mundo!"
