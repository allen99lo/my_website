import streamlit as st
import pandas as pd
import os

st.title("📊 我的工作班表管理系統")

# 設定檔案路徑 (假設你的檔案放在 static 資料夾)
file_path = "static/schedule.xlsx"

# 檢查檔案是否存在
if os.path.exists(file_path):
    # --- 功能一：直接在網頁顯示 ---
    st.subheader("🗓️ 班表即時預覽")
    try:
        # 讀取 Excel 檔案
        df = pd.read_excel(file_path)
        # 在網頁上顯示表格 (可縮放、排序)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"讀取 Excel 時發生錯誤: {e}")

    st.divider() # 分隔線

    # --- 功能二：提供下載按鈕 ---
    st.subheader("💾 下載原始檔案")
    with open(file_path, "rb") as file:
        st.download_button(
            label="點我下載 Excel 班表檔案",
            data=file,
            file_name="my_schedule.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.warning(f"找不到檔案：{file_path}，請確認檔案已上傳至 static 資料夾。")