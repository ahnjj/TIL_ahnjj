#실제 작업 처리하는 클래스
import pymysql
from ch22_db.Book_practice.BookVO import Book
import cryptography

class BookDAO:
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
        # 도서조회
        try:
            # 1. DB연결 (connect호출)
            self.connect()
            # 2. 도서정보출력 : select문 수행
            sql = 'select * from book'
            self.cursor.execute(sql)
            # 3. 결과 출력
            result = self.cursor.fetchall()
            for re in result:
                for r in re:
                    print(r, end=" ")
                print()
            # 4. DB접속 종료 (disconnect호출)
            self.disconnect()
            print('도서 조회 완료')
        except:
            print('도서 조회 실패')


    
    def insert(self, book):
        # 도서등록
        # 1. DB연결 (connect호출)
        try:
            self.connect()
            # 2. INSERT문 수행
            sql = 'insert into book values(%s, %s, %s, %s, %s, %s, %s)'

            # Getter통해 값 가져오기
            bNo = book.get_bNo()
            bName = book.get_bName()
            bAuthor = book.get_bAuthor()
            bPrice = book.get_bPrice()
            bDate = book.get_bDate()
            bStock = book.get_bStock()
            pNo = book.get_pNo()

            values = (bNo,bName, bAuthor,bPrice, bDate, bStock, pNo)
            self.cursor.execute(sql,values)
            self.conn.commit()
            # 3. DB접속 종료 (disconnect호출)
            self.disconnect()
            print('도서 입력 완료!')
        except:
            print('도서 입력 실패')

   

    def update(self, book):
        # 도서수정
        # 수정된 데이터 DB에 저장 : update문 수행
        try:
            # 1. DB연결 (connect호출)
            self.connect()

            # 2. UPDATE 문 수행
            sql = "update book set bookName=%s, bookAuthor=%s, " \
                + "bookPrice=%s, bookDate=%s, bookStock=%s, pubNo=%s where bookNo=%s"

            # Getter통해 값 가져오기
            bNo = book.get_bNo()
            bName = book.get_bName()
            bAuthor = book.get_bAuthor()
            bPrice = book.get_bPrice()
            bDate = book.get_bDate()
            bStock = book.get_bStock()
            pNo = book.get_pNo()

            values = (bName, bAuthor,bPrice, bDate, bStock, pNo, bNo)

            self.cursor.execute(sql, values)
            self.conn.commit()
            
            # 3. DB접속 종료 (disconnect호출)
            self.disconnect()
            print('도서 수정 완료')
        except:
            print('도서 수정 실패')

    
    def delete(self, bookNo):
        # 도서삭제
        try:
            # 1. DB연결 (connect호출)
            self.connect()
            sql = "DELETE FROM book WHERE bookNo=" + bookNo
            self.cursor.execute(sql)
            self.conn.commit()
            # 4. DB접속 종료
            self.disconnect()
            print('도서 삭제 완료')
        except:
            print('도서 삭제 실패')


    def search(self, bName):
        # 도서 검색하고 결과 출력
         # 1. DB연결
        self.connect()
        # 2. sql문 수행
        sql = 'SELECT * FROM book WHERE bookName LIKE "%'+bName+'%"'
        self.cursor.execute(sql)
        # 3. 결과 출력
        result = self.cursor.fetchall()
        print(result)

        # 4. DB접속 종료 (disconnect호출)
        self.disconnect()