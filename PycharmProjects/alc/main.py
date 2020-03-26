import alc.object.line as myLine


def main():
    _line_1 = myLine.Line(1)

    print('Hello World!{}'.format(_line_1.id))

    _line_2 = myLine.Line(2)

    print('Hello World!{}'.format(_line_2.id))


if __name__ == '__main__':
    # execute only if run as a script
    main()
