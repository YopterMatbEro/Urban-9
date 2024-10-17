def all_variants(text):
    """Генератор всех возможных вариантов текста"""
    count = 1
    while count <= len(text):
        for j in range(0, len(text) - count + 1):
            yield text[j:j + count]
        count += 1


if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)
    print()
    a = all_variants("flex")
    for i in a:
        print(i)
