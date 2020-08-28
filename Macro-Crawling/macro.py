import pyautogui

mouse_point = pyautogui.confirm("마우스를 로그인 학번 입력칸에 위치시킨 후 Enter")
if mouse_point == 'OK':
    id_x, id_y = pyautogui.position()
else:
    exit()

mouse_point = pyautogui.confirm("마우스를 로그인 비밀번호 입력칸에 위치시킨 후 Enter")
if mouse_point == 'OK':
    pw_x, pw_y = pyautogui.position()
else:
    exit()

mouse_point = pyautogui.confirm("마우스를 로그인버튼에 위치시킨 후 Enter")
if mouse_point == 'OK':
    lg_x, lg_y = pyautogui.position()
else:
    exit()
    
student_id = pyautogui.prompt("학번을 입력해주세요.")
password = pyautogui.password('종합정보 시스템 비밀번호를 입력해주세요. (hidden mode)')

pyautogui.click(id_x, id_y)
pyautogui.typewrite(student_id, interval=0.01)
pyautogui.click(pw_x, pw_y)
pyautogui.typewrite(password, interval=0.01)
pyautogui.click(lg_x, lg_y)

mouse_point = pyautogui.confirm("마우스를 로그아웃버튼에 위치시킨 후 Enter")
if mouse_point == 'OK':
    lgout_x, lgout_y = pyautogui.position()
else:
    exit()

mouse_point = pyautogui.confirm("마우스를 수강신청함버튼에 위치시킨 후 Enter")
if mouse_point == 'OK':
    sugang_x, sugang_y = pyautogui.position()
    pyautogui.click(sugang_x, sugang_y)
else:
    exit()

mouse_point = pyautogui.confirm("마우스를 'search'버튼에 위치시킨 후 Enter")
if mouse_point == 'OK':
    search_x, search_y = pyautogui.position()
    pyautogui.click(search_x, search_y)
else:
    exit()

num = int(pyautogui.prompt("몇 개의 강의를 담으시겠습니까?"))
lecture_position = []
for i in range(1, num +1):
    mouse_point = pyautogui.confirm("마우스를 강의 %d번째 강의 register 버튼에 위치시킨 후 Enter" %i)
    if mouse_point == 'OK':
        lec_x, lec_y = pyautogui.position()
        lecture_position.append([lec_x, lec_y])


confirm = pyautogui.confirm("설정이 완료되었습니다. 시작하시겠습니까? (끝 : ctrl + alt + delete)")
print(confirm)
if confirm == 'OK':
    while True:
        for i in range(38):
            pyautogui.click(search_x, search_y, interval=0.1)
            for position in lecture_position:
                pyautogui.click(position, interval=0.1)
                pyautogui.hotkey('\n', interval=0.1)
                pyautogui.hotkey('\n')
                
  
        pyautogui.click(lgout_x, lgout_y, interval=0.5)
        pyautogui.hotkey('\n', interval=0.5)
        pyautogui.click(id_x, id_y)
        pyautogui.typewrite(student_id, interval=0.01)
        pyautogui.click(pw_x, pw_y)
        pyautogui.typewrite(password, interval=0.01)
        pyautogui.click(lg_x, lg_y, interval=1)
        pyautogui.click(sugang_x, sugang_y, interval=0.5)

