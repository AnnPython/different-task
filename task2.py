class Velocity:
    def __init__(self, speed):
        self.speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, _znach):

        if _znach > 1079252848.8:
            raise ValueError('быстрее скорости света')

        elif _znach <=0:
          raise ValueError('меньше нуля')
        self._speed = _znach


    @speed.deleter
    def speed(self):
        del self._znach

    def converter_miles(self):
        return 'Результат миль/час '+ str( round( self._speed /1.609,1))

    def converter_uzlov(self):
        return 'Результат морских узлов '+ str( round( self._speed *1.852,1))

t = Velocity(100)

print('Задана скорость ' + str(t.speed)+' км/ч' )
print(t.converter_miles() )
print(t.converter_uzlov() )
