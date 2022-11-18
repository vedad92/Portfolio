import csv


def read_csv_to_dict(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        content = list(reader)
        f.close()
        return content


def read_csv_to_list(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        content = list(reader)
        f.close()
        return content


def append_csv(csv_file, list_to_append):
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list_to_append)
        f.close()


def write_csv(csv_file, id):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        L = []
        id = str(id)
        for row in reader:
            if row[0] != id:
                L.append(row)
        f.close()
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(L)
        f.close()


def make_id(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        id = len(list(reader))
        f.close()
        return id
