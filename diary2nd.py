import tkinter as tk
from tkinter import messagebox
from tkinter import *
import tkinter.font
import pymysql
from datetime import datetime
import datetime
import calendar


#
# 기본 틀, 페이지 간의 이동을 위한 클래스
#
class SampleApp(tk.Tk):
    # __init__(self) 메소드는 객체를 생성할 때 자동으로 호출되는 특수한 메소드
    # 생성자
    def __init__(self):
        tk.Tk.__init__(self)

        self._frame = None
        self.switch_frame(LoginPage)

    # 창 전환 메소드; 현재 창 종료 후 해당 창 열기
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)

        if self._frame is not None:  # 만약 지금 프레임이 켜져 있으면 종료.
            self._frame.destroy()

        self._frame = new_frame  # 새 프레임 시작!
        self._frame.pack()

    # 창 전환 메소드; 메인 페이지 열기
    def main_frame(self, login_id, year, month, frame):
        if month == 0:  # 0월이면 이전 해 12월 달으로.
            month = 12
            year -= 1
        if month == 13:  # 13월이면 다음 해 1월 달으로.
            month = 1
            year += 1

        if frame != '':  # 메인 프레임 켜져 있으면 닫고,
            frame.destroy()
        else:  # 아니면 현재 프레임 닫고,
            self._frame.destroy()

        Main(login_id, year, month)

    # 창 전환 메소드; 다이어리쓰기 페이지 열기
    def write_frame(self, login_id, year, en_month, month, day, frame):
        if frame != '':  # 다이어리 쓰기 페이지 열려 있으면 닫고, 아니면 현재 페이지 닫고
            frame.destroy()
        else:
            self._frame.destroy()

        WDiary(login_id, year, en_month, month, day)


#
# 로그인 페이지
#
class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=200, width=300, bg='#35475c')

        font = tkinter.font.Font(size=10, slant='italic', weight='bold')

        tk.Label(self, text="Welcome to Dwrite!", bg='#35475c', fg='#e6decb', font=font).place(x=85, y=13)

        # ID
        tk.Label(self, text="ID", bg='#35475c', fg='#e6decb', font=font).place(x=50, y=50)
        input_id = tk.Entry(self, fg='#35475c', bg='#e6decb', font=font)
        input_id.place(x=100, y=50)

        # PW
        tk.Label(self, text="Password", bg='#35475c', fg='#e6decb', font=font).place(x=30, y=80)
        input_pw = tk.Entry(self, show="*", fg='#35475c', bg='#e6decb')
        input_pw.place(x=100, y=80)

        # 로그인 버튼
        tk.Button(self, text="로그인", bd=0, bg='#35475c', fg='#e6decb', font=font,
                  command=lambda: self.login(input_id, input_pw)).place(x=80, y=130)

        # 회원가입 버튼, 누르면 회원가입 창으로 전환.
        tk.Button(self, text="회원가입 >", bd=0, bg='#35475c', fg='#e6decb', font=font,
                  command=lambda: master.switch_frame(SignupPage)).place(x=150, y=130)

    # 로그인 메소드
    def login(self, input_id, input_pw):
        login_id = input_id.get()
        login_pw = input_pw.get()

        today = datetime.datetime.today()
        month = today.month
        year = today.year

        # 데이터베이스
        db = pymysql.connect(host="localhost", user='root', password='?', db="project_login", charset='utf8')
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM login WHERE id = '{login_id}'and pw = '{login_pw}';")  # 입력한 id, pw 검색

        rows = cursor.fetchmany()

        # 이벤트 : id,pw이 맞지 않으면 오류메시지 출력
        if rows == ():
            tk.messagebox.showerror("Error", "ID/Password를 확인해주세요.")
        else:
            self.master.main_frame(login_id, year, month, '')

        db.commit()


#
# 회원가입 페이지
#
class SignupPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=280, width=300, bg='#35475c')

        font = tkinter.font.Font(size=10, slant='italic', weight='bold')  # font

        # 이름
        tk.Label(self, text="Username", bg='#35475c', fg='#e6decb', font=font).place(x=30, y=70)
        mk_name = tk.Entry(self, bg='#e6decb')
        mk_name.place(x=100, y=70)

        # ID
        tk.Label(self, text="ID", bg='#35475c', fg='#e6decb', font=font).place(x=50, y=100)
        mk_id = tk.Entry(self, bg='#e6decb')
        mk_id.place(x=100, y=100)

        # PW
        tk.Label(self, text="Password", bg='#35475c', fg='#e6decb', font=font).place(x=30, y=130)
        mk_pw = tk.Entry(self, show="*", bg='#e6decb')
        mk_pw.place(x=100, y=130)

        # 로그인 버튼
        tk.Button(self, text="로그인 >", command=lambda: master.switch_frame(LoginPage), bd=0, bg='#35475c', fg='#e6decb',
                  font=font).place(x=150, y=190)

        # 회원가입 버튼
        tk.Button(self, text="회원가입", bg='#35475c', fg='#e6decb', font=font,
                  command=lambda: self.signup(mk_name, mk_id, mk_pw), bd=0).place(x=78, y=190)

    # 회원가입 메소드
    def signup(self, mk_name, mk_id, mk_pw):
        # 입력받은 데이터를 해당 변수에 저장
        su_name = mk_name.get()
        su_id = mk_id.get()
        su_pw = mk_pw.get()

        # 이벤트 : 데이터가 입력되지 않았으면 오류메시지 출력
        if su_pw == '' or su_id == '' or su_name == '':
            tk.messagebox.showerror("Error", "데이터를 입력해주세요.")
        else:
            try:
                # 사용자가 입력한 이름, id, pw을 데이터 베이스에 저장.
                db = pymysql.connect(host="localhost", user='root', password='?', db="project_login", charset='utf8')
                cursor = db.cursor()
                cursor.execute(f"INSERT INTO login(id, name, pw) VALUES('{su_id}', '{su_name}', '{su_pw}');")
                print(type(su_id))

                try:
                    print(int(su_id))
                except:
                    # 이벤트 : 회원가입 완료 메시지 출력
                    tk.messagebox.showinfo("Clear", "회원가입이 완료되었습니다.")
                    # 로그인 창으로 전환
                    self.master.switch_frame(LoginPage)

                    db.commit()
                else:
                    tk.messagebox.showerror("Error", "ID 형식이 잘못되었습니다.\n ID를 숫자만으로 입력하실 수 없습니다.")
            except:
                # 이벤트 : id가 중복되었으면 오류메시지 출력
                tk.messagebox.showerror("Error", "ID가 중복되었습니다.")


# 메인 화면
#
class Main(tk.Frame):

    def __init__(self, login_id, year, month):
        frame = tk.Frame(height=700, width=600, bg='#f6f2e8')
        frame.pack()

        self.print_cal(login_id, frame, year, month)

        font2 = tkinter.font.Font(size=13, weight='bold')
        # 달 이동 버튼 ◀◁▶▷'👈''👉'
        arrow_font = tkinter.font.Font(size=25, weight='bold')
        but_font = tkinter.font.Font(size=15, weight='bold', slant='italic')
        tk.Button(frame, text='◀', fg='#35475c', bg='#f6f2e8', relief='groove', font=arrow_font, bd=0,
                  command=lambda: SampleApp.main_frame(self, login_id, year, month - 1, frame)).place(x=25, y=270)
        tk.Button(frame, text='▶', fg='#35475c', bg='#f6f2e8', relief='groove', font=arrow_font, bd=0,
                  command=lambda: SampleApp.main_frame(self, login_id, year, month + 1, frame)).place(x=530, y=270)

        db = pymysql.connect(host="localhost", user='root', password='?',
                             db="project_login", charset='utf8')
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM login WHERE id = '{login_id}';")  # 입력한 id, pw 검색

        rows = cursor.fetchmany()
        user_name = rows[0][1]

        user_name = tk.Label(frame, text=f"{user_name}'s Diary", font=font2, bg='#adbecc', fg='white', justify='right',
                             width=105, pady=10)
        user_name.place(x=0, y=0)

        tk.Button(frame, text='내가 쓴 일기 목록 📝', bg='#d3dde6', fg='#35475c', anchor='w', width='60', bd=0, padx=230, pady=10,

                  font=font2, command=lambda: diary_all(frame)).place(y=655)

        def diary_all(frame):  # 내가 쓴 일기 모음 보여주는 새 창
            newWindow = tk.Toplevel(app)
            frame1 = tk.Frame(newWindow, height=500, width=300,  bg='#adbecc')
            frame1.pack()

            db = pymysql.connect(host="localhost", user='root', password='?',
                                     db="project_login", charset='utf8')
            cursor = db.cursor()

            tk.Label(frame1, text='내가 쓴 일기 📝',bg='#adbecc', fg='#f6f2e8',
                     font=but_font, padx= 5, pady = 5).pack(side='top')

            font = tkinter.font.Font(size=13, weight='bold')

            try:
                cursor.execute(f"SELECT * FROM {login_id};")  # 입력한 id, pw 검색
            except:
                tk.Label(frame1, text='Diary is empty.', bg='#f6f2e8', fg='#adbecc', font=font, bd=0, padx=80, pady=10).pack(side="bottom", fill="both")
            else:
                rows = cursor.fetchall()
                rows = sorted(rows)

                if str(rows) == '[]':
                    tk.Label(frame1, text='Diary is empty.', bg='#f6f2e8', fg='#adbecc', font=font, bd=0, padx=80,
                         pady=10).pack(side="bottom", fill="both")

                else :
                    scrollbar = tk.Scrollbar(frame1)
                    scrollbar.pack(side="right", fill="y")
                    tk.Button(frame1, text="select", fg='#f6f2e8', bg='#adbecc', font=font, command=lambda: go_diary()).pack(side=BOTTOM, fill="both", expand=True)
                    listbox = tk.Listbox(frame1, yscrollcommand=scrollbar.set, bg='#f6f2e8', fg='#35475c', font=font, bd=0, selectbackground='#adbecc', height=10)
                    for i in range(len(rows)):
                        d_all = rows[i][0]
                        d_all2 = d_all

                        listbox.insert("end", f'{d_all2}')

                    listbox.pack(side="left", fill="both")
                    scrollbar.config(command=listbox.yview)


            def go_diary():
                print(listbox.get(ACTIVE))
                if listbox.get(ACTIVE) != '':
                    year = int(listbox.get(ACTIVE)[0:4])
                    month = int(listbox.get(ACTIVE)[5:7])
                    day = int(listbox.get(ACTIVE)[8:])

                    date = datetime.date(year, month, day)
                    en_month = date.strftime("%B")
                    newWindow.destroy()
                    SampleApp.write_frame(self, login_id, year, en_month, month, day, frame)

    # 달력 출력하기
    def print_cal(self, login_id, frame, year, month):

        font = tkinter.font.Font(size=25, weight='bold', slant='italic')
        weekfont = tkinter.font.Font(size=20, weight='bold', slant='italic')

        cal = calendar.Calendar()
        date = datetime.date(2021, month, 1)
        en_month = date.strftime("%B")  # 해달 달 영어로 표기, ex) June
        today = datetime.date.today()  # 오늘 날짜

        mon_year = (f'{en_month}, {year}')  # 월, 년도 ex) June, 2021
        cal_box = tk.LabelFrame(frame, height=540, width=520, bd=4, relief='groove', fg='#35475c', bg='#f6f2e8',
                                text=mon_year, font=font, labelanchor='n', padx=30, pady=30)
        tk.Label(cal_box, text='Mon  Tue  Wed  Thu  Fri  Sat  Sun', font=weekfont, fg='#35475c',
                 bg='#f6f2e8').pack()
        cal_box.place(x=50, y=100)
        cal_frame = tk.Label(cal_box, height=540, width=520, bd=0, bg='#f6f2e8', fg='#35475c', padx=10, pady=10)
        cal_frame.pack()

        y_value = 0
        for x in cal.monthdayscalendar(year, month):  # 달력 날짜 출력하기
            count = 0
            x_value = 0
            for i in x:
                if i == 0:
                    i = ''
                if today.day == i and today.month == month and today.year == year:  # 오늘 날짜는 글자 색 다르게
                    btn = tk.Button(cal_frame, text=i, fg='#de3a6f', bg="#f6f2e8", activebackground="#f6f2e8",
                                    activeforeground='#cf5735', bd=0, font=font,
                                    command=lambda x=i: SampleApp.write_frame(self, login_id, year, en_month, month, x,
                                                                              frame))
                else:
                    btn = tk.Button(cal_frame, text=i, fg='#35475c', bg="#f6f2e8", bd=0, font=font,
                                    command=lambda x=i: SampleApp.write_frame(self, login_id, year, en_month, month, x,
                                                                              frame))
                btn.grid(column=x_value, row=y_value)
                x_value += 1
                count += 1
                if (count % 7) == 0:
                    y_value += 1
                    x_value = 0


#
# 다이어리 작성 페이지
#
class WDiary(tk.Frame):
    def __init__(self, login_id, year, en_month, month, day):

        if day < 10:
            day0 = "0" + str(day)
        else:
            day0 = day

        date = datetime.date(year, month, day)

        frame = tk.Frame(height=700, width=600, bg='#35475c')
        frame.pack()

        bt_font = tkinter.font.Font(size=13, slant='italic', weight='bold')

        # 날짜 프레임
        label_font = tkinter.font.Font(size=25, slant='italic', weight='bold')
        diary_data = tk.LabelFrame(frame, height=540, width=520, bd=4, relief='groove',
                                   fg='#f6f2e8', bg='#35475c', text=f' {en_month} {day0}, {year}  ', font=label_font,
                                   labelanchor='nw')
        diary_data.place(x=40, y=80)

        # 내용
        # insertbackground : 커서 색상 ; wrap=tk.CHAR : 내용이 칸 넘어가지 않게 잘라주는거 ; yscrollcommand : 세로스크롤 제공
        diary_content = Text(diary_data, insertbackground='white', padx=10, pady=10, wrap=tk.CHAR, yscrollcommand='true'
                             , width=53, bd=0, font=bt_font, fg='white', bg='#35475c')
        diary_content.place(x=5, y=13)

        conn = pymysql.connect(host="localhost", user='root', password='?', db="project_login", charset='utf8')
        cursor = conn.cursor()

        cursor.execute(f"SHOW TABLES IN project_login LIKE '{login_id}';")  # 해당 id의 테이블이 있는지 검색.
        rows = cursor.fetchmany()
        if rows != ():
            cursor.execute(f"SELECT content FROM {login_id} WHERE date = '{date}';")  # 해당 날짜가 있는지 검색.
            rows2 = cursor.fetchmany(size=1)
            if rows2 != ():  # 해당 날짜가 이미 있으면,
                rows2 = rows2[0]
                rows2 = str(rows2[0])
                diary_content.insert("current", rows2)

        conn.commit()
        conn.close()

        # 현재 시간 출력 버튼
        time_font = tkinter.font.Font(size=13, weight='bold')
        tk.Button(frame, text="⏱", bd=0, fg='#f6f2e8', bg='#35475c', font=time_font,
                  command=lambda: self.button_clicked(diary_content)).place(x=30, y=650)

        # 취소 버튼
        tk.Button(frame, text="Cancel", bd=0, fg='#f6f2e8', bg='#35475c', font=bt_font,
                  command=lambda: SampleApp.main_frame(self, login_id, year, month, frame)).place(x=520, y=30)

        # 완료 버튼
        tk.Button(frame, text="Done", bd=0, fg='#f6f2e8', bg='#35475c', command=lambda: confirm(), font=bt_font).place(
            x=520, y=650)

        def confirm():
            year = date.year
            month = date.month

            intext = diary_content.get("1.0", END)
            text = ""

            for i in intext:
                if i == "'":
                    text += "'"
                text += i
            intext = text

            conn = pymysql.connect(host="localhost", user='root', password='?', db="project_login", charset='utf8')
            cursor = conn.cursor()

            cursor.execute(f"SHOW TABLES IN project_login LIKE '{login_id}';")  # 해당 id의 테이블이 있는지 검색.
            rows = cursor.fetchmany()
            if rows == ():  # 해당 id의 테이블이 없으면 만들기.
                cursor.execute(f"create table {login_id} (date TEXT NOT NULL, content TEXT NULL )ENGINE = INNODB;")

            cursor.execute(f"SELECT * FROM {login_id} WHERE date = '{date}';")  # 해당 날짜가 있는지 검색.
            rows2 = cursor.fetchmany()

            if rows2 != ():  # 해당 날짜가 이미 있으면, 내용만 수정.
                cursor.execute(f"UPDATE {login_id} SET content = '{intext}' WHERE date = '{date}';")

            else:  # 그렇지 않으면, 날짜와 내용 삽입.
                cursor.execute(f"INSERT INTO {login_id}(date, content) VALUES('{date}', '{intext}');")

            intext = intext.rstrip('\n')
            blank = ""
            for i in intext:
                if i != " ":
                    blank += i
            if blank == "":
                cursor.execute(f"delete FROM {login_id} WHERE date = '{date}';")

            conn.commit()
            conn.close()
            SampleApp.main_frame(self, login_id, year, month, frame)

    # 현재시각 출력 함수
    def button_clicked(self, diary_content):
        now = datetime.datetime.now()
        diary_content.insert("current", now.strftime('%p %I:%M'))


if __name__ == "__main__":  # __name__ : 현재 모듈의 이름을 담고있는 내장 변수, __main__ : 직접 실행된 모듈의 경우
    app = SampleApp()  # 직접 실행시킨 경우 다음과 같은 코드들을 실행시킨다. import 됐을 경우에는 출력되지 않음.
    app.title('Dwrite')
    app.mainloop()