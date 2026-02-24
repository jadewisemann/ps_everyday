import os
import re

def finalize_to_ultimate_style(root_path):
    # 티어 영문 이름 매핑
    tier_name_map = {
        '브론즈': 'Bronze', '실버': 'Silver', '골드': 'Gold', 
        '플래티넘': 'Platinum', '플래': 'Platinum', 
        '다이아': 'Diamond', '루비': 'Ruby',
        'B': 'Bronze', 'S': 'Silver', 'G': 'Gold', 
        'P': 'Platinum', 'D': 'Diamond', 'R': 'Ruby'
    }

    for root, dirs, files in os.walk(root_path):
        for filename in files:
            name_only, ext = os.path.splitext(filename)
            
            # 1. 문제 번호 추출 (#번호 또는 BOJ#번호)
            num_match = re.search(r"#(\d{4,6})", name_only) or re.search(r"BOJ#(\d{4,6})", name_only)
            if not num_match:
                continue
            number = num_match.group(1)
            
            # 2. 모든 괄호 뭉치 추출 ((), [], {})
            parts = re.findall(r"[\(\{\[](.*?)[\)\}\]]", name_only)
            
            if len(parts) >= 2:
                # 관례상 마지막 괄호는 티어, 그 앞은 분류
                raw_category = parts[-2]
                if "BOJ" in raw_category:
                    raw_category = parts[1] if len(parts) > 2 else "미분류"
                
                raw_tier = parts[-1]

                # 3. 제목 추출 (핵심 문자열만 추출)
                title = name_only
                # 괄호 패턴 및 번호 패턴 제거하여 순수 제목만 남김
                remove_patterns = [
                    r"\(BOJ#\d+\)", r"\(.*?\)", r"\[.*?\]", r"\{.*?\}", f"#{number}", "BOJ"
                ]
                for p in remove_patterns:
                    title = re.sub(p, "", title)
                
                title = title.strip("_ ").strip()

                # 4. 티어 변환 (예: Gold1)
                tier_abbr = raw_tier
                for kor, eng in tier_name_map.items():
                    if kor in raw_tier:
                        level = re.sub(r'[^0-9]', '', raw_tier)
                        tier_abbr = f"{eng}{level}"
                        break
                
                # 5. 최종 형식 조립: BOJ(분류)[티어]제목#번호.py
                # 예: BOJ(구현)[Bronze2]Hashing#15829.py
                new_name = f"BOJ({raw_category})[{tier_abbr}]{title}#{number}{ext}"
                
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_name)
                
                if filename != new_name:
                    try:
                        os.rename(old_path, new_path)
                        print(f"✅ 변경: {new_name}")
                    except Exception as e:
                        print(f"❌ 실패: {filename} -> {e}")

if __name__ == "__main__":
    finalize_to_ultimate_style(".")