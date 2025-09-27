#!/usr/bin/env python3
"""
Text to VCF (vCard) Converter
Converts text files containing contact information to VCF format.

Supports multiple input formats:
1. CSV-like format: Name,Phone,Email
2. Tab-separated format: Name    Phone    Email
3. Line-by-line format with patterns like "Name: John Doe"
4. Simple format with name and phone on separate lines
"""

import re
import os
import sys
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class Contact:
    """Data class to represent a contact."""
    name: str = ""
    phone: str = ""
    email: str = ""
    organization: str = ""
    
    def is_valid(self) -> bool:
        """Check if contact has minimum required information."""
        return bool(self.name.strip() or self.phone.strip() or self.email.strip())


class TextToVCFConverter:
    """Converter class to handle text file to VCF conversion."""
    
    def __init__(self):
        self.contacts: List[Contact] = []
    
    def clean_phone(self, phone: str) -> str:
        """Clean and format phone number."""
        if not phone:
            return ""
        # Remove common formatting characters
        cleaned = re.sub(r'[^\d+\-\(\)\s]', '', phone.strip())
        return cleaned.strip()
    
    def clean_email(self, email: str) -> str:
        """Validate and clean email address."""
        if not email:
            return ""
        email = email.strip()
        # Basic email validation
        if '@' in email and '.' in email.split('@')[1]:
            return email
        return ""
    
    def parse_csv_format(self, line: str, delimiter: str = ',') -> Optional[Contact]:
        """Parse CSV or delimited format: Name,Phone,Email[,Organization]"""
        parts = [part.strip() for part in line.split(delimiter)]
        if len(parts) < 2:
            return None
        
        contact = Contact()
        contact.name = parts[0] if parts[0] else ""
        contact.phone = self.clean_phone(parts[1]) if len(parts) > 1 else ""
        contact.email = self.clean_email(parts[2]) if len(parts) > 2 else ""
        contact.organization = parts[3] if len(parts) > 3 else ""
        
        return contact if contact.is_valid() else None
    
    def parse_key_value_format(self, lines: List[str]) -> List[Contact]:
        """Parse key-value format like 'Name: John Doe'."""
        contacts = []
        current_contact = Contact()
        
        for line in lines:
            line = line.strip()
            if not line:
                if current_contact.is_valid():
                    contacts.append(current_contact)
                    current_contact = Contact()
                continue
            
            # Look for key-value pairs
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower()
                value = value.strip()
                
                if key in ['name', 'full name', 'fullname']:
                    # If we encounter a new Name field and current contact has data,
                    # save the current contact and start a new one
                    if current_contact.is_valid() and current_contact.name:
                        contacts.append(current_contact)
                        current_contact = Contact()
                    current_contact.name = value
                elif key in ['phone', 'telephone', 'mobile', 'cell']:
                    current_contact.phone = self.clean_phone(value)
                elif key in ['email', 'e-mail', 'mail']:
                    current_contact.email = self.clean_email(value)
                elif key in ['organization', 'company', 'org']:
                    current_contact.organization = value
        
        # Don't forget the last contact
        if current_contact.is_valid():
            contacts.append(current_contact)
        
        return contacts
    
    def parse_simple_format(self, lines: List[str]) -> List[Contact]:
        """Parse simple format with name and phone on consecutive lines."""
        contacts = []
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            
            contact = Contact()
            
            # First line could be name
            if not re.match(r'^[\d\s\-\+\(\)]+$', line):  # Not just numbers
                contact.name = line
                i += 1
                
                # Next line might be phone
                if i < len(lines):
                    next_line = lines[i].strip()
                    if next_line and (re.match(r'^[\d\s\-\+\(\)]+$', next_line) or 
                                    re.match(r'^[\d\s\-\+\(\)]{7,}$', next_line)):
                        contact.phone = self.clean_phone(next_line)
                        i += 1
            else:
                # Line appears to be a phone number
                contact.phone = self.clean_phone(line)
                i += 1
            
            # Check next line for email
            if i < len(lines):
                next_line = lines[i].strip()
                if '@' in next_line:
                    contact.email = self.clean_email(next_line)
                    i += 1
            
            if contact.is_valid():
                contacts.append(contact)
            else:
                i += 1
        
        return contacts
    
    def auto_detect_format(self, content: str) -> List[Contact]:
        """Auto-detect the format and parse accordingly."""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        if not lines:
            return []
        
        # Check for CSV format (commas)
        comma_count = sum(1 for line in lines[:5] if ',' in line)
        if comma_count >= len(lines[:5]) * 0.6:  # 60% of first 5 lines have commas
            contacts = []
            for line in lines:
                contact = self.parse_csv_format(line, ',')
                if contact:
                    contacts.append(contact)
            return contacts
        
        # Check for tab-separated format
        tab_count = sum(1 for line in lines[:5] if '\t' in line)
        if tab_count >= len(lines[:5]) * 0.6:
            contacts = []
            for line in lines:
                contact = self.parse_csv_format(line, '\t')
                if contact:
                    contacts.append(contact)
            return contacts
        
        # Check for key-value format (contains colons)
        colon_count = sum(1 for line in lines[:10] if ':' in line)
        if colon_count >= len(lines[:10]) * 0.3:  # 30% of first 10 lines have colons
            return self.parse_key_value_format(lines)
        
        # Default to simple format
        return self.parse_simple_format(lines)
    
    def contact_to_vcf(self, contact: Contact) -> str:
        """Convert a contact to VCF format."""
        vcf_lines = ['BEGIN:VCARD', 'VERSION:3.0']
        
        if contact.name:
            # Split name into first and last
            name_parts = contact.name.split()
            if len(name_parts) >= 2:
                last_name = name_parts[-1]
                first_name = ' '.join(name_parts[:-1])
                vcf_lines.append(f'N:{last_name};{first_name};;;')
            else:
                vcf_lines.append(f'N:{contact.name};;;;')
            vcf_lines.append(f'FN:{contact.name}')
        
        if contact.phone:
            vcf_lines.append(f'TEL;TYPE=CELL:{contact.phone}')
        
        if contact.email:
            vcf_lines.append(f'EMAIL;TYPE=INTERNET:{contact.email}')
        
        if contact.organization:
            vcf_lines.append(f'ORG:{contact.organization}')
        
        vcf_lines.append('END:VCARD')
        return '\n'.join(vcf_lines)
    
    def convert_file(self, input_file: str, output_file: str = None) -> bool:
        """Convert text file to VCF format."""
        try:
            # Read input file
            with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse contacts
            self.contacts = self.auto_detect_format(content)
            
            if not self.contacts:
                print(f"No valid contacts found in {input_file}")
                return False
            
            # Generate output filename if not provided
            if not output_file:
                base_name = os.path.splitext(input_file)[0]
                output_file = f"{base_name}.vcf"
            
            # Write VCF file
            with open(output_file, 'w', encoding='utf-8') as f:
                for i, contact in enumerate(self.contacts):
                    if i > 0:
                        f.write('\n')
                    f.write(self.contact_to_vcf(contact))
            
            print(f"Successfully converted {len(self.contacts)} contacts")
            print(f"Output saved to: {output_file}")
            return True
            
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found")
            return False
        except Exception as e:
            print(f"Error processing file: {str(e)}")
            return False


def main():
    """Main function to handle command line usage."""
    if len(sys.argv) < 2:
        print("Usage: python txt_to_vcf.py <input_file.txt> [output_file.vcf]")
        print("\nSupported input formats:")
        print("1. CSV: Name,Phone,Email,Organization")
        print("2. Tab-separated: Name    Phone    Email")
        print("3. Key-value: Name: John Doe")
        print("4. Simple: Name on one line, phone on next")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    converter = TextToVCFConverter()
    success = converter.convert_file(input_file, output_file)
    
    if success:
        print("\nSample contacts converted:")
        for i, contact in enumerate(converter.contacts[:3]):  # Show first 3
            print(f"  {i+1}. {contact.name} - {contact.phone} - {contact.email}")
        if len(converter.contacts) > 3:
            print(f"  ... and {len(converter.contacts) - 3} more")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()