리눅스 정리
==============
참고 사이트 : https://opentutorials.org/course/2598

리눅스 준비
--------------
1. codeonweb
: 웹환경에서 리눅스를 실습할 수 있는 사이트 (https://www.codeonweb.com)

2. cloud9 (AWS)
: 웹환경에서 리눅스를 실습할 수 있는 통합 IDE툴 (https://aws.amazon.com/ko/cloud9)

3. 맥 (osx)
: 맥과 리눅스와 뿌리가 같아 조작법이 비슷함. 간단한 리눅스 실습가능

4. virtual box (가상머신)
: 하드웨어를 소프트웨어적으로 구현해서 그 위에서 운영체제 작동시키는 방법


디렉토리와 파일
---------------
<code>ls</code> : 현재 디렉토리 목록

<code>ls -al</code> : 현재 디렉토리 목록. 숨김파일까지 전부 보여주고 상세보기모드

<code>ls -l</code> : 현재 디렉토리 목록. 상세보기

<code>pwd</code> : 현재 디렉토리 위치

<code>mkdir</code> : 디렉토리 생성


<code>cd 디렉토리경로</code> : 디렉토리 이동

<code>cd ..</code> : 상위 디렉토리 이동

<code>rm filename</code> : 파일 삭제

<code>rm -r 디렉토리명</code> : 디렉토리 삭제

<code>명령어 --help</code> : 명령어 매뉴얼 안내

<code>man 명령어</code> : 명령어 상세 매뉴얼 안내

<code>cp filename1 filename2</code> : 파일1을 파일2로 복사

<code>mv filename1 filename2</code> : 파일1을 파일2로 이동, 변경

<code>sudo 명령어 </code> : 관리자 권한으로 명령실행(super user do)


파일 편집 (nano에디터)
---------------
<code>nano </code> : 나노 새 파일 실행

<code>nano filename</code> : 나노 파일 수정

상세 명령어는 에디터 하단에 안내됨. get help(^G) 보면 매뉴얼 나옴.


패키지 매니저
---------------
외부 프로그램을 쉽게 설치할수 있는 방법. 
apt, yum 등이 있음.

<code>sudo apt-get update;</code> : 최신상태의 소프트웨어 *목록* 다운

<code>sudo apt-cache search keyword</code> : 설치가능한 목록중에 keyword라는 이름의 프로그램 검색

<code>sudo apt-get install program_name</code> : 프로그램 다운&설치

<code>sudo apt-get upgrade</code> : 설치된 프로그램 업데이트

<code>sudo apt-get remove program</code> : 프로그램 삭제


파일 다운로드 방법
---------------
#### 1. wget

<code>wget download_url</code> : 파일 다운로드

<code>wget -O filename download_url</code> : 지정된 이름으로 파일 다운로드

#### 2. git
<code>sudo apt-get install git </code> : 깃 설치
<code>git clone git_source_url </code> : 깃 소스 다운로드


왜 GUI가 아니라 CLI인가?
----------------
1. 그래픽으로 소모되는 에너지가 적다
2. 순차적으로 진행되는 일을 자동화 할 수 있다
3. 파이프라인
  - a명령어의 출력을 b명령어의 입력으로 사용. 계속 이어서 명령어를 여러개 사용하는 것
  - ex: <code> ls -help | grep sort </code> ls의 명령어의 사용설명서 텍스트 중 sort라는 글자를 찾아서 보여줌


IO Redirection
-----------------
- Input Redirection
  <code>ls -l > filename.txt </code> : 명령어실행결과를 파일에 저장
  
  <code>ls -l 2> filename.txt </code> : 명령어실행결과가 에러일 때 파일에 저장
  
  <code>ls -l 1> filename.txt 2> error.log </code> : 명령어실행결과는 파일에저장하고 에러내용이 있으면 또 다른파일에 저장
  
  <code>ls -l >> filename.txt </code> : 명령어실행결과를 파일에 이어붙여서(append) 저장
  
- Output Redirection
  <code>cat < filename.txt </code> : 파일에 있는 값으로 명령어 실행 


쉘과 커널
-----------------
- 쉘 : 사용자가 명령을 입력하면 컴퓨터가 이해할 수 있도록 하는 프로그램
- 커널 : 쉘에서 받은 명령을 하드웨어에 전달하는 중간역할


쉘 스크립트
-----------------
<pre><code>#!/bin/bash
if ![-d dak]; then
  mkdir bak  
fi
cp *.log bak
</code></pre>

:현재 dak라는 디렉토리가 없다면 bak 디렉토리 생성하는 내용의 명령어.

이렇게 여러 명령어를 파일에 저장해서 실행시키는 것을 쉘 스크립트라고 한다.

<code>#!/bin/bash</code>를 먼저 써주는 것이 문법이다.


디렉토리의 구조 
--------------

<code> / </code> : 최상위 디렉토리, 루트

<code> /bin </code> : binary(2진수, 실행 프로그램) 의 준말. 각종 명령어(ls, ps, ping ...)가 저장되어있음

<code> /sbin </code> : system binary 의 준말. reboot, ifconfig 등..

<code> /etc </code> : configuration files. 프로그램이나 운영체제의 설정파일

<code> /var </code> : variable files. 변수 파일들. 로그같은게 맘대로 바뀜

<code> /tmp </code> : temporary files. 임시 파일들. 껐다켜면 삭제됨.

<code> /home </code> : 사용자별로 사용자 파일이 저장되는 디렉토리.




프로세스
-------------
#### 1. 컴퓨터 구조
- CPU (processor)
- RAM (Memory)
- HDD/SSD (stroage)

**stroage에 설치된 프로그램 실행 -> memory에 프로그램 적재 -> 적재된 프로그램을 CPU가 읽어서 처리**

#### 2. 프로세스 모니터링

<code> ps </code> : 실행중인 프로세스 리스트
<code> ps aux </code> : 백그라운드에서 실행중인 모든 프로세스 리스트
<code> sudo top </code> : 실행중인 프로세스 리스트
<code> sudo htop </code> : top 이랑 비슷한데 더 시각적임.


파일 찾기
---------
<code> locate filename </code> : 파일 검색. 하루에 한번 리눅스에서 sudo updatedb 명령어를 통해 파일 위치 DB를 업데이트함

<code> locate *.log </code> : log라는 확장명을가진 모든 파일 검색.

<code> find </code> : 실제 디렉토리를 바탕으로 파일을 검색. 

<code> find . -name filename </code> : 현재 디렉토리 아래에 있는 filename을 검색

<code> find / -name filename </code> : 전체범위에서 filename을 검색

<code> find ~ -name filename </code> : 홈 디렉토리 아래에 있는 filename을 검색

<code> find . -name "filename" -exec rm -f {} \;  </code> : 검색한 파일을 삭제

<code> whereis filename </code> : 파일이 어디에 있는지 주소 반환

<code> $PATH </code> : PATH에 등록된 값들을 기준으로 명령어 파일을 찾아서 실행함. 유저가 직접 수정 가능. 이런 변수를 환경변수라고 함.


백그라운드 실행
-------------

<code> Ctrl + Z </code> : 명령어 실행중에 Ctrl + Z를 누르면 실행중이던 프로그램이 백그라운드로 감. 프로그램창 최소화랑 비슷

<code> fg </code> : foreground. 아까 백그라운드로 보낸 프로그램 다시 불러들임.

<code> fg %2 </code> : 아까 백그라운드로 보낸 프로그램 중 2번 호출

<code> jobs </code> : 지금 백그라운드에 실행되고있는 프로그램 보여줌

<code> 명령어 & </code> : 명령어 실행시 처음부터 백그라운드로 실행시킴

<code> kill -9 %4 </code> : 백그라운드에 실행중인 프로그램 강제(-9옵션) 종료


항상 실행되는 프로그램 (daemon, service)
------------------
가전제품으로 따지면 냉장고 같은! 프로그램을 말함.

- 예제 : 아파치2 웹서버를 설치해서 실행 후 확인

<code>sudo apt-get install apache2</code>

<code>sudo service apache2 start</code>

<code>ps aux | grep apache2 </code>

<code>sudo service apache2 stop</code>

- 예제 
<code>/etc/rc3.d</code>에 부팅시에 자동실행되는 프로그램들이 링크되어있음



정기적으로 실행(cron)
----------------------
<code>crontab -e</code> : 정기적으로 실행시킬 명령어 모음집 편집

<code>분(0-59) 시간(0-23) 매달무슨날(1-31) 달(1-12) 요일(0-6) 명령어</code> : 순서로 지정


쉘을 시작할 때 실행
-----------------------
<code>alias l='ls -al' </code> : 'ls -al' 명령어를 l로도 쓸수 있게 별칭을 지어주는 작업. 주로 alias를 쉘 시작시에 실행한다.
<code>echo $SHELL </code> : bash는 홈디렉토리의 .bashrc 파일에서 쉘을 시작할 때 실행하는 명령어를 편집할 수 있다.


다중 사용자
--------------------
<code>id</code> : 자신의 유저 id정보가 나옴

<code>who</code> : 지금 접속해 있는 유저들이 나옴


관리자와 일반 사용자
-------------------
<code>su - root</code> : 접속정보를 슈퍼유저로 바꿀 때 사용하는 명령어

<code>sudo passwd -u root </code> : 보통은 보안상문제로 슈퍼유저 접속을 막아놓기 때문에 루트사용자의 패스워드를 unlock하기 위해 필요한 명령어

<code>sudo passwd -l root </code> : 언락한 루트 계정을 다시 lock


사용자 추가
----------------
<code>sudo useradd -m username</code> : username이라는 사용자 추가

<code>sudo usermod -a -G sudo username</code> : 유저계정을 사용자 그룹에 추가해서 패스워드를 지정할 수 있게함


권한
----------------
사용자들이 권한에 따라서 파일과 디렉토리를 사용할 수 있게함

<code>-rw-rw-r-- 1 owner group</code> : ls -l 했을 때 파일마다 나오는 부분. 맨 첫째자리는 type(file은 - / directory는 d),
                                        그 다음 9자리는 access mode

<code>rw-|rw-|r--</code> : access mode를 3등분하면 첫번째구역은 owner, 두번째구역은 group의 권한, 세번째 구역은 나머지사람들의 권한을 뜻한다.
                          r:읽기, w:쓰기, x:실행, -:권한없음 


<code>chmod o-r filename</code> : 파일이나 디렉토리가 가지고있는 others에 대한 read 권한을 없앤다. 소유자는 u로 쓴다.

<code>chmod o+r filename</code> : 파일이나 디렉토리가 가지고있는 others에 대한 read 권한을 준다.

<code>chmod 111 filename</code> : 권한을 바꿀 때 숫자로도 할 수 있다. 권한을 대상별로 3등분했을 때 각각 가지고 있는 
                                  r, w, x권한을 2의0승/2의1승/2의2승으로 표현한다. 예를들어 권한아예 없음은 0 권한 전부 있음을 7(1+2+4)로 표현


그룹
---------------
<code>useradd -G groupname username</code> : 유저 추가할 때 그룹지정

<code>sudo groupadd groupname</code> : 그룹 생성

<code>sudo usermod -a -G groupname username</code> : 이미 있는 유저에 그룹 추가

<code>chown username:groupname</code> : 파일의 소유자나 그룹을 변경





인터넷, 네트워크 그리고 서버
----------------------
client <-> server : request와 response를 주고받음. 인터넷을 매개로 하며 URL이나 ip주소를 통해 접근.
실제로는 URL입력하면 DNS 서버에서 도메인이름으로 ip주소를 알아내어 ip주소를 통해 접근한다. 
ip는 public address와 private address 두가지로 나뉜다. 두가지는 일치할수도 있지만 거의 다르다. private address는 서버컴퓨터의 실질적인 주소이고
public address는 실제 서버로 통하는 관문인 라우터의 주소이다. 


웹서버 (아파치)
------------------------
서버에서 웹 요청에 대해 응답을 주려면 웹서버가 필요하다. 대표적으로 apache, nginx, IIS 있다. 

<code>sudo apt-get install apache2</code> : 아파치 설치

<code>sudo service apache2 start</code> : 아파치 작동

<code>sudo service apache2 stop</code> : 아파치 중지

<code>sudo service apache2 restart</code> : 아파치 중지

<code>sudo apt-get install elinks</code> : 쉘에서 서버에 접속할 수 있게 하는 프로그램 설치

<code>ip addr</code> : 접속하고자하는 컴퓨터 ip확인 

<code>elinks http://10.0.2.15/</code> : 해당 ip로 접속 

<code>selinks http://localhost</code> : 자신의 컴퓨터에 존재하는 웹서버에 접속할 때는 localhost(=127.0.0.1)라는 키워드를 사용

<code>nano /etc/apache2/sites-enabled/000-default.conf</code> : 아파치 설정파일 확인. 웹서버 접속시에 보여줄 페이지를 찾을 루트 디렉토리, 로그 저장위치 등을 설정

<code>tail /var/log/apache2/access.log</code> : 로그파일 확인. 접속요청한 정보가 뜬다. 에러로그는 error.log


원격제어(ssh)
-------------
원격으로 쉘을 제어할 수 있는 방법. ssh client <-> ssh server

<code>sudo apt-get purge openssh-server openssh-client</code>: ssh 강력삭제!

<code>sudo apt-get install openssh</code>: ssh 서버 설치

<code>sudo service ssh start</code>: ssh 실행

<code>ssh username@192.168.0.65</code>: 클라이언트에서 서버컴퓨터 접속


포트(port)
----------------
: 서버 요청시에 포트번호를 적지않아도 생략되어 있음. 웹은 80번 ssh는 20번 이런식으로 지정된 포트로 접속함. 
1024번까지는 통신에 필요한 표준 프로그램들이 지정되어 있음. 최대 65000개 정도까지 있음. 

<code>ssh -p portnumber username@192.168.0.65</code>: 특정 포트로 접속

- 포트 포워딩 : 퍼블릭아이피(default gateway)를 통해서 router까지는 갈 수 있지만 그 내부에 컴퓨터로는 접속 할 수 없다. 
이 때 내부 컴퓨터별로 포트를 할당해서 외부에서도 접속할 수 있게 할 수 있다.

<code>ip route</code>: 내 컴퓨터의 디폴트 게이트웨이 아이피가 나온다. 이 아이피에 접속하면 일반적으로 공유기 설정 페이지로 가게된다. 여기에서 포트 포워드를 설정할 수 있다.



도메인
---------
- 도메인 : 도메인 서버에 어떤 도메인에 해당하는 ip를 저장해서, 브라우저에 도메인주소만입력해도 접속ip를 찾아서 연결해준다. 이런 기능을 사용하려면 도메인을 구매해야한다.

- 서브도메인 : cafe.naver.com, blog.naver.com 이런걸 서브도메인이라고 한다. 서브도메인 별로 각각 다른 서버를 연결할 수 있다.


인터넷을 통한 서버간 동기화 (rsync)
-----------------------------
<code>rsync -a original destination</code>: original에 있는 파일을 destination으로 복사하여 동기화. 

<code>rsync -azP local/directory username@192.168.0.65:~/directory</code>: z option- 압축, P option - 진행상황 보여줌. 컴퓨터와 컴퓨터 사이에 원격으로 파일을 싱크할 수 있다




로그인 없이 로그인 하기 (ssh key)
----------------------------
ssh공개키를 사용해서 id/pw 입력없이 로그인하는 방법

1. <code>ssh-keygen</code>: ssh키 생성 

2. <code>ssh-copy-id user@192.168.0.67</code>: 접속하고자하는 컴퓨터의 ~/.ssh/authorized_keys 라는 파일에 생성한 ssh 퍼블릭키의 내용을 이어붙인다. 

3. <code>rsync -avz . user@192.168.0.67:~/directory</code>: rsync는 기본적으로 ssh를 통해서 동작. 퍼블릭키가 등록돼있지 않으면 실행되지않음.


