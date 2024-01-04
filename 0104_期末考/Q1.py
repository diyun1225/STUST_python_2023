#定義炸雞類別：五個屬性、定義建構子、定義三個副函式、定義四個物件、分別呼叫三個副函式

#我是個網路美食家，我在網路上做了一個北中南好吃炸雞店紀錄，裡面有四個北中南評價很高的炸雞店，但有時候炸雞店的價格可能會微調
#因此我可以去改動價格店址，也可以搜尋各個炸雞店的地址，也可以直接線上訂購

#炸雞店：store_name:店名、address:店址、phone:訂餐電話、signature_dish:招牌餐、price:價格
class chicken:
     def __init__(self, store_name, address, phone,signature_dish,price):
        self.store_name = store_name
        self.address = address
        self.phone = phone
        self.signature_dish = signature_dish
        self.price = price

     def revise_price(self,new_price):
        #修改價格
        self.price = new_price
        print(f"更改成功，價格修改為: {self.price}")

     def online_order(self,quantity):
        #線上訂餐
        total_price = quantity * self.price
        print(f"點了 {quantity} 份{self.signature_dish}，總共 {total_price} 元")

     def search_store_address(self):
        #搜尋店面地址
        print(f"{self.store_name}的位置在 {self.address}")
        

if __name__ == '__main__':
    Napolifriedchicken = chicken("拿坡里炸雞","台北","02-25914052","脆皮炸雞",110)
    fatdfc = chicken("胖老爹炸雞","台中","04-24510078","紐奧良雞排",95)
    kfc = chicken("肯德基","台南","06-2818438","紙包雞套餐",200)
    chicken_house = chicken("炸雞洋行","台南","0976656999","半斤大雞腿",140)

  
    Napolifriedchicken.revise_price(220) #改變拿坡里炸雞的價格->220
    Napolifriedchicken.search_store_address() #搜尋拿坡里炸雞的地址
    Napolifriedchicken.online_order(10) #訂購拿坡里炸雞招牌餐10份

    fatdfc.revise_price(100)#改變胖老爹炸雞的價格->100
    fatdfc.search_store_address()#搜尋胖老爹炸雞的地址
    fatdfc.online_order(3)#訂購胖老爹炸雞招牌餐3份

    kfc.revise_price(250)#改變肯德基的價格->250
    kfc.search_store_address()#搜尋肯德基的地址
    kfc.online_order(5)#訂購肯德基招牌餐5份

    chicken_house.revise_price(150)#改變炸雞洋行的價格->150
    chicken_house.search_store_address()#搜尋炸雞洋行的地址
    chicken_house.online_order(20)#訂購炸雞洋行招牌餐20份
    