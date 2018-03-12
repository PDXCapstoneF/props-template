"""Properties template processor.
Usage:
    main.py load <template> <mapping> [<output>]
    main.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.
"""

import json
import sys
from string import Template

import javaproperties
from docopt import docopt

def substitute(props, mapping, template = lambda st, m: Template(st).substitute(m)):
    """
    Returns a substituted dictionary, where
    all the values in props have been substituted
    with values in mapping.
    Template is an optional function that 
    takes a template string and mapping and 
    translates it into another string.
    """
    return { k: template(v, mapping) for k, v in props.items() }

if __name__ == "__main__":
    arguments = docopt(__doc__, version="0.1")

    try:
        props = javaproperties.load(open(arguments['<template>'], 'r'))
        mapping = json.load(open(arguments['<mapping>'], 'r'))
    except Exception as e:
        print(e)
        exit()

    substitution = substitute(props, mapping)

    output = arguments['<output>']

    if output is not None:
        with open(output, 'w') as f:
            f.write(javaproperties.dumps(substitution))
    else:
        print(substitution)
