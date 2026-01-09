# pipeline

Usage

Run the ingestion script with CLI options (defaults shown):

```bash
python ingest_data.py --year 2021 --month 1
```

Override Postgres connection or table name:

```bash
python ingest_data.py \
	--pg-user root \
	--pg-password root \
	--pg-host localhost \
	--pg-port 5432 \
	--pg-database ny_taxi \
	--target-table yellow_taxi_data
```

For help and all options (run from the `pipeline` folder):

```bash
python ingest_data.py --help
```

Run in the dev container using `uv run` (example):

```bash
uv run python ingest_data.py \
	--pg-user=root \
	--pg-pass=root \
	--pg-host=localhost \
	--pg-port=5432 \
	--pg-db=ny_taxi \
	--target-table=yellow_taxi_trips_2021_1 \
	--year=2021 \
	--month=1 \
	--chunksize=100000
```
