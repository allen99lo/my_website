import streamlit as st
import pandas as pd
import os
from openpyxl import load_workbook

# 1. 強制設定為寬版顯示 (必須是第一個 Streamlit 指令)
st.set_page_config(layout="wide", page_title="班表管理系統")

st.title("📊 班表管理系統 (自動隱藏 Excel 隱藏欄位)")

file_path = "static/schedule.xlsx"

if os.path.exists(file_path):
    try:
        # --- A. 偵測並獲取 Excel 中「真正隱藏」的欄位 ---
        wb = load_workbook(file_path, read_only=False, data_only=True)
        ws = wb.active
        hidden_cols = []
        # 遍歷所有欄位，檢查其 hidden 屬性
        for col_letter, col_dimension in ws.column_dimensions.items():
            if col_dimension.hidden:
                # 這裡需要將英文字母轉成欄位索引或名稱
                # 簡單作法：我們先記錄哪些字母是隱藏的
                hidden_cols.append(col_letter)
        wb.close()

        # --- B. 讀取數據 ---
        # 讀取完整資料
        df = pd.read_excel(file_path)

        # 根據 openpyxl 偵測到的隱藏屬性，對應到 dataframe 的欄位並刪除
        # 如果你已知欄位名稱，也可以直接用 df.drop(columns=['欄位名'])
        # 這裡示範自動過濾（假設第一列是標題）
        actual_hidden_names = []
        for i, col in enumerate(df.columns):
            # 轉換索引為 Excel 字母 (A, B, C...)
            col_letter = chr(65 + i) 
            if col_letter in hidden_cols:
                actual_hidden_names.append(col)
        
        df_visible = df.drop(columns=actual_hidden_names)

        # --- C. 介面呈現：固定前 4 列 ---
        
        # 使用 st.container 配合 st.table 顯示前 4 列作為固定標題
        with st.container():
            st.subheader("📌 公告與說明 (固定前 4 列)")
            # 取得前 4 列數據 (不含標題列本身)
            header_info = df_visible.iloc[:4]
            st.table(header_info) 

        st.divider()

        # D. 顯示其餘班表資料 (支援捲動，自動固定表頭)
        st.subheader("📅 詳細班表內容")
        # 從第 5 列開始顯示 (index 4 開始)
        main_data = df_visible.iloc[4:]
        st.dataframe(main_data, use_container_width=True, height=600)

        # --- E. 下載按鈕 ---
        with open(file_path, "rb") as file:
            st.download_button(
                label="📥 下載原始 Excel 檔案",
                data=file,
                file_name="schedule.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:
        st.error(f"程式執行出錯: {e}")
else:
    st.warning("找不到檔案，請確認 static/schedule.xlsx 是否已上傳。")