import json
import xml.etree.ElementTree as ET
from datetime import datetime
import os

def export_to_json(passwords, compromised_passwords, filename=None):
    """
    Export password data to JSON format
    
    Args:
        passwords: Set of generated passwords
        compromised_passwords: Dict of compromised passwords with breach counts
        filename: Optional filename, if None generates timestamp-based name
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"password_analysis_{timestamp}.json"
    
    data = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "total_passwords": len(passwords),
            "compromised_passwords": len(compromised_passwords),
            "tool": "NameCrack"
        },
        "passwords": {
            "all_passwords": list(passwords),
            "compromised_passwords": compromised_passwords
        }
    }
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ JSON export successful: {filename}")
        return filename
    except Exception as e:
        print(f"❌ JSON export failed: {e}")
        return None

def export_to_xml(passwords, compromised_passwords, filename=None):
    """
    Export password data to XML format
    
    Args:
        passwords: Set of generated passwords
        compromised_passwords: Dict of compromised passwords with breach counts
        filename: Optional filename, if None generates timestamp-based name
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"password_analysis_{timestamp}.xml"
    
    # Create root element
    root = ET.Element("password_analysis")
    
    # Add metadata
    metadata = ET.SubElement(root, "metadata")
    ET.SubElement(metadata, "timestamp").text = datetime.now().isoformat()
    ET.SubElement(metadata, "total_passwords").text = str(len(passwords))
    ET.SubElement(metadata, "compromised_passwords").text = str(len(compromised_passwords))
    ET.SubElement(metadata, "tool").text = "NameCrack"
    
    # Add all passwords
    all_passwords_elem = ET.SubElement(root, "all_passwords")
    for password in passwords:
        password_elem = ET.SubElement(all_passwords_elem, "password")
        password_elem.text = password
    
    # Add compromised passwords
    compromised_elem = ET.SubElement(root, "compromised_passwords")
    for password, count in compromised_passwords.items():
        comp_password_elem = ET.SubElement(compromised_elem, "password")
        comp_password_elem.set("breach_count", str(count))
        comp_password_elem.text = password
    
    # Create tree and write to file
    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        print(f"✅ XML export successful: {filename}")
        return filename
    except Exception as e:
        print(f"❌ XML export failed: {e}")
        return None

def export_data(passwords, compromised_passwords, format_type, filename=None):
    """
    Universal export function
    
    Args:
        passwords: Set of generated passwords
        compromised_passwords: Dict of compromised passwords with breach counts
        format_type: 'json' or 'xml'
        filename: Optional filename
    """
    if format_type.lower() == 'json':
        return export_to_json(passwords, compromised_passwords, filename)
    elif format_type.lower() == 'xml':
        return export_to_xml(passwords, compromised_passwords, filename)
    else:
        print(f"❌ Unsupported format: {format_type}")
        return None
