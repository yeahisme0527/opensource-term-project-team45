from transformers import pipeline

def main():
    print("=== YehEun's Korean Sentiment Program ===")

    # 한국어 전용 감정 분석 모델 
    classifier = pipeline(
        "sentiment-analysis",
        model="WhitePeak/bert-base-cased-Korean-sentiment"
    )

    while True:
        text = input("문장을 입력하세요 (종료: exit): ")
        if text.lower() == "exit":
            print("프로그램을 종료합니다.")
            break

        result = classifier(text)[0]
        label = result['label']    # LABEL_0 / LABEL_1 / LABEL_2
        score = result['score']

        print(f"결과: {label} (확신도: {score:.4f})")
        print("-" * 40)

if __name__ == "__main__":
    main()

