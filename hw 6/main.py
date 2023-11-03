result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більшим за b")
        if b > 100:
            raise IndexError("b має бути меншим або рівним 100")
        return a / b
    except ValueError as ve:
        print(f"Помилка ValueError: {ve}")
        return None
    except IndexError as ie:
        print(f"Помилка IndexError: {ie}")
        return None
    except Exception as e:
        print(f"Інша помилка: {type(e).__name__}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)
