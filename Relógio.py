class NumberDisplay:
    def __init__(self, limite):
        self.__limit = limite
        self.__value = 0

    def increment(self):
        self.__value = (self.__value + 1) % self.__limit

    def getDisplayValue(self):
        if self.__value < 10:
            return "0" + str(self.__value)
        else:
            return str(self.__value)

    def getValue(self):
        return self.__value

    def setValue(self, replacementValue):
        self.__value = replacementValue


class ClockDisplay:
    def __init__(self):
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)
        self.__seconds = NumberDisplay(60)
        self.__updateDisplay()

    def getDisplayValue(self):
        return self.__displayString

    def timeTick(self):
        self.__seconds.increment()
        if self.__seconds.getValue() == 0:
            self.__minutes.increment()
            if self.__minutes.getValue() == 0:
                self.__hours.increment()
        self.__updateDisplay()

    def __updateDisplay(self):
        self.__displayString = (self.__hours.getDisplayValue() + ":" + self.__minutes.getDisplayValue() + ":" + self.__seconds.getDisplayValue() )

    def getTime(self):
        return self.__displayString

    def setTime(self, hora, minuto, segundo):
        self.__hours.setValue(hora)
        self.__minutes.setValue(minuto)
        self.__seconds.setValue(segundo)
        self.__updateDisplay()


def main():
    horario = ClockDisplay()
    print(horario.getTime())
    horario.timeTick()
    print(horario.getTime())
    horario.setTime(16, 30, 40)
    print(horario.getTime())

if __name__ == "__main__":
    main()