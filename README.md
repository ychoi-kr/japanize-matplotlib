# koreanize-matplotlib
matplotlib를 한국어 표시에 대응시킵니다.

## 사용법
matplotlib를 import한 후 koreanize_matplotlib를 import합니다.

```python
import matplotlib.pyplot as plt
import koreanize_matplotlib

plt.plot([-1, 0, 1, 2])
plt.title('그래프 제목', fontweight="bold")
plt.xlabel('간단한 그래프')
plt.show()
```


![demo](https://github.com/ychoi-kr/koreanize-matplotlib/raw/master/demo.png "demo")

## 설치

```sh
pip install koreanize-matplotlib
```

또는

```sh
python setup.py install
```


## 사용한 폰트
[나눔고딕](https://hangeul.naver.com/2021/fonts/nanum)

