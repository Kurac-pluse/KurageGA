# KurageGA

Qiita記事にて詳しい解説をしています。  
https://qiita.com/sesseki-kurage/items/f39cece127ee92257928

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3793561/6e871204-cd7b-e137-cd02-70786019d7de.png" width="40%" />

## 環境セットアップ
### 前提
python, Anaconda

### 手順
仮想環境を作成＆有効化、clone、準備
```
conda create -n llama2GA python=3.9
conda activate llama2GA
git clone https://github.com/Kurac-pluse/KurageGA.git
cd KurageGA/
mkdir models
```
パッケージのinstall
```
pip install langchain==0.0.348
pip install llama-cpp-python==0.2.20
pip install sentence-transformers==2.2.2
```

CUDA対応のGPUがある場合：  
`pip install faiss-gpu==1.7.2`  
CPUのみの場合：  
`pip install faiss-cpu`

下記のサイトからLlama2のモデルをダウンロード  
- [7Bのモデル](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main)  
- [13Bのモデル](https://huggingface.co/TheBloke/Llama-2-13B-Chat-GGUF/tree/main)  
- [70Bのモデル](https://huggingface.co/TheBloke/Llama-2-70B-Chat-GGUF/tree/main)

おすすめは「llama-2-7b-chat.Q5_K_M.gguf」

> [!CAUTION]  
> モデルの拡張子によっては、こちらのページ([llama.cpp](https://github.com/ggerganov/llama.cpp#be-prepared-to-re-convert-and--or-re-quantize-your-gguf-models-while-this-notice-is-up))からコンバーターをダウンロードして.ggufファイルに変換する必要があります。

用意したファイルを /KurageGA/models へ入れる

### 実行
`python main.py`

## 出力結果サンプル
2024年1月1日 8:00  
person1: At 8:00, I am taking "actions related to breakfast".  
person2: I am currently studying for my upcoming exam.

2024年1月1日 8:10  
person1: At 8:10, I am brushing my teeth.  
person2: I am taking a short break to relax before continuing my studies.

2024年1月1日 8:20  
person1: At 8:20, I am taking "actions related to getting ready to go out".  
person2: At 8:20, I am studying for my upcoming exam.
