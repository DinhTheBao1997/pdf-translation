from .translate_core import TransalteCore

def write_file(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer_en2vi = AutoTokenizer.from_pretrained("vinai/vinai-translate-en2vi", src_lang="en_XX")
model_en2vi = AutoModelForSeq2SeqLM.from_pretrained("vinai/vinai-translate-en2vi")


class VinaiTranslate(TransalteCore):
    def translate_en2vi(en_text: str) -> str:
        input_ids = tokenizer_en2vi(en_text, return_tensors="pt").input_ids
        output_ids = model_en2vi.generate(
            input_ids,
            decoder_start_token_id=tokenizer_en2vi.lang_code_to_id["vi_VN"],
            num_return_sequences=1,
            num_beams=5,
            early_stopping=True
        )
        vi_text = tokenizer_en2vi.batch_decode(output_ids, skip_special_tokens=True)
        vi_text = " ".join(vi_text)
        return en_text
