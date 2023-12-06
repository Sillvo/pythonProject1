

# Factoreal
def factorial(steps):
    f = 1
    step = 1
    while True:
        f = f * step
        step += 1
        if step > steps:
            return
        yield f


if __name__ == '__main__':
    ff=factorial(5)
    for n in ff:
        print (n)
