# 範例說明
透過 docker compose 自動化基於映像檔下載(image pull)建構與執行單一容器服務的應用

## 目的
練習透過指令建立與刪除 docker compose 服務

## 專案目錄
- case_01_compose_by_pull
  - app.py
  - compose.yaml

## 操作步驟
Step 1. 在**前景**建立並啟動 docker compose 服務
```shell
docker compose up
```

確認以下項目
1. 容器服務是否正確執行?
2. 容器目前的狀態?
3. 映像檔目前的狀態?

Step 2. 停止並刪除 docker compose 服務
```shell
docker compose down
```

確認以下項目
1. 容器是否已刪除?
2. 映像檔是否已刪除?

## 延伸問題 
1. 如何在停止並刪除 docker compose 服務時同時刪除映像檔?