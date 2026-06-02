#!/usr/bin/env python3
# organize_configs.py
# این اسکریپت باید بعد از delete_duplicate_name.py اجرا شود

import os
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

# پوشه‌ی اصلی کانفیگ‌ها
CONFIG_DIR = "config"
# پروتکل‌های مجاز و نام پوشه‌ی متناظر
PROTOCOLS = {
    "hysteria2": "hysteria2",
    "reality": "reality",
    "socks": "socks",
    "ss": "ss",
    "trojan": "trojan",
    "vless": "vless",
    "vmess": "vmess",
    "wireguard": "wireguard",
}
# برای پروتکل‌های ناشناخته
OTHER_DIR = "others"

def get_protocol_from_filename(filename: str) -> str:
    """
    تشخیص پروتکل از روی نام فایل.
    مثال: reality_1.txt -> reality, vless.txt -> vless
    """
    name_lower = filename.lower()
    for proto in PROTOCOLS.keys():
        if name_lower.startswith(proto):
            return proto
    return None

def count_configs_in_file(filepath: Path) -> int:
    """تعداد خطوط غیرخالی فایل را برمی‌گرداند (هر خط یک کانفیگ)"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [line.strip() for line in f if line.strip()]
            return len(lines)
    except Exception as e:
        print(f"خطا در خواندن {filepath}: {e}")
        return 0

def get_file_metadata(filepath: Path, dest_path: Path, protocol: str) -> dict:
    """متادیتای یک فایل را استخراج می‌کند"""
    size = filepath.stat().st_size
    config_count = count_configs_in_file(filepath)
    # استخراج شماره قسمت (اگر وجود داشته باشد) مثلاً reality_2.txt -> 2
    parts = 1
    stem = filepath.stem  # بدون پسوند
    if '_' in stem:
        try:
            parts = int(stem.split('_')[-1])
        except ValueError:
            parts = 1
    return {
        "name": filepath.name,
        "path": str(dest_path.relative_to(Path.cwd())),
        "size_bytes": size,
        "config_count": config_count,
        "parts": parts,
        "protocol": protocol
    }

def main():
    root_dir = Path.cwd()
    config_root = root_dir / CONFIG_DIR
    
    # ایجاد پوشه‌های اصلی
    config_root.mkdir(exist_ok=True)
    
    # ایجاد پوشه‌های پروتکل
    protocol_dirs = {}
    for proto, folder in PROTOCOLS.items():
        proto_path = config_root / folder
        proto_path.mkdir(exist_ok=True)
        protocol_dirs[proto] = proto_path
    
    others_path = config_root / OTHER_DIR
    others_path.mkdir(exist_ok=True)
    
    # اسکن فایل‌های txt در ریشه
    txt_files = list(root_dir.glob("*.txt"))
    # فایل‌هایی که در پوشه config هستند را پردازش نمی‌کنیم
    txt_files = [f for f in txt_files if CONFIG_DIR not in str(f.parent)]
    
    metadata = {
        "last_update": datetime.now(timezone.utc).isoformat(),
        "protocols": {},
        "summary": {
            "total_configs": 0,
            "total_files": 0,
            "total_size_bytes": 0
        }
    }
    
    # دیکشنری برای جمع‌آوری اطلاعات هر پروتکل
    protocol_data = {proto: {"files": [], "total_configs": 0, "total_size_bytes": 0} for proto in PROTOCOLS}
    protocol_data[OTHER_DIR] = {"files": [], "total_configs": 0, "total_size_bytes": 0}
    
    for filepath in txt_files:
        proto = get_protocol_from_filename(filepath.name)
        if proto is None:
            dest_dir = others_path
            proto_key = OTHER_DIR
        else:
            dest_dir = protocol_dirs[proto]
            proto_key = proto
        
        dest_path = dest_dir / filepath.name
        # انتقال فایل
        shutil.move(str(filepath), str(dest_path))
        print(f"انتقال: {filepath.name} -> {dest_path.relative_to(root_dir)}")
        
        # دریافت متادیتا
        meta = get_file_metadata(dest_path, dest_path, proto_key)
        protocol_data[proto_key]["files"].append(meta)
        protocol_data[proto_key]["total_configs"] += meta["config_count"]
        protocol_data[proto_key]["total_size_bytes"] += meta["size_bytes"]
        
        # بروزرسانی جمع‌بندی کلی
        metadata["summary"]["total_configs"] += meta["config_count"]
        metadata["summary"]["total_files"] += 1
        metadata["summary"]["total_size_bytes"] += meta["size_bytes"]
    
    # حذف پروتکل‌هایی که هیچ فایلی ندارند از خروجی نهایی (اختیاری)
    for proto, data in protocol_data.items():
        if data["files"]:
            metadata["protocols"][proto] = data
    
    # نوشتن فایل metadata.json در پوشه config
    json_path = config_root / "metadata.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"\nخلاصه عملیات:")
    print(f"تعداد کل فایل‌های جابجا شده: {metadata['summary']['total_files']}")
    print(f"تعداد کل کانفیگ‌ها: {metadata['summary']['total_configs']}")
    print(f"حجم کل: {metadata['summary']['total_size_bytes']} bytes")
    print(f"فایل متادیتا در {json_path} ذخیره شد.")

if __name__ == "__main__":
    main()
