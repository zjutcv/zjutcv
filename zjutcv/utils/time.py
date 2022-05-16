# Copyright (c) ZJUTCV. All rights reserved.
from datetime import datetime

import pytz


def print_time(time_zone='hongkong'):
    """
    Return current time in different time_zone
    Args:
        time_zone: The time zone.

    Returns:
        format_time (str): Formatted time string.

    """
    try:
        current_time = datetime.now(pytz.timezone(time_zone))
    except pytz.exceptions.UnknownTimeZoneError:
        raise TypeError(
            f'Timezone {time_zone} is not in {pytz.all_timezones_set}')

    format_time = current_time.strftime('%a %d %b %Y %H:%M:%S %Z %z')

    return format_time
