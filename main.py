from seven_dwarfs import Grumpy, Happy, Sleepy, Bashful, Sneezy, Dopey, Doc

x = {"a": 37, "b": 42, "c": 927}

var = "nate"
array_example = [1, 2, 3]

x = 123456789.123456789e123456789

if (
    very_long_variable_name is not None
    and very_long_variable_name.field > 0
    or very_long_variable_name.is_debug
):
    z = "hello " + "world."
else:
    world = "world.."
    a = "hello {}".format(world)
    f = rf"hello {world}"
    if this and that:
        y = "hello " "world"  # FIXME: https://github.com/psf/black/issues/26

# new feature


class Foo(object):
    def f(self):
        return 37 * -2

    def g(self, x, y=42):
        return y


def f(a: List[int]):
    return a[0] + a[1] - a[2]  # type: ignore


def very_important_function(
    template: str,
    *variables,
    file: os.PathLike,
    debug: bool = False,
):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, "w") as f:
        ...


# fmt: off
custom_formatting = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8,
]
# fmt: on
regular_formatting = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]
