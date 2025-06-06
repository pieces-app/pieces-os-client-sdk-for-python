#!/usr/bin/env python3
"""
Post-generation fixes for the Pieces OS Client SDK.
This script applies necessary modifications after OpenAPI generation.
"""

import re
import sys
from pathlib import Path


def fix_api_client_imports(file_path: Path) -> bool:
    """Fix the import mechanism in api_client.py to use dynamic imports."""
    try:
        content = file_path.read_text()

        # Check if already fixed
        if "import importlib" in content:
            print(f"✓ {file_path} already has dynamic imports")
            return True

        # Replace the import statement
        content = content.replace("import pieces_os_client.models", "import importlib")

        # Find and replace the getattr line
        old_pattern = r"klass = getattr\(pieces_os_client\.models, klass\)"

        replacement = """# Convert the class to snake case
                # NOTE:
                # The following regex substitution doesn't work properly:
                #
                #     snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', klass).lower()
                #
                # An issue arises because this regex inserts underscores between all adjacent
                # uppercase letters (except at the start), which is not desirable for sequences like
                # 'QGPT'. It turns 'QGPT' into 'q_g_p_t'.
                # The following regex substitution should fix that:
                snake_case = re.sub(
                    r'(?<=[a-z0-9])(?=[A-Z])'      # Between lowercase/digit and uppercase
                    r'|(?<=[A-Z])(?=[A-Z][a-z])',  # Between uppercase and uppercase-lowercase sequence
                    '_',
                    klass
                ).lower()
                # EXPLANATION:
                # (?<=[a-z0-9])(?=[A-Z]): Inserts an underscore between a lowercase letter or digit
                #                         and an uppercase letter. This handles transitions like
                #                         'myClass' to 'my_Class'.
                # (?<=[A-Z])(?=[A-Z][a-z]): Inserts an underscore in cases where a sequence of
                #                           uppercase letters is followed by an uppercase letter and
                #                           then a lowercase letter. This handles cases like
                #                           'XMLHttpRequest' to 'XML_Http_Request'.
                #
                # EXAMPLE OUTPUTS:
                #     'QGPT'           -> 'qgpt'
                #     'MyClassName'    -> 'my_class_name'
                #     'HTTPRequest'    -> 'http_request'
                #     'XMLHttpRequest' -> 'xml_http_request'

                # Import the class
                module = importlib.import_module(f"pieces_os_client.models.{snake_case}")
                klass = getattr(module, klass)"""

        content = re.sub(old_pattern, replacement, content)

        file_path.write_text(content)
        print(f"✓ Fixed dynamic imports in {file_path}")
        return True

    except Exception as e:
        print(f"✗ Error fixing {file_path}: {e}")
        return False


def fix_workstream_event_trigger(file_path: Path) -> bool:
    """Fix the 'copy' field name conflict in workstream_event_trigger.py."""
    try:
        content = file_path.read_text()

        # Check if already fixed
        if "copy_field: Optional[StrictBool]" in content:
            print(f"✓ {file_path} already has copy field renamed")
            return True

        # Replace the copy field definition
        content = re.sub(
            r"copy: Optional\[StrictBool\] = None",
            'copy_field: Optional[StrictBool] = Field(default=None, alias="copy")',
            content,
        )

        file_path.write_text(content)
        print(f"✓ Fixed 'copy' field conflict in {file_path}")
        return True

    except Exception as e:
        print(f"✗ Error fixing {file_path}: {e}")
        return False


def main():
    """Apply all post-generation fixes."""
    print("Applying post-generation fixes...")

    # Define the fixes to apply
    fixes = [
        ("src/pieces_os_client/api_client.py", fix_api_client_imports),
        (
            "src/pieces_os_client/models/workstream_event_trigger.py",
            fix_workstream_event_trigger,
        ),
    ]

    success = True
    for file_path_str, fix_func in fixes:
        file_path = Path(file_path_str)
        if not file_path.exists():
            print(f"✗ File not found: {file_path}")
            success = False
            continue

        if not fix_func(file_path):
            success = False

    if success:
        print("\n✓ All post-generation fixes applied successfully!")
        return 0
    else:
        print("\n✗ Some fixes failed to apply")
        return 1


if __name__ == "__main__":
    sys.exit(main())

