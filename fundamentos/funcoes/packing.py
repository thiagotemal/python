def test(**kargs):
    for item, posicao in kargs.items():
        print(f" item{item} e pos{posicao} ")

def testTupla(*args):
    for item in args:
        print(f"{item}")


if __name__ == "__main__":
    test(primeiro='primeiro',segundo='segundo', terceiro='tercero')
    testTupla('primeiro', 'segundo','tercero')