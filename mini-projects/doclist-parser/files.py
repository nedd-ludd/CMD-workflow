from bs4 import BeautifulSoup
import csv
import os

fin = "master.html"
fout = "links.csv"


def parse_html_file(file_path, output_file):
    with open(file_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    with open(output_file, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        if os.stat(output_file).st_size == 0:
            csv_writer.writerow(['link', 'file'])

        target_divs = soup.find_all('div', attrs={'data-target': 'doc'})

        for div in target_divs:
            data_id = div.get('data-id')
            full_link = f'https://drive.google.com/file/d/{data_id}/view?usp=drive_link'
            nested_div = div.find('div', string=lambda text: text and (
                text.endswith('.jpg') or text.endswith('.png')))

            if nested_div:
                image_text = nested_div.text[:-4]
                csv_writer.writerow([full_link, image_text])

            continue


parse_html_file(fin, fout)
