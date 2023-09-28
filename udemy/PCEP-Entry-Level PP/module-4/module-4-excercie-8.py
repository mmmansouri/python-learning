connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]

counter = 0
average = 0
for connection in connections:
    if connection[1] == 'Rome':
        counter += 1
        average += connection[2]

print(counter, 'connections lead to Rome with an average flight time of', average / counter)
