"""Generate JSON type hierarchy from LDC AIDA Annotation Ontology"""


import json
from collections import defaultdict


data = """FAC	Building	n/a
FAC	Building	ApartmentBuilding
FAC	Building	GovernmentBuilding
FAC	Building	House
FAC	Building	OfficeBuilding
FAC	Building	School
FAC	Building	StoreShop
FAC	Building	VotingFacility
FAC	GeographicalArea	n/a
FAC	GeographicalArea	Border
FAC	GeographicalArea	Checkpoint
FAC	Installation	n/a
FAC	Installation	Airport
FAC	Installation	MilitaryInstallation
FAC	Installation	TrainStation
FAC	Structure	n/a
FAC	Structure	Barricade
FAC	Structure	Bridge
FAC	Structure	Plaza
FAC	Structure	Tower
FAC	Way	n/a
FAC	Way	Highway
FAC	Way	Street
LOC	GeographicPoint	n/a
LOC	GeographicPoint	Address
LOC	Land	n/a
LOC	Land	Continent
LOC	Position	n/a
LOC	Position	AirSpace
LOC	Position	CrimeScene
LOC	Position	Field
LOC	Position	Neighborhood
LOC	Position	Region
ORG	Association	n/a
ORG	Association	Club
ORG	Association	Team
ORG	CommercialOrganization	n/a
ORG	CommercialOrganization	BroadcastingCompany
ORG	CommercialOrganization	Corporation
ORG	CommercialOrganization	Manufacturer
ORG	CommercialOrganization	NewsAgency
ORG	CriminalOrganization	CriminalOrganization
ORG	Government	n/a
ORG	Government	Agency
ORG	Government	Council
ORG	Government	FireDepartment
ORG	Government	LawEnforcementAgency
ORG	Government	LegislativeBody
ORG	Government	ProsecutorOffice
ORG	Government	Railway
ORG	International	n/a
ORG	International	Commission
ORG	International	MonitoringGroup
ORG	MilitaryOrganization	n/a
ORG	MilitaryOrganization	GovernmentArmedForces
ORG	MilitaryOrganization	Intelligence
ORG	MilitaryOrganization	NonGovernmentMilitia
ORG	PoliticalOrganization	n/a
ORG	PoliticalOrganization	Court
ORG	PoliticalOrganization	Party
PER	Combatant	n/a
PER	Combatant	Mercenary
PER	Combatant	Sniper
PER	Fan	n/a
PER	Fan	SportsFan
PER	MilitaryPersonnel	n/a
PER	MilitaryPersonnel	MilitaryOfficer
PER	Police	n/a
PER	Police	ChiefOfPolice
PER	Politician	n/a
PER	Politician	Governor
PER	Politician	HeadOfGovernment
PER	Politician	Mayor
PER	ProfessionalPosition	n/a
PER	ProfessionalPosition	Ambassador
PER	ProfessionalPosition	Firefighter
PER	ProfessionalPosition	Journalist
PER	ProfessionalPosition	Minister
PER	ProfessionalPosition	Paramedic
PER	ProfessionalPosition	Scientist
PER	ProfessionalPosition	Spokesperson
PER	ProfessionalPosition	Spy
PER	Protester	n/a
PER	Protester	ProtestLeader
VEH	Aircraft	n/a
VEH	Aircraft	Airplane
VEH	Aircraft	CargoAircraft
VEH	Aircraft	Helicopter
VEH	MilitaryVehicle	n/a
VEH	MilitaryVehicle	FighterAircraft
VEH	MilitaryVehicle	MilitaryBoat
VEH	MilitaryVehicle	MilitaryTransportAircraft
VEH	MilitaryVehicle	Tank
VEH	Rocket	Rocket
VEH	Watercraft	n/a
VEH	Watercraft	Boat
VEH	Watercraft	Yacht
VEH	WheeledVehicle	n/a
VEH	WheeledVehicle	Bus
VEH	WheeledVehicle	Car
VEH	WheeledVehicle	FireApparatus
VEH	WheeledVehicle	Train
VEH	WheeledVehicle	Truck
GPE	Country	Country
GPE	OrganizationOfCountries	OrganizationOfCountries
GPE	ProvinceState	ProvinceState
GPE	UrbanArea	n/a
GPE	UrbanArea	City
GPE	UrbanArea	Village
WEA	Bomb	n/a
WEA	Bomb	Grenade
WEA	Bomb	MolotovCocktail
WEA	Bullets	n/a
WEA	Bullets	Ammunition
WEA	Bullets	LiveRounds
WEA	Bullets	RubberBullets
WEA	Cannon	Cannon
WEA	Club	n/a
WEA	Club	Bat
WEA	DaggerKnifeSword	n/a
WEA	DaggerKnifeSword	Hatchet
WEA	Gas	n/a
WEA	Gas	PoisonGas
WEA	Gas	TearGas
WEA	GrenadeLauncher	GrenadeLauncher
WEA	Gun	n/a
WEA	Gun	Artillery
WEA	Gun	Firearm
WEA	MissileSystem	n/a
WEA	MissileSystem	AirToAirMissile
WEA	MissileSystem	AntiAircraftMissle
WEA	MissileSystem	MissileLauncher
WEA	MissileSystem	Missile
WEA	MissileSystem	SurfaceToAirMissile
WEA	ThrownProjectile	n/a
WEA	ThrownProjectile	Rock"""


# if __name__ == '__main__':
#     types = defaultdict(set)
#     for line in data.split('\n'):
#         t, st, sst = line.rstrip('\n').lower().split('\t')
#         if st != 'n/a':
#             types[t].add(st)
#             types[st]
#             if sst != 'n/a' and st != sst:
#                 types[st].add(sst)
#                 types[sst]
#     for i in types:
#         types[i] = list(types[i])

#     output_path = 'type_hierarchy.json'
#     with open(output_path, 'w') as fw:
#         json.dump(types, fw, indent=4)


if __name__ == '__main__':
    types = defaultdict(set)
    for line in data.split('\n'):
        t, st, sst = line.rstrip('\n').lower().split('\t')
        if st != 'n/a':
            t_st = '%s.%s/NAM' % (t, st)
            types['%s/NAM' % t].add(t_st)
            types[t_st]
            if sst != 'n/a':
                t_st_sst = '%s.%s.%s/NAM' % (t, st, sst)
                types[t_st].add(t_st_sst)
                types[t_st_sst]
    for i in types:
        types[i] = list(types[i])

    output_path = 'type_hierarchy.json'
    with open(output_path, 'w') as fw:
        json.dump(types, fw, indent=4)
