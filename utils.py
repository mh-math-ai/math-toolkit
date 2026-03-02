"""
수학 유틸리티 함수들 (개발 중)
common utility functions for math projects (under construction)
===============================

TODO: 첫 번째 프로그램 작성 후에 필요한 함수들만 추가
After finishing the first program, i'll gradually add only necessary functions here

planned contents:
    - solve_2x2(): 2x2 선형시스템 해
    - rotation_matrix(): 회전행렬 생성
    - normalize(): 벡터 정규화
    - get_intersection(): 두 직선의 교점
"""

import numpy as np  # 나중을 위해 미리 import

def solve_2x2(A, b):
    """
    2x2 선형시스템 A x = b의 해 구하기 (준비 중)
    
    Parameters:
        A: 2x2 행렬
        b: 2-벡터
    
    Returns:
        x: 해 벡터
    """
    # TODO: np.linalg.solve(A, b) 구현
    pass


def rotation_matrix(angle):
    """
    2D 회전행렬 생성 (준비 중)
    
    Parameters:
        angle: 회전각 (라디안)
    
    Returns:
        2x2 회전행렬
    """
    # TODO: [[cos, -sin], [sin, cos]] 반환
    pass


def normalize(v):
    """
    벡터 정규화 (준비 중)
    
    Parameters:
        v: 입력 벡터
    
    Returns:
        단위 벡터
    """
    # TODO: v / norm(v) 반환
    pass


def get_intersection(line1, line2):
    """
    두 직선의 교점 찾기 (준비 중)
    
    Parameters:
        line1, line2: (a, b, c) 형태의 직선 방정식 ax + by = c
    
    Returns:
        (x, y) 교점 좌표
    """
    # TODO: 선형시스템 풀어서 교점 반환
    pass
