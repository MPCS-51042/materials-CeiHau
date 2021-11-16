from collections import namedtuple

Observation = namedtuple("Observation", "color location_seen")


class BirdWatchingSession():
    def __init__(self):
        self.birds_seen = 0
        self.classifications = []

    def record(self, *observations):
        self.classifications += [self.classify(observation.color, observation.location_seen) for observation in
                                 observations]  # Where I made the change

        self.birds_seen = self.birds_seen + len(observations) #Where I maded

    def classify(self, color, location_seen):
        # It's a peninsula bird if it was seen on Solidarity Drive
        peninsula_bird = (location_seen == "Solidarity Drive")  # Where I made the change

        if peninsula_bird:
            if color == "black":
                return "Red-Shouldered Blackbird"
            if color == "red":
                return "Serrano (Field Museum's Scarlet Maccaw)"
            if color == "green":
                return "Pablo (Field Museum's Greenwing Maccaw)"
            if color == "grey":
                return "Seagull"
        else:
            if color == "brown":
                return "juvenile Bald Eagle"
            if color == "grey":
                return "Eastern Heron"
            if color == "black":
                return "Raven"


session = BirdWatchingSession()
session.record(Observation('black', 'Solidarity Drive'))
session.record(Observation('black', 'Clark Park'))
session.record(Observation('grey', 'Solidarity Drive'))

session.record(Observation('red', 'Solidarity Drive'))
session.record(Observation('brown', 'Starved Rock State Park'))
session.record(Observation('grey', 'Chicago River'))

print(session.classifications)
types = [type(item) for item in session.classifications]
print(types)
print(set(types))
