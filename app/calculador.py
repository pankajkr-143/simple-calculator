# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

class Calculador(object):
    
    def calculation(self, calc):
        
        return self.__calculation_validation(calc=calc)

    def __calculation_validation(self, calc):

        try:
            result = eval(calc)

            return self.__format_result(result=result)
        except (NameError, ZeroDivisionError, SyntaxError, ValueError):
            return 'Erro' 

    def __format_result(self, result):


        result = str(result)
        if len(result) > 15:
            result = '{:5.5E}'.format(float(result))
            
        return result
