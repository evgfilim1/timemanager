school_lessons = ['Физика семинар', 'Физика лекция', 'Астрономия', 'Алгебра', 'Геометрия',
                  'Математика лекция', 'Информатика', 'Химия', 'Биология', 'Русский язык',
                  'Литература', 'Английский язык', 'ОБЖ', 'История', 'Обществознание']

# 0 - phys, 1 - chem, 2 - gum
neural_types = {(0, 7): 0, (8, 9): 1, (10, 15): 2}

work_types = ['Семестровое д/з', 'Д/з', 'Подготовка к к/р', 'Подготовка к семинару',
              'Подготовка к сочинению', 'Чтение/анализ']