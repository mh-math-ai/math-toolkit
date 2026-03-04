import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

class LinearEquationVisualizer:
    def __init__(self):
        pass

    def get_equation_from_user(self):
        
        # get input from the user 
        equations = []
        print("\n=== 3원 1차 연립방정식 입력 ===")
        print("형식: ax + by + cz = d")
        print("예시: 2x + 3y - z = 5 는 2 3 -1 5 로 입력")
        
        for i in range(3):
            while True:
                try:
                    eq_input = input(f"\n방정식 {i+1}의 계수 a b c d를 입력하세요: ").strip().split()
                    if len(eq_input) != 4:
                        print("4개의 숫자를 입력해야 합니다! (a b c d)")
                        continue
                    
                    a, b, c, d = map(float, eq_input)
                    equations.append([a, b, c, d])
                    
                    print(f"입력된 방정식 {i+1}: {a}x + {b}y + {c}z = {d}")
                    break
                    
                except ValueError:
                    print("올바른 숫자를 입력하세요!")
                except KeyboardInterrupt:
                    print("\n프로그램을 종료합니다.")
                    return None
        
        return equations

    def check_solution_exists(self, A, b):
        # to check it the solution exists 
        # computing augmented matrix [A|b]'s rank
        rank_A = np.linalg.matrix_rank(A)
        augmented = np.column_stack([A, b])
        rank_Ab = np.linalg.matrix_rank(augmented)
        
        # print debugging 
        print(f"rank(A) = {rank_A}, rank([A|b]) = {rank_Ab}")
        
        return rank_A == rank_Ab

    def plot_row_picture(self, equations, range_val=5):
        fig = plt.figure(figsize=(15, 6))
        ax = fig.add_subplot(121, projection='3d')
        
        resolution = 30
        x = np.linspace(-range_val, range_val, resolution)
        y = np.linspace(-range_val, range_val, resolution)
        z = np.linspace(-range_val, range_val, resolution)
        X, Y = np.meshgrid(x, y)
        
        colors = ['red', 'green', 'blue']
        
        for i, eq in enumerate(equations):
            a, b, c, d = eq
            a_zero = abs(a) < 1e-10
            b_zero = abs(b) < 1e-10
            c_zero = abs(c) < 1e-10
            
            if not c_zero:  # z 계수 있음
                if not a_zero and not b_zero:  # x, y, z 모두 있음
                    Z = (d - a*X - b*Y) / c
                    mask = np.abs(Z) < range_val*2
                    Z_masked = np.where(mask, Z, np.nan)
                    ax.plot_surface(X, Y, Z_masked, alpha=0.3, color=colors[i])
                    
                elif a_zero and not b_zero:  # y, z만 (x free)
                    X_plane, Z_plane = np.meshgrid(x, z)
                    Y_plane = (d - c*Z_plane) / b
                    ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color=colors[i])
                    
                elif not a_zero and b_zero:  # x, z만 (y free)
                    Y_plane, Z_plane = np.meshgrid(y, z)
                    X_plane = (d - c*Z_plane) / a
                    ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color=colors[i])
                    
                elif a_zero and b_zero:  # z만 (x,y free)
                    z_const = d / c
                    X_plane, Y_plane = np.meshgrid(x, y)
                    Z_plane = np.full_like(X_plane, z_const)
                    ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color=colors[i])
                    
            elif not b_zero:  # z=0, y 있음
                if not a_zero:  # x, y만 (z free)
                    X_plane, Z_plane = np.meshgrid(x, z)
                    Y_plane = (d - a*X_plane) / b
                    ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color=colors[i])
                    
                else:  # y만 (x,z free)
                    y_const = d / b
                    X_plane, Z_plane = np.meshgrid(x, z)
                    Y_plane = np.full_like(X_plane, y_const)
                    ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color=colors[i])
                    
            elif not a_zero:  # z=0, b=0, x만 (y,z free)
                x_const = d / a
                Y_plane, Z_plane = np.meshgrid(y, z)
                X_plane = np.full_like(Y_plane, x_const)
                ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color=colors[i])
        
        
        # 해 검사
        A = np.array([eq[:3] for eq in equations])
        b = np.array([eq[3] for eq in equations])
        
        solution_exists = self.check_solution_exists(A, b)
        
        if solution_exists:
            try:
                solution = np.linalg.solve(A, b)
                ax.scatter(*solution, color='black', s=80, marker='o', 
                        edgecolors='white', linewidth=1)
                
                ax.text(solution[0], solution[1], solution[2], 
                    f'({solution[0]:.1f}, {solution[1]:.1f}, {solution[2]:.1f})',
                    color='black', fontsize=8)
                
                solution_text = f'Solution: ({solution[0]:.2f}, {solution[1]:.2f}, {solution[2]:.2f})'
            except np.linalg.LinAlgError:
                solution_text = "Infinite solutions"
        else:
            solution_text = "No solution"
            print("⚠️ 이 연립방정식은 해가 없습니다!")
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Row Picture: Planes\n{solution_text}')
        ax.set_xlim([-range_val, range_val])
        ax.set_ylim([-range_val, range_val])
        ax.set_zlim([-range_val, range_val])
        
        # 범례
        legend_elements = []
        for i, eq in enumerate(equations):
            a, b, c, d = eq
            legend_elements.append(Patch(facecolor=colors[i], 
                                    label=f'{eq[0]}x + {eq[1]}y + {eq[2]}z = {eq[3]}'))
        ax.legend(handles=legend_elements, loc='upper left', fontsize=8)
        
        return fig, ax

    def plot_column_picture(self, equations, range_val=5):
        """Column picture 그리기"""
        ax = plt.subplot(122, projection='3d')
        
        col1 = [eq[0] for eq in equations]
        col2 = [eq[1] for eq in equations]
        col3 = [eq[2] for eq in equations]
        b = [eq[3] for eq in equations]
        
        origin = [0, 0, 0]
        
        # 벡터 그리기
        ax.quiver(*origin, *col1, color='red', arrow_length_ratio=0.1, linewidth=2)
        ax.quiver(*origin, *col2, color='green', arrow_length_ratio=0.1, linewidth=2)
        ax.quiver(*origin, *col3, color='blue', arrow_length_ratio=0.1, linewidth=2)
        ax.quiver(*origin, *b, color='black', arrow_length_ratio=0.1, linewidth=2)
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Column Picture: Vectors')
        ax.set_xlim([-range_val, range_val])
        ax.set_ylim([-range_val, range_val])
        ax.set_zlim([-range_val, range_val])
        ax.grid(True)
        
        # 범례
        legend_elements = [
            Patch(color='red', label=f'col1: ({col1[0]:.1f}, {col1[1]:.1f}, {col1[2]:.1f})'),
            Patch(color='green', label=f'col2: ({col2[0]:.1f}, {col2[1]:.1f}, {col2[2]:.1f})'),
            Patch(color='blue', label=f'col3: ({col3[0]:.1f}, {col3[1]:.1f}, {col3[2]:.1f})'),
            Patch(color='black', label=f'b: ({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f})')
        ]
        ax.legend(handles=legend_elements, loc='upper left', fontsize=8)

    def visualize(self, equations):
        """메인 시각화 함수"""
        self.plot_row_picture(equations)
        self.plot_column_picture(equations)
        plt.tight_layout()
        plt.show()

    def interactive_mode(self):
        """대화형 모드"""
        print("=" * 50)
        print("   3원 1차 연립방정식 시각화 프로그램")
        print("=" * 50)
        
        while True:
            print("\n--- 메뉴 ---")
            print("1. 계수 입력 (a b c d 형식)")
            print("2. 방정식 입력 (예: 2x + 3y - z = 5)")
            print("3. 예제 실행")
            print("4. 종료")
            
            choice = input("\n선택하세요 (1-4): ").strip()
            
            if choice == '1':
                equations = self.get_equation_from_user()
                if equations:
                    self.visualize(equations)
                    
            elif choice == '2':
                equations = []
                print("\n방정식 3개를 입력하세요 (예: 2x + 3y - z = 5)")
                for i in range(3):
                    eq_str = input(f"방정식 {i+1}: ").strip()
                    eq = self.parse_equation_string(eq_str)
                    if eq:
                        equations.append(eq)
                        print(f"파싱 결과: {eq[0]}x + {eq[1]}y + {eq[2]}z = {eq[3]}")
                    else:
                        print("잘못된 형식입니다. 다시 시도하세요.")
                        break
                else:
                    self.visualize(equations)
                    
            elif choice == '3':
                print("\n예제를 선택하세요:")
                print("1. x = 3, y = 2, z = 1 (유일해)")
                print("2. x+y=3, y+z=4, x+z=5 (유일해)")
                print("3. 2x+3y+z=5, x+y=1, 3x+4y+z=5 (해 없음)")
                
                ex = input("선택 (1-3): ").strip()
                if ex == '1':
                    equations = [[1,0,0,3], [0,1,0,2], [0,0,1,1]]
                elif ex == '2':
                    equations = [[1,1,0,3], [0,1,1,4], [1,0,1,5]]
                elif ex == '3':
                    equations = [[2,3,1,5], [1,1,0,1], [3,4,1,5]]
                else:
                    print("잘못된 선택")
                    continue
                self.visualize(equations)
                
            elif choice == '4':
                print("프로그램을 종료합니다.")
                break
                
            else:
                print("잘못된 입력입니다. 다시 선택하세요.")

if __name__ == "__main__":
    visualizer = LinearEquationVisualizer()
    visualizer.interactive_mode()