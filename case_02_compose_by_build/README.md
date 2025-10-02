# 範例說明
透過 docker compose 自動化基於以 Dockerfile 建立映像檔(image build)建構與執行單一容器服務的應用

## 目的
練習透過指令停止與重啟 docker compose 服務

## 專案目錄
- case_02_compose_by_build
  - app.py
  - compose.yaml
  - dockerfile
  - requirements.txt

## 操作步驟
Step 1. 在**背景**建立並啟動 dockedr compose 服務
```shell
docker compose up -d
```

確認以下項目
1. 容器服務是否正確執行?
2. 容器目前的狀態?
3. 映像檔目前的狀態?

停止服務
```shell
docker compose stop
```

確認以下項目
1. 容器服務是否正確執行?
2. 容器目前的狀態?
3. 映像檔目前的狀態?

重啟服務
```shell
docker compose start
```

停止並刪除容器與所有映像檔
```shell
docker compose down --rmi all
```

確認以下項目
1. 容器是否已刪除?
2. 映像檔是否已刪除?

## 延伸問題
1. 如何在容器服務為執行中時修改 app.py 並重新建立映像檔與啟動容器?