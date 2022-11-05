from connector.edsm.systemsApi import System
from connector.edsm.systemApi import Bodies

system = System()
json_system = system.getSystem("sol")
print(json_system['id'])
print(json_system['name'])


bodies = Bodies()
json = bodies.getBodies("HD 43193")
print(json['id'])

json_2 = bodies.getBodiesById(85920)
print(json_2['name'])