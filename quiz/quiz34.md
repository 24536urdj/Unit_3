###
        def to_roman(number):
        if number > 100 :
            print(ValueError)
        else :
            num = [1, 4, 5, 9, 10, 40, 50, 90,
                   100, 400, 500, 900, 1000]
            sym = ["I", "IV", "V", "IX", "X", "XL",
                   "L", "XC", "C", "CD", "D", "CM", "M"]
            i = 12

            while number:
                div = number // num[i]
                number %= num[i]

                while div:
                    print(sym[i], end="")
                    div -= 1
                i -= 1



    
        number = 101
      
        to_roman(number)
![](https://github.com/24536urdj/Unit_3/blob/main/quiz/Screen%20Shot%202023-02-05%20at%209.54.16.png)
