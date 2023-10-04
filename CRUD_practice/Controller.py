# controller 클래스
# 메뉴에서 선택한 항목에 따라 메소드 수행

from ProductDAO import ProductDAO
from ProductVO import Product

class Controller:
    def __init__(self):
        self.dao = ProductDAO()

    def select(self):
        # 상품 조회
        # DAO 클래스의 select()호출(DAO : 도서정보출력)
        self.dao.select()
    
    def insert(self):
        # 도서등록
        # 데이터 입력 받기
        prdNo = input('상품번호 입력 : ')
        prdName = input('상품명 입력 : ')
        prdPrice = input('가격 입력 : ')
        prdMaker = input('메이커 입력 : ')
        prdColor = input('상품 색상 입력 : ')
        ctgNo = input('카테고리 입력 : ')
    

        product = Product(prdNo,prdName, prdPrice, prdMaker, prdColor,ctgNo) # 객체에 넣어서
        # DAO 클래스의 insert()호출하면서 product객체 전달
        self.dao.insert(product) # 객체를 넘겨준다.


    def update(self):
        # 상품 수정
        # 수정할 데이터 입력 받기
        prdNo = input('수정할 상품번호 입력 : ')
        prdName = input('상품명 입력 : ')
        prdPrice = input('가격 입력 : ')
        prdMaker = input('메이커 입력 : ')
        prdColor = input('상품 색상 입력 : ')
        ctgNo = input('카테고리 입력 : ')

        # 객체에 넣어서
        product = Product(prdNo, prdName, prdPrice, prdMaker, prdColor,ctgNo) # 객체에 넣어서
        # DAO 클래스의 insert()호출하면서 product객체 전달
        self.dao.update(product) # 객체를 넘겨준다.
    
    def delete(self):
        # 삭제할 상품 번호 입력 받기
        prdNo = input('삭제할 상품 번호 : ')
        self.dao.delete(prdNo)
    
    def search(self, option):
        if option == 1: 
            # 검색할 상품명 입력
            prdName = input('상품명 입력 :')
            # DAO 클래스의 Search()호출
            self.dao.search(1, prdName)
        else:
            # 메이커 입력
            prdMaker = input('메이커 입력 : ')
            self.dao.search(2,prdMaker)