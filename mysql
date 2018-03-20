DB - MySQL
=================
참고 사이트 : https://opentutorials.org/course/3161/19531


데이터베이스의 목적
-----------------
엑셀이 있음에도 데이터베이스를 사용하는 이유는 컴퓨터 언어를 통해서 데이터를 조작할 수 있다는 점 때문이다. 
웹이나 앱에 데이터를 연결하거나 아니면 데이터를 대용량으로 분석할 수도 있다.


MySQL 설치
----------------
1. https://www.mysql.com/products/community/ 에서 다운로드 및 설치

2. <code>cd /usr/local/mysql/bin </code> : mysql이 있는 폴더로 이동

3. <code>./mysql -uroot -p</code> : root사용자로 접속하여 mysql구동 비밀번호 입력요구함. 1번에서 설치시 나왔던 비밀번호를 입력한다.


MySQL 구조
-----------------
관계형 데이터베이스, 엑셀같은 표에 데이터가 저장된다. 이런 표들을 그룹핑한 것을 스키마 혹은 데이터베이스라고 한다. 
데이터베이스의 상위개념으로는 데이터베이스 서버가 있다. 


MySQL 서버접속
-------------------
<code>./mysql -uroot -p </code> : root계정으로 mysql 데이터베이스 서버 접속


MySQL 스키마(schema)의 사용
-------------------------
<code>CREATE DATABASE database_name</code>: 데이터베이스 생성

<code>DROP DATABASE database_name</code>: 데이터베이스 삭제

<code>SHOW DATABASES</code>: 데이터베이스 리스트 확인 

<code>USE database_name</code>: 특정 데이터베이스 사용


MySQL 테이블 구조
-------------------
- 열 :컬럼(column) 데이터의 구조
- 행 : row, record, 데이터 그 자체


MySQL 테이블 생성
--------------------
<pre><code>
CREATE TABEL table_name(
  id INT(11) NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL, 
  ... 
)
</code></pre>


MySQL INSERT
-------------------
상세 : https://dev.mysql.com/doc/refman/5.7/en/insert.html
<code>INSERT INTO table (field1, field2, field3) VALUES(value1, value2, value3) </code>

MySQL SELECT
-------------------
상세 : https://dev.mysql.com/doc/refman/5.7/en/select.html
<code>SELECT field1, field2, field3 FROM table </code>

<code>SELECT field1, field2, field3 FROM table WHERE field1='value'</code>

<code>SELECT field1, field2, field3 FROM table WHERE field1='value' ORDER BY field1 DESC</code>

<code>SELECT field1, field2, field3 FROM table WHERE field1='value' ORDER BY field1 DESC LIMIT 2</code>


MySQL UPDATE
-------------------
상세 : https://dev.mysql.com/doc/refman/5.7/en/update.html
<code>UPDATE table SET field=value WHERE field=value</code>


MySQL DELETE
-------------------
상세 : https://dev.mysql.com/doc/refman/5.7/en/delete.html
<code>DELETE FROM table WHERE field=value</code>


관계형 데이터베이스
------------------
복잡한 데이터를 여러 개의 테이블로 나눠서 보관함으로써 중복을없애고 볼때는 합쳐서 볼 수 있음. 
예를 들어 기자-기사 를 한테이블에 관리하면 한 기자가 여러개의 기사를 쓸수 있기 때문에 기자데이터가 겹치게됨.
이럴 때 기자 - 기사 테이블을 분리하고 기사테이블에서 기자의 id값만 가지고있는 식으로 관리를 하면 데이터 중복을 없앨 수 있음.
합쳐서 보고싶을 때는 JOIN을 사용해서 한 테이블처럼 표현해서 볼 수도 있음.


JOIN
---------------
두 개 이상의 테이블을 합쳐서 보여줄 때 쓰이는 방법.

<code>SELECT * FROM table1 LEFT JOIN table2 ON table1.field = table2.field;</code>


인터넷과 데이터베이스
---------------
                   internet
datebase client  <---------->  database server
(MySQL workbench)


MySQL Workbench
---------------
다운로드 : https://dev.mysql.com/downloads/workbench

