# pylint: disable=no-member
from configparser import ConfigParser
from functools import partial, reduce
from typing import Any, Mapping

from setuptools import setup

join = partial(reduce, lambda acc, x: acc + x)
fold = partial(reduce, lambda acc, x: [*acc, x])


def extras_require() -> Mapping[str, Any]:
    config = ConfigParser(
        converters={"list": lambda x: fold(filter(None, x.split("\n")), [])}
    )

    config.read("setup.cfg")

    return {
        i: config.getlist("options.extras_require", i)  # type: ignore
        for i in config["options.extras_require"]
    }


if __name__ == "__main__":
    setup(
        extras_require={
            **extras_require(),
            "all": join(extras_require().values(), []),
        }
    )
