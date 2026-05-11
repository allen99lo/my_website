import streamlit as st
import os

# 1. 設定網頁寬版顯示
st.set_page_config(layout="wide", page_title="班表管理系統")

st.title("📅 最新班表查閱系統")
st.info("點擊下方按鈕即可預覽班表截圖，或下載原始 Excel 檔案進行編輯。")

# 設定檔案路徑
image_path = "static/schedule.png"
file_path = "static/schedule.xlsx"

# --- 2. 顯示班表按鈕控制 ---
# 使用 st.button，當點擊時會觸發為 True
if st.button("🔍 顯示/重新整理班表"):
    if os.path.exists(image_path):
        st.image(image_path, caption="最新班表截圖", use_container_width=False)
    else:
        st.error(f"找不到截圖檔案：{image_path}，請確認檔案已上傳至 static 資料夾。")

st.divider() # 分隔線

# --- 3. 提供 Excel 下載 ---
if os.path.exists(file_path):
    with open(file_path, "rb") as file:
        st.download_button(
            label="📥 下載原始 Excel 班表",
            data=file,
            file_name="schedule.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.warning(f"無法提供下載：找不到原始檔案 {file_path}")

# --- 4. 頁腳資訊 ---
st.caption("系統提示：若班表有更新，請重新上傳 schedule.png 與 schedule.xlsx 至 GitHub。")
