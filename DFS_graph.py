
import networkx as nx
import matplotlib.pyplot as plt

# 네트워크 그래프 생성
G = nx.Graph()

# 노드 이름 목록 생성
nodes = [str(i) for i in range(1, 9)]

# 노드 데이터
graph = {
    '1': {'3', '7'},
    '2': {'3', '7', '8'},
    '3': {'1', '2', '6', '7'},
    '4': {'5', '7', '8'},
    '5': {'4', '8'},
    '6': {'3', '7', '8'},
    '7': {'1', '2', '3', '4', '6', '8'},
    '8': {'2', '4', '5', '6', '7'}
}

# 노드 데이터를 실제 그래프에 입력
G.add_nodes_from(graph.keys())
for i in graph.keys():
  for j in graph[i]:
    G.add_edge(i, j)

# 위치정보 가져오기
pos=nx.spring_layout(G)

# 초기 상태 저장
nx.draw(G, pos, with_labels = True)
plt.savefig(f"./img/DFS_{0}.png")

# 필요 변수 선언
target = ['1']
visit = ['1']
num = 1

# target이 바닥이 될때까지 반복
while target:
    # 가장 마지막에 있는 요소를 pop
    x = target.pop()

    # 그 노드와 연결된 노드들을 추출
    for i in graph[x]:
        # 만약 한번도 방문하지 않았다면
        if not i in visit:
            # visit에 추가
            visit.append(i)
            # target에 추가
            target.append(i) # 중요!!
    
    # 노드 색깔 지정
    color = []
    for i in G:
        # 선택된 노드일 경우 노란색
        if i == x:
            color.append("yellow")
        # 앞으로 선택될 노드일 경우 파란색
        elif i in target:
            color.append("blue")
        # 이미 방문한 노드일 경우 초록색
        elif i in visit:
            color.append("green")
        # 아무것도 아닐경우 검은 색
        else:
            color.append("black")

    # 화면 초기화
    plt.cla()

    _, ax = plt.subplots()

    # 네트워크 그래프 그리기
    nx.draw(G, pos, node_color=color, with_labels = True)
    # target 텍스트 추가
    plt.text(1.0, 1.0, str(target), ha='right', va='top', transform=ax.transAxes)
    # 그래프 저장
    plt.savefig(f"./img/DFS_{num}.png")
    num += 1