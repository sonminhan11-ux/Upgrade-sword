import streamlit as st
import random

# 0~30강 무기 이름
weapon_levels = [
    "철빛 초검", "은장 단검", "강철의 장도", "청강 예도", "흑철 도철검",
    "홍련 화도", "빙결 설월검", "뇌광 천우도", "암흑 사신의 검", "광휘 성검",
    "심연 파멸도", "폭풍천참검", "초신성의 검", "혼돈 멸신도", "태초 창세검",
    "요새 파쇄도", "격류 파도검", "유성낙하검", "그림자 추격도", "천공 제검",
    "운명 절단검", "백색광 파동검", "마력 집속도", "히드라의 독아검", "불멸의 불꽃도",
    "광풍 회오리검", "심판의 금검", "시간 절삭도", "영겁의 유산검", "블러드레인 참도",
    "킹갓 제네럴 엡솔루트 차원 파괴 검"
]

# 0~30강 ASCII 아트
weapon_ascii = [
"""
    /|
   / |
   | |
   | |
   | |
   |||
   |||
   |||
""",
"""
    /☆
   /☆|
   |☆|
   | |
   | |
   ║║║
   ║║║
   ║║║
""",
"""
    /▲\\
   /▲▲\\
   |▲▲|
   |▲|
   |▲|
   ║║║
   ║║║
   ║║║
""",
"""
    /✦\\
   /✦✦\\
   |✦✦|
   |✦|
   |✦|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /◆\\
   /◆◆\\
   |◆◆|
   |◆|
   |◆|
   ║█║
   ║█║
   ║█║
""",
"""
    /🔥\\
   /🔥🔥\\
   |🔥🔥|
   |🔥|
   |🔥|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /❄\\
   /❄❄\\
   |❄❄|
   |❄|
   |❄|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /⚡\\
   /⚡⚡\\
   |⚡⚡|
   |⚡|
   |⚡|
   ║█║
   ║█║
   ║█║
""",
"""
    /☠\\
   /☠☠\\
   |☠☠|
   |☠|
   |☠|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /✧\\
   /✧✧\\
   |✧✧|
   |✧|
   |✧|
   ║█║
   ║█║
   ║█║
""",
"""
    /☾\\
   /☾☾\\
   |☾☾|
   |☾|
   |☾|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /🌪\\
   /🌪🌪\\
   |🌪🌪|
   |🌪|
   |🌪|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /☄\\
   /☄☄\\
   |☄☄|
   |☄|
   |☄|
   ║█║
   ║█║
   ║█║
""",
"""
    /☢\\
   /☢☢\\
   |☢☢|
   |☢|
   |☢|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /🌟\\
   /🌟🌟\\
   |🌟🌟|
   |🌟|
   |🌟|
   ║█║
   ║█║
   ║█║
""",
"""
    /🏰\\
   /🏰🏰\\
   |🏰🏰|
   |🏰|
   |🏰|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /🌊\\
   /🌊🌊\\
   |🌊🌊|
   |🌊|
   |🌊|
   ║█║
   ║█║
   ║█║
""",
"""
    /🌠\\
   /🌠🌠\\
   |🌠🌠|
   |🌠|
   |🌠|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /☁\\
   /☁☁\\
   |☁☁|
   |☁|
   |☁|
   ║█║
   ║█║
   ║█║
""",
"""
    /☀\\
   /☀☀\\
   |☀☀|
   |☀|
   |☀|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /⚔\\
   /⚔⚔\\
   |⚔⚔|
   |⚔|
   |⚔|
   ║█║
   ║█║
   ║█║
""",
"""
    /💫\\
   /💫💫\\
   |💫💫|
   |💫|
   |💫|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /🔮\\
   /🔮🔮\\
   |🔮🔮|
   |🔮|
   |🔮|
   ║█║
   ║█║
   ║█║
""",
"""
    /🐉\\
   /🐉🐉\\
   |🐉🐉|
   |🐉|
   |🐉|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /🔥\\
   /🔥🔥\\
   |🔥🔥|
   |🔥|
   |🔥|
   ║█║
   ║█║
   ║█║
""",
"""
    /🌪\\
   /🌪🌪\\
   |🌪🌪|
   |🌪|
   |🌪|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /💰\\
   /💰💰\\
   |💰💰|
   |💰|
   |💰|
   ║█║
   ║█║
   ║█║
""",
"""
    /⏳\\
   /⏳⏳\\
   |⏳⏳|
   |⏳|
   |⏳|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /🕰\\
   /🕰🕰\\
   |🕰🕰|
   |🕰|
   |🕰|
   ║█║
   ║█║
   ║█║
""",
"""
    /🩸\\
   /🩸🩸\\
   |🩸🩸|
   |🩸|
   |🩸|
   ║▓║
   ║▓║
   ║▓║
""",
"""
    /⚡\\
   /⚡⚡\\
   |⚡⚡|
   |⚡|
   |⚡|
   ║█║
   ║█║
   ║█║
"""
]

# 강화 확률
def success_chance(level):
    if level <= 5:
        return 0.85
    elif level <= 10:
        return 0.7
    elif level <= 15:
        return 0.55
    elif level <= 20:
        return 0.4
    elif level <= 25:
        return 0.25
    else:
        return 0.15

# Streamlit UI
st.set_page_config(page_title="무기 강화 시뮬레이터", page_icon="⚔")

st.title("⚔ 무기 강화 시뮬레이터 (WEB ver.)")

# 상태 저장
if "level" not in st.session_state:
    st.session_state.level = 0

col1, col2 = st.columns(2)
with col1:
    st.subheader(f"현재 강화 단계: **{st.session_state.level}강**")
with col2:
    st.write(f"강화 성공 확률: **{int(success_chance(st.session_state.level) * 100)}%**")

# 무기 ASCII 출력
ascii_index = min(st.session_state.level, len(weapon_ascii) - 1)
st.code(weapon_ascii[ascii_index], language="text")
st.subheader(f"🗡 무기 이름: {weapon_levels[ascii_index]}")

# 강화 버튼
if st.button("강화 시도"):
    chance = success_chance(st.session_state.level)
    if random.random() < chance:
        st.session_state.level += 1
        st.success(f"강화 성공! 현재 {st.session_state.level}강")
    else:
        if st.session_state.level > 0:
            st.session_state.level -= 1
        st.error(f"강화 실패! 현재 {st.session_state.level}강")

# 초기화
if st.button("🔄 다시 시작"):
    st.session_state.level = 0
    st.info("강화를 초기화했습니다!")

if st.session_state.level == 30:
    st.balloons()
    st.success("🎉 30강 달성! 축하합니다! 🎉")
