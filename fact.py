#! /usr/bin/env python
"""State a random, meaningless "fact" as in XKCD.

Based on: https://xkcd.com/1930/
"""

from argparse import ArgumentParser
from random import choice


def state_event():
    return choice([
        "the %s equinox" % choice(["fall", "spring"]),
        "the %s %s" % (
            choice(["winter", "summer"]),
            choice(["solstice", "olympics"]),
            ),
        "the %s %s" % (
            choice(["earliest", "latest"]),
            choice(["sunrise", "sunset"]),
            ),
        "daylight %s time" % choice(["savings", "saving"]),
        "leap %s" % choice(["day", "year"]),
        "Easter",
        "the %s moon" % choice([
            "harvest",
            "super",
            "blood",
            ]),
        "Toyota Truck Month",
        "shark week",
        ])


def state_every_year():
    return "happens %s every year" % choice([
        "earlier",
        "later",
        "at the wrong time",
        ])


def state_drifts():
    return "drifts out of sync with the %s" % choice([
        "sun",
        "moon",
        "zodiac",
        "%s calendar" % choice(["Gregorian", "Mayan", "Lunar", "iPhone"]),
        "atomic clock in Colorado",
        ])


def state_this_year():
    return "might %s this year" % choice(["not happen", "happen twice"])


def state_fact():
    return choice([
        state_every_year(),
        state_drifts(),
        state_this_year(),
        ])


def state_change():
    return "%s of the %s" % (
        choice([
            "precession",
            "libration",
            "nutation",
            "libation",
            "eccentricity",
            "obliquity",
            ]),
        choice([
            "Moon",
            "Sun",
            "Earth's axis",
            "Equator",
            "prime meridian",
            "%s Line" % choice(["International Date", "Mason-Dixon"]),
            ]),
        )


def state_reason():
    return choice([
        "timezone legislation in %s" % choice([
            "Indiana",
            "Arizona",
            "Russia",
            ]),
        "a decree by the Pope in the 1500s",
        state_change(),
        "magnetic field reversal",
        "an arbitrary decision by %s" % choice([
            "Benjamin Franklin",
            "Isaac Newton",
            "FDR",
            ])
        ])


def state_apparently():
    return choice([
        "it causes a predictable increase in car accidents",
        "that's why we have leap seconds",
        "scientists are really worried",
        "it was even more extreme during the %s" % choice([
            "Bronze Age",
            "Ice Age",
            "Cretaceous",
            "1990s",
            ]),
        "there's a proposal to fix it, but it %s" % choice([
            "will never happen",
            "actually makes things worse",
            "is stalled in Congress",
            "might be unconstitutional",
            ]),
        "it's getting worse and noone knows why",
        ])


def state_extra():
    """Add afterthought as in xkcd tooltip."""
    return "\nWhile it may seem like trivia, it %s." % choice([
        "causes huge headaches for software developers",
        "is taken advantage of by high-speed traders",
        "triggered the 2003 Northeast Blackout",
        "has to be corrected for by GPS satellites",
        "is now recognized as a major cause of World War I",
        ])


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        '--extra', '-x', action='store_true', help="Add afterthought.")
    return parser.parse_args()


def main(extra=False):
    fact = "Did you know that %s %s because of %s?  Apparently %s." % (
        state_event(),
        state_fact(),
        state_reason(),
        state_apparently(),
        )
    print(fact)
    if extra:
        print(state_extra())


if __name__ == '__main__':
    args = parse_args()
    main(extra=args.extra)
