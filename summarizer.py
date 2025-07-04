from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summaries = summarizer(chunks, max_length=150, min_length=40, do_sample=False)
    return " ".join([s['summary_text'] for s in summaries])
