# Sumar
def sum(a: int, b: int):
    return a + b

def test_sum():
    results = sum(1, 2)
    compare = 3

    # Asercion -> Evual un valor
    assert compare == results

