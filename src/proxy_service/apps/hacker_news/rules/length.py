from __future__ import annotations

import re
import string

from .common import Rule, logger

WORD_LENGTH = 6
PATTERN = "(^| )([a-zA-Z-]{%s})([\n $%s])" % (WORD_LENGTH, string.punctuation)


def length_condition() -> re.Pattern:
    return re.compile(PATTERN)


def length_condition_action(string: str) -> str:
    def _replace(match_object: re.Match) -> str:
        return "{prefix}{value}™{suffix}".format(
            prefix=match_object.group(1), value=match_object.group(2), suffix=match_object.group(3)
        )

    result = re.sub(PATTERN, _replace, string)
    logger.debug('String "%s" replaced with "%s"', string, result)
    return result


length_rule = Rule(
    condition=length_condition,
    action=length_condition_action,
)
