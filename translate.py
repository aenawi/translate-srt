import pysrt
from deep_translator import GoogleTranslator
from tqdm import tqdm
import argparse
import os

def translate_text_to_arabic(text):
    # Translate using deep-translator
    return GoogleTranslator(source='auto', target='ar').translate(text)

def translate_srt_file(input_path, output_path):
    # Load .srt file
    subs = pysrt.open(input_path, encoding='utf-8')

    # Display final output file path
    print(f"Translating and saving to: {output_path}")

    # Start writing each translated line immediately
    with open(output_path, 'w', encoding='utf-8') as output_file:
        # Set up progress bar
        with tqdm(total=len(subs), desc="Translating subtitles", unit="subtitle") as pbar:
            for sub in subs:
                # Translate to Arabic
                arabic_text = translate_text_to_arabic(sub.text)
                
                # Format the subtitle entry
                subtitle_entry = f"{sub.index}\n{sub.start} --> {sub.end}\n{arabic_text}\n\n"
                
                # Write to output file immediately
                output_file.write(subtitle_entry)
                
                # Update progress bar
                pbar.update(1)

    print(f'Translation completed and saved to: {output_path}')

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Translate SRT subtitles to Arabic.")
    parser.add_argument("file", help="Path to the .srt file to be translated")
    parser.add_argument(
        "-o", "--output", 
        help="Folder or full path and filename for the translated output file. "
             "If only a folder or '.' is provided, saves with original filename and '-AR' suffix.",
        default=None
    )
    args = parser.parse_args()

    # Determine output path based on user input
    if args.output:
        if os.path.isdir(args.output) or args.output == ".":
            # Use the same filename with -AR suffix in the specified folder
            base_name = os.path.basename(args.file)
            name, ext = os.path.splitext(base_name)
            output_path = os.path.join(args.output, f"{name}-AR{ext}")
        else:
            # Use the provided file path directly
            output_path = args.output
    else:
        # Default to same directory as input file with -AR suffix
        base, ext = os.path.splitext(args.file)
        output_path = f"{base}-AR{ext}"

    # Call the translation function with the determined output path
    translate_srt_file(args.file, output_path)

if __name__ == "__main__":
    main()
