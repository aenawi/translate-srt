# Subtitle Translation to Arabic

This project is a Python-based tool designed to seamlessly translate `.srt` subtitle files from any language into Arabic, making it easier for Arabic-speaking audiences to enjoy content from around the world. Utilizing an open-source translation library, the tool provides an efficient solution for translating entire subtitle files while ensuring proper Arabic formatting, including right-to-left (RTL) text alignment. 

Whether you’re a content creator, language enthusiast, or just need a quick way to translate subtitles, this tool offers a straightforward, flexible approach with real-time progress tracking and options to save translations to custom output paths. With this tool, you can produce professional-quality Arabic subtitles compatible with popular media players and subtitle editors. 

--- 

## Requirements

- Python 3.6 to 3.12 (This project does not support Python 3.13 or higher due to dependencies)
- Required libraries (listed in `requirements.txt`):
  - `pysrt` for handling `.srt` files
  - `deep-translator` for translation
  - `tqdm` for progress bar
  - `arabic_reshaper` and `python-bidi` for proper RTL display of Arabic text

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

After activating your virtual environment (using either `venv` or `conda`), install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

The tool accepts a `.srt` file for translation and outputs a translated file with the option to specify a custom output location.

#### Basic Command

To translate a subtitle file and save it in the current directory:
```bash
python translate.py path/to/input_file.srt
```

This will create an output file in the same directory as the input file with `-AR` appended to the filename.

#### Specify a Custom Output Location

Use the `-o` or `--output` option to specify a folder or custom file path:
```bash
python translate.py path/to/input_file.srt -o path/to/output_directory/
```

For example:
```bash
python translate.py My.Movie.WEB.srt -o .
```
This will save the file in the current directory as `My.Movie.WEB-AR.srt`.

## Notes

- **RTL Display**: Ensure that the media player or subtitle editor supports RTL (Right-to-Left) display for proper Arabic text formatting.
- **Interruption Handling**: The script saves each translation line immediately, so if interrupted, you can resume from where it left off without losing progress.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or suggestions!
```

### Explanation of Updates

- **Python Version**: Specified Python 3.6 to 3.12 to avoid compatibility issues with removed modules in Python 3.13.
- **Environment Setup Options**: Added instructions for both `venv` and `conda` to set up a virtual environment, allowing flexibility based on user preference.
  
This ensures a clear setup process and compatibility for users on different systems or with different environment management preferences.
