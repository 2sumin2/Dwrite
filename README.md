# Diary - Dwrite
### python으로 다이어리 만들기

<div style="display:flex flex-direction:column">
<img src="https://user-images.githubusercontent.com/75177553/161414464-6975a69b-bda3-4068-8a10-a0f34bbcff75.png"/>
<img src="https://user-images.githubusercontent.com/75177553/161414423-0d563830-48eb-4697-aca4-17d129af721d.png"/></div>

![image](https://user-images.githubusercontent.com/75177553/161414581-d4be22c6-40a6-4642-a1ad-2411ed545650.png)

![image](https://user-images.githubusercontent.com/75177553/161414511-7fa584a9-3d8a-4124-a10b-60ea6f2fda47.png)
![image](https://user-images.githubusercontent.com/75177553/161414541-b6cd59f3-bc7d-4962-9439-80657a13038e.png)
        
<ol>
        <h4><li>Login</li></h4>
        <ul>
                <li>ID와 비밀번호 입력 받음. Ok >> Main Page로 이동 / Error >> 오류 메시지 출력</li>
                <li>회원가입 버튼 >> 회원가입 page로 이동</li>
        </ul>
        <h4><li>Sign Up</li></h4>
        <ul>
                <li>사용자 이름과 ID와 비밀번호 입력 받음. Ok >> 로그인 화면으로 이동 / Error >> 오류메시지 출력></li>
                <li>로그인 버튼 >> 로그인 page로 이동</li>
        </ul>
        <h4><li>Calendar</li></h4>
        <ul>
                <li>database에서 사용자 이름 불러와서 “사용자의 이름’s Diary” 출력</li>
                <li>이번달의 달력 표시 (오늘 날짜는 빨간색으로 표시)</li>
                <li>화살표 버튼 >> 이전달 혹은 다음달의 달력을 출력</li>
                <li>날짜 클릭 >> 그 날의 일기 쓰기 page로 이동</li>
                <li>내가 쓴 일기 목록’ 버튼 >> 사용자가 쓴 일기의 목록을 보여주는 창으로 이동</li>
        </ul>
        <h4><li>Diary</li></h4>
        <ul>
                <li>사용자가 클릭 한 날의 날짜 표기(월, 일, 년)</li>
                <li>일기 작성 (크기 고정, 가로로 내용이 길어지면 다음 줄로 출력, 세로로 내용이 길어지면 스크롤)</li>
                <li>‘Done’ 버튼 >> 내용 저장 후 메인 화면으로 이동 (저장내용이 공백 뿐이거나 개행 뿐일 시에는 저장 X)</li>
                <li>‘Cancel’ 버튼 클릭 >> 내용 저장x, 메인 화면으로 이동</li>
                <li>시계 모양 이모티콘 클릭 >> 현재 커서의 위치에 현재 시간 출력</li>
        </ul>
        <h4><li>History</li></h4>
        <ul>
                <li>Main 의 ‘내가 쓴 일기 목록’ 버튼 >> 사용자가 쓴 일기의 목록을 보여주는 창으로 이동</li>
                <li>다이어리가 기록된 날짜를 database에서 불러와서 출력 (날짜 순)</li>
                <li>날짜 클릭 후 ‘select’ 버튼 >> 그 날짜의 일기 페이지로 이동</li>
        </ul>
</ol>
 
