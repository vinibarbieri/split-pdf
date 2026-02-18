# split-pdf

Extract a range of pages from a PDF file.

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

### CLI

```bash
python main.py file.pdf 1 10
python main.py file.pdf 1 10 -o custom_name.pdf
```

### Interactive

```bash
python main.py
```

You'll be prompted for the file path, page range, and optional output name.

### Output

The extracted PDF is saved in the same directory as the source file. By default it's named `<original>_p<start>-<end>.pdf`. Use `-o` to set a custom name.

### Options

| Argument     | Description              |
|--------------|--------------------------|
| `file`       | Path to the PDF          |
| `start`      | Start page (1-based)     |
| `end`        | End page (1-based)       |
| `-o`         | Custom output filename   |

```bash
python main.py -h   # show help
```
