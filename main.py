# Run a Function only Once in Python

sum_has_run = False


def sum(a, b):
    global sum_has_run

    if sum_has_run:
        return

    sum_has_run = True

    return a + b


print(sum(100, 100))  # 👉️ 200

print(sum(100, 100))  # 👉️ None