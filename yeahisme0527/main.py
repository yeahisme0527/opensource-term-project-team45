from transformers import pipeline

def main():
    print("=== YehEun's Sentiment Analysis Program ===")
    
    # 허깅페이스 감정 분석 모델 로드
    classifier = pipeline("sentiment-analysis")

    while True:
        text = input("문장을 입력하세요 (종료: exit): ")

        if text.lower() == "exit":
            print("프로그램을 종료합니다.")
            break

        result = classifier(text)[0]
        label = result['label']
        score = result['score']

        print(f"결과: {label} (확신도: {score:.4f})")
        print("-" * 40)

if __name__ == "__main__":
    main()
