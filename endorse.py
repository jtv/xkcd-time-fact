#! /usr/bin/env python
"""Spit out a XKDC endorsement quote.

Based on: https://xkcd.com/1942/
"""

from __future__ import unicode_literals

from argparse import ArgumentParser
from random import choice


QUOTES = (
    "I disagree strongly with whatever work this quote is attached to.",

    "This quote was taken out of context.",

    "This quote is often falsely attributed to Mark Twain.",

    "I'm being quoted to introduce something, but I have no idea what it is "
    "and certainly don't endorse it.",

    "This quote is very memorable.",

    "I wrote this book, and the person quoting me here is taking credit "
    "for it.",

    "\"This entire thing is the quote, not just the part in quote marks.\"  "
    "[Quote marks, brackets, and editor's note are all in the original. "
    "--ed.]",

    "Websites that collect quotes are full of mistakes and never check "
    "original sources.",

    "This quote will be the only part of the presentation you remember.",

    "Oooh, look at me, I looked up a quote!",

    "If you're doing a text search in this document for the word 'butts,' "
    "the good news is that it's here, but the bad news is that it only "
    "appears in this unrelated quote.",

    "Wait, what if these quote marks are inside out, so everything in the "
    "rest of the document is the quotation and this part isn't?  "
    "Duuuuude.",

    "The editors of Bartlett's Familiar Quotations are a bunch of cowards "
    "who don't have the guts to print this.",

    "This quote only looks profound when it's in a script font over a "
    "sunset.",

    "I don't do a lot of public speaking, so I looked up a memorable quote "
    "to start my speech, and this is what I found.  OK, you're staring at me "
    "blankly, but this whole thing is a quote.  I know that sounds "
    "confusing, but...  You know what, never mind.",

    "Sent from my iPhone.",
    )


EXTRA_QUOTE = (
    "\"Since there's no ending quote mark, everything after this is part of "
    "my quote.",
    )


AUTHORS = ('XKCD', 'Randall Munroe')


def main(extra=False):
    if extra:
        candidates = QUOTES + EXTRA_QUOTE
    else:
        candidates = QUOTES

    quote = choice(candidates)
    signature = choice(AUTHORS)

    if quote.startswith('"'):
        # Special case: quote plays funny games with the quote marks.
        # Print it as given.
        quoted = quote
    else:
        # Quote the quote.
        quoted = '\u201c%s\u201d' % quote

    print("%s\n  \u2015 %s" % (quoted, signature))


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        '--extra', '-x', action='store_true',
        help="Consider using the quote from the cartoon's tooltip.")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(extra=args.extra)
