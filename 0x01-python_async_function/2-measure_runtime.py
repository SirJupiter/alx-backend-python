#!/usr/bin/env python3
"""Measuring runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    Function should return a float.

    Args:
        n (int): number of times wait_random will be spawned
        max_delay (int): specified delay

    Returns:
        float: total_time / n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
