def calculate(number):
    output = (number+4)*20
    if output > 100:
        return output/5
    else:
        return 0


class Coffee:
    def __init__(self):
        self.price = 10
        self.x = 1

    def buy(self):
        print(f"You bought coffee for {self.price}")

    def random_function(self):
        print(self.x)




class Mouse:
    def __init__(self):
        self.price = 100

    def buy(self):
        print(f"You bought a mouse for {self.price}")

def add(a,b):
    return a+b

class Ediya:
    def __init__(self):
        self.menu = {
            "espresso": 3
        }

    def buy(self, item, nickname):
        if item in self.menu:
            print(f"{nickname}, you just bought {item} for ${self.menu[item]}")
        else:
            print(f"Sorry, we don't have {item} on the menu!")

class Starbucks:
    def __init__(self):
        self.menu = {"americano":3,"latte":4,"gift_card":50,}
        
    def buy(self, item, nickname=None):
        if item in self.menu:
            print(f"{nickname}, you just bout {item} for ${self.menu[item]}")
        else:
            print(f"sorry, we do don't have {item} on the menu!")

    def get_menu(self):
        print(self.menu)
        
#     # 스타벅스
#     # 아메리카노 구매하기
#     # 라떼 구매하기
#     # 기프트카드 구매하기
#     # 메뉴보기
#     # 기프트카드 잔액보기

#     # 커피빈
#     # 아메리카노 구매하기
#     # 말차라떼 구매하기
#     # 메뉴보기

if __name__ == "__main__":
    starbucks = Starbucks()

    starbucks.buy("americano")
    starbucks.buy("latte")
    starbucks.buy("gift_card")

    starbucks.get_menu()

# if __name__ == "__main__":
#     x = [1,2,3,4,5]
#     # for i in x:
#     #     print(i)

#     print(add(1,2))

#     ediya = Ediya()

#     ediya.buy("espresso", "Iffy")
    
#     for i in x:
#         print(calculate(i))

#     def calculate(number):
#         output = (number+4)*20
#         if output > 100:
#             return output/5
#         else:
#             return 0

#     mouse = Mouse()
#     mouse1 = Mouse()
#     coffee = Coffee()

#     mouse.buy()
#     coffee.buy()


        

#     # 스타벅스
#     # 아메리카노 구매하기
#     # 라떼 구매하기
#     # 기프트카드 구매하기
#     # 메뉴보기
#     # 기프트카드 잔액보기

#     # 커피빈
#     # 아메리카노 구매하기
#     # 말차라떼 구매하기
#     # 메뉴보기