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
    Git 로그를 뒤져서 파일별 '최초 작성(커밋) 날짜'를 가져옵니다.
    """
    dates = {}
    
    # [중요] 한글 파일명이 \342\.. 형태로 깨지는 것을 방지
    subprocess.run(["git", "config", "--global", "core.quotepath", "false"])

    # git log 명령어: 
    # --reverse: 오래된 커밋부터 정렬 (최초 커밋 날짜를 잡기 위해)
    # --name-only: 파일명만 출력
    cmd = ["git", "log", "--reverse", "--name-only", "--pretty=format:DATE:%ad", "--date=short"]
    
    try:
        output = subprocess.check_output(cmd).decode("utf-8")
        
        current_date = None
        for line in output.splitlines():
            line = line.strip()
            if line.startswith("DATE:"):
                current_date = line.replace("DATE:", "").strip()
            elif line and current_date:
                # 파일명이 처음 등장했을 때만 날짜를 기록 (최초 풀이일)
                # 만약 수정한 날짜로 하고 싶다면 'if line not in dates:' 조건을 빼면 됩니다.
                if line not in dates: 
                    dates[line] = current_date
                    
    except Exception as e:
        print(f"Git log error: {e}")
        
    return dates

def generate_grass_svg(data_dict):
    """
    최근 365일간의 데이터를 기반으로 SVG 잔디 이미지를 생성합니다.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=364) # 52주
    
    daily_count = defaultdict(int)
    for file_info in data_dict:
        d = file_info.get("date")
        if d:
            daily_count[d] += 1

    width = 53 * 14 + 20
    height = 7 * 14 + 30
    svg = [f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append('<style>.day { shape-rendering: geometricPrecision; }</style>')
    
    current = start_date
    while current.weekday() != 6: # Sunday start
        current -= timedelta(days=1)

    for week in range(53):
        for day in range(7):
            date_str = current.strftime("%Y-%m-%d")
            count = daily_count[date_str]
            
            if count == 0: color = COLORS[0]
            elif count == 1: color = COLORS[1]
            elif count <= 2: color = COLORS[2]
            elif count <= 4: color = COLORS[3]
            else: color = COLORS[4]
            
            x = week * 14 + 10
            y = day * 14 + 10
            
            # 툴팁(title) 추가
            rect = f'<rect class="day" x="{x}" y="{y}" width="10" height="10" fill="{color}" rx="2" ry="2">'
            rect += f'<title>{date_str}: {count} solution(s)</title></rect>'
            svg.append(rect)
            
            current += timedelta(days=1)
            if current > end_date:
                break
    
    svg.append('</svg>')
    
    with open("grass_graph.svg", "w", encoding="utf-8") as f:
        f.write("".join(svg))

def generate_markdown():
    pattern = re.compile(r'(.+)\((.+)\^(.+)\)(.+)\^(\d+)\.(.+)')
    
    files = []
    file_dates = get_commit_dates()
    
    for file in os.listdir("."):
        if file.startswith(".") or file in ["README.md", "update_readme.py", "grass_graph.svg"]:
            continue
            
        match = pattern.match(file)
        if match:
            site, category, level, title, prob_id, ext = match.groups()
            title = title.replace("_", " ")
            lang = "Python" if ext == "py" else ext.upper()
            
            # Git 기록에 있으면 그 날짜, 없으면(방금 올린 파일) 오늘 날짜
            date = file_dates.get(file, datetime.now().strftime("%Y-%m-%d"))
            
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

    generate_grass_svg(files)
    files.sort(key=lambda x: x["date"], reverse=True) # 최신 풀이 순 정렬

    total_solved = len(files)
    content = f"### 📅 최근 1년 풀이 현황 (총 {total_solved}문제)\n\n"
    content += "![Solution Grass](grass_graph.svg)\n\n"
    content += "| 풀이 날짜 | 문제번호 | 난이도 | 알고리즘 | 제목 | 언어 |\n| :---: | :---: | :---: | :---: | :--- | :---: |\n"
    
    for f in files:
        content += f"| {f['date']} | {f['id']} | {f['level']} | {f['category']} | [{f['title']}]({f['link']}) | {f['lang']} |\n"
        
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