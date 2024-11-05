# Subtitle Translation to Arabic

This project is a Python-based tool designed to seamlessly translate `.srt` subtitle files from any language into Arabic, making it easier for Arabic-speaking audiences to enjoy content from around the world. The tool offers two translation methods:
1. Using Google Translate API (via deep-translator library)
2. Using Meta's Seamless M4T v2 Large Language Model for higher quality translations

Whether you're a content creator, language enthusiast, or just need a quick way to translate subtitles, this tool offers a straightforward, flexible approach with real-time progress tracking and options to save translations to custom output paths. With this tool, you can produce professional-quality Arabic subtitles compatible with popular media players and subtitle editors. 

--- 

## Requirements

### Basic Version (Google Translate)
- Python 3.6 to 3.12 (This project does not support Python 3.13 or higher due to dependencies)
- Required libraries (listed in `requirements.txt`):
  - `pysrt` for handling `.srt` files
  - `deep-translator` for translation
  - `tqdm` for progress bar
  - `arabic_reshaper` and `python-bidi` for proper RTL display of Arabic text

### LLM Version (Seamless M4T v2)
Additional requirements for LLM-based translation (listed in `requirements-llm.txt`):
- `torch` and `torchaudio` for the neural network backend
- `transformers` for handling the language model
- `sentencepiece` for text tokenization
- `protobuf` for model communication

## Installation

### 1. Clone the Repository

Download the project files or clone the repository:
```bash
git clone https://github.com/aenawi/translate-srt.git
cd translate-srt
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Choose one of the following methods to create an isolated environment for this project.

#### Option A: Using `venv`

1. **Create the Virtual Environment**:
```bash
python3 -m venv venv
```

2. **Activate the Virtual Environment**:
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

#### Option B: Using `conda`

1. **Create the Conda Environment**:
```bash
conda create -n translate-srt python=3.12
```

2. **Activate the Conda Environment**:
```bash
conda activate translate-srt
```

### 3. Install Dependencies

After activating your virtual environment (using either `venv` or `conda`), install the required dependencies based on your preferred translation method:

#### For Google Translate Version:
```bash
pip install -r requirements.txt
```

#### For LLM Translation Version:
```bash
pip install -r requirements-llm.txt
```

Note: The LLM version requires more disk space (approximately 5GB) as it downloads the Seamless M4T v2 model during first use.

## Usage

The tool accepts a `.srt` file for translation and outputs a translated file with the option to specify a custom output location.

### Basic Command

#### Using Google Translate:
```bash
python translate.py path/to/input_file.srt
```

#### Using Seamless M4T v2 LLM:
```bash
python translate-llm.py path/to/input_file.srt
```

This will create an output file in the same directory as the input file with `-AR` appended to the filename.

### Specify a Custom Output Location

Use the `-o` or `--output` option to specify a folder or custom file path:
```bash
python translate.py path/to/input_file.srt -o path/to/output_directory/
```
or
```bash
python translate-llm.py path/to/input_file.srt -o path/to/output_directory/
```

For example:
```bash
python translate-llm.py My.Movie.WEB.srt -o .
```
This will save the file in the current directory as `My.Movie.WEB-AR.srt`.

## Translation Methods Comparison

### Google Translate Version
- **Advantages**:
  - Faster translation speed
  - Minimal system requirements
  - No additional model downloads needed
  - Works well for simple, straightforward content
- **Limitations**:
  - Quality may vary for complex sentences
  - Requires internet connection
  - Subject to API limitations

### Seamless M4T v2 LLM Version
- **Advantages**:
  - Higher quality translations
  - Better handling of context and idioms
  - Works offline after initial model download
  - Consistent translation quality
- **Limitations**:
  - Requires more system resources
  - Initial download of ~5GB model
  - Slower translation speed
  - Requires a GPU for optimal performance

## Error Handling and Fallbacks

This tool includes built-in error handling to ensure a smooth translation process, even if certain subtitle lines encounter issues:

- **Translation Failures**: If an error occurs while translating a line (e.g., network issues or model errors), the tool will print an error message and use the original text for that line as a fallback.
- **Empty Translations**: In cases where the translation API or model returns `None` or an empty string, the tool automatically falls back to the original text, ensuring that "None" or blank lines are not written to the output file.
  
These mechanisms ensure that your subtitle file remains usable and intact, even if some translations cannot be processed.

[Rest of the README remains the same...]

## Upcoming Features

The following features are being considered for future updates to enhance functionality, improve user experience, and expand the tool's capabilities:

- [ ] **Multi-Language Support**: Expand translation options to allow users to select languages beyond Arabic, making the tool useful for a wider audience.

- [ ] **Batch Processing**: Add functionality to process multiple subtitle files in a single command, saving time for users working with series or collections of videos.

- [ ] **Error Logging**: Implement a detailed logging system to track any errors or translation issues, providing users with helpful insights and troubleshooting information.

- [ ] **Custom Translation API Integration**: Allow users to configure their own translation API keys (such as Google Translate API or Microsoft Translator) for higher-quality translations and to support users who prefer specific APIs.

- [ ] **AI Language Model (LLM) Integration**: Incorporate AI-powered language models (such as OpenAI’s GPT or other LLMs) to deliver more contextually accurate translations, especially for complex language structures and idiomatic expressions.

- [ ] **GUI Interface**: Develop a graphical user interface (GUI) for users who prefer a visual, interactive experience over command-line usage, making the tool more accessible to non-technical users.

- [ ] **Advanced RTL Formatting Options**: Enhance RTL support to include customizable formatting options, ensuring optimal subtitle display across various media players and subtitle editors.

- [ ] **Backup and Resume Feature**: Enable automatic backups and a resume option for longer translation processes, allowing users to pick up where they left off even after an unexpected interruption.

If you have suggestions for additional features or would like to contribute to the project, please reach out or open an issue in the GitHub repository!

## Notes

- **RTL Display**: Ensure that the media player or subtitle editor supports RTL (Right-to-Left) display for proper Arabic text formatting.
- **Interruption Handling**: The script saves each translation line immediately, so if interrupted, you can resume from where it left off without losing progress.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or suggestions!

---

### Updates

- **Error Handling and Fallbacks**: This new section describes how the tool manages translation failures by using the original text as a fallback for any line that fails to translate. It reassures users that the tool avoids outputting `None` or blank lines, ensuring a stable and complete subtitle file.
