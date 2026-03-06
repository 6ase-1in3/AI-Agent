import csv

with open('sheet_data.csv', 'r', encoding='utf-8', newline='') as f:
    reader = list(csv.reader(f))

# filter out empty rows
reader = [r for r in reader if len(r) > 0 and any(x.strip() for x in r)]

# Find the row indices for each section dynamically
db_idx = -1
oem_idx = -1
odm_idx = -1

for i, row in enumerate(reader):
    if row[0] == '資料區塊':
        db_idx = i
    elif row[0] == 'OEM流程':
        oem_idx = i
    elif row[0] == 'ODM流程':
        odm_idx = i

# 1. Database
if db_idx != -1:
    db_keys = reader[db_idx][1:]
    # The next row containing data should be db_idx + 1
    db_values = reader[db_idx+1][1:]
    with open('database.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['資料區塊', '涵蓋資料庫'])
        for i in range(min(len(db_keys), len(db_values))):
            if db_keys[i].strip():
                # Clean up the multiline values by removing '- ' and replacing newlines with '|'
                val = db_values[i].strip()
                val = val.replace('- ', '').replace('\n', '|').replace('\r', '')
                writer.writerow([db_keys[i].strip(), val])

# 2. OEM
if oem_idx != -1:
    oem_headers = reader[oem_idx][1:]
    oem_labels = []
    oem_rows = []
    for i in range(oem_idx+1, oem_idx+8):
        if i < len(reader) and len(reader[i]) > 0:
            oem_labels.append(reader[i][0].strip())
            oem_rows.append(reader[i][1:])
            
    with open('oem.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['階段名稱'] + oem_labels)
        for i in range(len(oem_headers)):
            if oem_headers[i].strip():
                row_data = [oem_headers[i].strip()]
                for r in oem_rows:
                    row_data.append(r[i].strip() if i < len(r) else '')
                writer.writerow(row_data)

# 3. ODM
if odm_idx != -1:
    odm_headers = reader[odm_idx][1:]
    odm_labels = []
    odm_rows = []
    for i in range(odm_idx+1, odm_idx+8):
        if i < len(reader) and len(reader[i]) > 0:
            odm_labels.append(reader[i][0].strip())
            odm_rows.append(reader[i][1:])
            
    with open('odm.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['階段名稱'] + odm_labels)
        for i in range(len(odm_headers)):
            if odm_headers[i].strip():
                row_data = [odm_headers[i].strip()]
                for r in odm_rows:
                    row_data.append(r[i].strip() if i < len(r) else '')
                writer.writerow(row_data)
