# Luftqualitaet-data
Datenquelle ist Umwelt Sachsen

http://www.umwelt.sachsen.de/umwelt/infosysteme/luftonline/recherche.aspx

# Data structure
## `raw/YEAR/MONTH/STATION,SUBSTANCE.csv`
These files are basically raw, only modifications are:
* Decimal symbol is a point and not a comma
* Missing data are empty fields instead of `n. def.`
* Separator is set to `,`

## `joint/YEAR/MONTH/STATION.csv`
Joints all `raw/YEAR/MONTH/STATION,SUBSTANCE.csv` into `joint/YEAR/MONTH/STATION.csv`
with one column for each substance.

# Scripts
The scripts that produce these files are in the repository [offenesdresden/Luftqualitaet-src](https://github.com/offenesdresden/Luftqualitaet-src).
