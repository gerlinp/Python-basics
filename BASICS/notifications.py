def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 4 )
    print(result)

yell("You are doing great")
yell("Dont forget to as for help")
yell("Don't Repeat Yourself. Keep things DRY")
