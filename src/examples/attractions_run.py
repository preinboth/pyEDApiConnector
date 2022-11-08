from src.connector.eddb.attractions import Attractions

attraction = Attractions()
json = attraction.get_attractions_by_name("Klimt Park")
