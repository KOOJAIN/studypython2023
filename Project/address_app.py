# 주소록 앱
# 2023-02-06
# JSH
# 15. 예외 처리 
# 15-1. 파일 없을때 나는 예외 
# 15-2. 입력시/ 개수가 다를때 예외 
# 15-3. 메뉴번호 입력 숫자외 예외 
import os                # 운영체제용 모듈 

# 2. 클래스 생성 
class Contact:
    # 생성자 - 이름, 전번, 이메일, 주소 
    def __init__(self, name, phone_num, email, addr) -> None:
        self.__name = name 
        self.__phone_num = phone_num 
        self.__email = email 
        self.__addr = addr
    
    # 4. str 재정의 
    def __str__(self) -> str:
        str_res = (f'이  름: {self.__name}\n'
                   f'핸드폰: {self.__phone_num}\n'
                   f'이메일: {self.__email}\n'
                   f'주  소: {self.__addr}')
        return str_res

    # 10. 객체 존재 여부 확인 (※클래스 함수)
    def isNameExist(self, name):
        if self.__name == name :
            return True
        else:
            return False
    
    # 12. 각 멤버변수 접근하는 함수 
    #getName, getPhoneNum, getEmail. getAddr
    def getName(self) -> str :
        return self.__name

    def getPhoneNum(self) -> str :
        return self.__phone_num

    def getEmail(self) :
        return self.__email

    def getAddr(self) :
        return self.__addr

# 5. 사용자 입력 
def set_contact():
    name, phone_num, email, addr = input('정보입력(이름/ 폰번호/ 이메일/ 주소) ').split('/')
    # print(name, phone_num, email, addr) 
    # 7. Contact 객체 만들기 
    contact = Contact(name, phone_num, email, addr)
    return contact

# 9. 주소록 출력 
def get_contacts(list):
    for item in list:
        print(item)
        print('====================')

# 10. 주소록 삭제 
def del_contact(list, name):
    count = 0
    for i, item, in enumerate(list):     # enumerate : 순번 지정 함수 
        if item.isNameExist(name):
            count+=1
            del list[i]                  # 리스트 삭제 

    if count > 0 :                       # 메세지 출력 
        print('삭제했습니다.')
    else:
        print('삭제할 주소록이 없습니다. ') 

# 13. 주소록 파일 저장 
def save_contacts(list):
    file = open('C:/Source/studyPython2023/Project/contacts.txt', 'w', encoding='utf-8')
    
    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddr()}'
        file.write(f'{text}\n')

    file.close()                       # 파일 닫아줘야함 !!     

# 14. 주소록 읽어오기 
def load_contacts(list):
    try:
        file = open('C:/Source/studyPython2023/Project/contacts.txt', 'r', encoding='utf-8')
    except Exception as e:     # 15-1  예외 처리 
        f = open('C:/Source/studyPython2023/Project/contacts.txt', 'w', encoding='utf-8')
        f.close()       #파일이 없어서 생기는 예외는 파일 생성하고 함수 아웃 
        return 
       
    while True:
        line = file.readline().replace('\n','')      # 15. 문장 끝 \n 제거 
        if not line : break

        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list.append(contact)

    file.close()   


# 추가. 화면 클리어
def clear_console():
    command ='clear'                  # Linux, Unix 화면클리어 명령어
    if os.name in ('nt', 'dos'):      # Window 운영체제라면 
        command = 'cls'               # 윈도우 화면 클리어 명령어
    
    os.system(command)
 
# 6. 메뉴 표시 
def get_menu():
    str_menu=('주소록 앱 v1.0\n'
             '1. 연락처 추가\n' 
             '2. 연락처 출력\n'
             '3. 연락처 삭제\n'
             '4. 앱 종료')
    print(str_menu)
    try:
        menu=int(input('메뉴 입력: '))
    except Exception as e:    # 15-3 숫자외 입력예외 처리 
        menu = 0              # 영문자, 특수문자 넣으면 전부 0으로 
         
    return menu

# 3. 전체 실행 
def run():
    contacts=list()                     # 주소를 담기 위한 빈리스트 생성 
    load_contacts(contacts)                 # 14. 주소록 읽어오기 
    # temp = Contact('장시현', '010-4233-3610', '42333610jsh@gmail.com', '부산광역시 남구 대연3동')    
    # set_contact()
    clear_console()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1 :                  # 8. 연락처 추가
            try:                            # 15-2 연락처 입역 잘못했을 때 예외처리 
                contact =set_contact()
                contacts.append(contact)
                input('주소록 입력 성공')    # 아무것도 안받는 입력 
            except Exception as e: 
                print('이름/전번/이메일/주소 순으로 입력해주세요.')
                input()
            finally:
                clear_console()
        elif sel_menu == 2:              # 9. 연락처 출력 
            get_contacts(contacts)
            input('주소록 출력 완료')
            clear_console()
        elif sel_menu == 3:              # 10. 연락처 삭제 
            name = input('삭제할 이름 입력 : ')
            del_contact(contacts, name)
            input()
            clear_console()
        elif sel_menu == 4:               # 13. 종료시 주소록 파일 저장 
            save_contacts(contacts)
            break
        else:
            clear_console()

# 1. 메인 실행 영역 
if __name__ == '__main__' :
    # print('주소록 앱 시작합니다.')
    run()