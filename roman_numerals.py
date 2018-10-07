def convert(data):
    result = ""

    while data > 1000:
        result += "M"
        data -= 1000

    if data % 500 == 0:
        if data == 1000:
            return "M"
        else:
            result += "D"
            return result

    # number now below 1000

    if data % 100 == 0:
        if data == 900:
            result += "CM"
            return result
        elif data > 500:
            result += "D"
            data -= 500
            while data > 0:
                result += "C"
                data -= 100
        else:
            if data >= 400:
                result += "CD"
                return result
            while data > 0:
                result += "C"
                data -= 100

    if data >= 900:
        result += "CM"
        data -= 900
    else:
        if data >= 500:
            if data == 500:
                result += "D"
                return result
            else:
                result += "D"
                while data > 600:
                    result += "C"
                    data -= 100
                data -= 500

    if data < 500:
        if data > 400:
            result += "CD"
            data -= 400
        else:
            while data > 100:
                result += "C"
                data -= 100

    #number is now below 100

    if data % 10 == 0:
        if data == 90:
            result += "XC"
            return result
        elif data > 50:
            result += "L"
            data -= 50
            while data > 0:
                result += "X"
                data -= 10
            return result
        elif data == 50:
            result += "L"
            return result
        elif data == 40:
            result += "XL"
            return result
        else:
            while data > 0:
                result += "X"
                data -= 10
            return result

    if data == 50:
        result += "L"
        return result

    if data > 50:
        if data >= 90:
            result += "XC"
            data -= 90
        else:
            result += "L"
            while data > 60:
                result += "X"
                data -= 10
            data -= 50

    if data < 50:
        if data > 40:
            result += "XL"
            data -= 40
        else:
            while data > 10:
                result += "X"
                data -= 10

    #number is now below 10

    if data == 5:
        result += "V"
        return result

    if data > 5:
        if data >= 9:
            result += "IX"
            data -= 5

        else:
            result += "V"
            while data > 5:
                result += "I"
                data -= 1
        return result
    if data < 5:
        if data == 4:
            result += "IV"
        else:
            while data > 0:
                result += "I"
                data -= 1

    # replace this for solution
    return result


print(convert(12))