# OAuth
- 두 개의 서비스를 연동하고자 할 때 제 3자인 사용자를 인증하는 방식.
- 페이스북이나 트위터에서 외부서비스가 일부기능을 사용할 수 있게 할 때의 인증 방식이다.
- 로그인의 개념이 사원증을 통해 건물에 출입하는 것이라면, OAuth는 방문증과 같은 개념이다. 
- 신생업체에서는 고유의 인증방식보다 페이스북이나 트위터의 OAuth 인증을 이용하여 개발/운영 비용을 줄이고 홍보효과까지 누리고 있다. 


### OAuth 1.0

##### 용어
>       User     -     Consumer     -     Service Provider

- User : Service Provider 에 계정을 가지고있으면서, Consumer를 이용하려는 사용자. ex) 일반 사용자
- Service Provider : OAuth를 사용하는  Open API를 제공하는 서비스 
ex) 트위터, 페이스북
- Consumer : OAuth 인증을 통해 Service Provider의 기능을 사용하려는 어플리케이션이나 웹서비스
ex) 운세, 통계, 심리테스트 앱


##### TOKEN

#### Request Token
- Consumer가 Service Provider에게 접근권한을 인증받기 위해 사용하는 값, 인증이 완료된 후에는 Access Token으로 교환한다.
 
#### Access Token
- 인증 후 Consumer가 Service Provider의 자원에 접근하기 위한 키를 포함한 값
- 지속적으로 가지고있으면서 허가된 행동을 할 때 사용되는  토큰 

#### OAuth 1.0 인증과정
![](https://oauth.net/core/diagram.png)

##### consumer 인증
1. consumer가 Request Token 요청 
2. Service Provider가 Request Token 허가 
3. 사용자 인증(로그인)

##### Access 키 발급
4. consumer가 Access Token 요청 
5. Service Provider가  Access Token 허가 
6. Access Protected Resource


#### oauth_signature
- OAuth 인증 정보를 암호화하고 인코딩한 서명 값.
- 토큰 생성을 요청/응답할 때 필요한 정보들을 매개변수라고 한다. 
##### oauth_signature 생성 순서 
1. ‘oauth_’로 시작하는 요청 매개변수를 모두 모은다.
2. 매개변수들을 정규화(normalize) : 사전순으로 정렬하고 키/밸류에 URL 인코딩
3. Signature Base String 생성 : HTTP method이름, Consumer가 호출한 URL 주소, 정규화한 매개변수를 ‘&’를 사용해 혼합
4. 키 생성 : Signature Base String을 Consumer Secret Key를 통해 암호화. Consumer Secret Key는 Consumer가 Service Provider에 사용등록할 때 받은 값이다.  


### OAuth 2.0
- OAuth 1.0은 웹 어플리케이션이 아니면 사용하기 곤란하고 절차가 복잡하여 구현이 어렵고 연산부담도 발생한다는 단점이 있다. 
- OAuth 2.0에서는 이런 단점을 개선하였다. 하지만 아직 1.0과 호환성이 없고 최종안이 나온게 아니지만 사용되고 있다.

#### OAuth 2.0 특징
- 웹 어플리케이션이 아닌 어플리케이션 지원 강화
- 암호화 필요없음. HTTPS사용. 
- Signature 단순화 정렬과 URL인코딩 필요 X
- 보안강화를 위해 Access Token의 Life-time을 지정할 수 있다. 원래는 만료 개념이없었음.
- 2.0에서는 1.0과 용어와 개념이 완전히 다르지만 아직 최종안이 없는 상태라 앞으로 정의가 바뀔 수 있다.

#### 용어
- resource owner : protected resource 에 접근하는 권한을 제공
- resource server : access token을 사용해서 요청을 수신할 때 권한을 검증한 후 적절한 결과로 응답 
- client : protected resource 에 접근을 요청하는 어플리케이션
- authorization server : 클라이언트가 성공적으로 access token을 발급받은 이후에 resource owner인지 인증하고 권한을 부여한다.

#### OAuth 2.0 인증과정

> resource owner - client - resource server 

1. Resource owner가 client에 접속

2. client에서 인증요청하면  Resource server에 접속

3. Resource owner가 로그인하고 필요한 scope list(권한) 선택 

4. Resource server가 client에 Authorization code 전송

5. client 가 resource server에 Authorization code를 보내면서 자신을 인증

6. Resource server에서 client에 access token을 줌 

7. client에서는 Resource server에 access token을 통해 api를 사용할수 있게됨


> TODO: google, twitter 등으로 실습해볼 것 !
