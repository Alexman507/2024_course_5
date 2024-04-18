from src import hh, dbmanager, config


def main():
    employer_ids = [  # Выбранные работодатели
        2365329,    # 1 UpTrader
        2061860,    # 2 ООО Фандог
        2539590,    # 3 ООО DM365
        77364,      # 4 Petrovich
        1795976,    # 5 ITMO
        856498,     # 6 LESTA GAMES
        10938683,   # 7 Yakov Lushkov Neuro-Agency
        10069618,   # 8 ООО Редеп Эдженси
        5817234,    # 9 ООО Оператор Газпром ИД
        10955120,   # 10 СДД
        5686111,    # 11 Olima
        4295296,    # 12 SoftWise
        2261,       # 13 Балтика
        581224,     # 14 Монополия
        53676,      # 15 ОБИТ
        773781,     # 16 DATADVANCE

            ]
    db_params = config.config()
    api = api_hh.HH()
    employers = api.get_employers(employer_ids=employer_ids)
    vacancies = api.get_vacancies()
    api.create_db(db_params)
    api.save_to_db()


if __name__ == '__main__':
    main()
