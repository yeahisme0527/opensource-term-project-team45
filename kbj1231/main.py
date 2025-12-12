from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# --- 1. 모델 이름 정의 ---
SUMMARIZATION_MODEL_NAME = "colli-ai/qwen3-1.7B-ko-summary-finetuned-06-12"
SENTIMENT_MODEL_NAME = "snunlp/KR-FinBert-SC"

# --- 2. 모델 및 토크나이저 로드 ---

# 🔹 요약 모델 로드
print(f"1. 요약 모델 로드 중: {SUMMARIZATION_MODEL_NAME}...")
try:
    summ_tokenizer = AutoTokenizer.from_pretrained(SUMMARIZATION_MODEL_NAME)
    summ_model = AutoModelForCausalLM.from_pretrained(SUMMARIZATION_MODEL_NAME)

except Exception as e:
    print(f"\n[오류] 요약 모델 로드 실패 {e}")
    exit()

# 🔹 감성 분류 모델 로드
print(f"2. 감성 분류 모델 로드 중: {SENTIMENT_MODEL_NAME}...")
try:
    classifier = pipeline("sentiment-analysis", model=SENTIMENT_MODEL_NAME)
except Exception as e:
    print(f"\n[오류] 감성 분류 모델 로드 실패: {e}")
    exit()

# --- 3. 테스트 데이터 ---
news_text = """
텍스트를 입력해주세요.
"""
print("-" * 50)

# --- 4. 요약 수행 ---
print("3. 요약 수행...")

# 프롬프트 생성
prompt = f"다음 기사를 요약하세요.\n{news_text}\n요약:"

# Tokenizer 호출
inputs = summ_tokenizer(
    prompt, 
    return_tensors="pt",
    truncation=True, 
    padding="longest"
)

summary_ids = summ_model.generate(
    **inputs,
    max_new_tokens=150,
    num_beams=4,
    do_sample=False,
    early_stopping=True,
    eos_token_id=summ_tokenizer.eos_token_id
)

generated_ids = summary_ids[0, inputs.input_ids.shape[-1]:]
summary_text = summ_tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

print(f"\n▶ 요약문: {summary_text}")
print("-" * 50)

# --- 5 & 6. 감성 분류 및 결과 출력 ---
print("4. 감성 분류 수행...")
# 디코딩된 summary_text 사용
result = classifier(summary_text)[0]
label = result['label']
score = result['score']

if label == "positive":
    stock_impact = "호재"
    sentiment_info = "긍정적"
elif label == "negative":
    stock_impact = "악재"
    sentiment_info = "부정적"
else:
    stock_impact = "중립"
    sentiment_info = "중립적"

print(f"\n[분석 결과]")
print(f"감성 라벨: {label} ({sentiment_info})")
print(f"신뢰도: {score:.4f}")
print(f"▶ 주식 뉴스 영향: {stock_impact}")