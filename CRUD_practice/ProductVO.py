# 데이터 클래스
class Product:
    def __init__(self, prdNo,prdName, prdPrice, prdMaker, prdColor, ctgNo): 
        # 객체 생성하면서 초기화
        self.__prdNo = prdNo
        self.__prdName = prdName
        self.__prdPrice = prdPrice
        self.__prdMaker = prdMaker
        self.__prdColor = prdColor
        self.__ctgNo = ctgNo

    def get_prdNo(self):
        return self.__prdNo
    
    def get_prdName(self):
        return self.__prdName
    
    def get_prdPrice(self):
        return self.__prdPrice
    
    def get_prdMaker(self):
        return self.__prdMaker
    
    def get_prdColor(self):
        return self.__prdColor
    
    def get_ctgNo(self):
        return self.__ctgNo