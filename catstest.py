from cats import Cat

cat1 = Cat("Сэм", "мальчик", 2)
cat2 = Cat("Барон", "мальчик", 2)

cat_list = [cat1, cat2]

for cat in cat_list:
    cat.get_list()