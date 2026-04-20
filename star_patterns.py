"""Python Simple Star Printing Patterns"""


def triangle(n):
    """Prints a right-angled triangle of stars."""
    for i in range(1, n + 1):
        print('*' * i)


def inverted_triangle(n):
    """Prints an inverted right-angled triangle of stars."""
    for i in range(n, 0, -1):
        print('*' * i)


def pyramid(n):
    """Prints a centered pyramid of stars."""
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


def inverted_pyramid(n):
    """Prints an inverted centered pyramid of stars."""
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


def diamond(n):
    """Prints a diamond shape of stars."""
    pyramid(n)
    inverted_pyramid(n)


if __name__ == "__main__":
    size = 5

    print("=== Right-Angled Triangle ===")
    triangle(size)

    print("\n=== Inverted Right-Angled Triangle ===")
    inverted_triangle(size)

    print("\n=== Pyramid ===")
    pyramid(size)

    print("\n=== Inverted Pyramid ===")
    inverted_pyramid(size)

    print("\n=== Diamond ===")
    diamond(size)
