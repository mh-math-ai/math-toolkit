"""
시각화 기본 클래스 (개발 중)
basic visualizer class (under construction)
=============================

TODO: 첫 번째 프로그램 작성 후에 점진적으로 실제 코드로 채울 예정
After finishing the first program, i'll fill the contents here gradually


expected structure:
    class MathVisualizer:
        - setup_plot(): 플롯 초기화
        - draw_vector(): 벡터 그리기
        - add_grid(): 그리드 추가
        - save_figure(): 저장하기
"""

class MathVisualizer:
    """모든 시각화의 기본이 될 클래스 (준비 중)"""
    
    def __init__(self):
        """생성자: 아직 구현 전"""
        # TODO: plt.style 설정, figure 크기 등 기본 설정
        pass
    
    def setup_plot(self, title, xlabel='x', ylabel='y'):
        """2D 플롯 기본 설정 (준비 중)"""
        # TODO: subplots 생성, 축 레이블 설정, 그리드 추가
        pass
    
    def draw_vector(self, start, vector, color='blue', label=None):
        """벡터(화살표) 그리기 (준비 중)"""
        # TODO: ax.arrow()를 사용한 벡터 시각화
        pass
    
    def show(self):
        """그래프 표시 (준비 중)"""
        # TODO: plt.show() 호출
        pass
