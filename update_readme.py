import os
import re
import subprocess
from datetime import datetime, timedelta
from collections import defaultdict
from urllib.parse import quote

# ---------------------------------------------------------
# 설정: 잔디 색상 (연한색 -> 진한색)
COLORS = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]

def get_commit_dates():
    """
    Git 로그를 뒤져서 파일별 작성(커밋) 날짜를 가져옵니다.
    반환값: {'파일명': 'YYYY-MM-DD', ...}
    """
    dates = {}
    # git log 명령어로 날짜와 파일명을 가져옴
    try:
        cmd = ["git", "log", "--name-only", "--pretty=format:DATE:%ad", "--date=short"]
        output = subprocess.check_output(cmd).decode("utf-8")
        
        current_date = None
        for line in output.splitlines():
            if line.startswith("DATE:"):
                current_date = line.replace("DATE:", "").strip()
            elif line.strip() and current_date:
                file_name = line.strip()
                # 가장 최근 날짜로 덮어씌워지므로, 역순으로 돌리거나
                # 처음 발견된(가장 예전) 날짜를 유지하려면 로직 조정 필요
                # 여기서는 '마지막으로 수정된 날짜' 기준 혹은 '처음 만든 날' 기준
                # 단순화를 위해 파일이 언급된 날짜 중 하나를 씁니다.
                if file_name not in dates: # 가장 최신 커밋 날짜 기준
                    dates[file_name] = current_date
    except Exception as e:
        print(f"Git log error: {e}")
    return dates

def generate_grass_svg(data_dict):
    """
    최근 365일간의 데이터를 기반으로 SVG 잔디 이미지를 생성합니다.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=364) # 52주
    
    # 날짜별 푼 문제 수 카운트
    daily_count = defaultdict(int)
    for file_info in data_dict:
        d = file_info.get("date")
        if d:
            daily_count[d] += 1

    # SVG 생성 시작
    width = 53 * 14 + 20 # 53주 * 14px + 여백
    height = 7 * 14 + 30 # 7요일 * 14px + 여백
    svg = [f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append('<style>.day { shape-rendering: geometricPrecision; }</style>')
    
    # 52주 x 7일 루프
    current = start_date
    # 시작 요일 맞추기 (일요일부터 시작하도록)
    while current.weekday() != 6: # 6 = Sunday
        current -= timedelta(days=1)

    for week in range(53):
        for day in range(7):
            date_str = current.strftime("%Y-%m-%d")
            count = daily_count[date_str]
            
            # 색상 결정 (문제 수에 따라 진해짐)
            if count == 0: color = COLORS[0]
            elif count == 1: color = COLORS[1]
            elif count <= 2: color = COLORS[2]
            elif count <= 4: color = COLORS[3]
            else: color = COLORS[4]
            
            x = week * 14 + 10
            y = day * 14 + 10
            
            rect = f'<rect class="day" x="{x}" y="{y}" width="10" height="10" fill="{color}" rx="2" ry="2" data-date="{date_str}" data-count="{count}"/>'
            svg.append(rect)
            
            current += timedelta(days=1)
            if current > end_date:
                break
    
    svg.append('</svg>')
    
    with open("grass_graph.svg", "w", encoding="utf-8") as f:
        f.write("".join(svg))

def generate_markdown():
    # 파일명 패턴 정규식
    pattern = re.compile(r'(.+)\((.+)\^(.+)\)(.+)\^(\d+)\.(.+)')
    
    files = []
    file_dates = get_commit_dates() # Git 날짜 정보 가져오기
    
    for file in os.listdir("."):
        if file.startswith(".") or file in ["README.md", "update_readme.py", "grass_graph.svg"]:
            continue
            
        match = pattern.match(file)
        if match:
            site, category, level, title, prob_id, ext = match.groups()
            title = title.replace("_", " ")
            lang = "Python" if ext == "py" else ext.upper()
            
            date = file_dates.get(file, datetime.now().strftime("%Y-%m-%d")) # 날짜 없으면 오늘
            
            files.append({
                "id": int(prob_id),
                "site": site,
                "category": category,
                "level": level,
                "title": title,
                "lang": lang,
                "link": quote(file),
                "date": date
            })

    # SVG 생성 실행
    generate_grass_svg(files)

    files.sort(key=lambda x: x["id"])
    
    # 통계 요약
    total_solved = len(files)
    
    # 마크다운 내용 조합
    content = f"### 📅 최근 1년 풀이 현황 (총 {total_solved}문제)\n\n"
    content += "![Solution Grass](grass_graph.svg)\n\n" # 생성된 SVG 이미지 삽입
    content += "| 사이트 | 문제번호 | 난이도 | 알고리즘 | 제목 | 언어 | 풀이 날짜 |\n| :---: | :---: | :---: | :---: | :--- | :---: | :---: |\n"
    
    for f in files:
        content += f"| {f['site']} | {f['id']} | {f['level']} | {f['category']} | [{f['title']}]({f['link']}) | {f['lang']} | {f['date']} |\n"
        
    return content

def update_readme():
    readme_path = "README.md"
    start_marker = ""
    end_marker = ""
    
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)
        
        if start_idx != -1 and end_idx != -1:
            new_content = (
                content[:start_idx + len(start_marker)] 
                + "\n" + generate_markdown() + "\n" 
                + content[end_idx:]
            )
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("README & Grass Updated!")
        else:
            print("Marker not found in README.md")
    except FileNotFoundError:
        print("README.md not found.")

if __name__ == "__main__":
    update_readme()