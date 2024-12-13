class UppercaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result

@UppercaseDecorator
def test():
    return "proszę mi nie przerywać jak ja Panu przerywam!" #https://www.youtube.com/watch?v=oFNTJK51M20&ab_channel=jachcy%F0%9F%87%B5%F0%9F%87%B1

# Sprawdzenie
print(test())
