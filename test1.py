# stack trace / traceback

def third():
    # print("hello!!!")
    try:
        print('begin third')
        n = int(input())
        if n == 1:
            5 / 0
        elif n == 2:
            int('ewrter')  # ValueError
        else:
            a + b  # NameError
        print("hello")

    # существует BaseExpection

    # 4 шаг - универсальный обработчик
    # except:
    #     print("exception was handled...:")

    # 3 шаг -добавили as
    except (ZeroDivisionError, ValueError, NameError) as exc:
        print("exception was handled...:")
        print(exc)  # посмотреть тип
        print(repr(exc))  # посмотреть техническую информацию
        print(exc.args)  # посмотреть аргументы -  это tuple

    # 2 шаг - expect объединили в tuple
    # except (ZeroDivisionError, ValueError, NameError) :
    #     print("exception was handled...")

    # 1 шаг - except ZeroDivisionError:
    #     print("exception ZeroDivisionError was handled...")
    # except ValueError:
    #     print("exception ZeroDivisionError was handled...")
    # except NameError:
    #     print("exception NameError was handled...")

    print("end third")


def second():
    print("begin second")
    third()
    print("end second")


def first():
    print("begin first")
    second()
    print("end first")


def main():
    print("begin main")
    first()
    print("end main")


main()
