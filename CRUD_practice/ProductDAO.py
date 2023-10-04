#실제 작업 처리하는 클래스
import pymysql
from ProductVO import Product
import cryptography

class ProductDAO:
    # 생성자
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        # DB연결
        self.conn = pymysql.connect(host='localhost', 
                            port=3306, 
                            db= 'sqldb4',  # db선택
                            user='root', 
                            passwd='wjd900105!',
                            charset='utf8')
        # cursor 객체 
        self.cursor = self.conn.cursor()

    
    def disconnect(self):
        # DB접속 종료
        self.cursor.close()
        self.conn.close()

    def select(self):
        # 상품 조회
        try:
            # 1. DB연결 (connect호출)
            self.connect()
            # 2. 도서정보출력 : select문 수행
            sql = 'SELECT * FROM product ORDER BY prdNo'
            self.cursor.execute(sql)
            # 3. 결과 출력
            result = self.cursor.fetchall()
            for re in result:
                for r in re:
                    print(r, end="  ")
                print()
            # 4. DB접속 종료 (disconnect호출)
            self.disconnect()
            print('상품 조회 완료')
        except:
            print('상품 조회 실패')


    
    def insert(self, product):
        # 상품 등록
        try:
            # 1. DB연결 (connect호출)
            self.connect()
            # 2. INSERT문 수행
            sql = 'insert into product values(%s, %s, %s, %s, %s, %s)'

            # Getter통해 값 가져오기
            prdNo = product.get_prdNo()
            prdName = product.get_prdName()
            prdPrice = product.get_prdPrice()
            prdMaker = product.get_prdMaker()
            prdColor = product.get_prdColor()
            ctgNo = product.get_ctgNo()

            values = (prdNo,prdName, prdPrice, prdMaker, prdColor,ctgNo)
            self.cursor.execute(sql,values)
            self.conn.commit()
            # 3. DB접속 종료 (disconnect호출)
            self.disconnect()
            print('상품 입력 완료!')
        except:
            print('상품 입력 실패')

   

    def update(self, product):
        # 수정된 데이터 DB에 저장 : update문 수행
        try:
            # 1. DB연결 (connect호출)
            self.connect()

            # 2. UPDATE 문 수행
            sql = "update product set prdName=%s, prdPrice=%s, " \
                + "prdMaker=%s, prdColor=%s, ctgNo=%s where prdNo=%s"

            # Getter통해 값 가져오기
            prdNo = product.get_prdNo()
            prdName = product.get_prdName()
            prdPrice = product.get_prdPrice()
            prdMaker = product.get_prdMaker()
            prdColor = product.get_prdColor()
            ctgNo = product.get_ctgNo()

            values = (prdName, prdPrice, prdMaker, prdColor,ctgNo, prdNo)
            
            self.cursor.execute(sql, values)
            self.conn.commit()
            
            # 3. DB접속 종료 (disconnect호출)
            self.disconnect()
            print('상품 수정 완료')
        except:
            print('상품 수정 실패')

    
    def delete(self, prdNo):
        # 상품 삭제
        try:
            # 1. DB연결 (connect호출)
            self.connect()
            sql = "DELETE FROM product WHERE prdNo=" + prdNo
            self.cursor.execute(sql)
            self.conn.commit()
            # 4. DB접속 종료
            self.disconnect()
            print('상품 삭제 완료')
        except:
            print('상품 삭제 실패')


    def search(self, option, keyword):
        # 상품 검색하고 결과 출력
        try: 
            # 1. DB연결
            self.connect()
            # 2. sql문 수행
            if option == 1:
                sql = 'SELECT * FROM product WHERE prdName LIKE "%'+keyword+'%"'
            else:
                sql = 'SELECT * FROM product WHERE prdMaker LIKE "%'+keyword+'%"'
            
            self.cursor.execute(sql)
            # 3. 결과 출력
            result = self.cursor.fetchall()
            for re in result:
                for r in re:
                    print(r, end=" ")
                print()

            # 4. DB접속 종료 (disconnect호출)
            self.disconnect()
        except:
            print('검색 실패!')