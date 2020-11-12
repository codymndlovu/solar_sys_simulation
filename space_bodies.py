class CelestialBody:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def show(self):
        fill(255)
        ellipse(0, 0, self.radius, self.radius)
        
class Planet(CelestialBody):
    def __init__(self, radius, mass, distance):
        CelestialBody.__init__(self, radius, mass)
        self.distance = distance
    
    def move(self):
        # get the force generated by the sun to attract different planets
        # get the acceleration, ie velocity to get the planet into orbit( zero the force from the sun )
        
        
class NSatellite(CelestialBody):
    pass