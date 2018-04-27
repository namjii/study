# PYTHON TEST (Test Driven Development)

### 단위테스트 vs 기능테스트

##### 단위테스트(Unit Test)
- 개발자 뷰
- 함수단위
- Mock 사용
- 빠름
- 더 좋은 코드에 기여

##### 기능테스트(Function Test)
- 사용자 뷰
- 요구사항 단위
- Fixture를 사용
- 느림


### unittest
- 파이썬 표준 라이브러리
- 테스트 자동화
- 테스트 구조화
- 테스트 결과 보고
- document: https://docs.python.org/3/library/unittest.html

#### 용어
- Test Case : 독립적인 테스트 단위
- Test Suite 
: TestCaset의 묶음. 보통은 테스트를 실행하면 모든 테스트를 모아서 실행하지만, 몇몇개만 원하는대로 실행하고 싶다면 TestSuite를 사용.
- Test Runner 
: 테스트를 실제로 수행하고 결과를 레포트
- Test Fixture : 테스트에 필요한 자료, 환경


#### Basic Example
<pre><code>
class SomethingTest(unites.TestCase):

    def test_upper(self):
        self.assertEqual(‘foo’.upper(), ‘FOO’)

if __name__ == '__main__':
    unittest.main()
</code></pre>

- Test Method 이름은 ‘test’로 시작해야한다.
- assert 함수를 통해서 원하는 결과값이 나오는지, 원하는 조건인지, 특정 exception이 발생했는지 등을 검사할 수 있다.
- setUp()과 tearDown() 메소드는 각 테스트 메소드가 실행되기 이전과 이후에 작동한다. setUp()이 성공적으로 작동하면 테스트자체의 성패와 상관없이 tearDown()이 작동한다.
> setUp() -> test_A() -> tearDown() -> setUp() 반복
- unittest.main()는 테스트를 실행하고나서 커맨드라인에 결과를 보여준다. (몇개 test 실행했고 걸린시간)

#### Command-Line InterFace
<pre><code>
python -m unites [test module | classes | methods]
</code></pre>
테스트를 커맨드라인에서도 실행할 수 있다.

#### 테스트 건너뛰기
- 건너뛰고싶은 테스트 메소드나 클래스가 있으면 skip() 데코레이터를 사용한다.
- 실패가 예상되는 테스트에는 @unittest.expectedFailure 데코레이터를 통해서 테스트를 통과시킬 수도 있다. 
<pre><code>
class MyTestCase(unites.TestCase):

    @unittest.skip(“demonstrating skipping”)
    def test_nothing(self):
        self.fail(“shouldn’t happen”)

    @unittest.skipIf(mylib.__version__ < (1, 3), “not supported in this library version”)
    def test_version(self):
        pass

</code></pre>
데코레이터에 지정된 텍스트는 결과화면에 나온다.

#### subtest
iterator를 돌면서 테스트 하는 경우에는 iteration중에 어떤 값이 테스트에 실패했는지 알기 위해서 subtest를 사용한다. subtest를 사용하면 결과화면에 실패한 값이 나온다.
<pre><code>

class NumbersTest(unittest.TestCase):

    def test_even(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

</code></pre>


#### assert 함수들
- assertEqual(a, b) :	a == b	 
- assertNotEqual(a, b)	: a != b	 
- assertTrue(x) : bool(x) is True	 
- assertFalse(x) : bool(x) is False	 
- assertIs(a, b) : a is b
- assertIsNot(a, b) : a is not b
- assertIsNone(x) : x is None
- assertIsNotNone(x) : x is not None
- assertIn(a, b) : a in b
- assertNotIn(a, b) : a not in b
- assertIsInstance(a, b) : isinstance(a, b)	
- assertNotIsInstance(a, b) : not isinstance(a, b)
- assertRaises(exc, fun, *args, **kwds) : fun(*args, **kwds) raises exc	 

- assertAlmostEqual(a, b) : round(a-b, 7) == 0	 
- assertGreater(a, b) : a > b
- assertGreaterEqual(a, b) : a >= b
- assertLess(a, b) : a < b	
- assertLessEqual(a, b) : a <= b
- assertRegex(s, r) : r.search(s)
- assertCountEqual(a, b) : a and b have the same elements in the same number, regardless of their order

