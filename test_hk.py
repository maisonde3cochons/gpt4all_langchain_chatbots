import gpt4all
# from langchain.llms import GPT4All

# model_name: Name of GPT4All or custom model. Including ".bin" file extension is optional but encouraged.
# model_path: Path to directory containing model file or, if file does not exist, where to download model.
#     Default is None, in which case models will be stored in `~/.cache/gpt4all/`.
# model_type: Model architecture to use - currently, options are 'llama', 'gptj', or 'mpt'. Only required if model
#     is custom. Note that these models still must be built from llama.cpp or GPTJ ggml architecture.
#     Default is None.
# allow_download: Allow API to download models from gpt4all.io. Default is True. 

gptj = gpt4all.GPT4All(model_name="ggml-mpt-7b-base.bin", model_path="/workspace/gpt-offline/gpt4all_langchain_chatbots/models/", model_type='mpt', allow_download=True)
messages = [{"role": "user", "content": "Who is the president of USA"}]
# messages: List[Dict],
# default_prompt_header: bool = True,
# default_prompt_footer: bool = True,
# verbose: bool = True,
# streaming: bool = True,
# gptj.chat_completion(messages, default_prompt_header=False, default_prompt_footer=False, verbose=True, streaming=True)
print("ok")
