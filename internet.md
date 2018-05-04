# 인터넷
참고: https://opentutorials.org/course/228/1450, 
http://blog.naver.com/PostView.nhn?blogId=hys7756&logNo=220839427918,
https://developer.mozilla.org/ko/docs/Web/HTTP

### 도메인이란?

#### IP  
인터넷에 연결되어있는 장치를 식별할 수 있는 주소 ex) 115.68.24.88

#### 도메인  
IP는 사람이 기억하고 이해하기 어렵기 때문에 IP에 이름을 부여한 것
<pre><code>
opentutorials.org -> 115.68.24.88
</code></pre>

#### 도메인의 구성요소  
* opentutorials.org  
    * opentutorials : 컴퓨터 이름  
    * org : 최상위 도메인 - 비영리단체  

* daum.co.kr
    * daum : 컴퓨터 이름
    * co :  국가형태의 최상위 도메인을 의미
    * kr : 대한민국의 NIC에서 관리하는 도메인을 의미

#### URL의 이해  
도메인 : 장치를 식별하기 위한 주소  ex) opentutorials.org
URL : 도메인 + 경로  ex) https://opentutorials.org/course/228/1450



### 도메인 검색 및 구입

#### 도메인 검색
- 누군가 선점하지 않은 도메인 검색 
- 도메인 입업체에서 도메인 검색기능 제공
- 도메인 업체 검색

#### 도메인 선정 고려사항
- 선호하는 최상위 도메인을 선택한다. com
- 쓰임에 맞는 최상위 도메인을 선택한다. ex) 비영리 서비스인 생활코딩의 홈페이지는 .org
- 도메인 이름에 최상위 도메인을 포함시킨다.    예를들면, flickr.com 는 flic.kr, delicious.com은 del.icio.us
- 짧을수록 좋다.
- 키보드 자판상에서 좌우 대칭이 입력하기에 편리하다.
- 악의적인 선점에 대비해서 예비 도메인을 구입하는 것이 유리


### 호스트 설정

#### 호스트
네트워크에 연결되어 있는 컴퓨터

#### 호스트 설정 
도메인을 호스트의 IP에 연결하는 행위

#### 도메인과 호스트의 관계
먼저 네임서버에서 IP를 찾아온 후 연결

#### 하나의 도메인으로 여러개의 호스트에 연결
ex) www.naver.com, blog.naver.com, cafe.naver.com



### 포워딩 설정

도메인으로 접근한 사용자를 다른 도메인으로 보내는 행위
ex) ooo2.org로 사용자가 접근하면 opentutorials.org로 보내는 것
보통 호스트를 설정할 수 없을 때 사용한다.

#### 호스트 설정과 포워딩의 차이
호스트 설정은 도메인과 IP를 연결하는 것이지만 포워딩은 다른 도메인으로 보내는 것이기 때문에 포워딩한 사용자의 URL이 변경됨



### 네임서버

#### 네임서버
도메인에 해당하는 IP를 알려주는 서비스


### hosts 파일

#### 브라우저가 도메인에 해당하는 IP를 찾는 순서
1. 로컬 캐시를 검색
2. hosts 파일을 검색
3. 도메인 네임서버를 검색


### HTTP
- Hypertext Transfer protocol. HTML(하이퍼텍스트 문서)를 WWW상에서 주고 받을수 있게하는 프로토콜
- 신뢰할만한 전송/세션 레이어의 커넥션을 통해 메시지를 주고받는 상태가 없는 요청/응답 프로토콜

User Agent <--------------------> Origin

#### HTTP 역사
- 0.9
: GET 메소드만 존재. HTML파일만 전송가능. 상태/오류 코드가 없고 문제시 설명과 함께 리턴됨

- 1.0 (RFC 1945)
: GET, HEAD, POST 메소드 지원. 상태코드 지원. 헤더가 있고 Content-Type을 정의해서 HTML이외의 파일도 전송가능. 

- 1.1 (Standard)
: GET, DELETE, POST 지원, 커넥션재사용, 요청/응답 파이프라이닝

#### HTTP 메시지 구조
: HTTP 메시지는 서버와 클라이언트 간에 데이터가 교환되는 방식이다. Request, Response 두 가지 타입이 있다.
ASCII로 인코딩된 텍스트라서 읽을 수 있는 형태이며 주로 브라우저, 웹서버에서 이러한 내용을 만들어낸다.

##### 1. Request
###### 1. start line
<pre><code>
POST / HTTP/1.1
</code></pre>
HTTP 메서드, 요청대상 경로, HTTP 버전

###### 2. header 
key: value 형태이며, 한 줄에 하나씩이라 값이 길면 한 줄이 상당히 길어진다. key와 콜론사이에 공백이 들어가면 안된다. 대소문자는 구별하지 않는다.
헤더는 몇 가지 그룹으로 나누어진다. 
<pre><code>
Host: localhost:8000
User-Agent: Mozilla/5.0 (Macintosh; ...) ... Firefox/51.0
Accept: text/html, application/xhtml+xml, ..., */*; q=0.8
Accept-Language: en-US, en; q=0.5
Accept-Encoding: g-zip, deflate                           <- 여기까지 Request Headers
Connection: keep-alive
Upgrade-Insecure-Requests: 1                              <- 여기까지 General Headers
Content-Type: multipart/form-data; boundary=-123656974
Content-Length: 345                                       <- 여기까지 Entity Headers

</code></pre>

- Content-Type  
  'primary object type / sepcific subtype' 형태로 정의된다. 컨텐츠 타입에 따라 브라우저가 해석하는게 달라진다.
   ex) text/plain, text/html, image/png, application/json...

- HTTP method  
  Safe: readonly, Idenpotent: 여러번 요청해도 같은값을 가져옴   
     
  - GET(Safe, Idempotent)
  
  - POST(Unsafe, Non-Idempotent)
  
  - PUT(Unsafe, Idempotent)
  
  - DELETE, PATCH, OPTIONS, HEAD, TRACE, CONNECT 가 있다.
   
- 상태코드
<pre><code>
1xx - Informational
2xx - Success
3xx - Redirection
4xx - Client error
5xx - Server error

</code></pre>

###### 3. blank line

###### 4. body 
모든 요청들에 본문이 있는 건 아니다. GET, HEAD, DELETE, OPIONS 처럼 리소스를 가져오는 요청은 본문이 필요없다.
대게 POST인 경우에 필요하다. Content-Type과 Content-Length 헤더값에 따라서 정의된다.

##### 2. Response
###### 1. start line
<pre><code>
HTTP/1.1 403 Forbidden
</code></pre>
HTTP 버전, 요청 코드, 상태코드 간략설명 

###### 2. header 
<pre><code>
Access-Control-Allow-Origin: *                      -> Response headers
Connection: Keep-Alive                              -> General headers
Content-Encoding: gzip                              -> Entity headers
Content-Type: text/html; charset=utf-8              -> Entity headers
Date: Wed, 10 Aug 2016 13:17:18 GMT                 -> General headers
Etag: "d9b3b803e9a0dc6f22e2f20a3e90f69c41f6b71b"    -> Response headers
Keep-Alive: timeout=5, max=999                      -> General headers
Last-Modified: Wed, 10 Aug 2016 05:38:31 GMT        -> Entity headers
Server: Apache                                      -> Response headers
Set-Cookie: csrftoken=....                          -> Response headers
Transfer-Encoding: chunked                          -> General headers
Vary: Cookie, Accept-Encoding                       -> Response headers
X-Frame-Options: DENY                               -> Response headers

</code></pre>

###### 3. blank line  

###### 4. body    
응답의 마지막부분은 본문이다. 모든 응답이 본문을 갖진 않는다. 

#### HTTP 트랜잭션
서버는 80번포트를 열고 요청대기 -> 클라이언트에서 URL 입력 -> 웹브라우저는 DNS에 물어봐서 URL의 IP 알아냄 -> 알아낸 IP와 포트번호 80번으로 TCP Connection을 연다 -> 브라우저에서 TCP connection에 GET요청 -> 서버는 요청확인 -> 응답메시지 생성해서 TCP Connection -> 웹브라우저는 TCP connection 응답확인 -> 클라이언트는 Content-length, ContentType을 참고해서 HTML 렌더링

- URL
<code>
[scheme]://[host]:[port]/[path]?[query]#[fregment]
</code>

- GET
<pre><code>
요청
Telnet example.com 80   -> 터미널에서 접속
GET /index.html HTTP/1.1  
Host: www.example.com -> 테스트용으로 기관에서 제공하는 URL

응답
HTTP/1.1 200 OK 
Cache-Control: max-age=604800
Content-Type: text/html 
Content-Length: 83 
Etag: "142342351"
Date: Wed, 14 Feb 2013 06:25:24 GMT 
Hello, World
</code></pre>


- POST
: form 제출, 데이터베이스에 데이터 추가하기 위한 메소드
  POST이후에 redirect 응답할 때, 303으로 하는 것이 맞지만 HTTP/1.0 호환을 위해 301, 302을 쓴다.
  redirect 할 때 POST를 유지할건지 GET으로 바꿀건지에 따라 308, 307을 쓸지 301, 302를 쓸지 결정.
  
- PUT
 : 생성, 대체할 때 사용. 성공시 200, 해당위치에없으면 201
 
- DELETE
 : 삭제할 때 사용. 202 Accepted, 204 No content, 200 OK로 응답 
 
- Conditional GET
 : 예전에 요청했던 내용 또 불러오면 낭비니까 변경된거있는지만 확인해서 보내달라고 하는 경우. 헤더에 Last-Modified 내용으로 파악. 변경된게 없을 경우 304 Not modified 응답. 아니면 ETag(고유id)로 변경여부를 확인할 수도 있다.

- Cache
서버와 클라이언트를 오고가는 HTTP 메시지를 저장. 서버까지 가지않아도 브라우저 안에서 페이지 렌더링가능.

#### State Management
: 로그인, 카트 목록 유지 등

- 쿠키
Set-Cookie 응답헤더를 서버에서 클라이언트로 보내면, 클라이언트는 쿠키를 보관하고있다가 필요할 때 인증하기 위해 보여줌

#### HTTPS 인증




### HTTPS와 SSL인증서

#### HTTPS VS HTTP
HTTPS에서의 S는 Secure로 보안이 강화된 HTTP라고 생각하면된다. HTTP 메시지를 암호화하여 주고받는다.
 

#### HTTPS와 SSL
두 가지가 같은 의미로 쓰일 때도 있지만 정확히는 HTTPS는 SSL프로토콜 위에서 돌아가는 프로토콜이다.

#### SSL과 TLS
두 가지는 같은 말이다. 네스케이프에 의해서 SSL이 발명되었고 보편화되면서 표준화 기구인 IETF가 관리하게 되면서 TLS라는 이름으로 바뀌었다.  

HTTP - 네트워크 인터페이스 > IP > TCP > __TLS__ > HTTP
 
#### SSL 디지털 인증서
SSL인증서는 클라이언트와 서버간의 통신을 제 3자가 보증해주는 전자화된 문서.
클라이언트가 서버에 접속한 직후에 서버는 클라이언트에게 이 인증서 정보를 전달하면 클라이언트에서는 인증서를 검증한 후 요청된 작업을 수행한다. SSL인증서를 사용하면 통신내용 노출과 변조를 막을 수 있고, 클라이언트가 접속하려는 서버가 신뢰할만한지 알수 있다. 

#### SSL에서 사용하는 암호화 종류
1. 대칭키

암호화할 때 사용하는 일종의 비밀번호를 키라고한다. 이 키를 가지고 암호를 푸는 복호화를 할 수 있다. 대칭키는 동일한 키로 암호화와 복호화를 하는 방식이다.

2. 공개키

대칭키 방식은 암호를 주고받는 사람들 사이에 대칭키를 전달하기 어렵다는 단점이 있다. 대칭키가 유출되면 암호를 복호화 할 수 있기 때문에 무용지물이 되기도 한다. 그래서 키를 두개 사용하는 공개키 방식이 나왔다. A키로 암호화하면 B키로 복호화하는 방식이다. 키 하나는 비공개키로 자신만이 가지고 있고, 나머지 하나는 공개키로 타인에게 제공한다. 이 공개키를 통해서 정보를 암호화하여 비공개키를 가진 사람에게 전송한다. 이런 방식을 사용하면 공개키가 유출되어도 정보가 유출되지 않는다. 

3. SSL 인증서

클라이언트가 접속한 서버가 신뢰할 수 있는 사이트임을 보장. SSL 통신에 사용할 공개키를 클라이언트에게 제공.

- CA

사이트의 신뢰여부를 보장하는 기업들을 Certificate Authority 라고한다. SSL을 통해서 암호화된 통신을 제공하려면 CA를 통해서 인증서를 구입해야한다. 

- 사설인증기관

직접 자신이 CA의 역할을 할수도 있는데 이런경우 브라우저에서 경고를 출력한다.

- SSL 인증서의 내용

서비스의 정보(인증서를 발급한 CA, 서비스의 도메인 등), 서버측의 공개키와 같은 정보를 담고있다. 이런 정보들은 CA가 공개키방식을 통해서 암호화시킨다.

- 브라우저에서는 내부적으로 공인된 CA 리스트가 등록되어있다.

- SSL 동작방법

SSL은 암호화된 데이터를 전송하기 위해 공개키와 대칭키를 혼합해서 사용한다. 실제 데이터는 대칭키 방식으로 암호화하고, 이 대칭키는 공개키 방식으로 암호화한다. 이런 통신은 악수-> 전송-> 세션종료 3단계를 통해서 이루어진다.

  - 악수 : 실제 데이터를 주고받기전에 클라이언트와 서버는 일종의 인사인 Handshake를 한다. 이 때 SSL인증서를 주고받는다. 
	
    1. Client Hello : 클라이언트가 서버에 접속한다. 클라이언트 측에서 생성한 랜덤데이터, 클라이언트가 지원하는 암호화방식, 세션아이디를 전송한다.
    
    2. ServerHello : Client Hello에 대한 응답. 서버 측에서 생성한 랜덤데이터, 서버가 선택한 클라이언트의 암호화방식, 인증서를 전송한다.
    
    3. 클라이언트는 서버의 인증서가 공인된것인지 내장된 CA리스트를 통해 확인한다. 확인할 때 내장된 CA의 공개키를 통해서 복호화가 성공하면 보증된 인증서이다. 만약 CA리스트에 인증서가 없다면 사용자에게 경고메시지를 출력한다. 그리고 1~2번 단계에서 생성한 서버의 랜덤데이터와 클라이언트의 랜덤데이터를 조합해서 pre master secret key 를 생성한다. 이 키는 handshake 다음단계인 세션단계에서 주고받을 데이터를 암호화하는데 쓰인다. 지금 단계에서는 클라이언트에서 pre master secret 키를 서버의 공개키로 암호화해서 서버로 안전하게 전달한다.
    
    4. 서버는 클라이언트가 전송한 pre master secret 키를 자신의 비공개키로 복호화한다. 이제 서버와 클라이언트는 일련의 과정을 거쳐서 pre master secret 값을 가지고 동일한master secret 값을 만들어낸다.  (이 master secret 값으로 세션키를 서버, 클라이언트 양쪽에서 생성한 후 대칭키 방식으로 데이터를 주고받게 된다.)
    
    5. 클라이언트와 서버는 핸드쉐이크 단계종료를 서로 알린다 
 
2. 세션
실제로 서버와 클라이언트가 데이터를 주고받는 단계. 핸드쉐이크 단계에서 생성한 session key값을 이용해 대칭키 방식으로 데이터를 암호화한다.  대칭키 방식을 사용하는 이유는 이미 앞에서 공개키방식을 사용하여 컴퓨터 파워를 많이 사용했기 때문에 자원을 아끼기 위해 속도는 느리지만 데이터를 안전하게 주고받을수 있는 공개키 방식으로 대칭키를 암호화하여 사용하는 것이다.

3. 세션 종료
데이터의 전송이 끝나면 SSL 통신이 끝났음을 서로에게 알린다. 이 때 통신에 사용한 대칭키인 세션키를 폐기한다.


### HTTP/2
- HTTP/1.1 보다 빠름
- 추가 기능: 헤더 압축, 한 번에 여러개 통신, 서버가 요청전에 미리예측해서 보냄, 필요한 파일들의 우선순위대로보내서 렌더린속도높임

