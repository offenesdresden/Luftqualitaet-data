# Luftqualitaet-data
Datenquelle ist Umwelt Sachsen

http://www.umwelt.sachsen.de/umwelt/infosysteme/luftonline/recherche.aspx

# Data update
The data in this repository gets automatically updated four times a day at `04:37`, `10:37`, `16:37` and `22:37`.
This can be incremented if needed, for that please open an issue.

# Data structure
## `raw/YEAR/MONTH/STATION,SUBSTANCE.csv`
These files are basically raw, only modifications are:
* Decimal symbol is a point and not a comma
* Missing data are empty fields instead of `n. def.`
* Separator is set to `,`

## `joint/YEAR/MONTH/STATION.csv`
Joints all `raw/YEAR/MONTH/STATION,SUBSTANCE.csv` into `joint/YEAR/MONTH/STATION.csv`
with one column for each substance.
* Within a single month all `.csv` files have the same columns.
* Data that is generated on a monthly basis has date `01-MM-YYYY` for the month `MM-YYY` and time is empty.
* Data that is generated on a daily basis has date `01-MM-YYYY` for that day and time is empty.

## `vis/YEAR/MONTH/STATION,SUBSTANCE.png`
These files are basically raw timeseries diagrams of `raw` files (currently just Dresden, with some modifications of the Python script in the same folder, you can easily create these for other cities)


# Scripts
The scripts that produce these files are in the repository [offenesdresden/Luftqualitaet-src](https://github.com/offenesdresden/Luftqualitaet-src).
