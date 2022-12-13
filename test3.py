# полная структура механизма обработки except

#
try:  # сюда помещаем потенциально опасный код
    pass
except NameError:  # обработчик
    pass
except Exception:
    pass
except BaseException:
    pass
else:  # выполняется если exception не произошел
    pass
finally:  # выполняется всегда
    pass

# генерация вручную
raise Exception
raise Exception("iquyewf")  # с данными

#
while True:
    pass
else:
    pass

#
for i in []:
    pass
else:
    pass
