isl_team = [
    {"team": "mumbaicity", "mp": 50, "won": 10, "drwan": 3, "loss": 2, "gf": 22, "ga": 8, "gd": 14, "pts": 33},
    {"team": "hyderabad", "mp": 46, "won": 11, "drwan": 5, "loss": 1, "gf": 20, "ga": 7, "gd": 10, "pts": 30},
    {"team": "goa", "mp": 40, "won": 17, "drwan": 5, "loss": 0, "gf": 25, "ga": 9, "gd": 19, "pts": 38},
    {"team": "bengaluru", "mp": 35, "won": 18, "drwan": 4, "loss": 5, "gf": 15, "ga": 5, "gd": 12, "pts": 40},
    {"team": "odisha", "mp": 55, "won": 5, "drwan": 4, "loss": 7, "gf": 29, "ga": 5, "gd": 19, "pts": 45}
]

from functools import reduce

# find highest point

point = list(map(lambda team: team['pts'], isl_team))
print(point)
high_point = max(map(lambda team: team['pts'], isl_team))
print(high_point)

# another methode to  finding high point

point_high = reduce(lambda p1, p2: p1 if p1 > p2 else p2, list(map(lambda team: team['pts'], isl_team)))
print(point_high, )

# find highest point team name

highpoint_team = list(filter(lambda team: team['pts'] == reduce(lambda p1, p2: p1 if p1 > p2 else p2,
                                                                list(map(lambda team: team["pts"], isl_team))),
                             isl_team))
print(highpoint_team)
# find lowest point team name

lowpoint_team = list(filter(lambda team: team['pts'] == reduce(lambda p1, p2: p1 if p1 < p2 else p2,
                                                               list(map(lambda team: team["pts"], isl_team))),
                            isl_team))
print(lowpoint_team)
