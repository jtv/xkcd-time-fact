#! /usr/bin/env python3
"""Star Wars Spointer Generator.

Implements https://xkcd.com/2243/
"""

from random import choice


def pick_villain():
    return choice([
        "Kyle Ren",
        "Malloc",
        "Darth Sebelius",
        "Theranos",
        "Lord Juul",
    ])


def pick_friend():
    return choice([
        "Kim Spacemeasurer",
        "Teen Yoda",
        "Dab Tweetdeck",
        "Yaz Progestin",
        "TI-83",
    ])


def pick_lightsaber():
    return choice([
        "beige",
        "ochre",
        "mauve",
        "aquamarine",
        "taupe",
    ])


def pick_superweapon():
    return choice([
        "Sun Obliterator",
        "Moonsquisher",
        "World Eater",
        "Planet Zester",
        "Superconducting Supercollider",
    ])


def pick_capability():
    return choice([
        (
            "blowing up a planet with a bunch of beams of energy that "
            "combine into one"
        ),
        (
            "blowing up a bunch of planets with one beam of energy that "
            "splits into many"
        ),
        (
            "cutting a planet in half and smashing the halves together "
            "like two cymbals"
        ),
        (
# XXX: Subscript "2"!
            "increasing the CO2 levels in a planet's atmosphere, causing "
            "rapid heating"
        ),
        "triggering the end credits before the movie is done",
    ])


def pick_enemy():
    return choice([
        "Boba Fett",
        "Salacious Crumb",
        "the Space Slug",
        "the bottom half of Darth Maul",
        "YouTube commenters",
    ])


def pick_battle():
    return choice([
        "a bow that shoots little lightsaber-headed arrows",
        (
            "X-Wings and TIE fighters dodging the giant letters of the "
            "opening crawl"
        ),
        (
            "a Sith educational display that uses Force lightning to "
            "demonstrate the dielectric breakdown of air"
        ),
        "Kylo Ren putting on another helmet over his smaller one",
        (
            "a Sith car wash where the bristles on the brushes are little "
            "light sabers"
        ),
    ])


def pick_parent1():
    return choice([
        "Luke",
        "Leia",
        "Han",
        "Obi-Wan",
        "a random junk trader",
    ])


def pick_parent2():
    return choice([
        "Poe",
        "BB-8",
        "Amilyn Holdo",
        "Laura Dern",
        "a random junk trader",
        "that one droid from the Jawa sandcrawler that says 'gonk'",
    ])


def spoil():
    return " ".join([
        "In this Star Wars movie, our heroes return to take on the",
        "First Order and new villain %s" % pick_villain(),
        "with help from their new friend %s." % pick_friend(),
        "Rey builds a new lightsaber with a %s blade," % pick_lightsaber(),
        "and they head out to confront the First Order's new superweapon,",
        "the %s," % pick_superweapon(),
        "a space station capable of %s." % pick_capability(),
        "They unexpectedly join forces with their old enemy %s" % pick_enemy(),
        "and destroy the superweapon in a battle featuring %s." % pick_battle(),
        "\n\nP.S.",
        "Rey's parents are %s and %s." % (pick_parent1(), pick_parent2()),
    ])

if __name__ == '__main__':
    print(spoil())
