#!/bin/python

import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--assault", action="store_true",
        help="Only choose an assault legend")
parser.add_argument("--support", action="store_true",
        help="Only choose a support legend")
parser.add_argument("--defense", action="store_true",
        help="Only choose a defense legend")
parser.add_argument("--recon", action="store_true",
        help="Only choose a recon legend")
parser.add_argument("--movement", action="store_true",
        help="Only choose a movement legend")
args = parser.parse_args()

legends = [
        'Bloodhound',
        'Gibraltar',
        'LifeLine',
        'Pathfinder',
        'Wraith',
        'Bangalore',
        'Caustic',
        'Mirage',
        'Octane',
        'Wattson',
        'Crypto',
        'Revenant',
        'Loba',
        'Rampart',
        'Horizon',
        'Fuse',
        'Valkyrie',
        'Seer',
        'Ash'
]

assault = [
        "Wraith",
        "Bangalore",
        "Mirage",
        "Octane",
        "Revenant"
        "Horizon",
        "Fuse",
        "Ash"
]

support = [
        "Lifeline",
        "Loba"
]

defense = [
        "Gibraltar",
        "Caustic",
        "Wattson",
        "Rampart"
]

recon = [
        "Bloodhound",
        "Pathfinder",
        "Crypto",
        "Valkyrie",
        "Seer"
]

movement = [
        "Pathfinder",
        "Octane",
        "Loba",
        "Horizon",
        "Valkyrie",
        "Ash"
]


if args.assault:
    print("Assault: ", assault[np.random.randint(len(assault)-1)])
elif args.support:
    print("Support: ", support[np.random.randint(len(support)-1)])
elif args.defense:
    print("Defensive: ", defense[np.random.randint(len(defense)-1)])
elif args.recon:
    print("Recon: ", recon[np.random.randint(len(recon)-1)])
elif args.movement:
    print("Movement: ", movement[np.random.randint(len(recon)-1)])
else:
    print("Random Legend: ",legends[np.random.randint(len(legends)-1)])
