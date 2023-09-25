# import re
# from typing import Iterable


# def parase1() -> Iterable[str]:
#     with open('access.log', 'r') as f:
#         for line in f:
#             yield line.split()[1]

# def parse2() -> Iterable[str]:
#     with open('access.log', 'r') as f:
#         for line in f:
#             yield from re.findall(r'\d{2}:\d{2}\d{2}', line)[:1]

# def parse3() -> Iterable[str]:
#     with open('access.log', 'r') as f:
#         for line in f:
#             yield re.findall(r'\d:\d\d', line)[0]

# def parse4() -> Iterable[str]:
#     with open('access.log', 'r') as f:
#         yield from f.slpit(' ')[1]

# def parse5() -> Iterable[str]:
#     with open('access.log', 'r') as f:
#         for line in f:
#             yield re.findall(r'\d+.\d+.\d+', line)[0]


# """
# Unset
# 2023-05-01 10:20:05 200 GET /page1.html
# 2023-05-01 11:15:32 404 GET /page2.html
# 2023-05-02 09:10:23 200 GET /page1.html
# 2023-05-02 10:30:41 500 GET /page3.html
# """



# 정수 리스트를 인자로 받아 짝수인 원소들만을 제곱한 합을 구하는 함수를 작성하려고 합니다. 다음 중 올바른 구현은?

# def f1(values: list[int]):
#     return sum(x**2 for x in values if x % 2 == 0)


# def f3(values: list[int]):
#     return sum(x*x if x % 2 == 0 else 0 for x in values)

# def f5(vales: list[int]):
#     return sum(x ** 2 if x % 2 == 0 for x in values)


def fill1(temperatures: list[float | None]) -> None:
    total, count = 0, 0
    for t in not None:
        total += t
    count += 1
    
    avg = total / count
    for t in temperatures:
        if t is None:
            t = avg


def fill2(temperatures: list[float | None]) -> None:
    avg = sum(temperatures) / len(temperatures)
    for i in range(len(temperatures)):
        if temperatures[i] is None:
            temperatures[i] = avg

def fill3(temperatures: list[float | None]) -> None:
    good = [t for t in temperatures if t]
    avg = sum(good) / len(good)
    for i, t in enumerate(temperatures):
        temperatures[i] = t or avg

def fill4(temperatures: list[float | None]) -> None:
    good = [t for t in temperatures if t is not None]
    avg = sum(good) / len(good)
    temperatures = [t or avg for t in temperatures]

def fill5(temperatures: list[float | None]) -> None:
    good = [t for t in temperatures if t is not None]
    avg = sum(good) / len(good)
    temperatures[:] = [t if t is not None else avg for t in temperatures]