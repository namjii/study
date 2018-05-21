# REST API (Representational State Transfer)
- HTTP 기반으로 필요한 자원에 접근하는 방식을 정해놓은 네트워크 아키텍쳐 
- 지속적인 연결이 없는 상태에서 __데이터를 교환하는 방식__. 일반적으로는 HTTP위에서 작동한다. 
- 정확히 정의된 표준 프로토콜이 아니라 아키텍쳐 스타일(구현 방식)이다.
- URI 기반으로 리소스에 접근하는 기술

     Request: GET http://www.domain.com/user/1
 
     Response: XML / JSON / String / …
     
- 어느 장비에서나 지원하는 HTTP프로토콜 사용
- HTTP 프로토콜 그 자체에 집중하며  간단하다는 장점을 이용

##### REST API의 탄생
2000년도에 로이 필딩(Roy Fielding)의 박사학위 논문에서 최초로 소개. HTTP의 주요 저자 중 한 사람으로써,   당시 웹 설계의 우수성에 비해서 제대로 사용되어지지 않는 모습에 발표했다. 

### REST의 특징

#### 클라이언트/서버 
- 서로 어떻게 구현되어있는지 서로 알 수 없고 일관적인 규칙으로 통신한다.
- 클라이언트와 서버의 역할이 구분되어있다. 서버는 API를 제공하고 요청시 로직 처리. 클라이언트는 사용자 인증과 세션을 관리하고 로그인정보 관리 서버로 리소스 요청.

#### 무상태성 (Stateless) : 
- 작업을 위한 상태정보(session, cookie)을 따로 저장하고 관리하지 않기 때문에 API서버는 들어오는 요청만을 단순히 처리하면 된다. 
- 서비스의 자유도가 높아지고 불필요한 정보를 관리하지 않아 구현이 단순해진다.
- 서버가 클라이언트의 상태를 관리할 필요가 없음. 필요한 경우에는 해당 상황에 대한 정보를 직접 관리한다.

#### 자제 표현구조(Self-descriptiveness)
- 자체적인 표현 방법을 가지고 있어 REST API 메시지만 보고도 이를 쉽게 해석할 수 있다.

#### 인터페이스 일관성(Uniform interface)
- 아키텍처를 단순화 하고 분리해 각 부분을 독립적으로 발전 시킬 수 있음.
- __리소스를 URI로 식별하고, JSON/XML 등으로 리소스를 표현, 헤더에 데이터에 대한 정보가 담겨있음.__


### REST 주요 구성요소 

- 리소스 : 접근할 대상. URI를 통해 식별

- 메소드 : 리소스에 대한 행위. 표준 HTTP 메소드에 따라 자원에 접근(CRUD)

- 메시지 : HTTP 헤더와 바디에 포함된 메시지는 메시지를 처리하기 위한 충분한 정보를 포함

#### 리소스
URI를 통해서 정리
> http://www.domain.com/books 
도서정보 리스트

> http://www.domain.com/books/1
1번 도서정보

>http://www.domain.com/books/1/photo
1번 도서정보의 사진

- URI(Uniform Resource Identifier) vs URL(Uniform Resource Locator)
: URL은 위치라는 의미를 담고있어서 적절치않다.

##### 명명 규칙
- 리소스명은 동사보다 명사를 활용해서 자원을 표현한다.
- 슬래시는 계층관계를 구분하며 뒤로 갈수록 넓은의미로 시작해 좁은 의미를 정의한다.
   ex) /sports/soccer/players/13
- 소문자만 사용
- 확장자를 넣지 않는다
- 마지막 문자로 슬래시를 쓰지 않는다.
- 가독성을 높이는 데에는 ‘-‘을 사용한다. (‘_’ 은 사용하지 않음)
- CRUD는 URI에 표시하지 않는다.


##### 리소스 형식 
- 도큐먼트(Document) : 가장 기본이되는 리소스 형식. 데이터베이스 레코드단위와 비슷. 단수표현 ex) 1번 도서
- 컬렉션(Collection) :  도큐먼트의 리스트 ex) 도서정보 리스트. 복수표현
- 컨트롤러(Controller) : CRUD 이외의 것. 동사/동사구 ex) buy
- (스토어(Store) : 클라이언트가 특별히 관리하는 형태를 갖는 것. 복수표현 ex) favorites, wish, mark, done )

#### 메소드
- 메소드를 통해 리소스에 대한 행위를 정의한다. 

##### 메소드 종류

- POST : 자원 생성 (Create)
- GET : 자원 조회 (Read)
- PUT :  자원 수정 (Update)
- DELETE : 자원 삭제 (Delete)

##### Endpoint
URI별 메소드로 구현된 항목
- POST http://www.domain.com/books : 새로운 도서정보 생성
- GET http://www.domain.com/books : 도서정보 조회
- GET http://www.domain.com/books/1 : 1번도서 조회
- PUT http://www.domain.com/books/1 : 1번도서 수정
- DELETE http://www.domain.com/books/1 : 1번도서 삭제

#### 메시지
Rest에서 자원에 대한 정보는 HTTP 바디와 헤더 응답상태코드를 활용한다.

##### HTTP 바디
- 바디에 포함된 데이터로 자원에 대한 정보전달. 
- 데이터 포맷으로는 JSON이 많이 쓰이며 XML도 가능. 
- GET 요청시 서버는 조건에 맞는 정보를 바디에 담아 클라이언트에 응답
- POST, PUT 요청시 클라이언트는 자원에 대한 정보를 HTTP바디에 담에 서버에 요청

##### HTTP 헤더
- HTTP바디에 담긴 컨텐츠 타입을 명시하여, 타입에 따라 데이터를 해석하도록한다. 
- 요청 헤더에는 “Accept”, 응답 헤더에는 “Content-Type”으로 정의한다.
- 컨텐츠 타입 예시 
  : application/json, application/xml, text/plain, image/png

##### 응답 상태코드
- 리소스 요청에 대한 응답은 응답 상태코드로 설명한다.
- 클라이언트에게 적절한 응답코드를 주는 것은 매우 중요하다.

- 200 ~ 399: Successful HTTP Response
    - 200 : OK (HTTP Message Body 있음)
    - 201 : OK (POST에 요청시)
    - 204 : OK but no content (HTTP Message Body 없음)
    - 3xx : 실패하지 않은 요청중 비정상 처리
    - 301 : 클라이언트가 요청한 리소스에 대한 URI가 변경됨. Location header에 변경된 URI명시.
- 400 ~ 599: Error HTTP Response
    - 400 : 요청이 부적절
    - 401 : 인증되지 않은 상태에서 보호된 리소스 요청
    - 403 : 공개되지 않은 리소스에 접근요청(인증과 무관)
    - 404 : Not Found (해당하는 URI 없음)
    - 405 : Method Not Allowed (허용된 Method랑 다름)
    - 406 : Not Acceptable (accept-header가 틀림)
    - 409 : 리소스 상태에 의해 해당 요청을 수행하지 못함
    - 5xx : 서버에러
