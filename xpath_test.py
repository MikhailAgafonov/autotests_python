# Где смотрим
http://suninjuly.github.io/cats.html

# Для класса row ищем 2 элемент
//div[@class="row"]/div[2]

# Ищем атрибут img с id = bullet
//img[@id='bullet']

# Поиск по полному совпадению текста
# <p> с аттрибутом text = Lenin cat
//p[text()="Lenin cat"]

# Поиск по неполному совпадению текста
# <p> с аттрибутом text включающим в себя слово cat
//p[contains(text(), "cat")]

# Простые булевы операции (and, or, not)
//img[@name='bullet-cat' and @data-type='animal']

# * - включает все элементы
//div/*[@class="jumbotron-heading"]

# Запросы регистро-зависимые. При такой попытке мы ничего не найдем
//div/*[@class="Jumbotron-heading"]
