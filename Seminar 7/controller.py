import view
import model
import logging

# logging.basicConfig(level=logging.INFO)
# Если хотим вести логи в терминале

logging.basicConfig(filename='log.txt',
filemode='a',
format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
datefmt='%H:%M:%S',
level=logging.INFO)
# level=logging.INFO, encoding='utf 8') # Если хотим чтобы всегда корректно отображался русский язык
# Если хотим вести логи в отдельном файле

def main_funcion():
    try:
        select = view.greeting()
        if select == 1:
            logging.info('Выбран режим калькулятор.')
            primer = view.get_math_example()
            result = model.calc(primer)
            view.view_result(result)
            logging.info('Результаты выведены.')
        elif select == 2:
            logging.info('Выбран режим конвертера.')
            massa = view.get_massa()
            logging.info(f'Введено значение {massa}')
            value = model.converter(massa)
            view.view_result(value)
            logging.info('Результаты выведены.')
    except Exception as err:
        logging.warning(f'Введено некорректное значение.{err}')
