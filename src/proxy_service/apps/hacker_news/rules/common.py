import logging
import re
from collections.abc import Callable

import attrs

logger = logging.getLogger(__name__)


@attrs.define(kw_only=True)
class Rule:
    condition: Callable[..., re.Pattern]
    action: Callable[[str], str]
