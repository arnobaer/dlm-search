# DLM Search

## Setup

Import default CSV data set.
```bash
python -m dlmsearch --import-csv data/default.csv
```

## Run

Run using gunicorn WSGI server.

```bash
gunicorn dlmsearch
```

## License

DLM Search is licensed under the [GNU General Public License Version 3](https://github.com/arnobaer/dlm-search/tree/master/LICENSE).

Open data [Digitales Landschaftsmodell - Namen](https://www.data.gv.at/katalog/dataset/69617480-d031-42e4-b520-ee1a2f8446af) by [BEV](https://bev.gv.at) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
