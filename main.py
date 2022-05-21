"""
Tarea 9
Uses of Regexes
Estudent: Daniela Martínez Madrid
"""
import re
import numpy as np

# Punto1. Extraer el nombre de un archivo de una trayectoria del sistema de archivo

PATH = '/Users/user/PycharmProyects/ tarea9/ venv/Scripts/python.exe'
print(re.split('[/:]', PATH)[-1])


# Punto 2.  Escribir la función date_in_spanish. Use re.sub para sustituir los nombres
# de los meses.

def date_in_spanish(date):
    """
    Translates a string date to spanish. That is, all references to months
    abbreviations like 'Jan', 'Feb', 'Mar' and so on are changed to 'Ene',
    'Feb', 'Mar', respectively.

    :param date:
        date : str
        Date to be translated

    :return:
     str
        The translated base_date.
          Examples
    --------
    >>> date_in_spanish("23-Apr-2021")
    23-Abr-2021
    >>> date_in_spanish("Dec-24-2020")
    Dic-24-2020
    """

    aux = re.split('[-:]', date)
    if aux[1] == 'Jan':
        repl = 'Ene'
    elif aux[1] == 'Apr':
        repl = 'Abr'
    elif aux[1] == 'Aug':
        repl = 'Ago'
    elif aux[1] == 'Sep':
        repl = 'Sept'
    elif aux[1] == 'Dec':
        repl = 'Dic'
    new_string = re.sub('[a-zA-Z]{3}', repl, date)
    return new_string


print(date_in_spanish("23-Apr-2021"))

print(date_in_spanish('2021-Jan-24'))

print(date_in_spanish("23-Apr-2021"))
print(date_in_spanish('12-Sep-1991'))


# Punto 3.  Escribir la siguiente función def from_standard_equity_option_convention, descrita a continuación.


def from_standard_equity_option_convention(code: str) -> dict:
    """
       Transform a standard equity option convention code to record representation.
    :param code: str
           Standard equity option convention code (see
        https://en.wikipedia.org/wiki/Option_naming_convention).
    :return: dict
        A dictionary containing:
        'symbol': Symbol name
        'expire': Option expiration base_date
        'right': Put (P) or Call (C).
        'strike': Option strike

    Examples:
    >>> from_standard_equity_option_convention('YHOO150416C00030000')
    {'symbol': 'YHOO', 'expire': '20150416', 'right': 'C', 'strike': 30.0}
    """

    aux = re.search(r'(\w{,6})([0-9]{6})([P|C])([0-9]{5})([0-9]{3})', code)
    sym = aux[1]
    date = aux[2]
    exp = '20' + date
    right = aux[3]
    strike = aux[4] + '.' + aux[5]
    return {'symbol': sym, 'expire': exp, 'right': right, 'strike': strike}


print(from_standard_equity_option_convention('YHOO150416C00030000'))

# Punto 4. Explique con palabras qué hace la siguiente instrucción
# symbols_str = re.sub(r"'", "''", str(symbols))

symbols_str = re.sub(r"'", "''", 'sy\'mbols')  # Escribimos cadenas que contengan el símbolo (') y esté será remplazado
# por el simbolo ('')
print(symbols_str)

# Punto 5. Escriba una cadena 'account' apropiada para que se ejecute la instrucción print
# if re.match(r'DU[0-9]{7}', account):
#     print("Account: ", account)

# Punto 6. Escriba la expresión regular de manera más sintética pero preservando la funcionalidad.
# if re.match('^([0-9][0-9][0-9][0-9][0-9][0-9])$', text):
#    LOGGER.info("Correct OTP format: %s.", text)
# Otra forma más sintética:
# if re.match('(\d{6})$', text):
#    LOGGER.info("Correct OTP format: %s.", text)

# Punto 7. ¿Cuál es el valor de 'reg_exp' que hace funcionar el código siguiente?
# if re.match(reg_exp, text) is None:
#    error_message = \
#        "Try again, your answer does not correspond to a comma " + \
#        "separated integers list. Type something like '1, 2, 3' " + \
#        "without the apostrophes."

if re.search(r"'|((\d,)+(\d)$)|^,$", 'text') is None:
    error_message = \
        "Try again, your answer does not correspond to a comma " + \
        "separated integers list. Type something like '1, 2, 3' " + \
        "without the apostrophes."


# Punto 8. Programar el método siguiente.
def collect_commission_adjustment(data):
    """
    Retrieve a commision adjustment record from the section "Commission
    Adjustments" in one Interactive Brokers activity report.

    PARAMETERS
    ----------
    data : list[]
        Line from the activity report in the "Commission Adjustment" section
        in list format. That is, each element in the list is a comma
        separated item from the line.

    RETURNS
    -------
        dict
        Containing the open position information in dictionary format.

    Examples
    --------
    >>> collect_commission_adjustment(['Commission Adjustments', 'Data', 'USD',
    ... '2021-04-23',
    ... 'Commission Computed After Trade Reported (C     210430C00069000)',
    ... '-1.0906123', '\\n'])
    {'end_date': '20210423', 'symbol': 'C', 'expire': '20210430', \
'right': 'C', 'strike': 69.0, 'sectype': 'OPT', 'amount': -1.0906123}
    >>> collect_commission_adjustment(
    ... ['Commission Adjustments', 'Data', 'USD', '2021-02-19',
    ... 'Commission Computed After Trade Reported (ALB)', '-0.4097', '\\n'])
    {'end_date': '20210219', 'symbol': 'ALB', 'sectype': 'STK', \
'amount': -0.4097}
    >>> collect_commission_adjustment(
    ... ['Commission Adjustments', 'Data', 'USD', '2021-02-19',
    ... 'Commission Computed After Trade Reported (ALB)', '-0.4097', '\\n'])
    {'end_date': '20210219', 'symbol': 'ALB', 'sectype': 'STK', \
'amount': -0.4097}
    """
    aux = re.search(r'(\([A-Z]+)(.+)', data[4])
    code = re.sub("[' ')]", '', aux[2])
    if aux[2] == ')':
        dic = dict(zip(['end_date', 'symbol', 'sectype', 'amount'],
                       [re.sub('-', '', data[3]), re.sub('\(', '', aux[1]),
                        'STK', data[-2]]))
    else:
        dic = dict(zip(['end date', 'symbol', 'expire', 'right', 'strike', 'sectype', 'amount'],
                       [re.sub('-', '', data[3]), re.sub('\(', '', aux[1]),
                        from_standard_equity_option_convention(code)['expire'],
                        from_standard_equity_option_convention(code)['right'],
                        from_standard_equity_option_convention(code)['strike'],
                        'OPT', data[-2]]))
    return dic


print(collect_commission_adjustment(
    ['Commission Adjustments', 'Data', 'USD', '2021-02-19', 'Commission Computed After Trade Reported (ALB)', '-0.4097',
     '\\n']))
print(collect_commission_adjustment(['Commission Adjustments', 'Data', 'USD', '2021-04-23',
                                     'Commission Computed After Trade Reported (C     210430C00069000)', '-1.0906123',
                                     '\\n']))


# Punto 9. De dos ejemplos de uso del siguiente método. En el primero, el método debe
# regresar un número de punto flotante y en el segundo np.nan

def banxico_value(tag, data):
    """
    Get data values from Banxico portals.
    Parameters
        ----------
        tag : str
            Internal tag name of the variable to retrieve.
        data : str
            Html page to locate the tag value.

        Returns
        --------
            float
            The associated tag value.

        Examples
        --------
        >>> print(banxico_value('ejemplotag', 'fhd---5452-45end'))
        nan

        float(re.search(tag + float_nt,'ejemplotagfh5452.45end').group(1))
        5452.45
        """
    float_nt = "[^0-9-]*([-]*[0-9]+.[0-9]+)[^0-9]"
    try:
        res = float(re.search(tag + float_nt, data).group(1))
    except AttributeError:
        res = np.nan
    return res

print(banxico_value('ejemplotag', 'fhd---5452-45end')) #ejemplo return nan
print(banxico_value('ejemplotag', 'ejemplotagfh5452.45end')) #ejemplo return 5452.45

# Punto 10. Describa en palabras qué hace el siguiente código.
# col_sel = list(map(lambda s: s if re.match("[Ii][Mm][Ff][0-9]+", s) else None,
#             dat_df.columns,))


# map(lambda s: s if re.match("[Ii][Mm][Ff][0-9]+", s) else None, dat_df.columns,), esta función
# recorre cada dato s de dat_df.colmns para operarlo con la función re.match("[Ii][Mm][Ff][0-9]+", s),
# por lo que va a guardar los datos de dat_df.columns que coinciden con el patrón "[Ii][Mm][Ff][0-9]+",
# esto es, tres letras (imf, sin distinguir las masyusculas) seguido de números, en caso de no coincidir
# guardará None.
# La instrucción list, nos permite ver la lista del objeto.

data_df = ['IMF955', 'fsgsdfg', 'iMf5344846', 'IM6']
col_sel = list(map(lambda s: s if re.match("[Ii][Mm][Ff][0-9]+", s) else None, data_df))
print(col_sel)

# Para terminar se reduce la lista sin las entradas None
col_sel = [c for c in col_sel if c is not None]
print(col_sel)


## Valoración de pylint: Your code has been rated at 8.10/10 (previous run: 8.21/10, -0.11)