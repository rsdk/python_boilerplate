"""Definition of Timer
See help(codetiming) for quick instructions, and
https://pypi.org/project/codetiming/ for more details.
https://github.com/realpython/codetiming

MIT License

Copyright (c) 2019 Real Python

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Standard library imports
import math
import time
from contextlib import ContextDecorator
from dataclasses import dataclass, field
from typing import Any, Callable, ClassVar, Dict, Optional


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


@dataclass
class Timer(ContextDecorator):
    """Time your code using a class, context manager, or decorator"""

    timers: ClassVar[Dict[str, float]] = dict()
    _start_time: Optional[float] = field(default=None, init=False, repr=False)
    name: Optional[str] = None
    text: str = "Elapsed time: {:0.4f} seconds"
    logger: Optional[Callable[[str], None]] = print
    last: float = field(default=math.nan, init=False, repr=False)

    def __post_init__(self) -> None:
        """Initialization: add timer to dict of timers"""
        if self.name:
            self.timers.setdefault(self.name, 0)

    def start(self) -> None:
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        # Calculate elapsed time
        self.last = time.perf_counter() - self._start_time
        self._start_time = None

        # Report elapsed time
        if self.logger:
            self.logger(self.text.format(self.last))
        if self.name:
            self.timers[self.name] += self.last

        return self.last

    def __enter__(self) -> "Timer":
        """Start a new timer as a context manager"""
        self.start()
        return self

    def __exit__(self, *exc_info: Any) -> None:
        """Stop the context manager timer"""
        self.stop()
