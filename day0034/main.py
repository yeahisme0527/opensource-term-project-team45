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
