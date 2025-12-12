# 권다영의 오픈소스 프로젝트 - 한국어 욕설/비속어 탐지 프로그램
---
## ▷ 프로젝트 개요
> 이 프로젝트는 한국어 문장을 입력하면 욕설/비속어 여부를 탐지하는 파이썬 프로그램입니다. 
> HuggingFace의 사전 학습된 한국어 혐오 발언 탐지 모델을 활용하여 문장을 분류하고, 각 결과에 대한 확신도(score) 를 함께 출력합니다.

| 항목 | 내용 |
| ---- | ---- |
| 사용 모델 | smilegate-ai/kor_unsmile |
| 입력 | 한국어 문장 1개 |
| 출력 | 욕설/비속어 여부 라벨 + 확신도 |

---
## ▷ 기능

- 한국어 문장 입력
- 욕설 / 비속어 포함 여부 분류
- 분류 결과에 대한 확신도 출력
- exit 입력 시 프로그램 종료
- HuggingFace pipeline 기반 간단한 구현

---
## ▷ 라벨 설명

---
## ▷ 데모 이미지
<img width="1232" height="1288" alt="image" src="https://github.com/user-attachments/assets/8752dd2a-56fb-4e05-b35a-9cb6068139e3" />

---
## ▷ 코드 동작
'''sh
from transformers import pipeline

def main():
    model_name = "smilegate-ai/kor_unsmile"
    print(f"[INFO] 모델 로딩 중... ({model_name})")
    classifier = pipeline("text-classification", model=model_name)
    print("[INFO] 모델 로딩 완료!\n")

    print("=== 한국어 욕설/비속어 탐지 프로그램 ===")
    print("종료하려면 exit 입력\n")

    while True:
        text = input("문장을 입력하세요: ").strip()

        if text.lower() == "exit":
            print("프로그램을 종료합니다.")
            break

        if not text:
            print("⚠ 공백 문장은 분석할 수 없습니다.\n")
            continue

        result = classifier(text)[0]
        label = result["label"]
        score = result["score"]

        print("\n[분석 결과]")
        print(f"- 라벨: {label}")
        print(f"- 확신도: {score:.4f}")
        print("-" * 30)

if __name__ == "__main__":
    main()
'''

---
## ▷ 실행방법


---
## ▷ 사용한 패키지와 그 version

---
## ▷ 참고 자료
