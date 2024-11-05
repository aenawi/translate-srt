import pysrt
from tqdm import tqdm
import argparse
import os
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from transformers import AutoProcessor, AutoModelForSeq2SeqLM
import torch
import re

# Load SeamlessM4T V2 model and processor
processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/seamless-m4t-v2-large")

def process_arabic_text(text):
    """
    Process Arabic text with proper reshaping and RTL marks.
    """
    # Handle HTML-style tags
    if '<i>' in text:
        parts = text.split('<i>')
        processed_parts = []
        for part in parts:
            if '</i>' in part:
                tag_parts = part.split('</i>')
                # Add RTL marks around the reshaped text
                processed_parts.append(f'<i>{tag_parts[0]}</i>\u200F{reshape(tag_parts[1])}\u200F')
            else:
                # Add RTL marks around the reshaped text
                processed_parts.append(f'\u200F{reshape(part)}\u200F')
        text = ''.join(processed_parts)
    else:
        # Add RTL marks around the reshaped text
        text = f'\u200F{reshape(text)}\u200F'
    
    return text

def translate_text(text, source_lang="eng", target_lang="arb"):
    try:
        # Process the input text
        inputs = processor(
            text=text,
            src_lang=source_lang,
            return_tensors="pt"
        )
        
        # Generate translation with explicit target language
        generated_ids = model.generate(
            **inputs,
            tgt_lang=target_lang,
            max_new_tokens=256,
            num_beams=5,
            do_sample=True,
            temperature=0.7
        )
        
        # Decode the generated IDs to get the translated text
        translated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        # Apply Arabic text processing with RTL marks
        return process_arabic_text(translated_text)
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return text

def translate_srt_file(input_path, output_path):
    subs = pysrt.open(input_path, encoding='utf-8')
    print(f"Translating and saving to: {output_path}")

    with open(output_path, 'w', encoding='utf-8') as output_file:
        with tqdm(total=len(subs), desc="Translating subtitles", unit="subtitle") as pbar:
            for sub in subs:
                arabic_text = translate_text(sub.text)
                subtitle_entry = f"{sub.index}\n{sub.start} --> {sub.end}\n{arabic_text}\n\n"
                output_file.write(subtitle_entry)
                pbar.update(1)

    print(f'Translation completed and saved to: {output_path}')

def main():
    parser = argparse.ArgumentParser(description="Translate SRT subtitles to Arabic.")
    parser.add_argument("file", help="Path to the .srt file to be translated")
    parser.add_argument(
        "-o", "--output", 
        help="Folder or full path and filename for the translated output file. "
             "If only a folder or '.' is provided, saves with original filename and '-AR' suffix.",
        default=None
    )
    args = parser.parse_args()

    if args.output:
        if os.path.isdir(args.output) or args.output == ".":
            base_name = os.path.basename(args.file)
            name, ext = os.path.splitext(base_name)
            output_path = os.path.join(args.output, f"{name}-AR{ext}")
        else:
            output_path = args.output
    else:
        base, ext = os.path.splitext(args.file)
        output_path = f"{base}-AR{ext}"

    translate_srt_file(args.file, output_path)

if __name__ == "__main__":
    main()
