#!/usr/bin/env python3
"""
Generate synthetic Vietnamese real-estate rows and append to an existing CSV.

Usage:
    python generate_synthetic_vn_real_estate.py --count 500

By default it appends to House_price/GiaChungCu_HCM_June2021_laydulieu_com.csv

The script preserves the CSV header ordering, encoding (UTF-8), skips duplicate header rows,
and allows specifying a custom output/input file with --file.
"""

import csv
import argparse
import random
import os
from faker import Faker

fake = Faker("vi_VN")

PROPERTY_TYPES = ["Căn hộ, chung cư"]
TRANSACTION_TYPES = ["Cần bán", "Cần thuê"]
CITY = "Hồ Chí Minh"
DISTRICTS = [
    "Quận 9","Quận Tân Bình","Quận Tân Phú","Quận 7","Quận 2","Quận 11",
    "Quận Thủ Đức","Huyện Bình Chánh","Quận Bình Tân","Quận 12","Quận 1","Quận 3"
]
DIRECTIONS = ["Đông Bắc", "Tây", "Nam", "Tây Bắc", "Bắc", "Tây Nam", "Đông", "Đông Nam"]
LEGAL_PAPERS = ["Đã có sổ", "Đang chờ sổ",""]
HEADER = [
    "GIỐNG - LOẠI","GIỐNG - NHU CẦU","GIỐNG - TỈNH THÀNH","QUẬN HUYỆN",
    "GIÁ - TRIỆU ĐỒNG","DIỆN TÍCH - M2","HƯỚNG","SỐ TẦNG",
    "SỐ PHÒNG","SỐ TOILETS","GIẤY TỜ PHÁP LÝ",
]


def sometimes_empty(value_func, empty_prob=0.15):
    if random.random() < empty_prob:
        return ""
    return value_func()


def generate_row():
    prop_type = random.choice(PROPERTY_TYPES)
    need = "Cần bán" if random.random() < 0.95 else random.choice(TRANSACTION_TYPES)
    province = CITY
    district = fake.random_element(elements=DISTRICTS)

    DISTRICT_PRICE_RANGE = {
        "cao": ["Quận 1", "Quận 3", "Quận 4", "Quận 5", "Quận Bình Thạnh", "Quận Phú Nhuận", "Quận 10"],
        "trung": ["Quận 2", "Quận 7", "Quận Tân Bình", "Quận Tân Phú", "Quận 11", "Quận 9", "Quận Thủ Đức"],
        "thap": ["Quận 12", "Quận Bình Tân", "Huyện Bình Chánh", "Huyện Nhà Bè", "Huyện Hóc Môn"]
    }

    if district in DISTRICT_PRICE_RANGE["cao"]:
        price_min, price_max = 3500, 8000   # triệu đồng
    elif district in DISTRICT_PRICE_RANGE["trung"]:
        price_min, price_max = 2000, 6000
    else:
        price_min, price_max = 1000, 4000

    def random_price():
        mean = (price_min + price_max) / 2
        std_dev = (price_max - price_min) / 6
        val = max(price_min, min(price_max, random.gauss(mean, std_dev)))
        return int(val)

    price = sometimes_empty(lambda: str(random_price()), empty_prob=0.03)

    # Diện tích có liên hệ nhẹ với khu vực
    if district in DISTRICT_PRICE_RANGE["cao"]:
        area_val = random.uniform(25, 90)
    elif district in DISTRICT_PRICE_RANGE["trung"]:
        area_val = random.uniform(40, 120)
    else:
        area_val = random.uniform(50, 150)
    area = sometimes_empty(lambda: f"{area_val:.1f}", empty_prob=0.05)

    # Hướng, phòng, toilet, giấy tờ — cho phép null tự nhiên hơn
    direction = sometimes_empty(lambda: fake.random_element(elements=DIRECTIONS), empty_prob=0.4)
    floors = ""  # luôn null theo yêu cầu
    rooms = sometimes_empty(lambda: str(random.randint(1, 4)), empty_prob=0.12)
    toilets = sometimes_empty(lambda: str(random.randint(1, 3)), empty_prob=0.12)
    legal = sometimes_empty(lambda: fake.random_element(elements=LEGAL_PAPERS), empty_prob=0.25)

    return [prop_type, need, province, district, price, area, direction, floors, rooms, toilets, legal]




def detect_header(existing_header, desired_header):
    """Return True if existing_header matches desired_header (ignoring minor whitespace)."""
    if not existing_header:
        return False
    # Normalize by stripping spaces
    ex = [h.strip() for h in existing_header]
    de = [h.strip() for h in desired_header]
    return ex == de


def append_synthetic_rows(target_path, count):
    # Ensure file exists
    if not os.path.exists(target_path):
        raise FileNotFoundError(f"Target CSV not found: {target_path}")

    # Read existing header to preserve order
    with open(target_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        try:
            existing_header = next(reader)
        except StopIteration:
            existing_header = []

    # If existing_header is empty, use our HEADER
    if not existing_header:
        existing_header = HEADER

    # If existing header differs in length from generated row, warn but proceed by aligning columns
    if len(existing_header) != len(HEADER):
        print("Warning: existing CSV header length differs from generator header.")
        print(f"Existing header ({len(existing_header)}): {existing_header}")
        print(f"Generator header ({len(HEADER)}): {HEADER}")

    # Generate rows
    new_rows = [generate_row() for _ in range(count)]

    # Align row lengths to existing_header length
    aligned_rows = []
    for r in new_rows:
        if len(r) < len(existing_header):
            r = r + [""] * (len(existing_header) - len(r))
        elif len(r) > len(existing_header):
            r = r[:len(existing_header)]
        aligned_rows.append(r)

    # Append to file without writing header again
    with open(target_path, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # If the existing file appears to have the same header as our header but also contains the header row at the end,
        # we simply append rows. CSV append won't duplicate header because we never write it here.
        for row in aligned_rows:
            writer.writerow(row)

    print(f"Appended {len(aligned_rows)} synthetic rows to {target_path}")


def main():
    parser = argparse.ArgumentParser(description='Append synthetic VN real-estate rows to existing CSV')
    parser.add_argument('--count', '-n', type=int, default=500, help='Number of synthetic rows to generate')
    parser.add_argument('--file', '-f', type=str, default='House_price/GiaChungCu_HCM_June2021_laydulieu_com.csv',
                        help='Path to the target CSV file to append to')
    args = parser.parse_args()

    try:
        append_synthetic_rows(args.file, args.count)
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == '__main__':
    main()
