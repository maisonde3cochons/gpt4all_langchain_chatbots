GPT4All은 AGI를 Local환경이나 Private 환경에서 사용할 경우 유용한 툴이다.

### 1. 지원 Models

#### GGML GPT-4 All J Models:

```
ggml-gpt4all-j-v1.3-groovy.bin
ggml-gpt4all-j-v1.2-jazzy.bin
ggml-gpt4all-j-v1.1-breezy.bin
ggml-gpt4all-j.bin
```

#### LLAMA Models:

```
ggml-gpt4all-l13b-snoozy.bin
ggml-vicuna-7b-1.1-q4_2.bin
ggml-vicuna-13b-1.1-q4_2.bin
ggml-wizardLM-7B.q4_2.bin
ggml-stable-vicuna-13B.q4_2.bin
ggml-nous-gpt4-vicuna-13b.bin
```

#### MPT Models:
```
ggml-mpt-7b-base.bin
ggml-mpt-7b-chat.bin
ggml-mpt-7b-instruct.bin
```


### 2. 활용 방법

> 참고 링크 : 
```
https://docs.gpt4all.io/gpt4all_python.html
https://gpt4all.io/index.html
```

> Windows 환경에서 다운로드해서 바로 사용 가능


> Ubuntu(WSL) 환경에서 설치하여 사용 시 필수 설치 패키지
```
pip install langchain==0.0.181
pip install pyllamacpp==2.1.3
pip install gpt4all
```

> 아래와 같은 python code 작성하여 실행 (ggml-mpt-7b-chat.bin model은 ~/.cache/gpt4all/ 위치에 저장된다)
> 상세 코드는 본 repos에 (gpt4all.py 참고)
```
import gpt4all
gptj = gpt4all.GPT4All("ggml-mpt-7b-chat.bin")
messages = [{"role": "user", "content": "Who is the president of USA?"}]
gptj.chat_completion(messages)

```

