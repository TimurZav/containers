xls_path=/home/timur/PycharmWork/containers/statistics_2021
mkdir "${xls_path}"/csv
mkdir "${xls_path}"/json

python3 ../scripts/read_sheets_from_excel.py

for file in "${xls_path}"/csv/*.csv;
do
#    echo "'${file}'";
    python3 ../scripts/statistics_2021.py "${file}" "${xls_path}"/json
done