from Controller import Controller


class Main:
    def __init__(self):
        self.controller = Controller()
        print()

    def start(self):
        # 메뉴 출력
        # 1. 상품조회 2. 상품 등록 3. 상품 정보 수정 4. 상품 삭제 5. 검색 6. 종료
        # 선택한 번호에 따라 controller 클래스의 메소드 호출
        

        while True:
            num = input("\n\n1. 상품조회 2. 상품 등록 3. 상품 정보 수정 4. 상품 삭제 5. 검색 6. 종료 : ")

            if num == '1':
                # 컨트롤러 클래스의 select() 호출
                self.controller.select()
            elif num == '2':
                self.controller.insert()
            elif num == '3':
                self.controller.update()
            elif num == '4':
                self.controller.delete()
            elif num == '5':
                option = input("\n 1. 상품명 검색 2. 제조회사 검색 : ")
                if option == '1':
                    self.controller.search(1)
                elif option == '2':
                    self.controller.search(2)
                else:
                    print("잘못 입력하셨습니다.")
            elif num == '6':
                print('종료합니다.')
                break
            else:
                print('잘못 입력하였습니다.')

# 현재 모듈이 시작모듈
if __name__ == "__main__":
    # start 메소드 실행하면서 시작
    m = Main()  # 객체 만들고
    m.start()
