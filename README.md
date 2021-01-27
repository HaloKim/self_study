# self_study
공부하자 😚

# NLP
1. Hugging Face API를 이용하여 ALBERT 모델 생성 중 Token 문제가 많았지만, Google의 Sentence Piece를 이용하여 토큰 모델을 생성하니 잘 진행되었다.
2. UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 102: invalid continuation byte
- 전처리에 문제가 있었기 때문에 처음부터 진행했더니 풀렸다.
3. Some weights of AlbertModel were not initialized from the model checkpoint at /content/drive/MyDrive/albert_model and are newly initialized: ['albert.pooler.weight', 'albert.pooler.bias']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
- Hugging Face의 Scratch Train에서 run_mlm을 사용하면 뜨는 경고, 이 모델에서 풀러를 사용하지 않기 때문에 당연히 뜨는 경고
